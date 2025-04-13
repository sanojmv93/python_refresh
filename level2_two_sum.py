def two_sum(nums, target):
    num_map = {}  # stores value: index
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_map:
            return [num_map[diff], i]
        num_map[num] = i

if __name__ == "__main__":
    u = list(map(int, input("Enter the list of numbers: ").split()))
    t = int(input("Enter the target sum:"))
    v = two_sum(u, t)
    for i in v:
        print("Value : ", u[i], "Position: ", i)