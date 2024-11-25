l1 = [2,3,4,2929,2929,2929,33]

print(type(l1))
print(l1)

l1.remove('krishna')
print(l1)

print(l1.count(2929))

l1.sort()
print(l1)

# list is mutable but string is immutable 

l1.pop()
print(l1)

l1.append(788)
print(l1)

l1.clear()
l1.extend([29,29,49,30])
l1.reverse()
print(l1)

print(l1[-6])

print(l1[0:4])