import re
from urllib.parse import urlencode
import requests
import time
import os
from hashlib import md5
from multiprocessing.pool import Pool

millis = int(round(time.time() * 1000))

headers = {
    'User-Afent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
}


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',

    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params) + '&timestamp={0}'.format(millis)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('abstract'):
                title = item.get('title')
                images = item.get('image_list', '')
                image_url = item.get('image_url', '')
                if images:
                    for image in images:
                        yield {
                            'image': image.get('url'),
                            'title': title
                        }
                else:
                    yield {
                        'image': image_url,
                        'title': title
                    }
            else:
                continue


def save_image(item):
    pattern = "[`~!@#$%^&*()_\-+=<>?:{}|,.\/;'\\[\]·~！@#￥%……&*（）——\-+={}|《》？：“”【】、；‘’，。、]"
    title = re.sub(pattern, repl=' ', string=item.get('title'))
    if not os.path.exists(title):
        os.mkdir(title)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{}/{}.{}'.format(title, md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print('Failed to save Image', e)


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        save_image(item)


GROUP_START = 0
GROUP_END = 20


def run():
    try:
        for i in range(GROUP_START, GROUP_END + 1):
            offset = i * 20
            main(offset)
        return 'good'
    except Exception as e:
        return print(e)

run()
# if __name__ == '__main__':
# pool = Pool()
# groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
# main()
# pool.map(main, groups)
# pool.close()
# pool.join()
