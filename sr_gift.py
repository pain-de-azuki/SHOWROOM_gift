import requests
import json
import pprint
from datetime import datetime

def main():
    url1 = 'https://www.showroom-live.com/api/live/gift_log?room_id=313757'
    url2 = 'https://www.showroom-live.com/api/live/gift_list?room_id=313757'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    r = requests.get(url1,headers=headers)
    r2 = requests.get(url2,headers=headers)
    json_log = r.json()
    json_list = r2.json()

    gift_master_list = []
    gift_master_list.extend(json_list.get('enquete'))
    gift_master_list.extend(json_list.get('normal'))

    for a_gift in json_log['gift_log']:
        pprint.pprint('name:{}'.format(a_gift['name']))
        pprint.pprint('gift_id:{}'.format(a_gift['gift_id']))
        pprint.pprint('num:{}'.format(a_gift['num']))
        time = datetime.fromtimestamp(a_gift['created_at'])
        pprint.pprint('created_at:{}'.format(time))

        gift_name = next(filter(lambda x: x.get('gift_id') == a_gift.get('gift_id'), gift_master_list)).get('gift_name', '')
        if gift_name != '':
            pprint.pprint('gift_name:{}'.format(gift_name))

if __name__ == "__main__":
    main()
