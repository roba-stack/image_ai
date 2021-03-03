from flickrapi import FlickrAPI
from urllib.request import urlretrieve
import sys,os,time
from pprint import pprint

key="f27144df93d518390ee782f382dd486f"
sercret="7f4eab14b2b45115"
imagename=sys.argv[1]
#コマンドプロンプト(Win)、ターミナル(Mac)上で、python data.py catなど.pyの後を指定して入力できるようにする。
save_dir="./images/"+imagename
if not os.path.exists(save_dir):os.mkdir(save_dir)
flickr=FlickrAPI(key,sercret,format="parsed-json")
flickr_result=flickr.photos.search(text=imagename,per_page=300,media="photos",
              sort="relevance",safe_search=1,extras="url_q,licence")
photos=flickr_result['photos']
#pprint(flickr_result)
for photo in photos['photo']:
    url_q = photo['url_q']
    filepath=save_dir+"/"+photo["id"]+".jpg"
    if os.path.exists(filepath):continue
    urlretrieve(url_q,filepath)
    time.sleep(1)
