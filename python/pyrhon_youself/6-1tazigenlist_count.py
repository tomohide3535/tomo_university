###多次元リストの要素数をカウントする。


# 入れ子のリストの要素数をカウントする。

def recursive_len(data):
    result = 0
    if isinstance(data, list):
        for elem in data:
            result += recursive_len(elem)
    else:
        result += 1
    return result

test_list = [
    [15, 1, 
    [77, 93, 40, 55],
    ],
    24,
    [34, 54],
    [44, 88, 22, 1, 4],
]

print(recursive_len(test_list))