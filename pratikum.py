list_a = [1, 2, 3, 4, 5]

print(list_a[2])

print(list_a[1:4])

print(list_a[-1])

list_a[3] = 10
print(list_a)

list_a[3:] = [11, 12, 13]
print(list_a)

list_b = list_a[:2]
print(list_b)

list_b.append("misalnya")
print(list_b)

list_b.extend([14, 15, 16])
print(list_b)

list_a.extend(list_b)
print(list_a)