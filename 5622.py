alpha = input()
time = 0

for i in range(len(alpha)):

    if "A"<=alpha[i]<="C":
        time += 3
    elif "D"<=alpha[i]<="F":
        time += 4
    elif "G"<=alpha[i]<="I":
        time += 5
    elif "J"<=alpha[i]<="L":
        time += 6
    elif "M"<=alpha[i]<="O":
        time += 7
    elif "P"<=alpha[i]<="S":
        time += 8
    elif "T"<=alpha[i]<="V":
        time += 9
    else:
        time += 10

print(time)