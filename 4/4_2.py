count = 0

with open ('input.txt', 'r') as f:
    for line in f:
        a, b = line.strip().split(',')
        a = a.split('-')
        b = b.split('-')
        if (int(a[0]) <= int(b[1]) and int(a[1]) >= int(b[0])):
            count += 1

print(count)