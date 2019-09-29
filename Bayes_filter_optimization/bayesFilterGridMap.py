import numpy as np 
import math

# Step no. 1
gridMap = np.ones((10,10)) # made a numpy 2D-array of all ones 
print "Grid map"
#print gridMap
# cells defining the obstacles(walls) 
walls = [[1,1],[4,5],[8,9],[9,9],[3,4],[5,5],[9,7],[9,1],[2,7],[0,9]] # made a list of coordinates on grid, defining the obstacles grid cells
#print walls[0][0]
for wall in walls: # iterate over loop and assign obstacles gird cells with a value integer 0 
    gridMap[wall[0], wall[1]] = 0

print "Update grid map with Obstacles"
#print gridMap #printing the updates 2D-girdmap


# Step no. 2
beliefMap = np.ones((10,10)) # define a same dimension 2D-numpy array 
mapSum = np.sum(beliefMap) # calculating the sum of all elements in 2D-numpy array
# iterate over all the elements of 2D-numpy array and divide each element by total
# sum of all the elements for calculating uniform probability distrubtion 
beliefMap = beliefMap/mapSum
print "Upadated belief map"
#print beliefMap


# Step no. 3 
fusedBeliefMap = beliefMap * gridMap # distribute the probabilities over updated 
#grid map
fusedmapsum = np.sum(fusedBeliefMap)
#print fusedmapsum
# when grid map is multiplyied with belife map
print "Fused map"
print fusedBeliefMap
#print "Sum before normalizing",fusedmapsum


# Step no. 4 
# re normalizing 
normfusedBeliefMap = fusedBeliefMap/fusedmapsum
print "Normalized Fused belive map"
#print normfusedBeliefMap
newSum = np.sum(normfusedBeliefMap)
#print "sum After normilizing",newSum



# Step no. 5 
# Rasing probabilities of those cells which are correspond
# to the sensor readings let say sensor reading = 3 cells 
x=0
y=0

def calculateDistance(x1,y1,x2,y2):
    d = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

SensorMeasurement_l = 2.8
SensorMeasurement_u = 3.2

for x in range(normfusedBeliefMap.shape[0]):
    for y in range(normfusedBeliefMap.shape[1]):
        print x," ",y
        distobs1 = calculateDistance(x,walls[0][0],y,walls[0][1])
        print "dist_obs1: ",distobs1
        if (SensorMeasurement_l<distobs1 and distobs1 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
        
        print x," ",y
        distobs2 = calculateDistance(x,walls[1][0],y,walls[1][1])
        print "dist_obs2: ",distobs2
        if (SensorMeasurement_l<distobs2 and distobs2 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7

        print x," ",y
        distobs3 = calculateDistance(x,walls[2][0],y,walls[2][1])
        print "dist_obs3: ",distobs3
        if (SensorMeasurement_l<distobs3 and distobs3<SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs4 = calculateDistance(x,walls[3][0],y,walls[3][1])
        print "dist_obs4: ",distobs4
        if (SensorMeasurement_l<distobs4 and distobs4 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs5 = calculateDistance(x,walls[4][0],y,walls[4][1])
        print "dist_obs5: ",distobs5
        if (SensorMeasurement_l<distobs5 and distobs5 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs6 = calculateDistance(x,walls[5][0],y,walls[5][1])
        print "dist_obs6: ",distobs6
        if (SensorMeasurement_l<distobs6 and distobs6 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs7 = calculateDistance(x,walls[6][0],y,walls[6][1])
        print "dist_obs7: ",distobs7
        if (SensorMeasurement_l<distobs7 and distobs7 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs8 = calculateDistance(x,walls[7][0],y,walls[7][1])
        print "dist_obs8: ",distobs8
        if (SensorMeasurement_l<distobs8 and distobs8 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs9 = calculateDistance(x,walls[8][0],y,walls[8][1])
        print "dist_obs9: ",distobs9
        if (SensorMeasurement_l<distobs9 and distobs9 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print x," ",y
        distobs10 = calculateDistance(x,walls[9][0],y,walls[9][1])
        print "dist_obs10: ",distobs10
        if (SensorMeasurement_l<distobs10 and distobs10 < SensorMeasurement_u):
            normfusedBeliefMap[x,y]=0.7
    
        print "--------------------------------------------------------------"



print normfusedBeliefMap