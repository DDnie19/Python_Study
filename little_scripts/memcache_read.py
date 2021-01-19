#!/usr/bin/env python3
#coding:utf8
import memcache
#链接
mc = memcache.Client(['139.129.5.191:12000'], debug=True)
#插入
mc.set("name", "python")
#读取
ret = mc.get('name')
print (ret)

# 输出结果

# debug=True表示运行出现错误时，可以显示错误信息，正式环境可以不加
