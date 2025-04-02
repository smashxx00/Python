# 判断字符串是否为回文的算法

from timeit import timeit

test_data = {
    "MALAYALAM": True,
    "String": False,
    "rotor": True,
    "level": True,
    "A": True,
    "BB": True,
    "ABC": False,
    "amanaplanacanalpanama": True,  # "一个人一个计划一条巴拿马运河"
}
# 确保测试数据有效
assert all((key == key[::-1]) is value for key, value in test_data.items())


def is_palindrome(s: str) -> bool:
    """如果字符串s是回文则返回True，否则返回False。

    >>> all(is_palindrome(key) is value for key, value in test_data.items())
    True
    """

    start_i = 0
    end_i = len(s) - 1
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True


def is_palindrome_traversal(s: str) -> bool:
    """如果字符串s是回文则返回True，否则返回False。

    >>> all(is_palindrome_traversal(key) is value for key, value in test_data.items())
    True
    """
    end = len(s) // 2
    n = len(s)

    # 我们只需要遍历到字符串长度的一半
    # 因为我们可以从第i个索引访问到倒数第i个元素
    # 例如：[0,1,2,3,4,5] => 第4个索引可以通过
    # 第1个索引访问（i==n-i-1）
    # 其中n是字符串的长度
    return all(s[i] == s[n - i - 1] for i in range(end))


def is_palindrome_recursive(s: str) -> bool:
    """如果字符串s是回文则返回True，否则返回False。

    >>> all(is_palindrome_recursive(key) is value for key, value in test_data.items())
    True
    """
    if len(s) <= 2:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False


def is_palindrome_slice(s: str) -> bool:
    """如果字符串s是回文则返回True，否则返回False。

    >>> all(is_palindrome_slice(key) is value for key, value in test_data.items())
    True
    """
    return s == s[::-1]


def benchmark_function(name: str) -> None:
    stmt = f"all({name}(key) is value for key, value in test_data.items())"
    setup = f"from __main__ import test_data, {name}"
    number = 500000
    result = timeit(stmt=stmt, setup=setup, number=number)
    print(f"{name:<35} 完成 {number:,} 次运行，耗时 {result:.5f} 秒")


if __name__ == "__main__":
    for key, value in test_data.items():
        assert is_palindrome(key) is is_palindrome_recursive(key)
        assert is_palindrome(key) is is_palindrome_slice(key)
        print(f"{key:21} {value}")
    print("一个人一个计划一条巴拿马运河")

    # 完成500,000次运行，耗时0.46793秒
    benchmark_function("is_palindrome_slice")
    # 完成500,000次运行，耗时0.85234秒
    benchmark_function("is_palindrome")
    # 完成500,000次运行，耗时1.32028秒
    benchmark_function("is_palindrome_recursive")
    # 完成500,000次运行，耗时2.08679秒
    benchmark_function("is_palindrome_traversal")
