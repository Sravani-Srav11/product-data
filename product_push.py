import requests
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--productids",required=True,help="provide list of productids in comma separated values")
parser.add_argument("--locales",required=True, help="provide locales in comma separated")
args = parser.parse_args()
articles = args.productids.split(',')
locales = args.locales.split(',')
url = "https://xxxxxxxx/update/articles"
requestbody = {
  "locales": ["en-PH","en-US"],
  "articleNumbers":["EE9033","EY4494","EY4495","GA0061","GA0062"],
  "isProdUpdate" : False
}

while len(articles) > 0:
    split_product = articles[:4]
    requestbody["articleNumbers"] = split_product
    requestbody["locales"] = locales
    print(requestbody)
    # r = requests.post(url=url,json=requestbody,headers={"Content-Type": "application/json","x-api-key": "xxxxxxxxxxxxxxxxxxx", "x-signature": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"},verify=False)
    # if r.status_code == 200:
    #     print("success")
    # else:
    #     print("request is failed")
    del articles[:4]
