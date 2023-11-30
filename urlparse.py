from urllib.parse import urlparse

def domain_name(url):
    # Parse the URL using urlparse https://docs.python.org/3/library/urllib.parse.html
    parsed_url = urlparse(url)

    # Get the netloc attribute (network location)
    netloc = parsed_url.netloc
    print(netloc)

    # Check if 'www.' is present and remove it
    if netloc.startswith("www."):
        netloc = netloc[4:]

    # Split netloc to keep just the domain name (index 0 -> first value)
    domain_name = netloc.split('.')[0]

    return domain_name

result = domain_name("http://www.github.com/carbonfive/raygun")
print(result)