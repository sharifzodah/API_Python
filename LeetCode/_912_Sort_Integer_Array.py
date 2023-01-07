def sortArray(nums):
    freq = [0] * 100001
    result = [0] * len(nums)
    min_num = 50000
    max_num = nums[0]
    for number in nums:
        freq[number + 50000] += 1
        min_num = min(number, min_num)
        max_num = max(number, max_num)
    i = min_num + 50000
    j = max_num + 50000
    index = 0
    while i <= j:
        if freq[i] == 1:
            result[index] = i - 50000
            index += 1
        elif freq[i] > 1:
            k = 0
            while k < freq[i]:
                result[index + k] = i - 50000
                k += 1
            index += freq[i]
        i += 1
    return result


ints = [-10125, 5, 98, 0, 14580, 98, 66, 0, 12, 98]
array = sortArray(ints)
print(array)
