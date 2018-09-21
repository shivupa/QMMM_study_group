#!/usr/bin/env python
import argparse
import numpy
import os
import sys
sys.path.append(os.path.realpath(__file__))
import rmsd
import MDAnalysis

'''
---------
Script
---------
This script takes an xtc trajectory file generated from a UIOWA-BD simulation and a pdb file for the protein of interest
and calculates the RMS deviation between each frame in the trajectory and the reference pdb structure

Resulting RMS deviation values for each frame are outputted to a text file named 'output.txt' (or whatever name the
user specifies

---------
Notes
---------
This script should be run from the main simulation directory with the command 'python (path to script) > output.txt'

The rmsd.py script must be located in the same directory as the xtc_rmsd.py script when this script is run

The pdb files must be 'go' models (not full atom models) and can be taken from the first frame located in the output
MOVIE directory
'''

def xtc2numpyarray(xtcfilepath, pdbfilepath):
    '''
    Loads coordinates from an xtc trajectory file and returns a numpy array,
    using a pdb file as the topology.

    ---------
    Arguments
    ---------
    xtcfilepath: (str) path to the xtc file
    pdbfilepath: (str) path to the pdb file

    ---------
    Returns
    ---------
    coords_arr: (numpy.ndarray) numpy array of shape (nframes, natoms, 3) 
    representing coordinates of each frame in trajectory
    '''

    f = MDAnalysis.Universe(pdbfilepath, xtcfilepath)
    coords = []
    for frame in f.trajectory:
        coords.append(f.atoms.positions)
    coords_arr = numpy.asarray(coords)
    return coords_arr

def pdb2numpyarray(pdbfilepath):
    '''
    Loads a pdb file and returns a numpy array of the coordinates

    ---------
    Arguments
    ---------
    filepath: (str) path to the pdb file

    ---------
    Returns
    ---------
    coords_arr: (numpy.ndarray) numpy array of shape (nframes, natoms, 3) 
    representing coordinates of reference structure
    ''' 

    f = MDAnalysis.Universe(pdbfilepath)
    coords = f.atoms.positions
    coords_arr = numpy.asarray(coords)
    return coords_arr

def parse_arguments():
    '''
    Parses command lines arguments.

    --------
    Returns
    --------
    pdbpath: (str) The file path to the reference pdb, which is also used as a 
        topology file for the xtc file

    xtcpath: (str) The file path the xtc trajectory file.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdb', dest='pdbpath', required=True,
                        help="The file path to the reference PDB, which is used"
                             " both as the reference structure and topology "
                             "file for the XTC trajectory file."
                        )
    parser.add_argument('--xtc', dest='xtcpath', required=True,
                        help="The file path to the XTC trajectory file."
                        )
    args = parser.parse_args()
    return args.pdbpath, args.xtcpath


def main():
    '''
    Run the main function.
    '''
    # First, parse command line arguments
    pdbpath, xtcpath = parse_arguments()

    # Get numpy array of coordinates for trajectory
    # Again, note the pdb files must be 'go'models and not full-atom models
    coordinates = xtc2numpyarray(xtcpath, pdbpath)

    # Get numpy array of coordinates for reference structure
    ref_coordinates = pdb2numpyarray(pdbpath)

    # Iterate through the frames of the trajectory and calculate the RMS 
    # deviation relative to the ref_coordinates
    rmsd_list = []
    for frame in coordinates:

        # This module is from the rmsd.py script that must be in the same directory
        # as this script
        r = rmsd.rmsd(frame, ref_coordinates)
        rmsd_list.append(r) 
        numpy.savetxt("rmsd.txt", rmsd_list)

if __name__ == "__main__":
    main()
