print(bin(10))#转二进制
print(hex(23))#转十六进制
tup=(1,2,3,4)
li=list(tup)
print(type(li))
tupList=tuple(li)
print(type(tupList))
dic1=dict()
print(type(dic1))
dic1['name']='sss'
dic1['age']='20'
print(dic1)
dic2=dict(name='jjj',pro='computer')
print(dic2)
print(bytes('我喜欢python',encoding='utf-8'))