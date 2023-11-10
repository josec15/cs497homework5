# Question 5
# Lexicographical Numbers

# Given an integer m, return all the numbers in the range[1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space.

def lexNums(n):
    res = []
    curr = 1
    for i in range(n):
        res.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            if curr >= n:
                curr = curr // 10
            curr += 1
            while curr % 10 == 0:
                curr = curr // 10
    return res

n = 13
print(lexNums(n))