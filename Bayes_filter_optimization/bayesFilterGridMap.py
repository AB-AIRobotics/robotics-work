import numpy as np 


# Step no. 1
gridMap = np.ones((10,10)) # made a numpy 2D-array of all ones 
print "Grid map"
print gridMap
# cells defining the obstacles(walls) 
walls = [[1,1],[4,5],[8,9],[9,9],[3,4],[5,5],[9,7],[9,1],[2,7],[0,9]] # made a list of coordinates on grid, defining the obstacles grid cells

for wall in walls: # iterate over loop and assign obstacles gird cells with a value integer 0 
    gridMap[wall[0], wall[1]] = 0

print "Update grid map with Obstacles"
print gridMap #printing the updates 2D-girdmap


# Step no. 2
beliefMap = np.ones((10,10)) # define a same dimension 2D-numpy array 
mapSum = np.sum(beliefMap) # calculating the sum of all elements in 2D-numpy array
# iterate over all the elements of 2D-numpy array and divide each element by total
# sum of all the elements for calculating uniform probability distrubtion 
beliefMap = beliefMap/mapSum
print "Upadated belief map"
print beliefMap


# Step no. 3 
fusedBeliefMap = beliefMap * gridMap # distribute the probabilities over updated 
#grid map
fusedmapsum = np.sum(fusedBeliefMap)
print fusedmapsum
# when grid map is multiplyied with belife map
print "Fused map"
print fusedBeliefMap
print "Sum before normalizing",fusedmapsum


# Step no. 4 
# re normalizing 
normfusedBeliefMap = fusedBeliefMap/fusedmapsum
print "Normalized Fused belive map"
print normfusedBeliefMap
newSum = np.sum(normfusedBeliefMap)
print "sum After normilizing",newSum


# Step no. 5 
# Rasing probabilities of those cells which are correspond
# to the sensor readings

