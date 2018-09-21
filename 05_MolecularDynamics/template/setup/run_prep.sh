#!/bin/bash
#
# run_prep.sh

BINARIES=../../uiowa_bd/binaries
SCRIPTS=../../scripts

GOPREP=${BINARIES}/uiowa_goprep.16-06-12.exe

echo "Using protein.pdb from this directory."

# Generate the parameters for Go contacts (all of which are intramolecular)
INPUT=protein.inp
PREFIX=protein
${GOPREP} ${INPUT}

mv annotated.pdb                     ${PREFIX}.annotated.pdb
mv internal.parameters               ${PREFIX}.internal.parameters
mv centered.charge.parameters        ${PREFIX}.charge.parameters
mv uncentered.charge.parameters      ${PREFIX}.uncentered.charge.parameters
mv go.parameters                     ${PREFIX}.go.parameters
mv folded.restart                    ${PREFIX}.restart.file



# Move all the necessary files to the main simulation directory (../)
cp ${PREFIX}.charge.parameters ../
cp ${PREFIX}.internal.parameters ../

cp ${PREFIX}.go.parameters ../
cp ${PREFIX}.restart.file ../restart.file.initial
cp ${PREFIX}.restart.file ../restart.file
