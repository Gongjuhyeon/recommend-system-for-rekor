import pandas as pd
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import json

import requests
serviceKey='PpfhPSmfMfOtRZsPoFifviss7EHlttKgrpDvEB4gQT7PqzGAs1uOC5lLpFNjT0jhBuKAwuVos9V30ozLvfRdKQ%3D%3D'

url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/categoryCode?ServiceKey={}&contentTypeId=12&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest'.format(serviceKey)


response = requests.get(url)
print(response.text)
json_api =response.json()

print(json_api['response']['body']['items']['item'][0])
#df11=json_normalize(json_file['getRivrLvlhPpnSttusInfo']['item'])
#print(response.content)