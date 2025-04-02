"""快速排序算法的纯Python实现

运行文档测试请使用以下命令：
python3 -m doctest -v quick_sort.py

手动测试请运行：
python3 quick_sort.py
"""

from __future__ import annotations

from random import randrange


def quick_sort(collection: list) -> list:
    """快速排序算法的纯Python实现。

    :param collection: 一个可变的、可比较的项目集合
    :return: 按升序排序后的相同集合

    示例：
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    # 基本情况：如果集合有0或1个元素，则已经排序完成
    if len(collection) < 2:
        return collection

    # 随机选择一个基准点索引，并从集合中移除基准元素
    pivot_index = randrange(len(collection))
    pivot = collection.pop(pivot_index)

    # 将剩余元素分成两组：小于等于基准值的组和大于基准值的组
    lesser = [item for item in collection if item <= pivot]
    greater = [item for item in collection if item > pivot]

    # 递归地对较小和较大的组进行排序，并与基准值组合
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


if __name__ == "__main__":
    # 获取用户输入并转换为整数列表
    user_input = input("请输入用逗号分隔的数字：\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]

    # 打印用户提供的列表的排序结果
    print(quick_sort(unsorted))
