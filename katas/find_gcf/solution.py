def find_GCF(a, b):
    small_num, big_num = sorted([a, b])

    for num in range(small_num, 0, -1):
        if small_num % num == 0 and big_num % num == 0:
            return num
