grade = input()

if grade[0] == "A":
    score = 4.0
    if grade[1] == "+":
        score += 0.3
    if grade[1] == "-":
        score -= 0.3
if grade[0] == "B":
    score = 3.0
    if grade[1] == "+":
        score += 0.3
    if grade[1] == "-":
        score -= 0.3
if grade[0] == "C":
    score = 2.0
    if grade[1] == "+":
        score += 0.3
    if grade[1] == "-":
        score -= 0.3
if grade[0] == "D":
    score = 1.0
    if grade[1] == "+":
        score += 0.3
    if grade[1] == "-":
        score -= 0.3
if grade[0] == "F":
    score = 0.0

print(score)