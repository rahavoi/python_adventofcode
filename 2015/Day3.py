file = open('Day3.txt', 'r')
line = file.read().strip()

def updatePos(currentPos, posCount):
    if(currentPos in posCount.keys()):
        visited = posCount.get(currentPos) + 1
    else:
        visited = 1
        
    posCount[currentPos] = visited 

steps = 0
santaPosition = (0, 0)
robotPosition = (0, 0)

santaPosCount = {santaPosition : 1}
robotPosCount = {}

for c in line:
    if(steps %2 == 0):
        currentPosition = santaPosition
        currentPosCount = santaPosCount
    else:
        currentPosition = robotPosition
        currentPosCount = robotPosCount
    
    if(c == '^'):
        currentPosition = (currentPosition[0], currentPosition[1] - 1)
    elif(c == 'v'):
        currentPosition = (currentPosition[0], currentPosition[1] + 1)
    elif(c == '>'):
        currentPosition = (currentPosition[0] + 1, currentPosition[1])
    elif(c == '<'):
        currentPosition = (currentPosition[0] - 1, currentPosition[1])
    
    updatePos(currentPosition, currentPosCount)
    
    if(steps %2 == 0):
        santaPosition = currentPosition
    else:
        robotPosition = currentPosition
    
    steps += 1   
    
santaPosCount.update(robotPosCount)

print(len(santaPosCount))      

