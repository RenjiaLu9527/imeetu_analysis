 # -*- coding:utf-8 -*-
import _thread
import time
from mitmproxy import http
import random
import json
import os,sys
import requests
	

print("\n\n开始监听...\n")


#http://hyql.imeetu.cc/app/index.php?i=5&c=invite&a=index&do=index

#./index.php?i=5&c=invite&a=other&do=index&uid=23758
#	GET /app/index.php?i=5&c=invite&a=other&do=index&uid=23619  
isFirst = 1
countM = 239269
i = 0
def request(flow: http.HTTPFlow):
	global isFirst,countM,i
	# redirect to different host
	#print ("请求链接..")z
	if (isFirst == 1) and (flow.request.pretty_host == "hyql.imeetu.cc") :
		print ("\n========监听到 hyql.imeetu.cc\n")
		#flow.request.path = "/app/index.php?i=5&c=invite&a=other&do=index&uid=239301 "
		#flow.request.path = "/app/index.php?i=5&c=invite&a=index&do=index"
		isFirst = 0
		headers_copyM = flow.request.headers
		try:
			_thread.start_new_thread( getgirlsinfo, (countM,headers_copyM ) )
			pass
		except Exception as e:
			print ("线程出错")
		else:
			pass

		#tem = input("\n[%8d]输入任意字符继续..\n\n"%i)
		#isFirst = 1
		i = i + 1
	else:
		print ("【】跳过抓包线程")

def getgirlsinfo(count,headers_copy):
	#str = ("1","1,2","1,2,3","1,2,3,4","1,2,3,4,5","1,2,3,4,5,6","1,2,3,4,5,6,7","1,2,3,4,5,6,7,8","1,2,3,4,5,6,7,8,9","1,2,3,4,5,6,7,8,9,0")
	maxid = 1000000
	d = 50000
	goahead = "goahead"
	requests.adapters.DEFAULT_RETRIES = 5
	s = requests.session() 
	s.keep_alive = False
	while goahead == "goahead":
		maxid = maxid + d
		while count <= maxid  :
			# 打开一个文件
			fo = open("./girls_00239269/girls_%08d"%count+".html", "w",encoding='UTF-8')
			
			#print (headers_copy)
			url="http://hyql.imeetu.cc/app/index.php?i=5&c=invite&a=other&do=index&uid="+str(count)
			#url="http://hyql.imeetu.cc/app/index.php?i=4&c=invite&a=index&do=index123"
			
			try:

				respone=s.get(url,timeout=10,headers=headers_copy)
			except Exception as e:
				print("count:%8d"%count+"异常 重试 [LOG]\n%s\n"%e)
				s = requests.session()
				count = count - 1
				time.sleep( 1 )
			else:
				
				print("count:%8d"%count+"  状态码：%8d"% respone.status_code+"\n")
				
				fo.write(respone.text)
			finally:
				pass
			
			
			fo.close()
			count = count + 1

		goahead = input("【】结束请输入end\n")
		if (goahead != "end"):
			goahead = "goahead"


