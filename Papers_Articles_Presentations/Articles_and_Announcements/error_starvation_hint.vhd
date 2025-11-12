-- PART 2: THE INVESTIGATION



-- VHDL Testbench to expose the Costas Loop Error Starvation



--



-- This testbench will demonstrate the intermittent lock loss 



-- and help us discover the root cause through systematic 



-- investigation.







library IEEE;



use IEEE.STD_LOGIC_1164.ALL;



use IEEE.NUMERIC_STD.ALL;



use IEEE.MATH_REAL.ALL;



use STD.TEXTIO.ALL;



use IEEE.STD_LOGIC_TEXTIO.ALL;







entity tb_costas_mystery is



end entity;







architecture testbench of tb_costas_mystery is



    



    constant CLK_PERIOD : time := 10 ns;  -- 100 MHz



    constant DATA_WIDTH : integer := 16;



    constant PHASE_WIDTH : integer := 12;



    



    -- Testbench signals



    signal clk : std_logic := '0';



    signal reset : std_logic := '1';



    signal freq_select : std_logic := '0';



    signal rf_input : signed(DATA_WIDTH-1 downto 0);



    



    -- DUT outputs



    signal i_data, q_data : signed(DATA_WIDTH-1 downto 0);



    signal phase_error : signed(DATA_WIDTH-1 downto 0);



    signal vco_freq : signed(PHASE_WIDTH-1 downto 0);



    signal lock_detect : std_logic;



    



    -- Stimulus generation



    signal input_phase : real := 0.0;



    signal carrier_freq : real := 10000.0;  -- 10 kHz carrier



    signal noise_level : real := 0.1;       -- 10% noise



    



    -- Investigation signals



    signal lock_time_f1 : time := 0 ns;



    signal lock_time_f2 : time := 0 ns;



    signal lock_lost_f2 : boolean := false;



    signal test_phase : integer := 0;



    



    -- Random number generation for noise



    shared variable seed1, seed2 : integer := 1;



    



    component costas_loop_puzzle is



        generic (



            DATA_WIDTH : integer := 16;



            PHASE_WIDTH : integer := 12;



            F1_OFFSET : integer := 1000;



            F2_OFFSET : integer := 3000



        );



        port (



            clk         : in  std_logic;



            reset       : in  std_logic;



            rf_input    : in  signed(DATA_WIDTH-1 downto 0);



            freq_select : in  std_logic;



            i_data      : out signed(DATA_WIDTH-1 downto 0);



            q_data      : out signed(DATA_WIDTH-1 downto 0);



            phase_error : out signed(DATA_WIDTH-1 downto 0);



            vco_freq    : out signed(PHASE_WIDTH-1 downto 0);



            lock_detect : out std_logic



        );



    end component;



    



begin







    -- Clock generation



    clk <= not clk after CLK_PERIOD / 2;



    



    -- Device Under Test



    DUT: costas_loop_puzzle



        generic map (



            DATA_WIDTH => DATA_WIDTH,



            PHASE_WIDTH => PHASE_WIDTH,



            F1_OFFSET => 1000,



            F2_OFFSET => 3000



        )



        port map (



            clk => clk,



            reset => reset,



            rf_input => rf_input,



            freq_select => freq_select,



            i_data => i_data,



            q_data => q_data,



            phase_error => phase_error,



            vco_freq => vco_freq,



            lock_detect => lock_detect



        );



    



    -- RF Input Signal Generation



    process(clk)



        variable rand_val : real;



        variable current_freq : real;



        variable signal_amplitude : real;



        variable noise_component : real;



    begin



        if rising_edge(clk) then



            -- Select frequency based on freq_select



            if freq_select = '0' then



                current_freq := carrier_freq + 1000.0;  -- F1



            else



                current_freq := carrier_freq + 3000.0;  -- F2



            end if;



            



            -- Generate phase



            input_phase <= input_phase + (current_freq * 2.0 * MATH_PI * real(CLK_PERIOD / 1 sec));



            



            -- Add noise (uniform random)



            uniform(seed1, seed2, rand_val);



            noise_component := (rand_val - 0.5) * noise_level * 32767.0;



            



            -- Generate clean signal + noise



            signal_amplitude := 32767.0 * 0.8;  -- 80% of full scale



            rf_input <= to_signed(integer(



                signal_amplitude * cos(input_phase) + noise_component



            ), DATA_WIDTH);



        end if;



    end process;



    



    -- Main Test Sequence



    process



        variable l : line;



        variable lock_start_time : time;



    begin



        



        -- Initial setup



        write(l, string'("=== COSTAS LOOP MYSTERY INVESTIGATION ==="));



        writeline(output, l);



        write(l, string'("Testing for intermittent lock loss between F1 and F2..."));



        writeline(output, l);



        



        reset <= '1';



        freq_select <= '0';



        wait for 100 ns;



        reset <= '0';



        



        -- TEST 1: Lock to F1 and measure performance



        write(l, string'("TEST 1: Locking to F1 (1kHz offset)..."));



        writeline(output, l);



        test_phase <= 1;



        



        lock_start_time := now;



        wait until lock_detect = '1' for 50 us;



        



        if lock_detect = '1' then



            lock_time_f1 <= now - lock_start_time;



            write(l, string'("✓ F1 Lock achieved in "));



            write(l, now - lock_start_time);



            writeline(output, l);



        else



            write(l, string'("✗ F1 Lock FAILED - timeout"));



            writeline(output, l);



        end if;



        



        -- Let it settle and verify stability



        wait for 10 us;



        



        -- TEST 2: Switch to F2 and observe behavior



        write(l, string'("TEST 2: Switching to F2 (3kHz offset)..."));



        writeline(output, l);



        test_phase <= 2;



        



        freq_select <= '1';  -- Switch to F2



        lock_start_time := now;



        



        -- Wait a bit and check if lock is maintained or reacquired



        wait for 5 us;



        



        if lock_detect = '0' then



            write(l, string'("⚠ Lock lost during F2 transition!"));



            writeline(output, l);



            lock_lost_f2 <= true;



            



            -- Wait for reacquisition



            wait until lock_detect = '1' for 100 us;



            if lock_detect = '1' then



                lock_time_f2 <= now - lock_start_time;



                write(l, string'("✓ F2 Lock eventually reacquired in "));



                write(l, now - lock_start_time);



                writeline(output, l);



            else



                write(l, string'("✗ F2 Lock FAILED completely - timeout"));



                writeline(output, l);



            end if;



        else



            lock_time_f2 <= now - lock_start_time;



            write(l, string'("✓ F2 Lock maintained/acquired in "));



            write(l, now - lock_start_time);



            writeline(output, l);



        end if;



        



        -- TEST 3: Multiple transitions to expose intermittent behavior



        write(l, string'("TEST 3: Rapid F1/F2 transitions (stress test)..."));



        writeline(output, l);



        test_phase <= 3;



        



        for i in 1 to 5 loop



            -- F1



            freq_select <= '0';



            wait for 2 us;



            write(l, string'("Transition "));



            write(l, i);



            write(l, string'(" F1: Lock="));



            write(l, std_logic'image(lock_detect));



            writeline(output, l);



            



            -- F2  



            freq_select <= '1';



            wait for 2 us;



            write(l, string'("Transition "));



            write(l, i);



            write(l, string'(" F2: Lock="));



            write(l, std_logic'image(lock_detect));



            writeline(output, l);



        end loop;



        



        -- TEST 4: Add noise and see what happens



        write(l, string'("TEST 4: High noise environment test..."));



        writeline(output, l);



        test_phase <= 4;



        



        noise_level <= 0.3;  -- Increase to 30%



        freq_select <= '0';   -- Start with F1



        wait for 5 us;



        



        write(l, string'("F1 with 30% noise: Lock="));



        write(l, std_logic'image(lock_detect));



        writeline(output, l);



        



        freq_select <= '1';   -- Switch to F2



        wait for 10 us;



        



        write(l, string'("F2 with 30% noise: Lock="));



        write(l, std_logic'image(lock_detect));



        writeline(output, l);



        



        -- Final analysis



        write(l, string'(""));



        writeline(output, l);



        write(l, string'("=== INVESTIGATION SUMMARY ==="));



        writeline(output, l);



        write(l, string'("F1 lock time: "));



        write(l, lock_time_f1);



        writeline(output, l);



        write(l, string'("F2 lock time: "));



        write(l, lock_time_f2);



        writeline(output, l);



        write(l, string'("F2 lock lost during transition: "));



        write(l, boolean'image(lock_lost_f2));



        writeline(output, l);



        write(l, string'(""));



        writeline(output, l);



        write(l, string'("CLUE: Notice the dramatically different behavior between F1 and F2"));



        writeline(output, l);



        write(l, string'("CLUE: Check the loop gains when freq_select changes"));



        writeline(output, l);



        write(l, string'("CLUE: Error starvation occurs when correction signals become too weak"));



        writeline(output, l);



        



        wait;



    end process;



    



    -- Continuous monitoring for debugging



    process(clk)



        variable l : line;



        variable prev_lock : std_logic := '0';



    begin



        if rising_edge(clk) then



            -- Detect lock transitions for detailed analysis



            if lock_detect /= prev_lock then



                if lock_detect = '1' then



                    write(l, time'image(now));



                    write(l, string'(" LOCK ACQUIRED - F"));



                    if freq_select = '0' then



                        write(l, string'("1"));



                    else



                        write(l, string'("2"));



                    end if;



                    write(l, string'(" Phase Error: "));



                    write(l, integer'image(to_integer(phase_error)));



                    writeline(output, l);



                else



                    write(l, time'image(now));



                    write(l, string'(" LOCK LOST - F"));



                    if freq_select = '0' then



                        write(l, string'("1"));



                    else



                        write(l, string'("2"));



                    end if;



                    write(l, string'(" Phase Error: "));



                    write(l, integer'image(to_integer(phase_error)));



                    writeline(output, l);



                end if;



            end if;



            prev_lock := lock_detect;



        end if;



    end process;







end testbench;







-- WHAT TO LOOK FOR IN THE SIMULATION:



-- 1. F1 locks quickly and reliably



-- 2. F2 takes much longer to lock (if at all)



-- 3. Transitions from F1→F2 often cause lock loss



-- 4. Under noise, F2 performance degrades dramatically



-- 5. Phase error signals in F2 mode are much smaller



--



-- These symptoms point to ERROR STARVATION in F2 mode!



-- The next part will show the solution...
