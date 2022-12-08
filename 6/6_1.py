
index=4

f = open('input.txt', 'rb')

buffer = [f.read(1), f.read(1),f.read(1), f.read(1)]

while(len(set(buffer)) < 4):
    f.seek(-4,1)
    buffer.remove(f.read(1))
    f.seek(3,1)
    buffer.append(f.read(1))
    index+=1

f.close()
print(index)



