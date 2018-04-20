# 给定两个字符串，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。区分大小写
# "This is me","is This me"  True

from collections import Counter


def check_same(s1, s2):
    if len(s1) != len(s2):
        return False

    return Counter(s1) == Counter(s2)


if __name__ == '__main__':
    print(check_same("This is non", "is This now"))
