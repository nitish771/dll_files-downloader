import sys
import webbrowser
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import details

if __name__ == '__main__':

    missing_dll = 'd3dx9'

    if len(sys.argv) > 1:
        missing_dll = ' '.join(sys.argv[1:])

    elif missing_dll == '':
        missing_dll = input("What dll file to download\n").replace('.dll', '')
        # print(missing_dll)

    try:
        html = urlopen(f"https://www.dll-files.com/{missing_dll}.dll.html")
        bs = BeautifulSoup(html, 'lxml')
        details.detail(bs)
        link = bs.find_all('div', {'class': 'download-link'})
        link = 'https://dll-files.com/' + link[0].a['href']
        webbrowser.open(link)

        ## Download

        # file = requests.get(link, allow_redirects=True)
        # open('/home/wannacry/Documents/' + missing_dll +
        #      '.zip', 'wb').write(file.content)

    except HTTPError:
        print("file not found")

    except URLError as a:
        print("url error")
