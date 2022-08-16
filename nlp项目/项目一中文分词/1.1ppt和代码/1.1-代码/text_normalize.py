def b2q(uchar):
    """半角转全角"""
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return chr(inside_code)


def q2b(uchar):
    """全角转半角"""
    inside_code = ord(uchar)    # 先将其转成ASCⅡ码，再进行下一步操作
    if inside_code == 0x3000:  # 全角空格   因为全角空格和半角空格的ASCⅡ码差值不符合下面的规律，所以要单独讨论
        inside_code = 0x0020
    else:  # 半角 = 全角 - 0xfee0
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return chr(inside_code)


def string_q2b(ustring):
    """把字符串全角转半角"""
    return ''.join([q2b(uchar) for uchar in ustring])   # 将字符串里的所有字符都通过函数转成半角再用join串起来


if __name__ == '__main__':
    s = '天气不错！是么？'
    print(string_q2b(s))
