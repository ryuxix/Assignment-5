# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    from collections import Counter
    if not numbers:
        return None
    freq = Counter(numbers)
    return max(freq, key=freq.get)

# Test Cases for problem 1
print(most_frequent([1, 3, 2, 3, 4, 1, 3])) # This should print out [3].
print(most_frequent([])) # This should print out none.

"""
Time and Space Analysis for problem 1:
- Best-case: Best case is when it's constant O(1) because if the list has only one element then counting and returning has a constant time.
- Worst-case: Worst case is when O(n) which means it's linear causing an increase in time or memory which will shown when we count the frequencies for all n elements and find the max.
- Average-case: Average case would be linear O(n) because generally each element is visited once when counting.
- Space complexity: With it being linear O(n) it requires extra space to store the frequency of each unique element.
- Why this approach? Using collections and Counter provides a simple and efficient way to count and find the most common element.
- Could it be optimized? I think it could not be optimized because counting each element at least once is necessary so O(n) time is probably best for this problem.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test cases for problem 2 
print(remove_duplicates([4, 5, 4, 6, 5, 7])) # This should print out one [4, 5, 6, 7].
print(remove_duplicates([1, 1, 1])) # This should only print out one [1].

"""
Time and Space Analysis for problem 2:
- Best-case: Best case would be linear O(n) because even if all elements are unique the loop still checks each one once.
- Worst-case: Worst case for linear O(n) when the function must go through every element in the list to build the result.
- Average-case: Average case for linear O(n) would be when each element is checked once and a set are O(1) on average.
- Space complexity: Linear O(n) is using the extra space for the seen set and the result list which can each hold up to n elements.
- Why this approach? Using this approach shows that a set allows for constant time lookups while keeping a list in the original order that it was in.
- Could it be optimized? I would say it can't be optimized because every element must be checked at least once to remove duplicates.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

# Test cases for problem 3
print(find_pairs([1, 2, 3, 4], 5)) # This should print out these pairs [(1, 4), (2, 3)].
print(find_pairs([2, 4, 6, 8], 10)) # This should print out these pairs [(2, 8), (4, 6)].

"""
Time and Space Analysis for problem 3:
- Best-case: Best case would be linear O(n) when there is a few or no pairs exist and the loop still checks each element once.
- Worst-case: Worst case for linear O(n) is when each element is processed once and checked in the set in constant time.
- Average-case: Average case for linear O(n) when the hash lookups and inserts both average so one pass through the list is enough.
- Space complexity: The seen set may store up to n elements and the pairs list could hold up to n pairs.
- Why this approach? Using a set allows constant time lookups and avoiding the need for nested loops.
- Could it be optimized? It could be optimized by sorting and using two pointers that could make it O(n log n) (which means it would be long linear) but it would be slower than O(n).
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    data = []
    for i in range(n):
        if size == capacity:
            print(f"Resizing from capacity {capacity} to {capacity * 2}")
            capacity *= 2
            data = data.copy()
        data.append(i)
        size += 1
    print(f"Final list: {data}")
    
# Test cases for problem 4
add_n_items(6) # This should print [0,1,2,3,4,5].
add_n_items(1) # This should just print out [0].


"""
Time and Space Analysis for problem 4:
- When do resizes happen? The resize occurs whenever the list's current size equals its capacity.
- What is the worst-case for a single append? Worst case is linear O(n) when resizing happens all existing elements must be copied to a new list.
- What is the amortized time per append overall? The amortized time per append would be O(1) because the time would stay constant.
- Why does doubling reduce the cost overall? It reduce overall cost because doubling shows that resizes become less frequent as the list grows which makes the append constant.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):

    # Optimized Verison of Problem 5
    # Instead of creating a new list we update the original list in place.
    # This reduces extra memory usage.

    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
 
 # Original Problem 5
   # total = 0
   # result = []
   # for num in nums:
    #    total += num
   #     result.append(total)
    #return result

"""
Comparison Performace 
Original version:
The time complexity: is linear O(n)
The space complexity: is linear O(n) it creates a new list for results
Optimized version:
The time complexity: is linear O(n)
The space complexity: is constant O(1) it updates the input list directly using constant extra space

Optimized Performance:
- Both codes take the same time but the optimized one uses less memory.
- This optimization is good for large input lists.
"""


# Test cases for problem 5
print(running_total([1, 2, 3, 4])) # This should print this [1, 3, 6, 10].
print(running_total([-1, 2, -3, 4])) # This should print this [-1, 1, -2, 2].



"""
Time and Space Analysis for problem 5:
- Best-case: Best case would be linear O(n) because even if the list is small or simple each element must be processed once.
- Worst-case: Worst case for linear O(n) would be every element is visited to compute cumulative sums.
- Average-case: Average case for linear O(n) would be for typical inputs the function performs one pass through the list.
- Space complexity: Linear O(n) would make a new list that could store the running totals which can have up to n elements.
- Why this approach? It uses a single running total variable to build the result in one pass.
- Could it be optimized? I think it could be optimized if you reduce extra space to constant O(1) but in doing this the time complexity would remain linear O(n).
"""

# Used resource 1 and 3 to determine my answers for the writing portion 