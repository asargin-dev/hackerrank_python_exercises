arr = [2, 3, 6, 6, 5]

arr = list(arr)

arr.sort()

max_of_arr = max(arr)

for i in arr[::-1]:
    if i == max_of_arr:
        arr.remove(i)

print(max(arr))
