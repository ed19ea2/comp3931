import copy
# uncomment and recomment datasets as necessary.
data = [
    [[5, 50], [50, 51], [51, 95]],
    [[5, 10], [10, 50], [50, 51]],
    [[10, 50], [50, 51], [51, 100]],
    [[15, 50], [50, 51], [51, 100]],
    [[0, 15], [15, 50], [50, 51]],
    [[0, 50], [50, 51], [51, 95]]
    ]

vertices = [0, 5, 10, 15, 50, 51, 95, 100]

tree = [[[5, 50], [50, 51], [51, 95]]]

'''
data = [
    [[10, 14], [14, 17], [17, 20]],
    [[10, 14], [14, 17], [17, 29]],
    [[0, 10], [10, 14], [14, 29]],
    [[0, 10], [10, 14], [14, 16]],
    [[10, 14], [14, 16], [16, 25]],
    [[10, 14], [14, 20], [20, 25]]
    ]

vertices = [0, 10, 14, 16, 17, 20, 25, 29]

tree = [[[10, 14], [14, 17], [17, 20]]]
'''
'''
data = [
    [[0, 10], [10, 14], [14, 16]],
    [[0, 10], [10, 14], [14, 30]],
    [[0, 10], [10, 20], [20, 30]],
    [[0, 10], [10, 15], [15, 20]],
    [[0, 10], [10, 11], [11, 15]],
    [[0, 10], [10, 11], [11, 16]]
    ]

vertices = [0, 10, 11, 14, 15, 16, 20, 30]

tree = [[[0, 10], [10, 14], [14, 16]]] 
'''

# Computing a contour tree with determined tetrahedra (Freudenthal) and edge arcs of respective tetrahedra

for tet in range(6): #using indexes to easily check previous tet/vertex/branch on tree
    print("\n**current tet:", tet, "contains", data[tet], "**")
    print(tree,"\n")
    if tet == 0: #first tet is already in the contour tree
        continue
    else:
        for arc in range(3):
            if data[tet][arc] in data[tet-1] or data[tet][arc] in tree[0]:
                print(data[tet][arc], "of tet", tet, "exists in previous tet or is already in the tree")
                continue
            if data[tet][arc][0] < min(tree[0][0]): #current arc lower than lowest arc on tree
                print("$\/$ new lowest arc", data[tet][arc], "which updates", min(tree[0]))
                tree[0].append([data[tet][arc][0], min(tree[0][0])])
                tree[0].sort()
                continue
            if data[tet][arc] > max(tree[0]): #current arc higher than highest arc on tree
                print("$/\$ new highest arc", data[tet][arc], "which updates", max(tree[0]))
                tree.append([data[tet][arc]])
            else:
                tree[0].append(data[tet][arc])
                print("$$$", data[tet][arc], "added to tree[0]")
                tree[0].sort()

print("\n")
                
# "Zipping up" / merging the tree which must be after the initial tree is computed

zippedTree = copy.deepcopy(tree) # make an independent copy of the initial tree, not a reference to it 


# first merge along branches
print(tree, "\n")
for branch in range(len(tree)):
    for arc in range(len(tree[branch])-2): # -2 since we don't check the first or last arc of the branch
        if vertices.index(tree[branch][arc][1]) != vertices.index(tree[branch][arc][0])+1: #check if the head of the current arc is not the next higher unique value after the tail
            print(tree[branch][arc],"removed from tree")
            arcToRemove = tree[branch][arc]
            zippedTree[branch].remove(arcToRemove)

# then check if there are any branches that can be added to tree[0], i.e. if the tail of the arc of the branch is equal to the tail of the last arc on tree[0]
for branch in range(len(zippedTree)):
    if zippedTree[branch][0][0] == zippedTree[0][-1][1]:
        print(zippedTree[branch], "has been merged")
        zippedTree[0].append(zippedTree[branch][0])
        zippedTree.remove(tree[branch])

print("\nTree before zipping:")
print(tree)
print("Final tree:")
print(zippedTree)









            
            
