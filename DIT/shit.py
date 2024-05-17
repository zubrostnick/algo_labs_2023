left = 0
right = len(array)
while left < right:
    m = left + (right - left) // 2
    if x > array[m]:
        left = m + 1
    else:
        right = m
return array[right] == x