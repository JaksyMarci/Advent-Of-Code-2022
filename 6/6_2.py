buffer=[]
index=14

f = open('input.txt', 'rb')

for i in range(14):
    buffer.append(f.read(1))


while(len(set(buffer)) < 14):
    f.seek(-14,1)
    buffer.remove(f.read(1))
    f.seek(13,1)
    buffer.append(f.read(1))
    index+=1

f.close()
print(index)



