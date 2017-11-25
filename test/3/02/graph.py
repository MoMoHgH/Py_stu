#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rrdtool
import time
# 定义图表上方标题
title="网卡流量监控图 ("+time.strftime('%Y-%m-%d',time.localtime(time.time()))+")"
#绘制图表
# "MINUTE:12" 每12分钟放置一条次要格线
# "HOUR:1" 每一个小时放置一条主要格线
# "HOUR:1" 控制每一个小时输出一个label标签
# "0:%H" 0表示数字一格线对齐，%H表示标签通过小时显示 
rrdtool.graph( "Flow.png", "--start", "-1d","--vertical-label=Bytes/s","--x-grid","MINUTE:12:HOUR:1:HOUR:1:0:%H",\
 "--width","650","--height","230","--title",title,                  #图表大小和标题
 "DEF:inoctets=Flow.rrd:wlp2s0_in:AVERAGE",                         #网卡入流量源 DN 及 CF(MAX,MIN.AVERAGE,LAST)
 "DEF:outoctets=Flow.rrd:wlp2s0_out:AVERAGE",                       #
 "CDEF:total=inoctets,outoctets,+",                                 #总流量




 "LINE1:total#FF8833:Total traffic",                                #以线条绘制总流量
 "AREA:inoctets#00FF00:In traffic",                                 #以面积绘制入流量
 "LINE1:outoctets#0000FF:Out traffic",                              #以线条绘制出流量
 "HRULE:61440#FF0000:Alarm value\\r",                               #以水平线绘制警告线 警告值61440 约60
 "CDEF:inbits=inoctets,8,*",                                        #出入*8 换算成bit
 "CDEF:outbits=outoctets,8,*",
 "COMMENT:\\r",                                                     #输出换行
 "COMMENT:\\r",
 "GPRINT:inbits:AVERAGE:Avg In traffic\: %6.2lf %Sbps",             #图表下方输出MAX MIN AVG 
 "COMMENT:   ",                                                     #%6.12lf 宽度6 小数点后两位
 "GPRINT:inbits:MAX:Max In traffic\: %6.2lf %Sbps",                 #
 "COMMENT:  ",
 "GPRINT:inbits:MIN:MIN In traffic\: %6.2lf %Sbps\\r",
 "COMMENT: ",
 "GPRINT:outbits:AVERAGE:Avg Out traffic\: %6.2lf %Sbps",
 "COMMENT: ",
 "GPRINT:outbits:MAX:Max Out traffic\: %6.2lf %Sbps",
 "COMMENT: ",
 "GPRINT:outbits:MIN:MIN Out traffic\: %6.2lf %Sbps\\r")

