from bs4 import  BeautifulSoup
import urllib
import urllib.request
import os
url='https://bohaishibei.com/post/category/main/page/1/'

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')
html_list = soup.find_all('article')

for i in html_list:
     page_name = i.a['title']
     page_url = i.a['href']
     img_dir = str(page_name).strip()
     os.makedirs(os.path.join("D:\\newproject", img_dir))
     page_html = urllib.request.urlopen(page_url)
     page_soup = BeautifulSoup(page_html,'html.parser')
     img_list = page_soup.find_all('article')
     img_url_list = []
     for x in img_list:
            img_list_a = x.find_all('img') ##img_url 是一个列表
            cnt = 0
            os.chdir("D:\\newproject\\" + img_dir)
            paths = ("D:\\newproject\\" + img_dir+'\\')
            for y in range(1,len(img_list_a)+1):
                img_ = img_list_a[y-1]
                img_url = img_['src']
                img_tp = (img_url.split('.')[-1])
                img_name = str(cnt) + '.' + img_tp
                urllib.request.urlretrieve(img_url, '{}{}'.format(paths, img_name))
                cnt = cnt + 1

print ('hello')