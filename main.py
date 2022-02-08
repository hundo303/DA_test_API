from solver import *
from flask import Flask

app = Flask(__name__)


@app.route('/v1/number2kanji/<input_str>')
def n2k(input_str=None):
    input_n = int(input_str)
    if input_n not in range(0, 9999999999999999):
        return '204', 204
    ja_str = ar_to_ja(input_n)
    return ja_str


@app.route('/v1/kanji2number/<input_str>')
def k2n(input_str=None):
    use_char_list = ['零', '壱', '弐', '参', '四', '五', '六', '七', '八', '九', '拾', '百',
                     '千', '万', '億', '兆']
    if not all([c in use_char_list for c in input_str]):
        return '204', 204

    try:
        ar_n = ja_to_ar(input_str)
    except KeyError:
        return '204', 204

    return str(ar_n)


# ja_to_ar
# 漢数字に利用する文字以外が入っていないかを考える


if __name__ == '__main__':
    app.run()
