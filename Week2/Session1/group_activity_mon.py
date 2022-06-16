# Write a function that takes a list of numbers and returns the sum
# def foo(some_list):
#   return sum
# foo([1,2,3,4,5])
# print(foo([1,2,3,4,5]))
# 15

def sum_list(some_list):
    sum = 0
    if some_list:
        for num in some_list:
            sum += num

    return sum

print(sum_list([1,2,3,4,5]))
print(sum_list([10,20,30]))
print(sum_list([]))
print(sum_list(None))
# foo([10,20,30])
# print(foo([10,20,30]))
# 60



























# def sum_of_list(list_of_nums):
#     sum = 0

#     # for num in list_of_nums:
#     #     sum += num # sum = sum + num

#     for index in range(0,len(list_of_nums)):
#         sum += list_of_nums[index]


#     return sum

# print(sum_of_list([3, 10, 25]))
