nums = [2, 2, 2, 2, 5, 5]

# for i in range(len(nums)):
#     print("x"*nums[i])

for x_count in nums:
    output = ""

    for count in range(x_count):
        output += "x"
    print(output)
