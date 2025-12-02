-- PART 3: THE SOLUTION
-- Fixed Costas Loop with Proper Gain Management
--
-- This version eliminates error starvation while maintaining stability
-- across the frequency range using multiple complementary techniques.

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
use IEEE.MATH_REAL.ALL;

entity costas_loop_fixed is
    generic (
        DATA_WIDTH : integer := 16;
        PHASE_WIDTH : integer := 12;
        F1_OFFSET : integer := 1000;
        F2_OFFSET : integer := 3000
    );
    port (
        clk         : in  std_logic;
        reset       : in  std_logic;
        rf_input    : in  signed(DATA_WIDTH-1 downto 0);
        freq_select : in  std_logic;
        
        -- Outputs for comparison with original
        i_data      : out signed(DATA_WIDTH-1 downto 0);
        q_data      : out signed(DATA_WIDTH-1 downto 0);
        phase_error : out signed(DATA_WIDTH-1 downto 0);
        vco_freq    : out signed(PHASE_WIDTH-1 downto 0);
        lock_detect : out std_logic;
        
        -- Additional debug outputs
        effective_kp : out signed(7 downto 0);
        effective_ki : out signed(7 downto 0);
        error_power  : out unsigned(15 downto 0)
    );
end entity;

architecture fixed_behavioral of costas_loop_fixed is
    
    -- VCO signals
    signal vco_phase : signed(PHASE_WIDTH-1 downto 0) := (others => '0');
    signal vco_i, vco_q : signed(DATA_WIDTH-1 downto 0);
    signal vco_control : signed(DATA_WIDTH-1 downto 0) := (others => '0');
    
    -- Mixer outputs
    signal mixer_i, mixer_q : signed(DATA_WIDTH-1 downto 0);
    
    -- Loop filter components
    signal integrator : signed(DATA_WIDTH+4-1 downto 0) := (others => '0');
    signal error_signal : signed(DATA_WIDTH-1 downto 0);
    
    -- Lock detection with error power measurement
    signal error_magnitude : unsigned(DATA_WIDTH-1 downto 0);
    signal error_power_accum : unsigned(19 downto 0) := (others => '0');
    signal lock_counter : unsigned(15 downto 0) := (others => '0');
    
    -- SOLUTION 1: More conservative gain scaling
    constant BASE_KP : signed(7 downto 0) := to_signed(32, 8);
    constant BASE_KI : signed(7 downto 0) := to_signed(2, 8);
    
    -- SOLUTION 2: Error-magnitude-based adaptive gains
    signal adaptive_kp : signed(7 downto 0);
    signal adaptive_ki : signed(7 downto 0);
    signal error_boost : signed(3 downto 0);
    
    -- SOLUTION 3: Frequency-dependent but reasonable scaling
    signal freq_scale_kp : signed(7 downto 0);
    signal freq_scale_ki : signed(7 downto 0);
    
    -- SOLUTION 4: Anti-starvation monitoring
    signal starvation_detect : std_logic := '0';
    signal min_error_counter : unsigned(11 downto 0) := (others => '0');
    
begin

    -- SOLUTION 1: Conservative frequency-dependent scaling
    -- Instead of KP/4 and KI/8, use more moderate reductions
    process(freq_select)
    begin
        if freq_select = '0' then  -- F1 mode
            freq_scale_kp <= BASE_KP;                    -- Full gain
            freq_scale_ki <= BASE_KI;                    -- Full gain
        else  -- F2 mode - moderate reduction for stability
            freq_scale_kp <= shift_right(BASE_KP, 1);    -- KP/2 (was KP/4)
            freq_scale_ki <= shift_right(BASE_KI, 1);    -- KI/2 (was KI/8)
        end if;
    end process;
    
    -- SOLUTION 2: Error-magnitude-based boost to prevent starvation
    process(clk, reset)
        variable error_mag : unsigned(DATA_WIDTH-1 downto 0);
    begin
        if reset = '1' then
            error_boost <= (others => '0');
            error_power_accum <= (others => '0');
        elsif rising_edge(clk) then
            error_mag := unsigned(abs(error_signal));
            
            -- Accumulate error power for analysis
            if error_power_accum(19 downto 16) /= "1111" then
                error_power_accum <= error_power_accum + resize(error_mag, 20);
            end if;
            
            -- Adaptive boost when error signals are getting weak
            if error_mag < 50 and lock_detect = '0' then
                -- Boost gains when error is small but not locked (starvation!)
                if error_boost < 7 then
                    error_boost <= error_boost + 1;
                end if;
            elsif error_mag > 200 then
                -- Reduce boost when error is large (good correction available)
                if error_boost > 0 then
                    error_boost <= error_boost - 1;
                end if;
            end if;
        end if;
    end process;
    
    -- SOLUTION 3: Combine frequency scaling with error-based adaptation
    adaptive_kp <= freq_scale_kp + resize(error_boost, 8);
    adaptive_ki <= freq_scale_ki + resize(shift_right(error_boost, 1), 8);  -- Half boost for integral
    
    -- SOLUTION 4: Anti-starvation detection and intervention
    process(clk, reset)
    begin
        if reset = '1' then
            starvation_detect <= '0';
            min_error_counter <= (others => '0');
        elsif rising_edge(clk) then
            -- Detect prolonged periods of very small error (starvation symptom)
            if unsigned(abs(error_signal)) < 20 and lock_detect = '0' then
                if min_error_counter < 4095 then
                    min_error_counter <= min_error_counter + 1;
                end if;
            else
                min_error_counter <= (others => '0');
            end if;
            
            -- Flag starvation when error stays tiny for too long without lock
            starvation_detect <= '1' when min_error_counter > 1000 else '0';
        end if;
    end process;
    
    -- VCO phase accumulator (unchanged)
    process(clk, reset)
    begin
        if reset = '1' then
            vco_phase <= (others => '0');
        elsif rising_edge(clk) then
            vco_phase <= vco_phase + vco_control;
        end if;
    end process;
    
    -- VCO sine/cosine generation (unchanged)
    vco_i <= to_signed(integer(32767.0 * cos(real(to_integer(vco_phase)) * MATH_PI / 2048.0)), DATA_WIDTH);
    vco_q <= to_signed(integer(32767.0 * sin(real(to_integer(vco_phase)) * MATH_PI / 2048.0)), DATA_WIDTH);
    
    -- Quadrature mixers (unchanged)
    process(clk)
    begin
        if rising_edge(clk) then
            mixer_i <= shift_right(rf_input * vco_i, 15);
            mixer_q <= shift_right(rf_input * vco_q, 15);
        end if;
    end process;
    
    -- Costas loop error detector (unchanged)
    process(clk)
        variable q_sign : signed(DATA_WIDTH-1 downto 0);
    begin
        if rising_edge(clk) then
            if mixer_q >= 0 then
                q_sign := to_signed(1, DATA_WIDTH);
            else
                q_sign := to_signed(-1, DATA_WIDTH);
            end if;
            error_signal <= shift_right(mixer_i * q_sign, 8);
        end if;
    end process;
    
    -- FIXED Loop filter with anti-starvation measures
    process(clk, reset)
        variable scaled_error : signed(DATA_WIDTH+4-1 downto 0);
        variable prop_term : signed(DATA_WIDTH+4-1 downto 0);
        variable final_kp, final_ki : signed(7 downto 0);
    begin
        if reset = '1' then
            integrator <= (others => '0');
            vco_control <= (others => '0');
        elsif rising_edge(clk) then
            -- Apply additional boost if starvation detected
            if starvation_detect = '1' then
                final_kp := adaptive_kp + 16;  -- Emergency boost
                final_ki := adaptive_ki + 4;   -- Emergency boost
            else
                final_kp := adaptive_kp;
                final_ki := adaptive_ki;
            end if;
            
            -- Scale error by final adaptive gains
            scaled_error := resize(error_signal * final_ki, DATA_WIDTH+4);
            prop_term := resize(error_signal * final_kp, DATA_WIDTH+4);
            
            -- Integrate
            integrator <= integrator + scaled_error;
            
            -- PI controller output
            vco_control <= resize(shift_right(integrator + prop_term, 4), DATA_WIDTH);
        end if;
    end process;
    
    -- Enhanced lock detector with power-based thresholding
    process(clk, reset)
    begin
        if reset = '1' then
            lock_counter <= (others => '0');
            lock_detect <= '0';
        elsif rising_edge(clk) then
            error_magnitude <= unsigned(abs(error_signal));
            
            -- Adaptive lock threshold based on current error levels
            -- This prevents false lock declarations during starvation
            if error_magnitude < 150 and not starvation_detect = '1' then
                if lock_counter < 65535 then
                    lock_counter <= lock_counter + 1;
                end if;
            else
                lock_counter <= (others => '0');
            end if;
            
            -- Declare lock after consistent low-error period (non-starved)
            if lock_counter > 1000 then
                lock_detect <= '1';
            else
                lock_detect <= '0';
            end if;
        end if;
    end process;
    
    -- Output assignments
    i_data <= mixer_i;
    q_data <= mixer_q;
    phase_error <= error_signal;
    vco_freq <= resize(vco_control, PHASE_WIDTH);
    
    -- Debug outputs to show the fix in action
    effective_kp <= adaptive_kp + (16 when starvation_detect = '1' else 0);
    effective_ki <= adaptive_ki + (4 when starvation_detect = '1' else 0);
    error_power <= error_power_accum(19 downto 4);
    
end fixed_behavioral;

-- CONFIGURATION FOR COMPARISON TESTING
configuration compare_original_vs_fixed of tb_costas_mystery is
    for testbench
        -- Uncomment one of these to test:
        -- for DUT : costas_loop_puzzle use entity work.costas_loop_puzzle(behavioral);  -- Original buggy version
        for DUT : costas_loop_puzzle use entity work.costas_loop_fixed(fixed_behavioral);  -- Fixed version
    end for;
end configuration;

-- SOLUTION SUMMARY:
-- ==================
-- 
-- ERROR STARVATION occurs when loop gains are reduced so aggressively that
-- the correction signals become too weak to maintain lock, especially under
-- noise or disturbance conditions.
--
-- THE FIXES APPLIED:
-- 
-- 1. CONSERVATIVE GAIN SCALING: Instead of KP/4 and KI/8 at F2, use KP/2 and KI/2
--    This maintains sufficient loop authority while still improving stability
--
-- 2. ERROR-ADAPTIVE GAINS: Monitor error magnitude and boost gains when error 
--    signals are weak but lock hasn't been achieved (classic starvation symptom)
--
-- 3. STARVATION DETECTION: Explicitly detect prolonged periods of tiny error
--    without lock and apply emergency gain boost
--
-- 4. SMART LOCK DETECTION: Prevent false lock declarations during starvation
--    by considering error power context
--
-- ANALOGY: The original design was like trying to parallel park by making
-- increasingly tiny steering adjustments until you can't feel the wheel at all.
-- The fix ensures you always maintain enough "steering authority" to correct
-- course while still being smooth enough for stability.
--
-- KEY LESSON: In control systems, stability and responsiveness must be balanced.
-- Going too far in either direction creates failure modes - instability from
-- too much gain, or starvation from too little gain.

-- TEST RESULTS YOU SHOULD SEE:
-- - F1 and F2 both lock reliably
-- - Transition F1→F2 maintains lock or reacquires quickly  
-- - Performance degrades gracefully under noise (no sudden failures)
-- - Error signals remain healthy (not starved) in both modes
