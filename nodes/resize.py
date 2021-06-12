import numpy as np

def adjust_size(big, small, ei_matrix):
    '''Reduce bigger matrix to n x n where n: size of smaller matrix, by generating nCk subsets of big matrix.
    Input:
    - big (numpy array): bigger matrix which will be made smaller
    - small (numpy array): smaller matrix, for reference
    - ei_matrix (numpy array): EI matrix of bigger matrix
    Return:
    row, col: row and column from which the best subset starts.
    k: size(small matrix)
    resized: best nCk subset of bigger matrix
    ei_resized: subset of bigger EI matrix'''
    k = len(small)
    maxProduct = 0

    for r in range(0, len(big)-k+1):
        for c in range(0, len(big)-k+1):
            nCk = big[r:r+k, c:c+k]
            dot = np.sum(small * nCk)
            if dot > maxProduct:
                maxProduct = dot
                resized = nCk
                row, col = r, c

    ei_resized = ei_matrix[row:row+k, col:col+k]
    return row, col, k, resized, ei_resized
