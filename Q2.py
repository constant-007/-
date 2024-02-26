def replace_char(s, k):

    if len(s) <= k:
        return s

    result = s[:k] # 用于存储结果
    tmp = set(result) # 用于存储前k个字符

    # 遍历k之后的字符, 如果字符与前k个字符中的任意一个相同, 则替换为'-', 否则保留原字符
    for i in s[k:]:
        if i in tmp:
            result.append('-')
        else:
            result.append(i)
        
    # 将结果列表转换为字符串并返回
    return ''.join(result)

s = input('请输入字符串：')
k = int(input('请输入k：'))
print(replace_char(s, k))