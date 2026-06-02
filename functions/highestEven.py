def highest_even(lst):
    max_even = float('-inf')
    for num in lst:
        if num%2==0:
            if num>=max_even:
                max_even = num
    return max_even

ls = [-2,-4]
print(highest_even(ls))