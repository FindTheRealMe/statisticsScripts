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
conf=basedir+'/dockers/mydomain-clean.xxx.com.product.conf'
#confdir=basedir+'/dockers/'
confdir="/usr/local/alibabasoft/nginx/conf/dockers/"
def generate_dict(file,dockername_with_backend={}):
        upstream_backend_pattern=re.compile(r'^\s*docker\s+\b(?:[0-9]{1,3}\.){3}[0-9]{1,9}\b:80.*$')
        upstream_name_pattern=re.compile(r'^\s*upstream\s+(.*)\s*{')
        docker_name_pattern=re.compile(r'^\s*docker_name\s+(.*);')
        singleleftforward_brace_pattern=re.compile(r'^\s*}\s*$')
        proxy_pass_pattern=re.compile(r'^\s*proxy_pass\s+http://(.*);')

        up_name=''
        ups_tag=False
        docker_tag=False
        count=0
        ups_d={}
        dockername_proxypass_d={}
        with close(file,'r') as f:

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
                if docker_name_pattern.search(i):
                    docker_tag=True
                    docker_name=docker_name_pattern.search(i).group(1)

                if docker_tag:
                    if proxy_pass_pattern.search(i):
                        proxypass_ups=proxy_pass_pattern.search(i).group(1)
			if proxypass_ups in ups_d:
                    	    dockername_proxypass_d[docker_name]=proxypass_ups
			    docker_tag=False
            for k,v in dockername_proxypass_d.iteritems():

                if v in ups_d:
                    dockername_with_backend[k]=[value.split()[1] for value in ups_d.get(v)]
        return dockername_with_backend

def settings(setarg):
        domainPrincipalJsonStr='{"imdockerchat.xxx.com":"任凯","closesmart.xxx.com":"任凯","closeapi.xxx.com":"任凯","adidaswireless.xxx.com":"任凯","public.xxx.com":"任凯","www.xxx.com":"任凯","xxx.com":"任凯","*.xxx.com":"任凯","www.xxx.com xxx.com *.xxx.com":"任凯","alibabaletsgo.xxx.com":"任凯","alibabah5.xxx.com":"任凯","icomethelper.xxx.com":"任凯","quartz-letsgo.xxx.com":"任凯","mydomain-main.xxx.com":"任凯","crontab.xxx.com":"任凯","baojierake.xxx.com":"孟昭云","dingding.xxx.com":"孟昭云","imdocker.xxx.com":"徐新","mydomain-bizcounter.xxx.com":"徐新","public-global.xxx.com":"徐新","adidaswireless-global.xxx.com":"徐新","mydomain-global.xxx.com":"徐新","mydomain-remind.xxx.com":"徐新","mydomain-remindgroup.xxx.com":"徐新","greatwall.xxx.com":"徐新","statistics.xxx.com":"王路","mydomain-statistics.xxx.com":"王路","mydomain-recall.xxx.com":"王路","mydomain-recommend.xxx.com":"王路","authorization.xxx.com":"王路","close.xxx.com":"王路","mydomain-close.xxx.com":"王路","mydomain-search.xxx.com":"王路","m.xxx.com":"邓朝瑞","adidaswireless-comment.xxx.com":"常亮","public-comment.xxx.com":"常亮","alibabah5-comment.xxx.com":"常亮","mydomain-comment.xxx.com":"常亮","adidaswireless-ducoin.xxx.com":"常亮","mydomain-ducoin.xxx.com":"常亮","mydomain-main.xxx.com":"常亮","mydomain-fdmall.xxx.com":"常亮","public-order.xxx.com":"杨耿","mydomain-bussiness-order.xxx.com":"杨耿","mydomain-close-order.xxx.com":"杨耿","mydomain-order.xxx.com":"杨耿","mydomain-rent.xxx.com":"杨耿","mydomain-insurance.xxx.com":"杨耿","mydomain-macpro.xxx.com":"杨耿","adidaswireless-clean.xxx.com":"尹亮","public-clean.xxx.com":"尹亮","alibabah5-clean.xxx.com":"尹亮","mydomain-clean.xxx.com":"尹亮","api-smart.xxx.com":"尹亮","adidaswireless-smart.xxx.com":"尹亮","mydomain-smart.xxx.com":"尹亮","adidaswireless-fdmall.xxx.com":"尹亮","public-fdmall.xxx.com":"尹亮","adidaswireless-photomydomain.xxx.com":"尹亮","mydomain-photomydomain.xxx.com":"尹亮","adidaswireless-linen.xxx.com":"尹亮","mydomain-linen.xxx.com":"尹亮","public-userregister.xxx.com":"常亮","public-uic.xxx.com":"常亮","mydomain-uic.xxx.com":"常亮","public-lodgeunitold.xxx.com":"常亮","alibabah5-lodgeunitold.xxx.com":"常亮","settlement.xxx.com":"邓朝瑞","appup.xxx.com":"徐新","adidaswireless-appup.xxx.com":"徐新","mydomain-appup.xxx.com":"徐新","closesns.xxx.com":["常亮","刘孝松"],"mydomain-closesns.xxx.com":["常亮","刘孝松"],"alipayletsgo.xxx.com":"杨耿","adidaswireless-alipay.xxx.com":"杨耿","public-alipay.xxx.com":"杨耿","alibabah5-alipay.xxx.com":"杨耿","mydomain-alipay.xxx.com":"杨耿","mydomain-audit.xxx.com":"孟昭云","bizguard.xxx.com":["任凯","陈龙"],"mydomain-bizguard.xxx.com":["任凯","陈龙"],"bizverify.xxx.com":["任凯","陈龙"],"mydomain-coupon.xxx.com":["徐新","贾龙龙"],"public-innerbusiness.xxx.com":"孟昭云","mydomain-central.xxx.com":"尹亮","public-mydomaincentral.xxx.com":"尹亮","mydomain-alipay-channel.xxx.com":["熊方磊","杨耿"],"public-buyout.xxx.com":"孟昭云","mydomain-buyout.xxx.com":"孟昭云","public-macpro-front.xxx.com":"杨耿","mydomain-mq-central.xxx.com":"陈龙","dingding-pro.xxx.com":"谭琳琳","adidaswireless-order.xxx.com":"杨耿","activity.xxx.com":"郭威","datacentral.xxx.com":["杨唐海","孟昭云"],"gitlab111.idc.xxx.com":"运维组","image.xxxstatic1.com":"运维组","image.xxxstatic2.com":"运维组","image.xxxstatic3.com":"运维组","imgsec.xxxstatic1.com":"运维组","mydomain-operations.xxx.com":"王路","public-operations.xxx.com":"王路","macpro.xxx.com":"杨耿","mydomain-macpro-front.xxx.com":"杨耿","jianguan.xxx.com":"杨颖"}'
        if setarg=='domainPrincipalDict':
		domainPrincipalDict=json.loads(s=domainPrincipalJsonStr)
		return domainPrincipalDict
if __name__ == '__main__':
    dockername_with_backend = {}
    for i in os.listdir(confdir):
        if i.endswith(".conf"):
            file=confdir+'/'+i
            generate_dict(file,dockername_with_backend)
    domainPrincipalDict=settings('domainPrincipalDict')
    for k,v in dockername_with_backend.iteritems():
       principal=domainPrincipalDict.get(k,"暂无")
       if type(principal) is list: principal=",".join(principal)
       backends=",".join(v)
       print '域名: %s  对应的后端机: %s  服务的负责人: %s'%(k,backends,principal)
