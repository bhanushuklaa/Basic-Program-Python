#Binary Search program using recursive
def binarySearch(list1, n, low, high):
    if high>=low:
        mid = low + (high-low)//2
        if list1[mid] == n:
            return mid
        elif list1[mid] > n:
            return binarySearch(list1, n, low, mid-1)
        else:
            return binarySearch(list1, n, mid+1, high)
    else:
        return -1


list_input = int(input("Enter number of elements: "))
list1 = list(map(int, input("\nEnter the numbers: ").strip().split()))[:list_input]
print("\nList is - ", list1)
n = int(input("Enter the number to search from the above list: "))


result = binarySearch(list1, n, 0, len(list1)-1)
if result!=-1:
    print(f"{n} present at index: {result}")
else:
    print("Not found")