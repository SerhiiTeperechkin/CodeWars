def domain_name(url):
    domain = ['http://', 'www.', 'https://']
    for i in domain:
        url = url.replace(i, '')
    return url.split('.')[0]
