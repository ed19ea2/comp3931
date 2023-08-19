'''
data = [
    [5, 50, 51, 95],
    [5, 10, 50, 51],
    [10, 50, 51, 100],
    [15, 50, 51 , 100],
    [0, 15, 50, 51],
    [0, 50, 51, 95]
    ]

tree = [[5, 50, 51, 95]]
'''

data = [
    [10, 14, 17, 20],
    [10, 14, 17, 29],
    [0, 10, 14, 29],
    [0, 10, 14, 16],
    [10, 14, 16, 25],
    [10, 14, 20, 25]
    ]

tree = [[10, 14, 17, 20]] #expected [[0, 10, 14, 16, 17, 20, 25], [17, 29]]

'''
data = [
    [0, 10, 14, 16],
    [0, 10, 14, 30],
    [0, 10, 20, 30],
    [0, 10, 15, 20],
    [0, 10, 11, 15],
    [0, 10, 11, 16]
    ]

tree = [[0, 10, 14, 16]] #expected [[0, 10, 11, 14, 16], [14, 15, 20, 30]]
'''

#Computing a contour tree with determined tetrahedra (Freudenthal) and respective vertices of each tetrahedra

newCreated = False

for tet in range(6): #using indexes to easily check previous tet/vertex/branch on tree
    print("\n**current tet:", tet, "contains", data[tet], "**")
    print(tree,"\n")
    if tet == 0: #first tet is already in the contour tree
        continue
    else:
        for vertex in range(4):
            if data[tet][vertex] in data[tet-1] or data[tet][vertex] in tree[0]:
                print(data[tet][vertex], "of tet", tet, "exists in previous tet or is already in the tree")
                continue
            if data[tet][vertex] > max(tree[0]):

#TODO: Check if the contour of the current tet overlaps with a branch that was made from the previous tet, i.e. adding a vertex to a branch
### Currently, a branch contains no more than 2 vertices. Test with 3rd dataset.
                
                if newCreated: #if a new branch on the current tet has already been made
                    tree[len(tree)-1].append(data[tet][vertex]) #add current vertex to most recently made branch
                    tree[len(tree)-1].sort() #sort the most recently made branch in asc. order
                    print("vertex added to new branch")
                else:
                    tree.append([data[tet][vertex-1],data[tet][vertex]]) #add new branch that contains the previous vertex and the current vertex
                    newCreated == True #set flag to say that a new branch has been made in this tet
                    print("* new branch created from", data[tet][vertex], "of tet", tet)
                    
#TODO: Check if any branches can be collapsed, i.e. if a branch can be merged into tree[0] if the max value of tree[0] is part of a contour that
#       has a max value > max value of tree[0]. Test with 2nd dataset.
                    
            else:
                tree[0].append(data[tet][vertex]) #add the current vertex to tree[0]
                print("*", data[tet][vertex], "added to tree[0]")
                tree[0].sort()

print("\n")
print(tree)
                


