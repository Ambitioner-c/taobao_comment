import requests
import random
from time import sleep


# 下次运行需要主动更改cookie和referer参数，内容直接复制浏览器控制台信息
Headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/80.0.3987.106 Safari/537.36',
           'cookie': 'cna=gSYsFs5GqgcCAXLV/PLN3yGH; hng=CN%7Czh-CN%7CCNY%7C156; lid=ambitioner%E4%B8%B6; enc=L9HQuV5GHNRsGeq9rZ3xafuSSX2F46GZYB4B2JCyacx3KPhqjHSF%2FRo%2Bw0y9Jx6i4DQECoE%2BjkAgHqXEFzKm1A%3D%3D; _m_h5_tk=29d764e2058930bfd11ab05d80a3cb86_1582804356322; _m_h5_tk_enc=9fb28a8f39883bf19bac2ddcb7ac12d0; sgcookie=DGRVAmM8cBxFOvUJDfVh%2B; uc1=cookie14=UoTUOLtV3hIT0Q%3D%3D; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&nk2=Any3BqBNXeXE67%2BP&vt3=F8dBxd3yPWVaWUFtXLY%3D&id2=UUGjMVyuhEU30A%3D%3D; t=305a8d13ab3531a86d28e9bb0cb44aa5; tracknick=ambitioner%5Cu4E36; uc4=nk4=0%40AJc9Jh4DCme1Xd6KuxQkwbBbdrKdGxI%3D&id4=0%40U2OU%2FjjOW%2Bci6bsS%2BHdj1aRVz0Ys; lgc=ambitioner%5Cu4E36; _tb_token_=53fe3566ebe74; cookie2=120014477303a6b4aa6e519bb3cec0e9; l=dBIU44EgqnlweYHXBOCZlurza77TlIRfguPzaNbMi_5Ky_L0ShbOoRwjJEp6cjWcM6Tp4JfUk2eT7FZu8z8foTB7K9cdvdnBBef..; isg=BExMFmfIfsaqqGnJK-yGBA0QHaN-hfAv0Phb6KYNNPeMMe07z5fFvsPH1TkJeSiH',
           'referer': 'https://detail.tmall.com/item.htm?spm=a230r.1.14.13.36cd5022lfyaGb&id=605258110430&cm_id=140105335569ed55e27b&abbucket=10&sku_properties=10004:709990523;5919063:6536025'}


def get_comment(page):

    url = 'https://rate.tmall.com/list_detail_rate.htm' \
          '?itemId=602858459541' \
          '&spuId=1340548940' \
          '&sellerId=713805254' \
          '&order=3' \
          '&currentPage=' + str(page) + \
          '&append=0' \
          '&content=1' \
          '&tagId=' \
          '&posi=' \
          '&picture=' \
          '&groupId=' \
          '&ua=098%23E1hvcpvPvBhvUpCkvvvvvjiPn2q9tj38PFLZljrCPmPpzjlWRFLO0j3URFcwsj3CPQGCvvpvvPMMvphvC9mvphvvvvyCvhACIzt%2FjaQaRfUTnZJt9b8rVTtYVVzOdiZBRknbkbm65i9Xwhb9%2B2Kzr2E9ZRAn%2BbeAhj3mAXZTKFyzOvxr08TJ%2Bulz8e0xdBuKdeQEKphv8vvvpHIvvvvvvvCHhQvvvLvvvhZLvvmCvvvvBBWvvvHyvvCHhQvvv7oEvpvVvpCmpR2vuphvmvvvpLhKEzV2RphvCvvvphm5vpvhvvCCBUwCvvpv9hCvdphvhppCtKRavvvHNAZNog7EUfvtCQhvCli4zYMwNwGtvpvhvvCvp86CvvyvvZ3n1pvvmCJCvpvZ7DQvvRdw7Di44AM5MCxfsldoz0vtvpvhvvCvpv%3D%3D&needFold=0' \
          '&_ksTS=1582893081626_352' \
          '&callback=jsonp353' \

    html = requests.get(url, headers=Headers)
    html = html.text

    return html


def doc_write(page, html):

    pathname = '../data/' + str(page) + '.html'
    with open(pathname, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    my_page = 1
    while True:
        sleep(random.randint(2, 6))

        my_html = get_comment(my_page)

        if 'rateDetail' in str(my_html):
            doc_write(my_page, my_html)

            print('%s has finished.' % my_page)
            my_page += 1
        else:
            print('Error.')
            break
