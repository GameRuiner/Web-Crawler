import urllib.request

# function try to open url, in case error return 'error' 
def url_open(url):
    try: 
        site = urllib.request.urlopen(url)
    except urllib.error.HTTPError as err:
        site = "error"
        if err.code == 404:
            print("Page not found!")
        elif err.code == 403:
            print("Access denied!")
        else:
            print("Something happend! Error code", err.code)
    except urllib.error.URLError as err:
        site = "error"
        print("Some other error happened", err.reason)
    return site
            
