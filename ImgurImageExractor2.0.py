import urllib2,os,thread,Queue,time
from bs4 import BeautifulSoup
i=0
q=Queue.Queue()

def dwld():
	os.system(q.get())
def enQ(link):
	i=0
	page=urllib2.urlopen(link).read()
	soup=BeautifulSoup(page)
	for a in soup.findAll('img',src=True):
		if(a['src'][-3:]=="jpg" or a['src'][-3:]=="png"):
			try:
				print "found " +str(i)+ " items"
				q.put("wget -nc "+"\""+a['src'][2:]+"\""+" -P ImgurImgDump/")
				i+=1
			except:
				pass
def openImgur(link):
	j=0
	page=urllib2.urlopen(link).read()
	soup=BeautifulSoup(page)
	for a in soup.findAll('a',href=True):
		if(a['href'][:len("/gallery/")]=="/gallery/" and j>3):
			print "Link Count : " +str(j)+ " : http://imgur.com"+a['href']	
			thread.start_new_thread(enQ,("http://imgur.com"+a['href'],))
		j+=1

thread.start_new_thread(openImgur,("http://www.imgur.com",))

while True:
	while not q.empty():
		dwld()
