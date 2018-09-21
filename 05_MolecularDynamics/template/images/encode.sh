#!/bin/sh
#
# encode.sh
#
# Script for encoding images to a movie.  The images should be numbered, with 
# zero-padding. The movie is encoded with the h.264 codec (the same codec used 
# in high-definition movies).
#
# This script must be run from the directory containing the saved frames.

# Set the mplayer environment variables (change for your configuration)
LD_LIBRARY_PATH=/local/usr/lib; export LD_LIBRARY_PATH
PATH=${PATH}:/local/usr/bin; export PATH

# convert targa to png
for i in *.tga; do
  PREFIX=$(basename ${i} .tga)
  convert ${i} ${PREFIX}.sgi
done

# This script is meant to be used with 1280x720 images
WIDTH=$(identify -format "%w" ${PREFIX}.sgi)
HEIGHT=$(identify -format "%h" ${PREFIX}.sgi)

# high motion = 5928 kbps
# moderate motion  = 4512 kbps
mencoder \
  -ovc x264 \
  -x264encopts pass=1:turbo:bitrate=5928:bframes=1:subq=6:frameref=6:me=hex:partitions=all:threads=auto:keyint=300 \
  -mf type=sgi:w=${WIDTH}:h=${HEIGHT}:fps=60 \
  -nosound \
  -o /dev/null mf://\*.sgi

mencoder \
  -ovc x264 \
  -x264encopts pass=2:turbo:bitrate=5928:bframes=1:subq=6:frameref=6:me=hex:partitions=all:threads=auto:keyint=300 \
  -mf type=sgi:w=${WIDTH}:h=${HEIGHT}:fps=60 \
  -nosound \
  -o gfp.mov mf://\*.sgi
