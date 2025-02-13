# Array, List
arr = [5,6,8,9]
# print(arr)

# print(len(arr))

# print( arr[0] + 10  )

# add item to the end of the list
arr.append(10)
# print(arr)

# add item to a specific index to a list
arr.insert(2, 15)
print(arr)

# overwrite an item
arr[0] = 30


# remove an item from the end
num = arr.pop()
print(num)

arr.pop(0)
print(arr)

# in operator

strings = ["hello", "world"]
if "hello" in strings:
    print("hello is in strings list")

if "bye" not in strings:
    print("the word bye does not seem to appear in the strings list")


arr2 =  [7,8,9,0]
if 9 in arr2:
    print("9 is in arr2")

