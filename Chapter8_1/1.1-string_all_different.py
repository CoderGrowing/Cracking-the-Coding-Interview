# 请实现一个算法，确定一个字符串的所有字符是否全都不同。这里我们要求不允许使用额外的存储结构。
# aeiou True
# Balabala False


def is_all_different(s):
    return len(s) == len(set(s))


def is_all_different_without_data_structure(s):
    index = 0

    while index < len(s):
        for i in range(index+1, len(s)):
            if s[index] == s[i]:
                return False
        index += 1
    return True


if __name__ == '__main__':
    print(is_all_different("aeiou"))
    print(is_all_different_without_data_structure("aeiou"))
    print(is_all_different_without_data_structure("abcdefghijklmnopaqrst"))