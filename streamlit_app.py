import requests

api_key = "f0e46463ccf90abd0defd9c79c8568e922e07a835961b1676cdb2065ecc23494"
url = "http://apis.data.go.kr/B551011/EngService2/searchStay2"
params = {
    "ServiceKey": api_key,
    "numOfRows": 1,
    "pageNo": 1,
    "MobileOS": "ETC",
    "MobileApp": "hotel_analysis",
    "_type": "json",
    "areaCode": 1  # 서울
}

res = requests.get(url, params=params)
print("HTTP status code:", res.status_code)
print(res.json().get("response", {}).get("header", {}))
