# Project Reports

Your report welcome here!

## Embiggener Test Results

On 2022-11-09, we ran the new `axi_embiggener.vhd` module through its testbench with
```
./run.py --gui <testname>
```
and grabbed screen shots from gtkwave. This module is a specialized upsizer for the AXI-Stream-like interface between the DVB-S2 Encoder and the DAC FIFO found in the Analog Devices ADRV-9371 ZC706 reference design. It purpose is to convert the 32-bit output of the Encoder (16 bits I, 16 bits Q) into the 128-bit input to the DAC FIFO (I Q I Q I Q I Q) as configured for single-DAC output.

### Back-to-Back Frames Test

This test shows frames being transferred without delays.

![Back to back frames](https://user-images.githubusercontent.com/5356541/201252145-62e9ddaa-925a-492b-873f-d23a1faadbbe.png "Back to back frames")

You can see that `s_tready` and `s_tvalid` are both asserted continuously, so that the input interface to the embiggener is running an AXI-S style transfer on every clock cycle. However, `m_tvalid` is only asserted on every fourth cycle.

### Slow Master Frames Test

This test shows frames being transferred with some extra delays imposed by the encoder (supplying 32-bit frames to the input interface).

![Slow Master frames](https://user-images.githubusercontent.com/5356541/201252285-84690474-17a7-4ff9-a115-155fb3d2a388.png "Slow Master frames")

You can see that `s_tready` and `s_tvalid` are no longer asserted continuously, so that the input interface to the embiggener sometimes has to wait for additional input to arrive. `m_tvalid` also has to wait until all four 32-bit input words have been received.

### Slow Slave Frames Test

This test shows frames being transferred with some extra delays imposed by the DAC FIFO (consuming 128-bit frames from the output interface).

![Slow Slave frames](https://user-images.githubusercontent.com/5356541/201252281-b81771e1-6cd2-428f-b8f6-9b331736b89e.png "Slow Slave frames")

You can see that `m_tready` sometimes goes low, so that the output interface from the embiggener cannot always transfer the 128-byte frame when it is ready. It then has to deassert s_tready so that the encoder holds the data until we are ready for it.

### Slow Both Frames Test

This test shows frames being transferred with delays imposed by both the provider and the consumer.

![Slow Both frames](https://user-images.githubusercontent.com/5356541/201252287-b96bd787-49e8-442f-96fa-d14d8cd25ea6.png "Slow Both frames")

You can see a combination of the behaviors shown above.

### Conclusion

All tests appear to be passing.

### Encoder Standalone Implementation with Embiggener

Integration completed. Synthesis completed. Implementation passed. 

### Reference Design with Modified Encoder

Integration completed. Synthesis completed. 
