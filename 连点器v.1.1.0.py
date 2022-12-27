import pynput.mouse as mouse
from time import *
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from random import *
import webbrowser as web

fangxiang = 'left'


def connectator():
    global fangxiang
    m = mouse.Controller()
    connectator_window = Tk()
    connectator_window.title('连点鸡~~~')
    connectator_window.geometry('600x400')

    def dianji():
        global fangxiang
        try:
            entry_get = entry.get()
            entry_get_1 = entry_1.get()
            entry_get_2 = entry_2.get()
            if entry_get == '':
                entry_get = 1
            else:
                entry_get = int(entry_get)
            if entry_get_1 == '':
                entry_get_1 = 0
            else:
                entry_get_1 = float(entry_get_1)
            if entry_get_2 == '':
                entry_get_2 = 1
            else:
                entry_get_2 = int(entry_get_2)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否点击（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        sleep(1)
                    if fangxiang == 'left':
                        for b in range(entry_get):
                            m.click(mouse.Button.left, entry_get_2)
                            sleep(entry_get_1)
                    elif fangxiang == 'right':
                        for c in range(entry_get):
                            m.click(mouse.Button.right, entry_get_2)
                            sleep(entry_get_1)
                    elif fangxiang == 'middle':
                        for d in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.right, entry_get_2)
                            sleep(entry_get_1)
            if entry_get <= 1000:
                if entry_get_2 <= 30:
                    if entry_get >= 50:
                        question = askquestion('确定？', '%s' % '确定要点击大于50遍吗？')
                        if question == 'yes':
                            if entry_get_1 <= 1:
                                question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                                if question == 'yes':
                                    if entry_get_2 >= 10:
                                        question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                        if question == 'yes': ok()
                                    else:
                                        ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            if entry_get_2 >= 10:
                                question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                if question == 'yes':
                                    ok()
                                else:
                                    ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            ok()
                    else:
                        ok()
                else:
                    showerror('错误', '%s' % '请勿每次点击大于30次或者请勿刷大于1000遍')
                    entry.delete(0, END)
                    entry_1.delete(0, END)
                    entry_2.delete(0, END)
            else:
                showerror('错误', '%s' % '请勿刷大于1000遍或者每次点击大于30次')
                entry.delete(0, END)
                entry_1.delete(0, END)
                entry_2.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)
            entry_1.delete(0, END)

    def suiji():
        global fangxiang
        try:
            entry_get = entry.get()
            entry_get_1 = entry_1.get()
            entry_get_2 = entry_2.get()
            if entry_get == '':
                entry_get = 1
            else:
                entry_get = int(entry_get)
            if entry_get_1 == '':
                entry_get_1 = 0
            else:
                entry_get_1 = float(entry_get_1)
            if entry_get_2 == '':
                entry_get_2 = 1
            else:
                entry_get_2 = int(entry_get_2)

            def ok():
                question = askretrycancel('确定？', '%s' % '最后一遍，是否点击（可能造成卡顿）')
                if question:
                    j = 5
                    showinfo('准备', '%s' % '开始计时5秒钟')
                    for a in range(5):  # 倒计时
                        print('倒计时:' + str(j))
                        j = j - 1
                        sleep(1)
                    if fangxiang == 'left':
                        for b in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.left, entry_get_2)
                            sleep(entry_get_1)
                    elif fangxiang == 'right':
                        for c in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.right, entry_get_2)
                            sleep(entry_get_1)
                    elif fangxiang == 'middle':
                        for d in range(entry_get):
                            m.position = (randint(-1, 3000), randint(-1, 2000))
                            m.click(mouse.Button.right, entry_get_2)
                            sleep(entry_get_1)
            if entry_get <= 1000:
                if entry_get_2 <= 30:
                    if entry_get >= 50:
                        question = askquestion('确定？', '%s' % '确定要点击大于50遍吗？')
                        if question == 'yes':
                            if entry_get_1 <= 1:
                                question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                                if question == 'yes':
                                    if entry_get_2 >= 10:
                                        question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                        if question == 'yes': ok()
                                    else:
                                        ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            if entry_get_2 >= 10:
                                question = askquestion('确定？', '%s' % '确定要每次点击大于10次吗？')
                                if question == 'yes':
                                    ok()
                                else:
                                    ok()
                            else:
                                ok()
                    elif entry_get_1 <= 1:
                        question = askquestion('确定？', '%s' % '确定要点击间隔小于1秒吗？')
                        if question == 'yes':
                            ok()
                    else:
                        ok()
                else:
                    showerror('错误', '%s' % '请勿每次点击大于30次或者请勿刷大于1000遍')
                    entry.delete(0, END)
                    entry_1.delete(0, END)
                    entry_2.delete(0, END)
            else:
                showerror('错误', '%s' % '请勿刷大于1000遍或者每次点击大于30次')
                entry.delete(0, END)
                entry_1.delete(0, END)
                entry_2.delete(0, END)
        except Exception as x:
            showerror('错误', '%s' % x)
            entry.delete(0, END)
            entry_1.delete(0, END)

    def left():
        global fangxiang
        fangxiang = 'left'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fangxiang))

    def right():
        global fangxiang
        fangxiang = 'right'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fangxiang))

    def middle():
        global fangxiang
        fangxiang = 'middle'
        showinfo('成功', '%s' % '设置成功，键为{}'.format(fangxiang))

    def github():
        web.open('https://github.com/jingcygz/Connectator')

    label = Label(connectator_window, text="制作：小井井")
    label.pack()

    label_1 = Label(connectator_window, text="点击次数")
    label_1.place(relx=0.3, rely=0.3)

    label_2 = Label(connectator_window, text="间隔")
    label_2.place(relx=0.3, rely=0.4)

    label_3 = Label(connectator_window, text="每次点击点击次数")
    label_3.place(relx=0.3, rely=0.5)

    entry = Entry(connectator_window)
    entry.place(relx=0.5, rely=0.3)

    entry_1 = Entry(connectator_window)
    entry_1.place(relx=0.5, rely=0.4)

    entry_2 = Entry(connectator_window)
    entry_2.place(relx=0.5, rely=0.5)

    button = Button(connectator_window, text="左键", command=left)
    button.place(relx=0.3, rely=0.6)

    button_1 = Button(connectator_window, text="中键", command=middle)
    button_1.place(relx=0.5, rely=0.6)

    button_1 = Button(connectator_window, text="右键", command=right)
    button_1.place(relx=0.7, rely=0.6)

    button_2 = Button(connectator_window, text="开始", command=dianji)
    button_2.place(relx=0.5, rely=0.7)

    button_3 = Button(connectator_window, text="随机地点连点", command=suiji)
    button_3.place(relx=0.5, rely=0.8)

    button_3 = Button(connectator_window, text="小破站", command=github)
    button_3.place(relx=0.5, rely=0.9)

    connectator_window.mainloop()


if __name__ == '__main__':
    connectator()
