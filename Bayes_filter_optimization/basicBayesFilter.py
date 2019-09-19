#!/user/bin/python

sensorData = [0,0,0,1]

#Sensor model constants 
pSH = 0.7
pSnH = 0.1
pnSH = 0.3
pnSnH = 0.9

pH = 0.5 # Initilize using general probability 
pnH = 1- pH
# Bayes Formulas 
#pHS = (pSH*pH)/(pSH*pH)+(pSnH*pnH)
#pHnS = (pnSH*pH)/(pnSH*pH)+(pnSnH*pnH)

for i in range(len(sensorData)):
    pnH = 1- pH
    if (sensorData[i]==1):
        pHS = (pSH*pH)/((pSH*pH)+(pSnH*pnH))
        pH = pHS
        print "True case",pHS
    else:
        pHnS = (pnSH*pH)/((pnSH*pH)+(pnSnH*pnH))
        pH = pHnS
        print "False case",pHnS
    
print "Result", pH      


