'''Assign possible identities to nodes'''

def terminal(identity_dict, test_terminal, ref_terminal):
    
    for terminalNode in test_terminal:
        identity_dict[terminalNode] = [node for node in ref_terminal]
    return identity_dict

def long_stroke(identities, test_long_nodes, ref_long_nodes):
    for node in test_long_nodes:
        identities[node].append(ref_long_nodes[0])
        identities[node].append(ref_long_nodes[1])
    return identities

def short_stroke(identities, test_short_nodes, ref_short_nodes):
    for node in test_short_nodes:
        identities[node].append(ref_short_nodes[0])
        identities[node].append(ref_short_nodes[1])
    return identities

def others(identities, all_nodes):
    nodes_used = set([item for sublist in identities.values() for item in sublist])
    nodes_remaining = [node for node in all_nodes if node not in nodes_used]
    for key in identities.keys():
        if not identities[key]:
            identities[key] = nodes_remaining
            
    return identities
