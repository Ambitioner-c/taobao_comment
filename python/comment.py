import requests
import random
from time import sleep


Headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/80.0.3987.106 Safari/537.36',
           'cookie': 'cna=gSYsFs5GqgcCAXLV/PLN3yGH; hng=CN%7Czh-CN%7CCNY%7C156; lid=ambitioner%E4%B8%B6; enc=L9HQuV5GHNRsGeq9rZ3xafuSSX2F46GZYB4B2JCyacx3KPhqjHSF%2FRo%2Bw0y9Jx6i4DQECoE%2BjkAgHqXEFzKm1A%3D%3D; _m_h5_tk=29d764e2058930bfd11ab05d80a3cb86_1582804356322; _m_h5_tk_enc=9fb28a8f39883bf19bac2ddcb7ac12d0; sgcookie=DGRVAmM8cBxFOvUJDfVh%2B; uc1=cookie14=UoTUOLRwaXjqcg%3D%3D; t=7458db744d83ab1d06ee636f30708330; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&nk2=Any3BqBNXeXE67%2BP&vt3=F8dBxd3yPWVaWUFtXLY%3D&id2=UUGjMVyuhEU30A%3D%3D; tracknick=ambitioner%5Cu4E36; uc4=nk4=0%40AJc9Jh4DCme1Xd6KuxQkwbBbdrKdGxI%3D&id4=0%40U2OU%2FjjOW%2Bci6bsS%2BHdj1aRVz0Ys; lgc=ambitioner%5Cu4E36; _tb_token_=7e7e5b3b03377; cookie2=145734a209d5cb9239724be258b59208; x5sec=7b22726174656d616e616765723b32223a226266393232346466353634623961343735323239356464663533346366383730434b574c332f4946454a4c796e4d624b2f367a3357673d3d227d; l=dBIU44EgqnlwebYUBOfwZDQk4QQTWdAXCsPr98cToIB1O56Z7dWpxHwEaNbBT3QQEt5AYeKzK6zxJRUp78ULyx_ceTwhKXIpBUJB8e1..; isg=BGRkyc3t5o_MVRGxU2Qu_OUoNWtW_YhnaPBDsH6JiyplKQnzpw7b9yjP7YEx8cC_',
           'referer': 'https://detail.tmall.com/item.htm?id=602858459541&ali_refid=a3_430583_1006:1103534738:N:FcbnhkUVpVThyuKFufQFZg==:2de1d8285a37a32169146d902490766b&ali_trackid=1_2de1d8285a37a32169146d902490766b&spm=a230r.1.14.1&sku_properties=10004:709990523;5919063:6536025'}


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
          '&ua=098%23E1hvEpvxv7OvUvCkvvvvvjiPn2q9sjE2PLMUtj3mPmPpljnhPLsOQjYnn2SWAjlHRphvCvvvvvmCvpvZz2saf4dNznQGDFnfYMdwFYAC7IVrvpvEvvFQvT0rvPFrdphvmpvWvUnMNQvIsu6Cvvyv2mh2HBZvUnJ5vpvhvvmv9FyCvvpvvvvv2QhvCvvvMMGEvpCWvVtSvvwTD7zOaXZBWD0U%2BExrVTtYVVzOa4QBnk19kbmxfBKKNB3r0j7%2BhfUeCbmDYE7rV16kARLUTE9XaDdXS47BhC3qVUcnDOvfjfyCvm9vvvvnphvvvvvv9krvpvkCvvmm86Cv2vvvvUUdphvUUQvv9krvpv9FkphvC99vvpHgo8yCvv9vvUvgAHkORphCvvOvCvvvphmjvpvhvvpvv86CvCh92U0mNc6vaCOidAI3pQeHA46CvvyvCPKmiTwvNCVrvpvEvvFl9sWsvUAEdphvmpvWgQnI4vmGH46CvvyvCb821wZvpBArvpvEvvkC96lnvh77dphvmpvhoUWcHQmudv%3D%3D&needFold=0' \
          '&_ksTS=1582839364887_2210' \
          '&callback=jsonp2211' \

    html = requests.get(url, headers=Headers)
    html = html.text

    return html


def doc_write(page, html):

    pathname = '../data/' + str(page) + '.html'
    with open(pathname, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    my_page = 15
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
