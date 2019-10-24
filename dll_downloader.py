## get link -> send it to idm -> downoad -> send to movie folder -> done
import sys,webbrowser,re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

if len(sys.argv)>1:
	missing_dll = ' '.join(sys.argv[1:])

else:
	missing_dll =  input("What dll file to download\n") 

try:
	html = urlopen(f"https://dll-files.com/{missing_dll}.dll.html")
	bs = BeautifulSoup(html.read(),'lxml')

except HTTPError:
	print("file not found")

except URLError as a:
	print("url error")
	
else:
	bit_version = bs.findAll('span',{'class':'bit'})
	links =  bs.findAll('td',{'class','url'})

print(len(links))
download_link_pattern = re.compile(r'/download.+')

index = i = 0

for bit in  bit_version:
	
	if '64' in bit:
		index = i
	else:
		i += 1
print(index)
# for link in links:
	
# 	links_list = download_link_pattern.findall(str(link))

# webbrowser.open('https://www.dll-files.com'+links_list[index])