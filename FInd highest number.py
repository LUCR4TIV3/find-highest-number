arr = []
numsuffix = ("")
for i in range(10):
    if (i+1) == 1:
        numsuffix = ("st")
    elif (i+1) == 2:
        numsuffix = ("nd")
    elif (i+1) == 3:
        numsuffix = ("rd")
    else:
        numsuffix = ("th")
    num = (input(f"what do you want the {i+1}{numsuffix} number in your 10 value array"))
    try:
     while not (num.isdigit() and 1 <= int(
             num) <= 100):  # I use isdigit as my check system, making sure the user enter a valid input and the code doesn't crash.
         num = input("Invalid input, please enter an integer between 1 and 100: ")
    except ValueError:
        num = input("Invalid input, please enter an integer between 1 and 100: ")
    num = int(num)
    arr.append(num)

print(arr)

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

sorted_arr = bubble_sort(arr)
print(f"The sorted array is {sorted_arr}")
def find_highest_integer(array):
    if len(array) == 1:
        return array[0]
    else:
        max_rest = find_highest_integer(array[1:])
        return array[0] if array[0] > max_rest else max_rest



print("The highest integer in the list is:", find_highest_integer(arr))