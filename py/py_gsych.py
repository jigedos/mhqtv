#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64
import requests

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "歌星mv"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
			"周杰伦": "周杰伦",
    "陈奕迅": "陈奕迅",
    "Beyond": "Beyond",
    "刘德华": "刘德华",
    "郭富城": "郭富城",
    "张学友": "张学友",
    "黎明": "黎明",
    "李宗盛": "李宗盛",
    "邓丽君": "邓丽君",
    "朴树": "朴树",
    "林子祥": "林子祥",
    "任贤齐": "任贤齐",
    "张信哲": "张信哲",
    "孙楠": "孙楠",
    "张宇": "张宇",
    "周华健": "周华健",
    "蔡依林": "蔡依林",
    "薛之谦": "薛之谦",
    "洛天依": "洛天依",
    "初音未来": "初音未来",
    "许嵩": "许嵩",
    "戴佩妮": "戴佩妮",
    "邓紫棋": "邓紫棋",
    "张韶涵": "张韶涵",
    "蔡健雅": "蔡健雅",
    "莫文蔚": "莫文蔚",
    "刘若英": "刘若英",
    "周深": "周深",
    "毛不易": "毛不易",
    "汪苏泷": "汪苏泷",
    "李宇春": "李宇春",
    "徐佳莹": "徐佳莹",
    "杨宗纬": "杨宗纬",
    "胡彦斌": "胡彦斌",
    "杨千嬅": "杨千嬅",
    "张靓颖": "张靓颖",
    "李荣浩": "李荣浩",
    "杨丞琳": "杨丞琳",
    "林志炫": "林志炫",
    "陶喆": "陶喆",
    "胡夏": "胡夏",
    "李玉刚": "李玉刚",
    "弦子": "弦子",
    "陈小春": "陈小春",
    "萧亚轩": "萧亚轩",
    "鹿晗": "鹿晗",
    "纵贯线": "纵贯线",
    "许巍": "许巍",
    "林俊杰": "林俊杰",
    "赵雷": "赵雷",
    "谭咏麟": "谭咏麟",
    "凤凰传奇": "凤凰传奇",
    "二手玫瑰": "二手玫瑰",
    "容祖儿": "容祖儿",
    "周传雄": "周传雄",
    "SHE": "SHE",
    "苏打绿": "苏打绿",
    "五月天": "五月天",
    "张国荣": "张国荣",
    "梅艳芳": "梅艳芳",
    "孙燕姿": "孙燕姿",
    "李健": "李健",
    "华晨宇": "华晨宇",
    "袁娅维": "袁娅维",
    "大张伟": "大张伟",
    "TFBOYS": "TFBOYS",
    "王俊凯": "王俊凯",
    "易烊千玺": "易烊千玺",
    "王源": "王源",
    "田馥甄": "田馥甄",
    "小虎队": "小虎队",
    "张杰": "张杰",
    "王菲": "王菲",
    "伍佰": "伍佰",
    "刀郎": "刀郎",
    "草蜢": "草蜢",
    "潘玮柏": "潘玮柏",
    "梁静茹": "梁静茹",
    "林宥嘉": "林宥嘉",
    "蔡徐坤": "蔡徐坤",
    "周慧敏": "周慧敏",
    "李圣杰": "李圣杰",
    "张惠妹": "张惠妹",
    "萧敬腾": "萧敬腾",
    "周笔畅": "周笔畅",
    "焦迈奇": "焦迈奇",
    "尤长靖": "尤长靖",
    "郑中基": "郑中基",
    "谭维维": "谭维维",
    "陈慧娴": "陈慧娴",
    "张艺兴": "张艺兴",
    "王嘉尔": "王嘉尔",
    "刘宪华": "刘宪华",
    "张敬轩": "张敬轩",
    "李克勤": "李克勤",
    "阿杜": "阿杜",
    "郭静": "郭静",
    "崔健": "崔健",
    "庾澄庆": "庾澄庆",
    "汪峰": "汪峰",
    "那英": "那英",
    "杨坤": "杨坤",
    "叶倩文": "叶倩文",
    "王心凌": "王心凌",
    "张震岳": "张震岳",
    "韩红": "韩红",
    "齐秦": "齐秦",
    "张雨生": "张雨生",
    "黄品源": "黄品源",
    "林忆莲": "林忆莲",
    "丁当": "丁当",
    "郑智化": "郑智化",
    "李玟": "李玟",
    "谢霆锋": "谢霆锋",
    "黄小琥": "黄小琥",
    "徐小凤": "徐小凤",
    "任嘉伦": "任嘉伦",
    "卓依婷": "卓依婷",
    "逃跑计划": "逃跑计划",
    "青鸟飞鱼": "青鸟飞鱼",
    "飞儿乐队": "飞儿乐队",
    "花儿乐队": "花儿乐队",
    "南拳妈妈": "南拳妈妈",
    "水木年华": "水木年华",
    "动力火车": "动力火车",
    "筷子兄弟": "筷子兄弟",
    "鹿先森乐队": "鹿先森乐队",
    "信乐队": "信乐队",
    "旅行团乐队": "旅行团乐队",
    "By2": "By2",
    "郁可唯": "郁可唯",
    "宋亚森": "宋亚森",
    "费玉清": "费玉清",
    "费翔": "费翔",
    "金志文": "金志文",
    "黄家强": "黄家强",
    "方大同": "方大同",
    "吴克群": "吴克群",
    "罗大佑": "罗大佑",
    "光良": "光良",
    "田震": "田震",
    "凤飞飞": "凤飞飞",
    "谭晶": "谭晶",
    "王杰": "王杰",
    "羽泉": "羽泉",
    "金池": "金池",
    "屠洪刚": "屠洪刚",
    "戴荃": "戴荃",
    "郭采洁": "郭采洁",
    "罗志祥": "罗志祥",
    "王力宏": "王力宏",
    "林肯公园": "林肯公园",
    "迈克尔杰克逊": "迈克尔杰克逊",
    "泰勒·斯威夫特": "泰勒·斯威夫特",
    "阿黛尔": "阿黛尔",
    "BIGBANG": "BIGBANG",
    "LadyGaga": "LadyGaga",
    "贾斯丁比伯": "贾斯丁比伯",
    "中岛美雪": "中岛美雪",
    "仓木麻衣": "仓木麻衣",
    "后街男孩": "后街男孩",
    "布兰妮": "布兰妮",
    "夜愿乐队": "夜愿乐队"
      
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {
			'list':[]
		}
		return result
	cookies = ''
	def getCookie(self):
		cookies_str = self.fetch("https://agit.ai/138001380000/MHQTV/raw/branch/master/bbcookie.txt").text
		cookies_dic = dict([co.strip().split('=') for co in cookies_str.split(';')])
		rsp = requests.session()
		cookies_jar = requests.utils.cookiejar_from_dict(cookies_dic)
		rsp.cookies = cookies_jar
		content = self.fetch("http://api.bilibili.com/x/web-interface/nav", cookies=rsp.cookies)
		res = json.loads(content.text)
		if res["code"] == 0:
			self.cookies = rsp.cookies
		else:
			rsp = self.fetch("https://www.bilibili.com/")
			self.cookies = rsp.cookies
		return rsp.cookies
		
	def categoryContent(self,tid,pg,filter,extend):		
		result = {}
		url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&duration=4&page={1}'.format(tid,pg)
		if len(self.cookies) <= 0:
			self.getCookie()
		rsp = self.fetch(url,cookies=self.cookies)
		content = rsp.text
		jo = json.loads(content)
		if jo['code'] != 0:			
			rspRetry = self.fetch(url,cookies=self.getCookie())
			content = rspRetry.text		
		jo = json.loads(content)
		videos = []
		vodList = jo['data']['result']
		for vod in vodList:
			aid = str(vod['aid']).strip()
			title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
			img = 'https:' + vod['pic'].strip()
			remark = str(vod['duration']).strip()
			videos.append({
				"vod_id":aid,
				"vod_name":title,
				"vod_pic":img,
				"vod_remarks":remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def cleanSpace(self,str):
		return str.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
	def detailContent(self,array):
		aid = array[0]
		url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)

		rsp = self.fetch(url,headers=self.header)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		title = jo['title'].replace("<em class=\"keyword\">","").replace("</em>","")
		pic = jo['pic']
		desc = jo['desc']
		typeName = jo['tname']
		vod = {
			"vod_id":aid,
			"vod_name":title,
			"vod_pic":pic,
			"type_name":typeName,
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":"",
			"vod_actor":"",
			"vod_director":"",
			"vod_content":desc
		}
		ja = jo['pages']
		playUrl = ''
		for tmpJo in ja:
			cid = tmpJo['cid']
			part = tmpJo['part']
			playUrl = playUrl + '{0}${1}_{2}#'.format(part,aid,cid)

		vod['vod_play_from'] = 'B站'
		vod['vod_play_url'] = playUrl

		result = {
			'list':[
				vod
			]
		}
		return result
	def searchContent(self,key,quick):
		result = {
			'list':[]
		}
		return result
	def playerContent(self,flag,id,vipFlags):
		# https://www.555dianying.cc/vodplay/static/js/playerconfig.js
		result = {}

		ids = id.split("_")
		url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid=%20%20{1}&qn=112'.format(ids[0],ids[1])
		rsp = self.fetch(url, cookies=self.cookies)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		ja = jo['durl']
		
		maxSize = -1
		position = -1
		for i in range(len(ja)):
			tmpJo = ja[i]
			if maxSize < int(tmpJo['size']):
				maxSize = int(tmpJo['size'])
				position = i

		url = ''
		if len(ja) > 0:
			if position == -1:
				position = 0
			url = ja[position]['url']

		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = {
			"Referer":"https://www.bilibili.com",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = 'video/x-flv'
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]