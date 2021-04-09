import requests


_url = 'https://njvss-appointments-public.s3.amazonaws.com/data/data.json'
ADDRESS_FIELD = 'Facility Address'


def get_json():
    result = requests.get(_url)
    return result.json()


def available_only(data):
    return [t for t in data if t['available'] == 'yes']


def extract_addres(res):
    return res['official'][ADDRESS_FIELD].replace('\n', ' ')
