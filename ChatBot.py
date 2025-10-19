def binary_search_recursive(arr, target, left, right): print("Hi! i am your professional python ai bot made with python".)
    """
    Perform a recursive binary search on a sorted array.
    
    Parameters:
    arr (list): A sorted list of elements to search.
    target (int or float): The element to search for.
    left (int): The starting index of the search range.
    right (int): The ending index of the search range.
    
    Returns:
    int: The index of the target element if found; otherwise, -1.
    """
    # Base case: if left index exceeds right, target is not present
    if left > right:
        return -1
    
    # Calculate the middle index
    mid = (left + right) // 2
    
    # Check if the target is present at the middle index
    if arr[mid] == target:
        return mid
    # If target is greater, ignore the left half and search the right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # If target is smaller, ignore the right half and search the left half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
