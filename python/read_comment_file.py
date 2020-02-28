import json
import re


def read(pathname):
    with open(pathname, 'r') as f:
        html = f.readlines()[1]
        html_dict = json.loads(re.findall(r'jsonp\d+\((.+?})\)', html)[0])

    return html_dict


def analysis(html_dict):
    # 评价
    for j in html_dict['rateDetail']['rateList']:
        print(j['rateContent'])


if __name__ == '__main__':
    my_page = 3
    my_pathname = '../data/' + str(my_page) + '.html'

    # 获取html_dict
    my_html_dict = read(my_pathname)

    # 解析html_dict
    analysis(my_html_dict)
