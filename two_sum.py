def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i

    # Find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]

    return []  # No solution found

def main():
    # Getting user input for the list of numbers
    nums = input("Enter numbers separated by spaces: ")
    nums = [int(num) for num in nums.split()]

    # Getting user input for the target
    target = int(input("Enter the target number: "))

    # Finding and printing the result
    result = twoSum(nums, target)
    if result:
        print("Indices:", result)
    else:
        print("No two sum solution found.")

if __name__ == "__main__":
    main()
