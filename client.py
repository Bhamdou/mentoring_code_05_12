import requests

response = requests.get('http://127.0.0.1:5000/posts')
posts = response.json()

for post in posts:
    print(post['title'])


response = requests.get('http://127.0.0.1:5000/authors')
authors = response.json()

print('---authors')
for author in authors:
    print(author['name'])