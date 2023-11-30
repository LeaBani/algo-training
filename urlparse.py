from urllib.parse import urlparse

def domain_name(url):
    
    # Add 'http://' if no scheme is provided so that the algo is working for any url
    if not urlparse(url).scheme:
        url = 'http://' + url

    # Parse the URL
    parsed_url = urlparse(url)

    # Get the network location part from the parsed URL
    netloc = parsed_url.netloc

    # Check if 'www.' is present and remove it
    if netloc.startswith("www."):
        netloc = netloc[4:]

    # Split the netloc to get just the domain name - [0], the first value
    domain_name = netloc.split('.')[0]

    return domain_name

result = domain_name("www.xakep.ru")
print(result)