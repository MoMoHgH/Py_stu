#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
import sys
workbook = xlsxwriter.Workbook('text.xlsx')
worksheet = workbook.add_worksheet()
chart = workbook.add_chart({'type':'column'})
#数据表头名称
title = [u'业务名称',u'星期一',u'星期二',u'星期三',u'星期四',
        u'星期五',u'星期六',u'星期日',u'平均流量']
#业务名称
busname = [u'业务官网',u'新闻中心',u'购物频道',u'体育频道',u'法律频道']
#各频道流量列表
data = [
        [156,123,170,154,160,182,190],
        [81,79,75,82,89,98,95],
        [210,224,230,223,254,260,265],
        [126,123,142,156,192,198,183],
        [120,126,133,120,155,169,170],
        ]
Format = workbook.add_format()
Format.set_border()                     #单元格边框加粗(1)像素

format_title = workbook.add_format()
format_title.set_border()
format_title.set_bg_color('#cccccc')    #设置单元格背景颜色
format_title.set_align('center')        #设置文字居中
format_title.set_bold()

format_ave = workbook.add_format()
format_ave.set_border()
format_ave.set_num_format('0.00')       #设置单元格数字显示格式



#将数据写入单元格，并引用不同格式对象
worksheet.write_row('A1',title,format_title)
worksheet.write_column('A2',busname,Format)
worksheet.write_row('B2',data[0],Format)
worksheet.write_row('B3',data[1],Format)
worksheet.write_row('B4',data[2],Format)
worksheet.write_row('B5',data[3],Format)
worksheet.write_row('B6',data[4],Format)

#定义数据图表函数
def chart_serise(cur_row):
    worksheet.write_formula('I'+cur_row, \
            '=AVERAGE(B'+cur_row+':H'+cur_row+')',format_ave)
    chart.add_series({
            'categories':'=Sheet1!$B$1:$H$1',                 #将周一到周五作为数据标签（X轴）
            'values':    '=Sheet1!$B$'+cur_row+':$H$'+cur_row, #频道一周数据作为数据区域
            'line':      {'color': 'black'},                  #线条颜色
            'name':      '=Sheet1!$A$'+cur_row,               #将频道名称作为图例项
        })

for row in range(2,7):
    chart_serise(str(row))
chart.set_table() #设置X轴表格格式
#chart.set_style(30) #设置图表样式
chart.set_size({'width':577,'height':287})     #设置图表大小
chart.set_title({'name': u'业务流量周报图表'})
chart.set_y_axis({'name': 'Mb/s'})             #设置Y轴小标题
worksheet.insert_chart('A8',chart)             #插入图表
workbook.close()
