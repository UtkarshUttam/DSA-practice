nums = [0,0,1,1,1,2,2,3,3,4]
# result = []
# k = 0
# for i in range(0,len(nums)):
#     if nums[i] not in result:
#         result.append(nums[i])
#     else:
#         nums.pop(i)
#         k += 1
#         i -= 1     
# print(k+1,nums)
# print(result)
i=0
while (i < (len(nums)-1)):
    if (nums[i] == nums[i+1]):
        nums.pop(i)
        i -= 1
    i += 1
k = len(nums)
print(k)