#!/usr/bin/env python
import numpy
import scipy.spatial.distance

def distance_squared(p0, p1):
    '''
    Find the square of the distance between ``p0`` and ``p1``.

    ---------
    Arguments
    ---------
    p0: (numpy.ndarray) A shape (3,) array representing x,y,z coordinates
    p1: (numpy.ndarray) A shape (3,) array representing x,y,z coordinates

    -------
    Returns
    -------
    d2: square of the euclidean distance between ``p0`` and ``p1``.
    '''
    return scipy.spatial.distance.euclidean(p0,p1)**2

def centroid(coordinates):
    '''
    Find the centroid of ``coordinates``.

    ---------
    Arguments
    ---------
    coordinates: (numpy.ndarray) A shape (natoms, 3) array of coordinates

    -------
    Returns
    -------
    c: (numpy.ndarray) A shape  (1,3) array of coordinates indicating the center
        of geometry of ``coordinates``.
    '''
    return coordinates.mean(axis=0)[numpy.newaxis,:]

def rmsd(mobile, reference): 
    '''
    Calculates the RMS deviation between two structures following least-
    squares alignment. Uses the Kabsh algorithm.

    ---------
    Arguments
    ---------
    mobile: (numpy.ndarray) shape (natoms, 3) numpy array, where natoms is the 
        number of atoms, representing the coordinates of the protein for which
        to calculate the RMS deviation 

    reference: (numpy.ndarray) shape (natoms, 3) numpy array representing the 
        reference structure.

    -------
    Returns
    -------
    mobile: (float) The RMS deviation of ``mobile`` relative to ``reference``,
        calculated via the following equation:

        RMS deviation =  sqrt( sum( (x_0,i-x_1,i)^2 + (y_0,i - y_1,i)^2 + (z_0,i - z_1,i)^2 ))
        
        where i runs over the atom index (from 0 to natoms-1), and the 
        calculation is performed following least-squares alignment.
    '''
    
    # Center both mobile and reference on centroid.
    c = centroid(reference) 
    reference -= c
    c = centroid(mobile)
    mobile -= c
    
    # Use Kabsch algorithm to calculate optimal rotation matrix.
    # Calculate covariance matrix.
    covariance_matrix = numpy.dot(numpy.transpose(reference), 
                                  mobile)
    
    # Singular Value Decomposition.
    V, S, Wt = numpy.linalg.svd(covariance_matrix)
    d = numpy.sign(numpy.linalg.det(numpy.dot(numpy.transpose(Wt),
                                              numpy.transpose(V)
                                              )
                                    )
                   )
    
    U = numpy.dot(numpy.transpose(Wt), 
               numpy.dot(numpy.array(((1,0,0),
                                      (0,1,0),
                                      (0,0,d))), 
                         numpy.transpose(V)
                         )
                  )
    
    # Multiplying mobile (n*3 matrix) by 3*3 optimal rotation matrix
    # ``U`` gives least_squares alignment.
    l_aligned = mobile.dot(U)
    
    # Sum distances squared over each particle, and take the square root to 
    # return RMSD.
    square_sum = 0
    for i in range(len(l_aligned)):
        square_sum += distance_squared(l_aligned[i],reference[i])
    av = square_sum/len(l_aligned)
    rmsd_ = numpy.sqrt(av)
    return rmsd_
