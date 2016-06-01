
"""
urllib2 functions
"""
import urllib2 
"""
urlopen(url,data,timeout)
第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。

第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT

第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面
"""
response = urllib2.urlopen("http://www.baidu.com")#this is the object, in order to show the contends, call the read function
print response.read()

"""
推荐使用request对象，这样在构建对象是
"""




######################################################


import urllib


