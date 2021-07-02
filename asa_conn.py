#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng


import re
#
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
asa_dict = {}
re_result = re.match('\w{3}\s+\w{7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{5})\s+\w{7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{5}).*bytes\s+(\d+).*flags\s+(\w{3})\\n\s+\w{3}\s+\w{7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})\s+\w{7}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{5}).*bytes\s+(\d+).*flags\s+(\w*)\s*',asa_conn).groups()
key1 = re_result[0],re_result[1],re_result[2],re_result[3]
val1 = re_result[4],re_result[5]
asa_dict[key1]=val1
key2 = re_result[6],re_result[7],re_result[8],re_result[9]
val2 = re_result[11],re_result[10]
asa_dict[key1]=val1
asa_dict[key2]=val2
print('\n\n打印字典\n')
print(asa_dict)
print('\n\n格式化打印输出\n')
src='src'
src_ip='src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes_name'
flags = 'flags'
format_str1 =('%5s : %-20s |%10s : %-10s |%10s : %-10s |%10s : %-10s|' % ('src',key1[0],'src_p',key1[1],'dst',key1[2],'dst_p',key1[3]))
format_str2 =('%7s : %-20s |%10s : %-10s' % ('bytes',val1[0],'flags',val1[1]))
format_str3 =('%5s : %-20s |%10s : %-10s |%10s : %-10s |%10s : %-10s|' % ('src',key2[0],'src_p',key2[1],'dst',key2[2],'dst_p',key2[3]))
format_str4 =('%7s : %-20s |%10s : %-10s' % ('bytes',val2[0],'flags',val2[1]))
print(format_str1)
print(format_str2)
print('='*110)
print(format_str1)
print(format_str2)
print('='*110)
