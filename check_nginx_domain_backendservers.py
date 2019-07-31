#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-28 15:49
__author__ = 'qiaokaiqiang'
import os,re
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
basedir=os.path.dirname(os.path.abspath(__file__))
conf=basedir+'/servers/service-clean.xiaozhu.com.product.conf'
#confdir=basedir+'/servers/'
confdir="/usr/local/xzsoft/nginx/conf/servers/"
def generate_dict(file,servername_with_backend={}):
        upstream_backend_pattern=re.compile(r'^\s*server\s+\b(?:[0-9]{1,3}\.){3}[0-9]{1,9}\b:80.*$')
        upstream_name_pattern=re.compile(r'^\s*upstream\s+(.*)\s*{')
        server_name_pattern=re.compile(r'^\s*server_name\s+(.*);')
        singleleftforward_brace_pattern=re.compile(r'^\s*}\s*$')
        proxy_pass_pattern=re.compile(r'^\s*proxy_pass\s+http://(.*);')

        up_name=''
        ups_tag=False
        server_tag=False
        count=0
        ups_d={}
        servername_proxypass_d={}
        with open(file,'r') as f:

            for i in f:
                count+=1
                if upstream_name_pattern.search(i):
                    ups_tag=True
                    upstream_pos=count
                    up_name=upstream_name_pattern.search(i).group(1).strip()
                    upstream_l=[]
                    continue

                if ups_tag and  singleleftforward_brace_pattern.search(i):
                    ups_tag=False
                    upstream_l=[]
                    up_name=None

                if ups_tag:
                    if upstream_backend_pattern.search(i):
                        upstream_l.append(i.strip())

                if up_name:
                    ups_d[up_name]=upstream_l
                if server_name_pattern.search(i):
                    server_tag=True
                    server_name=server_name_pattern.search(i).group(1)

                if server_tag:
                    if proxy_pass_pattern.search(i):
                        proxypass_ups=proxy_pass_pattern.search(i).group(1)
			if proxypass_ups in ups_d:
                    	    servername_proxypass_d[server_name]=proxypass_ups
			    server_tag=False
            for k,v in servername_proxypass_d.iteritems():

                if v in ups_d:
                    servername_with_backend[k]=[value.split()[1] for value in ups_d.get(v)]
        return servername_with_backend

def settings(setarg):
        domainPrincipalJsonStr='{"imserverchat.xiaozhu.com":"任凯","opensmart.xiaozhu.com":"任凯","openapi.xiaozhu.com":"任凯","securewireless.xiaozhu.com":"任凯","wirelesspub.xiaozhu.com":"任凯","www.xiaozhu.com":"任凯","xiaozhu.com":"任凯","*.xiaozhu.com":"任凯","www.xiaozhu.com xiaozhu.com *.xiaozhu.com":"任凯","xzcallback.xiaozhu.com":"任凯","xzh5.xiaozhu.com":"任凯","icomethelper.xiaozhu.com":"任凯","quartz-callback.xiaozhu.com":"任凯","service-main.xiaozhu.com":"任凯","crontab.xiaozhu.com":"任凯","baojierake.xiaozhu.com":"孟昭云","dingpa.xiaozhu.com":"孟昭云","imserver.xiaozhu.com":"徐新","service-bizcounter.xiaozhu.com":"徐新","wirelesspub-global.xiaozhu.com":"徐新","securewireless-global.xiaozhu.com":"徐新","service-global.xiaozhu.com":"徐新","service-remind.xiaozhu.com":"徐新","service-remindgroup.xiaozhu.com":"徐新","greatwall.xiaozhu.com":"徐新","statistics.xiaozhu.com":"王路","service-statistics.xiaozhu.com":"王路","service-recall.xiaozhu.com":"王路","service-recommend.xiaozhu.com":"王路","authorization.xiaozhu.com":"王路","open.xiaozhu.com":"王路","service-open.xiaozhu.com":"王路","service-search.xiaozhu.com":"王路","m.xiaozhu.com":"邓朝瑞","securewireless-comment.xiaozhu.com":"常亮","wirelesspub-comment.xiaozhu.com":"常亮","xzh5-comment.xiaozhu.com":"常亮","service-comment.xiaozhu.com":"常亮","securewireless-ducoin.xiaozhu.com":"常亮","service-ducoin.xiaozhu.com":"常亮","service-main.xiaozhu.com":"常亮","service-fdmall.xiaozhu.com":"常亮","wirelesspub-order.xiaozhu.com":"杨耿","service-bussiness-order.xiaozhu.com":"杨耿","service-open-order.xiaozhu.com":"杨耿","service-order.xiaozhu.com":"杨耿","service-rent.xiaozhu.com":"杨耿","service-insurance.xiaozhu.com":"杨耿","service-promotion.xiaozhu.com":"杨耿","securewireless-clean.xiaozhu.com":"尹亮","wirelesspub-clean.xiaozhu.com":"尹亮","xzh5-clean.xiaozhu.com":"尹亮","service-clean.xiaozhu.com":"尹亮","api-smart.xiaozhu.com":"尹亮","securewireless-smart.xiaozhu.com":"尹亮","service-smart.xiaozhu.com":"尹亮","securewireless-fdmall.xiaozhu.com":"尹亮","wirelesspub-fdmall.xiaozhu.com":"尹亮","securewireless-photoservice.xiaozhu.com":"尹亮","service-photoservice.xiaozhu.com":"尹亮","securewireless-linen.xiaozhu.com":"尹亮","service-linen.xiaozhu.com":"尹亮","wirelesspub-userregister.xiaozhu.com":"常亮","wirelesspub-uic.xiaozhu.com":"常亮","service-uic.xiaozhu.com":"常亮","wirelesspub-lodgeunitold.xiaozhu.com":"常亮","xzh5-lodgeunitold.xiaozhu.com":"常亮","settlement.xiaozhu.com":"邓朝瑞","appup.xiaozhu.com":"徐新","securewireless-appup.xiaozhu.com":"徐新","service-appup.xiaozhu.com":"徐新","opensns.xiaozhu.com":["常亮","刘孝松"],"service-opensns.xiaozhu.com":["常亮","刘孝松"],"paycallback.xiaozhu.com":"杨耿","securewireless-pay.xiaozhu.com":"杨耿","wirelesspub-pay.xiaozhu.com":"杨耿","xzh5-pay.xiaozhu.com":"杨耿","service-pay.xiaozhu.com":"杨耿","service-audit.xiaozhu.com":"孟昭云","bizguard.xiaozhu.com":["任凯","陈龙"],"service-bizguard.xiaozhu.com":["任凯","陈龙"],"bizverify.xiaozhu.com":["任凯","陈龙"],"service-coupon.xiaozhu.com":["徐新","贾龙龙"],"wirelesspub-innerbusiness.xiaozhu.com":"孟昭云","service-center.xiaozhu.com":"尹亮","wirelesspub-servicecenter.xiaozhu.com":"尹亮","service-pay-channel.xiaozhu.com":["熊方磊","杨耿"],"wirelesspub-buyout.xiaozhu.com":"孟昭云","service-buyout.xiaozhu.com":"孟昭云","wirelesspub-promotion-front.xiaozhu.com":"杨耿","service-mq-center.xiaozhu.com":"陈龙","dingpa-pro.xiaozhu.com":"谭琳琳","securewireless-order.xiaozhu.com":"杨耿","activity.xiaozhu.com":"郭威","datacenter.xiaozhu.com":["杨唐海","孟昭云"],"gitlab111.idc.xiaozhu.com":"运维组","image.xiaozhustatic1.com":"运维组","image.xiaozhustatic2.com":"运维组","image.xiaozhustatic3.com":"运维组","imgsec.xiaozhustatic1.com":"运维组","service-operations.xiaozhu.com":"王路","wirelesspub-operations.xiaozhu.com":"王路","promotion.xiaozhu.com":"杨耿","service-promotion-front.xiaozhu.com":"杨耿","jianguan.xiaozhu.com":"杨颖"}'
        if setarg=='domainPrincipalDict':
		domainPrincipalDict=json.loads(s=domainPrincipalJsonStr)
		return domainPrincipalDict
if __name__ == '__main__':
    servername_with_backend = {}
    for i in os.listdir(confdir):
        if i.endswith(".conf"):
            file=confdir+'/'+i
            generate_dict(file,servername_with_backend)
    domainPrincipalDict=settings('domainPrincipalDict')
    for k,v in servername_with_backend.iteritems():
       principal=domainPrincipalDict.get(k,"暂无")
       if type(principal) is list: principal=",".join(principal)
       backends=",".join(v)
       print '域名: %s  对应的后端机: %s  服务的负责人: %s'%(k,backends,principal)
