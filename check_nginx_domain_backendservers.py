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
        try:
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
        except Exception as e:
                   pass
        for k,v in servername_proxypass_d.iteritems():
             if v in ups_d:
                   servername_with_backend[k]=[value.split()[1] for value in ups_d.get(v)]
        return servername_with_backend

def settings(setarg):
        domainPrincipalJsonStr='{"domainmy.goolefx.com":"负责人1","domainmy2.goolefx.com":"负责人2"}'
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
