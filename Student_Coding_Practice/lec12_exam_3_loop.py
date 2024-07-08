#1

def common_end(a, b):
  if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
    return True
  else:
    return False


#2
def array_count9(nums):
    count=0
    for i in range(0,len(nums)):
        if nums[i]==9:
            count+=1
    return count

#3
def sum_even_numbers(arr):
    sum_even = 0
    for num in arr:
        if num % 2 == 0:
            sum_even += num
    return sum_even
  
  # Using a while loop
numbers = [3,5,78,5,434,333,6788]
  
sum_even_while = 0
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        sum_even_while += numbers[index]
    index += 1

print("Sum of even numbers (while loop):", sum_even_while)