#Two lists
list1 = []
list2 = []

#Index ranges from 1 to 10 to multiply
for i in range(1, 11):
    list1.append(4*i)
print(f"list1 contains {list1}")

#Index to access the list2 is from 0 t0 9
for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)
print(f"list2 contains {list2}")

print("Checking whether at least a number is divisible by 5 in list1 => ")
#any() a work
print(any(list2))
print()
# All numbers in list1 are in form: 4*i-3
for i in range(1, 21):
    list1.append(4*i-3)
print(f"list1 contains {list1}")

# list2 stores info of odd numbers in list1
for i in range(0, 20):
    list2.append(list1[i] % 2 == 1)
print(f"list2 contains {list2}")

print("Checking if list2 are all odds")
print(all(list2))
