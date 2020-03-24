import sys

input = sys.argv[1]
floor = 0

for i in range( len(input) ):
    if(input[i] == '('):
        floor += 1
    else:
        floor -= 1
    
    if(floor == -1):
        print("In basement after {}th instruction".format(i + 1))
        break
        
        
print(floor)        
        
