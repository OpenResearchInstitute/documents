#!/bin/bash
# This is an example script used for checking out and using a floating
# Vivado license from the ORI license server. For instructions and details, see:
# https://github.com/phase4ground/documents/blob/master/Remote_Labs/Working-With-FPGAs.md

# connect to server
ssh -f -N -L 127.0.0.1:2100:127.0.0.1:2100 -L 127.0.0.1:2101:127.0.0.1:2101 your-github-username@flexlm-server.openresearch.institute

# report status on the tunnels
lsof -i :2100

# set the license server location
export XILINXD_LICENSE_FILE=2100@127.0.0.1

# start Vivado
. /tools/Xilinx/Vivado/2020.2/settings64.sh
/tools/Xilinx/Vivado/2020.2/bin/vivado

# drop the tunnels to the license server
kill -HUP `lsof -t -i :2100`

# report status on the tunnels (silent if the kill succeeded)
lsof -i :2100
