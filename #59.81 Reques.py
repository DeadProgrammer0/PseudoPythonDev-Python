import requests

# TODO : Make program using any API key.

payload = {
    'page':2,
    'count':25
}
ge = requests.get('http://httpbin.org/get', params=payload)

print(ge.url)

data = {
    'usename':'Max',
    'pass':'testing'
}
po = requests.post('http://httpbin.org/post', data=data)

r_dict = po.json()
print(r_dict['form'])

auth = ('max','testing')
au = requests.get('http://httpbin.org/basic-auth/cord/test', auth=('cord','test'))

print(au)






















