import urllib.request
import time
import re

#url  ='http://blog.csdn.net/robin__chou/article/details/49099227'

#文章列表
mainurl = 'http://blog.csdn.net/Robin__Chou/article/list/'

EassyList = []

#i = 0;

#从文章类表中获取文章代码
def getURL(url):
	reg = r'<span class=\"link_title\"><a href=\"/robin__chou/article/details/(.+?)\">'
	rtre = re.compile(reg)
	#伪装成浏览器
	req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        });
	oper = urllib.request.urlopen(req);
	data = oper.read() 		#读取HTML文件
	data = data.decode('utf-8')
	rt = re.findall(rtre, data);	
	return rt

def getList():
	num = ['1','2','3','4','5'] 	#页面编号
	for it in num:
		ls = getURL(mainurl + str(it))
		for index in ls:
			EassyList.append(index)

getList()
print(EassyList)

#lst = getURL(mainurl)

while(True):
	for item in EassyList:
		ur = "http://blog.csdn.net/robin__chou/article/details/" + item  #拼接访问地址
		print(ur)							 #打印显示访问地址
		it = urllib.request.Request(ur,headers = {
        	'Connection': 'Keep-Alive',
        	'Accept': 'text/html, application/xhtml+xml, */*',
        	'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        	'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        	});								#伪装浏览器访问地址
		oper = urllib.request.urlopen(it);				
		#data = oper.read()						#读取数据
		#time.sleep(1);

'''
while(True):
	req = urllib.request.Request(url,headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        });

	oper = urllib.request.urlopen(req);
	data = oper.read()
	time.sleep(1);
	print(i);
	i = i+1;
'''


