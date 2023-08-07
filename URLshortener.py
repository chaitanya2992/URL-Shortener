import requests
def Shorten_Link(full_link, link_name):
    API_Key = 'c6a03c9ba47a485a0f3591b919139e870c36e'
    Base_URL = 'https://cutt.ly/api/api.php'
    payload = {'key':API_Key, 'short':full_link, 'name':link_name}
    request = requests.get(Base_URL, params = payload)
    data = request.json()
    print('')

    try:
        title = data['url']['title']
        short_Link= data['url']['shortLink']
        print('Title:', title)
        print('Link:', short_Link)
    except:
        status = data['url']['status']
        print('Error Status:', status)

Link = input('Enter a link: ')
name = input('Give your link a name: ')

Shorten_Link(Link, name)