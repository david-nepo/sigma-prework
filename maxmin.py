def maxmin(arr):
    return [sorted(arr)[0], sorted(arr)[-1]]

s = input("Enter integers for an array (separated by spaces): ")
arr = [int(num) for num in s.split()]

print(f"\nArray: {arr}")
print(f"Min, Max: {maxmin(arr)}")