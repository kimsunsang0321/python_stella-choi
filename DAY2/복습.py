sum = 0
mul = 1
for i in range(1, 11):
    if i % 2 == 1:
        mul += i
    if i % 2 == 0:
        sum += i
print(mul - sum)