from collections import defaultdict
test_list = []
N = int(input("Number of elements:"))
print("Enter the elements:")
for i in range(N):
    element = input()
    test_list.append(element)
test_list = list(set(test_list))
temp = defaultdict(list)
for j in test_list:
    temp[str(sorted(j))].append(j)
result = list(temp.values())
print(str(result))