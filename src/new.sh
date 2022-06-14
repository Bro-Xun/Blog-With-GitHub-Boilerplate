#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com
#
#echo "Shell 传递参数实例！";
#echo "执行的文件名：$0";
#echo "第一个参数为：$1";
#echo "第二个参数为：$2";
#echo "第三个参数为：$3";

default=$(date +"%Y%m%d")
time=$(date +"%Y-%m-%d %H:%M")
month=$(date +"%m")
day=$(date +"%d")
year=$(date +"%Y")
case $month in
	"1") m= "Jan"
	;;
	"2") m= "Feb"
	;;
	"3") m= "Mar"
	;;
	"4") m= "Apr"
	;;
	"5") m= "May"
	;;
	"6") m= "Jun"
	;;
	"7") m= "Jul"
	;;
	"8") m= "Aug"
	;;
	"9") m= "Sept"
	;;
	"10") m= "Oct"
	;;
	"11") m= "Nov"
	;;
	"12") m= "Dec"
	;;
esac

title="$m $day $year"

if [ $1 == "" ]
then
	echo "no given value, use default:$defult"
	touch ${1}.md
	echo "---
layout: post
title: $title
slug: $1
date: $time
status: publish
author: starmoe
categories:
  - diary
tags:
  - nothing
---
<!--generted by linux shell-->" > ${1}.md

elif [ $1 == "help" ]
then
	echo "too lazy to write help info ... later to do it."
else
	touch ${1}.md
	echo "---
layout: post
title: $title
slug: $1
date: $time
status: publish
author: starmoe
categories:
  - diary
tags:
  - nothing
---
<!--generted by linux shell-->" > ${1}.md
fi
