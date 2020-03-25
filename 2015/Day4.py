import hashlib
input = 'yzbqklnj'

for i in range(282749, 100000000):
    test = input + str(i)
    hash = hashlib.md5(test.encode()).hexdigest()
    
    if(hash.startswith('000000')):
        print(hashlib.md5(test.encode()).hexdigest())
        print(i)
        break
