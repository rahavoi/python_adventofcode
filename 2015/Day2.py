file = open('Day2.txt', 'r')
lines = file.readlines()

ribbon = 0
total = 0
for line in lines: 
    sides = line.strip().split('x')
    l = int(sides[0])
    w = int(sides[1])
    h = int(sides[2])
    
    surface = 2*l*w + 2*w*h + 2*h*l;
    if(l < w):
        if(w < h):
            smallest = l * w
            ribbon += 2*l + 2*w
        else:
            smallest = l *h
            ribbon += 2*l + 2*h
    else:
        if(l < h):
            smallest = w * l
            ribbon += 2*l + 2*w
        else:
            smallest = w * h
            ribbon += 2*w + 2*h
        
    bow = l*w*h
    ribbon += bow
    total += smallest + surface

print("Total wrapping paper needed: {}".format(total))
print("Total ribbon needed: {}".format(ribbon))
