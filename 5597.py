asdf = [i for i in range(1, 31)]

for i in range(28):
    num = int(input())
    asdf.remove(num)

print(min(asdf[0], asdf[1]))
print(max(asdf[0], asdf[1]))