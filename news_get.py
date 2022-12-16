import requests

headers = {'X-Api-Key': 'f040917943de4696b4ab451acf3fc3b7'}
url = 'https://newsapi.org/v2/everything'
params = {
    'q': '太陽電池 OR 太陽光発電',
    'sortBy': 'publishedAt',
    'pageSize': 100
}
response = requests.get(url, headers=headers, params=params)

import pandas as pd
pd.options.display.max_colwidth = 25

if response.ok:
    data = response.json()
    df = pd.DataFrame(data['articles'])
    print('totalResults:', data['totalResults'])

print(df[[ 'publishedAt', 'title', 'url']])