import json
import requests


# wordsapi.com
# url = 'https://wordsapiv1.p.mashape.com/words/example'
# response = requests.get(
#     url,
#     headers={
#         "X-Mashape-Key": "",
#         "Accept": "application/json",
#     }
# )

test = {'q': 'www'}
with open('wordsapi-example.json', 'w+', encoding='utf8') as f:
    json.dump(test, f)
