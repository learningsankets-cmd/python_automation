names = ["John", "Mosh", "Mario", "Ama"]
names[0] = "Jon"
# print(names)

nums = [1, 399, 1, 96782, 11, 4, 1231, 121]
max = nums[0]
for num in nums:
    if num > max:
        max = num
# print(max)


# 2d list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# for row in matrix:
#     for item in row:
        # print(item)



numbers = [2,4,1,3,4,1]
numbers.append(23)
numbers.insert(3, 20)
numbers.reverse()
# numbers.sort()
# numbers.clear()
numbers.remove(1)
numbers.index(23)
# print(numbers.count(1))

numbers2 = numbers.copy() # just an independent copy 

        


nums1 = [1,1,2,3,2,3,5,6,7]

nums2 = []

for num in nums1:
    if num not in nums2:
        nums2.append(num)

# print(nums2)




