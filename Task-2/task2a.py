nums = [25, 12, 35, 88, 11]
print(nums)
print(nums[0])
print(nums[2:4])
print(nums[-1])

names = ["pd", "hk", "hp"]
print(names)

mx = [nums, names]
print(mx)

nums.append(33)  # appends the list from last
print(nums)

nums.insert(3, 43)  # inserts element at a specific location
print(nums)

nums.remove(43)  # removes specified elements
print(nums)

nums.pop(1)  # removes element according to location
print(nums)

nums.pop()  # pop according to lifo
print(nums)

del nums[2:]  # removes elements after 2nd location
print(nums)

nums.extend([22, 66, 77, 11])  # extends the list by multiple items
print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)
