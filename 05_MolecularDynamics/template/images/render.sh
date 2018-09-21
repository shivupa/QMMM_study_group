#!/bin/bash

for i in *.tachyon; do
  PREFIX=$(basename ${i} .tachyon)
  cat ${i} | sed -e 's/Resolution [[:digit:]]\+\s[[:digit:]]\+/Resolution 1280 720/' > temp.tachyon
  tachyon temp.tachyon -o ${PREFIX}.tga
done

