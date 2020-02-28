import json
import re


def read(pathname):
    with open(pathname, 'r') as f:
        html = f.readlines()[1]
        html_dict = json.loads(re.findall(r'jsonp\d+\((.+?)\)', html)[0])

    return html_dict


def analysis(html_dict):
    # 评价
    print(html_dict['rateDetail']['rateList'][0]['rateContent'])


if __name__ == '__main__':
    my_pathname = '../data/1.html'
    my_html_dict = read(my_pathname)
    analysis(my_html_dict)
