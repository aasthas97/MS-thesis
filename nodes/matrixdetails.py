import numpy as np

def get(matrix, ei_matrix, lengths):
    """Return
    nodes (list): [[node_label, terminal_or_not]]
    strokes (dict): {strokenumber: [start_point, end_point, length]}
    longest_stroke, shortest_stroke (int): stroke numbers
    """
    nodes = []
    for i in range(len(matrix)):
        nodes.append([i])
        # check if terminal
        unique, counts = np.unique(matrix[i], return_counts=True)
        counts = dict(zip(unique, counts))
        if 1 in counts.keys() and counts[1] == 1: # terminal node
            nodes[i].append(True)
        else:
            nodes[i].append(False)

    strokes = dict()
    maxLen = 0
    minLen = 1
    shortest_stroke = None # set to none to avoid errors when there is only 1 stroke and hence, no smallest stroke
    longest_stroke = None

    for rownumber in range(len(ei_matrix)):
        columns = np.where(ei_matrix[rownumber] != 0)[0] # columns with which row is connected
        stroke_nums = ei_matrix[rownumber, columns] # strokes that connect rownumber and columns
        for stroke in stroke_nums:
            if stroke not in strokes:
                row, col = np.where(ei_matrix == stroke)[0][0], np.where(ei_matrix == stroke)[1][0]
                strokes[stroke] = [nodes[row][0], nodes[col][0], lengths[int(stroke-1)]]
                if lengths[int(stroke-1)] > maxLen:
                    maxLen = lengths[int(stroke-1)]
                    longest_stroke = stroke
                if lengths[int(stroke-1)] < minLen and stroke != longest_stroke:
                    minLen = lengths[int(stroke-1)]
                    shortest_stroke = stroke

    return nodes, strokes, longest_stroke, shortest_stroke