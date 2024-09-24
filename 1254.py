S = input()

rev = ''.join(reversed(S))

for i in range(len(S)):

    temp = S + rev[len(S)-i:]
    rev_temp = ''.join(reversed(temp))


    if rev_temp == temp:
        print(len(S) + i)
        break