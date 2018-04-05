 #!/usr/bin/python 
 # -*- coding:utf-8 -*-
import random
import os,sys
import pymysql
import requests
 

#信息类
class userInfo:

	mini = 100101
	maxi = 239268
	threadname = "root_a"
	path = "H:/Python36/_workplace/imeetu/girls_00100000/"



	output = open('_error_sql_%s.txt'%threadname, 'w')
	db = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="imeetu",charset='utf8')

	infokey = ("网页编号","昵称","性别","生日","星座","身高","体重","所在城市","我的家乡",
			"身份","学校","专业",
			"个性标签","兴趣爱好")

	def __init__(self,list_baseInfo,list_professionInfo,str_personalityInfo,str_hobbyInfo):
		i=0
		self.mydict = {}
		for info in (list_baseInfo + list_professionInfo):
			#print(str(userInfo.infokey[i])+":"+str(info))
			self.mydict[userInfo.infokey[i]] = info
			i = i + 1
		self.mydict[userInfo.infokey[-1]] = str_hobbyInfo
		self.mydict[userInfo.infokey[-2]] = str_personalityInfo

		#数据库连接
	def queryInfo(self):
		pass

	
	#插入新问题
	def insertInfo(self):
		try:
			#print ("[I]: 准备执行插入数据库")
			sqlstr = "INSERT INTO userinfo  VALUES (NULL,%s,\'%s\', \'%s\',\'%s\',\'%s\',%s,%s,	\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');" \
				%(self.mydict[userInfo.infokey[0]],self.mydict[userInfo.infokey[1]],self.mydict[userInfo.infokey[2]],\
					self.mydict[userInfo.infokey[3]],self.mydict[userInfo.infokey[4]],self.mydict[userInfo.infokey[5]],\
					self.mydict[userInfo.infokey[6]],self.mydict[userInfo.infokey[7]],self.mydict[userInfo.infokey[8]],\
					self.mydict[userInfo.infokey[9]],self.mydict[userInfo.infokey[10]],\
					self.mydict[userInfo.infokey[11]],self.mydict[userInfo.infokey[12]],self.mydict[userInfo.infokey[13]])

			cursor = userInfo.db.cursor() 
			cursor.execute(sqlstr)
			userInfo.db.commit()
			print("[I]: %s 储存成功"%self.mydict[userInfo.infokey[0]])
		except Exception as e:
			print("[E]: %s 储存出错"%self.mydict[userInfo.infokey[0]]+str(e))
			userInfo.output.write(sqlstr+"\n")
		else:
			pass

	def selectInfo(self,resultfile):
		rf = open(resultfile, 'a')
		cursor = userInfo.db.cursor() 
		sql ="select xingquaihao from userinfo"
		try:
			i=0
			# 执行SQL语句
			cursor.execute(sql)
			# 获取所有记录列表
			results = cursor.fetchall()
			mystr=""
			for row in results:
				mystr=row[0]
				# 打印结果
				print (str(i))
				i=i+1
				rf.write(mystr+" ")
				if i % 100 = 0 :
					rf.write("\n")
		except Exception as e:
			print("[E]: %s 获取数据出错"%str(e))
		finally:
			rf.close()


print("开始执行...")
u = userInfo([1,2,3],[4,5,6],"7","8")

u.selectInfo("_xingquaihao.txt")
