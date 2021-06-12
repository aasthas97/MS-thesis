import pandas as pd
import numpy as np

def load(from_, to_):
    """Loads the adjacency and EI matrices, and length array.
    Inputs:
    from_ (int): item number from which to start
    to_ (int): item number at which to stop (not included)"""

    allMatrices = dict()
    for imnumber in range(from_, to_):
        for skelnumber in range(1, 11):
            fname = '%d_%d' % (imnumber, skelnumber)
            fpath = 'C:/Users/aasth/Documents/Thesis/BPL/' + fname+'matrix.csv'
            matrix_df = pd.read_csv(fpath, header = None)
            matrixArray = matrix_df.to_numpy()
            allMatrices[fname] = matrixArray
    
    print('Matrices loaded.')

    allLengths = dict()
    for imnumber in range(from_, to_):
        for skelnumber in range(1, 11):
            fname = '%d_%d' % (imnumber, skelnumber)
            fpath = 'C:/Users/aasth/Documents/Thesis/BPL/' + fname+'lengths.csv'
            len_df = pd.read_csv(fpath, header = None)
            lenList = len_df[0].values.tolist()
            lenList_norm = normLength(lenList) # normalize lengths
            allLengths[fname] = lenList_norm

    print('Lengths loaded.')

    allEI = dict()
    for imnumber in range(from_, to_):
        for skelnumber in range(1, 11):
            fname = '%d_%d' % (imnumber, skelnumber)
            fpath = 'C:/Users/aasth/Documents/Thesis/BPL/' + fname+'eimatrix.csv'
            ei_df = pd.read_csv(fpath, header = None)
            ei_df = ei_df.fillna(0)
            eiArray = ei_df.to_numpy()
            allEI[fname] = eiArray
            
    print('EI matrices loaded.')

    return allMatrices, allEI, allLengths

def normLength(lenList):
    """Normalizes lengths by dividing by the max value.
    Input: lenList (array) containing length values (int/float)
    Output: lenListNorm (array) containing normalized length values (float)."""

    normfactor = max(lenList)
    lenListNorm = [length/normfactor for length in lenList]
    return lenListNorm 