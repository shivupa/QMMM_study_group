#!/bin/bash
# 
# Run the UIOWA_BD simulation
#

# Path to the UIOWA BD binary.
# Currently, the binary specified represents a static compilation using Intel's
# ifort compiler, along with the -O2 option (second level of optimization). I 
# find this gives good speed.
UIOWA_BD=../../uiowa_bd/binaries/uiowa_bd_45-07-12-o2

# Make sure the necessary directories are set up.
if [ ! -d MOVIE ]; then
  mkdir MOVIE
fi

if [ ! -d OUTPUT ]; then
  mkdir OUTPUT
fi

if [ ! -d RESTARTS ]; then
  mkdir RESTARTS
fi

# Make sure there is a restart.file
if [ ! -e restart.file ]; then
  echo "Using restart.file.initial as the initial configuration of the system."
  cp restart.file.initial restart.file
fi

### Run the simualtion ###
# For the UIOWA BD main binary, you need to specify the input parameters via 
# STDIN. I use redirects to do this.
# sim.out contains log information.
# Information on the arguments:
#   - The first argument is the random seed. This should be less than (2^31-1)
#   - The second and third integers are "multiplicative factors" for determining
#     memory usage.  Just leave them as 1 and 1.
${UIOWA_BD} 100 1 1 < sim.inp > sim.out

# Note that coordinates are found in the testout.xtc file.
