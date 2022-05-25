# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
static_prefix="../src/static/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Prism",
    "type": "git",
    "url": "https://github.com/Reedo0910/Maverick-Theme-Prism.git",
    "branch": "deploy"
}

enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "starmoe's diary"
site_logo = "${static_prefix}favicon.ico"
site_build_date = "2019-12-18T16:51+08:00"
author = "starmoe"
email = "ztzylf12345@163.com"
author_homepage = "https://hexo.hydi.xyz/"
description = "Stand unbowed to anxiety or depression, as a place for us must be somewhere in world."
key_words = ['starmoe', 'life', 'diary']
language = 'zh-CN'
external_links = [
#    {
#        "name": "Maverick",
#        "url": "https://github.com/AlanDecode/Maverick",
#        "brief": "🏄‍ Go My Own Way."
#    },
#    {
#        "name": "三無計劃",
#        "url": "https://www.imalan.cn",
#        "brief": "熊猫小A的主页。"
#    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/WFA897264",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/bro-xun",
        "icon": "gi gi-github"
    },
    {
        "name": "Telegram",
        "url": "https://t.me/BroXun",
        "icon": "gi gi-telegram"
    },
#    {
#        "name": "Weibo",
#        "url": "https://weibo.com/5245109677/",
#        "icon": "gi gi-weibo"
#    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
