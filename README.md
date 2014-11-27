Oklink Python Client Library
==================================

Python Client Library for the Oklink API for use with two legged oAuth2, API+Secret

## Version

0.0.1

## Requirements
- [Oklink Account](https://www.oklink.com)
- [Requests](http://docs.python-requests.org/en/latest/)
- [oauth2client](https://developers.google.com/api-client-library/python/guide/aaa_oauth)


## Usage

```python
from oklink.api import OklinkClient
client = OklinkClient.api_secret(api_key="", api_secret="")
r = client.buttonsButton({'name':"python button",'price':2,'price_currency':'BTC'})
print(r.button)
```


