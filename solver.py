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

    ja_str = ''
    for i in range(len(ar_re)):
        if ar_re[i] == '0':
            if i % 4 == 0:
                ja_str += q.get()
            continue

        if (i + 3) % 4 == 0:
            ja_str += '拾'
        elif (i + 2) % 4 == 0:
            ja_str += '百'
        elif (i + 1) % 4 == 0:
            ja_str += '千'
        elif i % 4 == 0 and i != 0:
            ja_str += q.get()

        ja_str += ar_ja_dict[ar_re[i]]

    return ja_str[::-1]


def ja_to_ar(input_ja: str):
    ja_ar_dict = {'壱': 1, '弐': 2, '参': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    ar_n = 0
    tmp_n = 0
    for i in range(1, len(input_ja)):
        if input_ja[i] == '拾':
            tmp_n += ja_ar_dict[input_ja[i - 1]] * 10
        elif input_ja[i] == '百':
            tmp_n += ja_ar_dict[input_ja[i - 1]] * 100
        elif input_ja[i] == '千':
            tmp_n += ja_ar_dict[input_ja[i - 1]] * 1000

        elif input_ja[i] == '兆':
            tmp_n += ja_ar_dict.get(input_ja[i - 1], 0)
            ar_n += tmp_n * 1000000000000
            tmp_n = 0
        elif input_ja[i] == '億':
            tmp_n += ja_ar_dict.get(input_ja[i - 1], 0)
            ar_n += tmp_n * 100000000
            tmp_n = 0
        elif input_ja[i] == '万':
            tmp_n += ja_ar_dict.get(input_ja[i - 1], 0)
            ar_n += tmp_n * 10000
            tmp_n = 0

    ar_n += tmp_n
    ar_n += ja_ar_dict.get(input_ja[-1], 0)

    return ar_n


if __name__ == '__main__':
    pass
