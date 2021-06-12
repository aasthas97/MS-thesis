import itertools
import numpy as np

def getIdentityPermutations(identities):
    """Returns list of indices"""
    pos_copy = identities.copy()
    all_indices = []
    idx = []
    # first check elements with fixed values
    singval_id = [k for k, v in identities.items() if len(v) == 1]
    singvals = [v for k, v in identities.items() if len(v) == 1]
    for i in range(len(singval_id)):
        idx.insert(singval_id[i], singvals[i][0])
        del pos_copy[singval_id[i]]
    
    if len(pos_copy) == 0: # if no keys with >1 vals
        all_indices.append(idx)
        return all_indices
    
    # only keys with >1 vals left now
    while len(pos_copy) > 0:
        ks = list(pos_copy.keys())
        mulval = pos_copy[ks[0]]
        mul_ids = [k for k, v in pos_copy.items() if v == mulval]
        for a in mul_ids: del pos_copy[a]

        for perm in itertools.permutations(mulval):
            oneidx = [x for x in idx]
            [oneidx.insert(mul_ids[x], perm[x]) for x in range(len(mul_ids))]
            all_indices.append(oneidx)
#             print(oneidx)
    return all_indices

def findProbableNodes(identities, all_nodes):
    """Find out which node identities are more probable than others (based on frequency of occurrence).
    Eg. In {0: [0, 1, 1], 1: [0, 0, 1]}, 1 occurs more frequently for the key 0 and vice-versa.
    Return {0: [1], 1: [0]}"""
    for k in identities.keys():
        unique, counts = np.unique(identities[k], return_counts=True) # get # of times of occurrence of each item for each key
        nodeCounts = list(zip(unique, counts))
        probableNodes = [node[0] for node in nodeCounts if node[1] > 1] # values that occur more than once
        if probableNodes:
            identities[k] = probableNodes
            [all_nodes.remove(node) for node in probableNodes if node in all_nodes] # remove nodes that have been assigned already from all_nodes
            # for node in probableNodes:
            #     if node in all_nodes:
            #         all_nodes.remove(node)
        else: # if no value occurs more than others, assign all_nodes to the key
            identities[k] = all_nodes
    
    return identities