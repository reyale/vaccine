import requests


_url = 'https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers'
ADDRESS_FIELD = 'address'


def get_json():
    result = requests.get(_url)
    return result.json()


def available_only(data):
    return [p for p in data['providerList'] if p['availableAppointments'] == 'Y']


def extract_addres(res):
    return res['address']
