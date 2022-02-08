import queue


def ar_to_ja(input_ar: int):
    ar_ja_dict = {'1': '壱', '2': '弐', '3': '参', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}
    q = queue.Queue()
    for digit in ['万', '億', '兆']:
        q.put(digit)

    ar_str = str(input_ar)
    ar_re = ar_str[::-1]

    if input_ar == 0:
        return '零'

    return_str = ''
    for i in range(len(ar_re)):
        if ar_re[i] == '0':
            if i % 4 == 0:
                return_str += q.get()
            continue

        if (i + 3) % 4 == 0:
            return_str += '拾'
        elif (i + 2) % 4 == 0:
            return_str += '百'
        elif (i + 1) % 4 == 0:
            return_str += '千'
        elif i % 4 == 0 and i != 0:
            return_str += q.get()

        return_str += ar_ja_dict[ar_re[i]]

    return return_str[::-1]


def ja_to_ar(input_ja: str):
    pass


if __name__ == '__main__':
    print(ar_to_ja(9999999999999999))
