import urllib.request
import urllib.parse
import bs4


def site_map(url):

    #help function wich return dictionary with title and set of links
    def aux(url_link):	 
        website_link = urllib.request.urlopen(url_link)
        soup_link = bs4.BeautifulSoup(website_link, "html.parser")
        set_link = set()
        res_link = {}
        
        # find all links, choose only http and https
        for link_link in soup_link.findAll('a'):
            link_url_link = link_link.get('href')
            if link_url_link[0] != '#':
                set_link.add(link_url_link)
                if link_url_link not in res:
                    parse = urllib.parse.urlparse(link_url_link)
                    if parse.scheme == 'http' or parse.scheme == 'https':
                        res[link_url_link] = {}
                        res[link_url_link] = aux(link_url_link)
              
        title = soup_link.find_all('title')
        if len(title) > 0:
            res_link['title'] = title[0].getText()
        else:
            res_link['title'] = 'NO TITLE' 
        res_link['links'] = set_link
        return res_link

    res = {}
    website = urllib.request.urlopen(url)
    soup = bs4.BeautifulSoup(website, "html.parser")
    for link in soup.findAll('a'):
        link_url = link.get('href')
        if link_url[0] != '#':
            parse = urllib.parse.urlparse(link_url)
            print(parse.scheme)
            if parse.scheme == 'http' or parse.scheme == 'https':
                res[link_url] = aux(link_url)
    return res

# only for test
if __name__ == "__main__":
    url = 'http://0.0.0.0:8000/'
    s_map = site_map(url)
    #print(s_map)
    for item in s_map:
    	print(item, s_map[item])

