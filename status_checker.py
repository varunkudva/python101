# coding=utf-8
import requests

if __name__ == '__main__':
    r = requests.get('https://egov.uscis.gov/casestatus/landing.do')
    print(r.content)
