# # 利用configure（）方法或config（）方法来实现文本变化
#
# import tkinter
# import time
#
#
# def gettime():
#     timestr=time.strftime('%H:%M:%S')
#     print(timestr)
#     lb.configure(text= timestr)
#     root.after(1000,gettime)
#
# root = tkinter.Tk()
# root.title('时钟')
#
# lb = tkinter.Label(root,text='',fg='blue',font=("黑体",80))
# lb.pack()
# gettime()
# root.mainloop()






#利用textvariable变量来实现文本变化

import tkinter
import time

def gettime():
    #获取当前时间（时分秒必须大写H，M，S）
    var.set(time.strftime("%H:%M:%S"))
    #每隔1s调用函数gettime自身获取时间
    root.after(1000,gettime)

root  = tkinter.Tk()
root.title('时钟')
var = tkinter.StringVar()

lb = tkinter.Label(root,textvariable=var,fg='blue',font=('黑体',80))
lb.pack()
gettime()
root.mainloop()