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


    for a_gift in json_log['gift_log']:
        pprint.pprint('name:{}'.format(a_gift['name']))
        pprint.pprint('gift_id:{}'.format(a_gift['gift_id']))
        pprint.pprint('num:{}'.format(a_gift['num']))
        time = datetime.fromtimestamp(a_gift['created_at'])
        pprint.pprint('created_at:{}'.format(time))

        for list_enquete in json_list['enquete']:
            if a_gift['gift_id'] == list_enquete['gift_id'] :
                pprint.pprint('gift_name:{}'.format(list_enquete['gift_name']))

        for list_normal in json_list['normal']:
            if a_gift['gift_id'] == list_normal['gift_id'] :
                pprint.pprint('gift_name:{}'.format(list_normal['gift_name']))

if __name__ == "__main__":
    main()
