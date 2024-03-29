#!/usr/bin/env python3

my_list = [1, 3, 5, 7, 9]

def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low + high) // 2 # 如果(low + high)不是偶数, Python自动将mid向下取整.
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
