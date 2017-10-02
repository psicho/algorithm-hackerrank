n = int(input())
s = []
plus = 0
for i in range(n):
    grade = int(input())
    plus = grade
    if grade % 5 == 0 or grade < 38:
        s.append(grade)
    else:
        for i in range(1, 3):
            plus += 1
            if plus % 5 == 0 and plus - grade < 3:
                s.append(plus)
                break
        if plus % 5 != 0 and i == 2:
            s.append(grade)

print(s)