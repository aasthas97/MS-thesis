# Main file to run for the whole pipeline
import get_data
import resize
import matrixdetails
import nodeidentity
import permutation

category_from = 1
category_to = 4

# load BPL data
allMatrices, allEI, allLengths = get_data.load(category_from, category_to)

for reference in allMatrices.keys():
    allDotProducts = [] # store reference vs others dot products
    for test in allMatrices.keys():
        print('%s against %s' % (reference, test))
        # get reference data
        ref_matrix = allMatrices[reference]
        ref_ei = allEI[reference]
        ref_lengths = allLengths[reference]
        # get test data
        test_matrix = allMatrices[test]
        test_ei = allEI[test]
        test_lengths = allLengths[test]
        if len(test_matrix) > 10: print('Skipping due to size.') # use break here so that everything else does not have to be put in an else loop
        else:
            # resize matrices
            ref_size = len(ref_matrix)
            test_size = len(test_matrix)
            if ref_size < test_size: 
                # make test_matrix small
                row, col, size, test_matrix, test_ei = resize.adjust_size(test_matrix, ref_matrix, test_ei)
            elif test_size < ref_size:
                # make ref small
                row, col, size, ref_matrix, ref_ei = resize.adjust_size(ref_matrix, test_matrix, ref_ei)                
            else:
                # no change
                pass
            
            ref_nodes, ref_strokes, ref_longest_stroke_num, ref_shortest_stroke_num = matrixdetails.get(ref_matrix, ref_ei, ref_lengths)
            ref_terminal = [node[0] for node in ref_nodes if node[1] is True]

            test_nodes, test_strokes, test_longest_stroke_num, test_shortest_stroke_num = matrixdetails.get(test_matrix, test_ei, test_lengths)
            test_terminal = [node[0] for node in test_nodes if node[1] is True]

            # get start and end nodes of longest stroke
            ref_longest_nodes = ref_strokes[ref_longest_stroke_num][0:2] # will always have a longest stroke so no if condition
            test_longest_nodes = test_strokes[test_longest_stroke_num][0:2]
            ref_shortest_nodes = ref_strokes[ref_shortest_stroke_num][0:2] if ref_shortest_stroke_num else None
            test_shortest_nodes = test_strokes[test_shortest_stroke_num][0:2] if test_shortest_stroke_num else None
            all_nodes = [node[0] for node in ref_nodes]
            identities = dict()
            for node in test_nodes:
                identities[node[0]] = []

            # assign identities to test nodes
            identities = nodeidentity.terminal(identities, test_terminal, ref_terminal) # terminal nodes
            identities = nodeidentity.long_stroke(identities, test_longest_nodes, ref_longest_nodes) # longest stroke
            if ref_shortest_nodes and test_shortest_nodes:
                identities = nodeidentity.short_stroke(identities, test_shortest_nodes, ref_shortest_nodes)
            identities = nodeidentity.others(identities, all_nodes)
            identities = permutation.findProbableNodes(identities, all_nodes)
            # get index permutations
            indices = permutation.getIdentityPermutations(identities)