#!/usr/bin/env python3
#
# Read the frequency of a peak value from the RSA5065N Spectrum Analyzer
# Open Research Institute -- Remote Lab West
#
# https://github.com/phase4ground/documents
#
import pyvisa as visa
import time

nominal_frequency_hz = 905_050_000  # 0 for absolute frequency
number_of_measurements = 600

rm = visa.ResourceManager("@py")
sa = rm.open_resource("TCPIP::rsa5065n.sandiego.openresearch.institute::INSTR")

try:
    # We will use marker 8 (the last marker) to reduce the likelihood of conflict
    # with markers set by the operator.
    sa.write("CALCulate:MARKer8:MODE ON")  # enable the marker

    sample_time = round(time.time(), 1)  # round to nearest 0.1 second

    for i in range(0, number_of_measurements):
        sample_time = round(sample_time + 0.1, 1)  # wait for next 0.1 second boundary
        while time.time() < sample_time:
            pass
        sa.write("CALCulate:MARKer8:MAXimum:MAX")  # move the marker to the peak
        marker_freq = float(
            sa.query("CALCulate:MARKer8:X?")
        )  # read the frequency of the peak
        print(f"{sample_time:.1f} {marker_freq - nominal_frequency_hz:.1f}")

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    sa.write("CALCulate:MARKer8:MODE OFF")  # done with the marker, disable it
    sa.close()
    rm.close()
