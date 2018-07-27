import urllib.request
import ssl

context = ssl._create_unverified_context()
response = urllib.request.urlopen('https://www.python.org', context=context)
print(response.read().decode('utf-8'))
print("***************")
print(type(response))