import os  
os.system("whoami")  

try:
    d=int(input("你要加几个签"))
    for i in range(d):
        e=input("你这个签要加什么")
        a=open("新建文本文档.txt","a")
        a.write(","+e)
        a.close()
except:
    print("错误")
    
