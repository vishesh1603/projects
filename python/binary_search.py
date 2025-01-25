def binary_search_recursive(arr, target, left, right):
    # Base case: if the range is invalid, target is not in the array
    if left > right:
        return -1  # Target not found

    mid = left + (right-left) // 2  # Calculate the middle index
    for i in arr:
        print(left,mid,right)

    # Check if the target is at the middle
    if arr[mid] == target:
        return mid

    # If the target is smaller, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)

    # If the target is larger, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

# Example usage
if __name__ == "__main__":
    array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 5

    result = binary_search_recursive(array, target, 0, len(array) - 1)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.z")
