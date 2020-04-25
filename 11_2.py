# 如何区分简单插入和非递归的归并排序

# sample input:
# 10
# 3 1 2 8 7 5 9 4 6 0
# 1 2 3 7 8 5 9 4 6 0

# 插入排序: 前面有序，后面没变化

# 10
# 3 1 2 8 7 5 9 4 0 6
# 1 3 2 8 5 7 4 9 0 6

# 归并排序：分段有序

import numpy as np

input = [3, 1, 2, 8, 7, 5, 9, 4, 6, 0]
output1 = [1, 2, 3, 7, 8, 5, 9, 4, 6, 0]
output2 = [1, 3, 2, 8, 5, 7, 4, 9, 0, 6]


def InsertorMerge(input, output):
    pos = len(output)
    insert_flag = True
    merge_flag = True

    for i in np.arange(0, len(output), 1):
        if (i < pos) and (output[i] > output[i + 1]):
            pos = i + 1

        if (i >= pos):
            if output[i] == input[i]:
                continue
            else:
                insert_flag = False

    if (insert_flag):
        print("It is Insert Sort")
        return

    l = 2
    length = 0
    while (l <= len(output)):
        for i in np.arange(0, len(output), 1):
            if (i + l) % (2 * l) == 0:
                if input[i] > input[i - 1]:
                    length = l
                    break
                else:
                    continue
        if(length):
            break
        l = l * 2

    print("It is Merhe Sort, length = %d" % (length))


if __name__ == "__main__":
    InsertorMerge(input, output1)
    InsertorMerge(input, output2)