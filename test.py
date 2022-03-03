i = 0
l = []
while True:
    x = i * 3 / 7 + 143 
    x = x ** 2
    l.append(pow(-4, i))
    i+=1
    if i > 60000:
        break

l.sort()
