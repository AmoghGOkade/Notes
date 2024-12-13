def kruskal(Wlist):
    edges = []
    component = {}
    tree_edges = []
    for u in Wlist.keys():
        '''edges.extend([(d, u, v) for (v, d) in Wlist[u]])'''
        for (v, d) in Wlist[u]:
            edges.append((d, u, v))
            
        component[u] = u
        
    edges.sort()    # we have used the weight as the 1st index in edges, so it gets sorted based on that

    for (d, u, v) in edges:
        if component[u] != component[v]:    #edge doesn't create a cycle
            tree_edges.append((u, v))
            c_old = component[u]        #can't write component[u] instead of c_old in the bottom line because component[u] might get changed before changing all nodes that have component[u]
            for i in Wlist.keys():
                if component[i] == c_old:   #if a node is of component u, change it to component v
                    component[i] = component[v]

    return tree_edges

#Using union-find data structure (faster)
def kruskal_fast(Wlist):
    edges = []
    mcst_edges = []
    for u in Wlist.keys():
        '''edges.extend([(d, u, v) for (v, d) in Wlist[u]])'''
        for (v, d) in Wlist[u]:
            edges.append((d, u, v))
    
    component = {}
    members = {}  #key - component name, value - list of vertices belonging to that component
    size = {}   #component name: no. of vertices belonging to it
    for i in Wlist.keys():
        component[i] = i
        members[i] = [i]
        size[i] = 1
    
    for (u, v, d) in edges:
        if component[u] != component[v]:
            mcst_edges.append((u, v, d))
            if size[component[u]] > size[component[v]]:
                c_old = component[v]
                c_new = component[u]
            else:
                c_old = component[u]
                c_new = component[v]
            
            for i in members[c_old]:
                component[i] = c_new
                members[c_new].append(i)    #need not destroy c_old data of members and size, because it is never being used
                size[c_new]+=1

    return mcst_edges
