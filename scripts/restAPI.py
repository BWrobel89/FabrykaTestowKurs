# CREATE -> POST
# READ -> GET
# UPDATE - > PUT
# DELETE -> DELETE

import requests

# post = requests.post('http://httpbin.org/post')
# put = requests.put('http://httpbin.org/put')
# delete = requests.delete('http://httpbin.org/delete')
#
# print(delete)

parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=parameters)
print(r.url)
print(r.text)
print(r.encoding)