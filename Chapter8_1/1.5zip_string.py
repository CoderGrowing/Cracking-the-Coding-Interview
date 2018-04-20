# 利用字符重复出现的次数将字符串压缩。若压缩后的字符串没有变短，则返回原先的字符串。
# aabcccccaaa  a2b1c5a3


def zip_string(s: str):
    if len(set(s)) == len(s):
        return s

    result = ""
    index = 0
    count = 1

    for i in range(index+1, len(s)):
        if s[index] == s[i]:
            count += 1
        else:
            result += s[index]
            result += str(count)
            index = i

    return result


if __name__ == '__main__':
    print(zip_string("aabccccaaa"))