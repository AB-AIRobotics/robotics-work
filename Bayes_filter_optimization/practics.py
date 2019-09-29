import numpy as np 

gridMap = np.ones((10,10)) # made a numpy 2D-array of all ones 
#print gridMap
# walls = np.array([[1,1],[4,5],[8,9],[9,9],[3,4],[5,5],[9,7],[9,1],[2,7],[0,9]]) # made a numpy 1D-array of having coordinates/2D-grid
# cells defining the obstacles(walls) 
walls = [[1,1],[4,5],[8,9],[9,9],[3,4],[5,5],[9,7],[9,1],[2,7],[0,9]] # made a list of coordinates on grid, defining the obstacles grid cells

for wall in walls: # iterate over loop and assign obstacles gird cells with a value integer 0 
    gridMap[wall[0], wall[1]] = 0

print "Original Grid map"
print gridMap #printing the updates 2D-girdmap

'''
# assigning the corresponding (y,x) grid cells with a value integer 0
gridMap[1,1]=0
gridMap[1,3]=0
gridMap[7,1]=0
gridMap[7,4]=0
gridMap[9,1]=0
gridMap[8,5]=0
gridMap[3,9]=0
gridMap[5,5]=0
gridMap[2,0]=0
gridMap[7,1]=0
gridMap[4,5]=0
gridMap[5,5]=0
gridMap[6,6]=0
gridMap[7,7]=0
'''
'''
# assigning the corresponding (y,x) grid cells with a value integer 1 using for loop
for i in range(gridMap.shape[0]):
    for j in range(gridMap.shape[1]):
        if(i == 1 and j ==1):
            gridMap[i,j] = 1
        if(i == 1 and j ==5):
            gridMap[i,j] = 1
        if(i == 2 and j ==1):
            gridMap[i,j] = 1
        if(i == 5 and j ==7):
            gridMap[i,j] = 1
        if(i == 4 and j ==9):
            gridMap[i,j] = 1
        if(i == 3 and j ==6):
            gridMap[i,j] = 1
        if(i == 7 and j ==3):
            gridMap[i,j] = 1
        if(i == 8 and j ==9):
            gridMap[i,j] = 1
        if(i == 9 and j ==5):
            gridMap[i,j] = 1
        if(i == 2 and j ==6):
            gridMap[i,j] = 1
'''
#print gridMap

beliefMap = np.ones((10,10)) # define a same dimension 2D-numpy array 
mapSum = np.sum(beliefMap) # calculating the sum of all elements in 2D-numpy array
# iterate over al the elements of 2D-numpy array and divide each element by total sum of all the elements for 
#for i in range(beliefMap.shape[0]):  # calculating uniform probability distrubtion 
#    for j in range(beliefMap.shape[1]):
    #    beliefMap[i,j] = beliefMap/mapSum
beliefMap = beliefMap/mapSum

print "Upadated belief map"
print beliefMap

fusedBeliefMap = beliefMap * gridMap
fusedmapsum = np.sum(fusedBeliefMap)
#print fusedmapsum
# when grid map is multiplyied with belife map
print "Fused map"
print fusedBeliefMap

# re normalizing 

# for i in range(fusedBeliefMap.shape[0]):
#     for j in range(fusedBeliefMap.shape[1]):
newSum = np.sum(fusedBeliefMap)
print newSum
normfusedBeliefMap = fusedBeliefMap/newSum
print "Normalized Fused belive map"
print normfusedBeliefMap



while(x<(normfusedBeliefMap.shape[0]-1) and y<(normfusedBeliefMap.shape[1]-1)):
    for x in range(normfusedBeliefMap.shape[0]):
        for y in range(normfusedBeliefMap.shape[1]):
            #print x, " ", y
            if (normfusedBeliefMap[x,y] == 0):
                normfusedBeliefMap[x,y]=0.4
            else:
                normfusedBeliefMap[x,y]=0.6
#print normfusedBeliefMap


 '''
            print "dist_obst2", distobs2 = calculateDistance(x,wall[1][1],y,walls[1][1])
            print "dist_obst3", distobs3 = calculateDistance(x,wall[2][2],y,walls[2][2])
            print "dist_obst4", distobs4 = calculateDistance(x,wall[3][3],y,walls[3][3])
            print "dist_obst5", distobs5 = calculateDistance(x,wall[4][4],y,walls[4][4])
            print "dist_obst6", distobs6 = calculateDistance(x,wall[5][5],y,walls[5][5])
            print "dist_obst7", distobs7 = calculateDistance(x,wall[6][6],y,walls[6][6])
            print "dist_obst8", distobs8 = calculateDistance(x,wall[7][7],y,walls[7][7])
            print "dist_obst9", distobs9 = calculateDistance(x,wall[8][8],y,walls[8][8])
            print "dist_obst10", distobs10 = calculateDistance(x,wall[9][9],y,walls[9][9])
            '''
