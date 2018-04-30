seq = []
for i in range(1, 101):
    seq.append(i)

print("Count 1 : {}".format(seq.count(1)))
print("101 is not in range(1,101)? {}.".format(101 not in seq))
print("1 is in range(1,101)? {}.".format(1 in seq))
print("Min : {}".format(min(seq)))
print("Max: {}".format(max(seq)))
print("5th item:{}".format(seq[5]))
print("Just even: {}".format(seq[1::2]))
print("Just odd: {}".format(seq[::2]))
print("Reversed odd: {}".format(seq[98:: - 2]))
print("Reversed even: {}".format(seq[99:: - 2]))
a = [1, 2]

print("[1, 2] + [1, 2] + [3] = {}".format(a + a + [3]))
print("[1, 2]*3 = {}".format(a * 3))

lists = [[]] * 3
lists[0].append(1)
lists[1].append(2)
lists[2].append(3)
print(lists)
