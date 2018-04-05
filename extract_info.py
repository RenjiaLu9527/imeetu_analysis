#!/usr/bin/python 
# -*- coding:utf-8 -*-

#author wheee
#time 20180402
#description：从本地html文件中获取数据

from bs4 import BeautifulSoup
import re
from threading import Thread
import _thread	
import time
from userInfoClass import userInfo


print("\n[i] 开始执行...\n\n")

#
SPLITCHAR = "-" #分隔符


#


	

#返回下一个文件名称
def nextfilename(c):
	if c <= 99999 :
		return "girls_%05d"%c+".html"
	else:
		return "girls_%08d"%c+".html"

def mainthread(threadName,startid,endid,path):
	count = startid-1
	fo = open("_error_filename_"+threadName+".txt", "a+")
	filename = ""
	#主循环
	while count <= endid :
		try:
			count = count + 1
			filename = nextfilename(count)
			html_doc = open(path+filename,'r',encoding='UTF-8')
			soup = BeautifulSoup(html_doc, 'lxml')

			#print(filename)

			#listInfo4 = soup.find_all("ul",attrs={"class":"mui-table-view"},limit=4) 
			listInfo4 = soup.select("ul[class='mui-table-view']",limit = 4) 

			#第一块 基本信息区
			list_baseInfo = [count]
			spaninfo  = BeautifulSoup(str(listInfo4[0]), 'lxml').select("span[class='rt']") #返回 <span class="rt">女</span>
			i=1
			for li1 in spaninfo:
				if i==5 :
					highweight = str(li1.get_text()).split("/",1)
					list_baseInfo.append(int(re.match('^\d+', highweight[0]).group()))
					list_baseInfo.append(int(re.match('^\d+', highweight[1]).group()))
				else:
					list_baseInfo.append(li1.get_text())
				i=i+1
			#print(list_baseInfo)
			#测试
			if (len(list_baseInfo) != 9) or (list_baseInfo.count("") > 3) or (list_baseInfo[5] == 0 and list_baseInfo[6] == 0):
				print("[E]: %8d 第一块基本信息区无效"%count)
				fo.write(filename+"- [E]: 第一块基本信息区无效\n")
				continue


			#第二块 职业信息区
			list_professionInfo = []
			spaninfo = BeautifulSoup(str(listInfo4[1]), 'lxml').select("span[class='rt']")
			for li2 in spaninfo:
				list_professionInfo.append(li2.get_text())
			#print(list_professionInfo)

			#测试
			if len(list_professionInfo) != 3 or list_professionInfo.count("")==3:
				print("[E]: %8d 第二块 职业信息区无效"%count)
				fo.write(filename+"- [E]: 第二块职业信息区无效\n")
				continue


			#第三块 个性标签区
			str_personalityInfo = ""
			liinfo = BeautifulSoup(str(listInfo4[2]), 'lxml').select("ul[class='gexing_biaoqian'] > li")
			for li3 in liinfo:
				str_personalityInfo =str_personalityInfo+" "+li3.get_text()
			str_personalityInfo = str_personalityInfo.strip()
			#print(str_personalityInfo)

			#第四块 兴趣爱好区
			str_hobbyInfo = ""
			liinfo = BeautifulSoup(str(listInfo4[3]), 'lxml').select( \
						"ul[class='gexing_biaoqian'] > li")
			for li4 in  liinfo:
				str_hobbyInfo = str_hobbyInfo + " " + li4.get_text()
			str_hobbyInfo = str_hobbyInfo.strip()
			#print(str_hobbyInfo)

			u = userInfo(list_baseInfo,list_professionInfo,str_personalityInfo,str_hobbyInfo)
			u.insertInfo()
		except Exception as e:
			print("[E]: %8d 其他异常"%count+ repr(e))
			fo.write(filename+"- [E]: 其他异常"+str(e)+"\n")
		else:
			pass

	#关闭文件
	fo.close()



#===========================================================================================
try:
	mainthread("Thread-5",134864,250000,"H:/Python36/_workplace/imeetu/girls_00100000/")
	#t=Thread(target=mainthread,args=("Thread-1",1,20000,"H:/Python36/_workplace/imeetu/girls/"))
	#t.start()
	#_thread.start_new_thread( mainthread, ("Thread-1",1,20000,"H:/Python36/_workplace/imeetu/girls/"))
	#_thread.start_new_thread( mainthread, ("Thread-2",20001,40000,"H:/Python36/_workplace/imeetu/girls_20001/"))
	#_thread.start_new_thread( mainthread, ("Thread-3",40001,55000,"H:/Python36/_workplace/imeetu/girls_20001/"))
except Exception as e:
	print ("[E]: 无法启动线程 "+repr(e))

while 1:
	time.sleep(100)
	print("[I]: wait...")






