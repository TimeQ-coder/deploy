def solotion_nums(nums):
    """
    :param nums: 非严格递增数组  eg:nums = [0,0,1,1,1,2,2,3,3,4]
    :return: 返回去重后的数组长度及数组 eg:5, nums = [0,1,2,3,4]
    """
    # 双指针法去重
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    # 返回去重后的数组长度及数组
    return slow + 1, nums[:slow + 1]


def is_good_char(c):
    char_count = {}
    for i in c:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    first_char = next(iter(char_count.values()))
    for j in char_count.values():
        if j != first_char:
            return False
    return True


def NumAddNum(nums, target):
    """
    两数之和，返回对应下标
    :param nums:数组
    :param target:两数之和的目标值
    :return:返回两个数对应的下标
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


def lst():
    lst = [1, 2, 3, 4]
    # lst.insert(1, ['a', 'b'])
    lst.remove(3)
    print(lst)


def matrix_vector_dot_product(matrix, vector):
    import numpy as np
    # 补全代码
    m_shape = np.asarray(matrix).shape
    v_shape = np.asarray(vector).shape
    if m_shape[-1] != v_shape[0]:
        return -1
    else:
        # res = [int(i) for i in np.matmul(matrix, vector)]
        res = np.matmul(matrix, vector).tolist()
        return res


from typing import List, Union


def transpose_matrix(a: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    import numpy as np
    arr = np.asarray(a).T
    res = arr.tolist()
    return res


import fastapi
from fastapi import FastAPI

app = FastAPI()


def output(x):
    print(x)


if __name__ == '__main__':
    names = input().split()
    print(list(set(names)))
