# -*- coding: utf-8 -*-

WIN = 'Windows'
MAC = 'Darwin'
import os
from platform_specific import play, p, tk
p('Loading 加载中... ', end = '\r', flush = True)
from lesstk import screenCenter, msgbox
import sys
import pickle
from time import time
from random import randint
import platform
from socket import socket
# import complete

def main():
    global group
    group = randint(0,2)
    checkInternet()
    loadSounds()
    p('App is running 程序正在运行... ', flush = True)
    greet()
    Exp()
    result = Ask().result
    Upload(result)
    thank()
    p('Exiting 正在退出... ')

def checkInternet():
    s = socket()
    s.settimeout(5)
    try:
        s.connect(('www.surveymonkey.com', 80))
        s.close()
    except:
        msgbox('', '''Error: Internet connection failed. 
Click OK to quit the app. 

错误：无法连接到服务器。
点击OK来退出程序。''')
        sys.exit(1)

def loadSounds():
    with open('sounds.bytes', 'rb') as f:
        data = pickle.load(f)
    with open('temp', 'wb') as f:
        f.write(data)    

def greet():
    global group
    msgbox('','''Welcome to the Sound Perception Experiment. 

欢迎来到声波感知实验。''')
    msgbox('Important 重要',
    '''Please do NOT give your friends any spoilers about this experiment. 

请不要向你的朋友剧透这个实验。''')
    msgbox('Important 重要',
    '''You should only do this experiment ONCE. 
Do not submit multiple results. 

这个实验一人只做一次。
请勿重复上传实验结果。''')
    msgbox('','''Also, your participation here is anonymous. 

另外，您在本次实验中是匿名的。''')
    if group == 0:
        msgbox('','''In this experiment, you will hear two sounds. 
They are similar, but they are two different sounds. 
Compare them, and tell me if you perceive any difference. 

在这个实验中，你会听到两段声音。
它们很相似，但有差别。
比较它们，然后告诉我，你有没有察觉到不同。''')
    elif group == 1:
        msgbox('','''In this experiment, you will hear two sounds. 
They are similar, but they are two different sounds. 
They have different initial phases. 
Compare them, and tell me if you perceive any difference. 

在这个实验中，你会听到两段声音。
它们很相似，但有差别。
它们的初始相位不同。
比较它们，然后告诉我，你有没有察觉到不同。''')
    elif group == 2:
        msgbox('','''In this experiment, you will hear two sounds. 
They are similar, but they are two different sounds. 
Compare them, and tell me if you perceive any difference. 

在这个实验中，你会听到两段声音。
它们很相似，但有差别。
比较它们，然后告诉我，你有没有察觉到不同。''')
        msgbox('','''Both of the sounds are a harmony of C and E, 
but they have different initial phases. 
In sound A, crests of C align with crests of E. 
In sound B, crests of C align with troughs of E. 

两段声音都是C(哆)和E(咪)组成的和弦，
但是它们初始相位不同。
声音A中，C的波峰与E的波峰对齐。
声音B中，C的波峰与E的波谷对齐。''')
    else:
        assert False, 'Invalid group ID. '
    msgbox('','''You may only play each sound 3 times, 
but you may listen to them in whatever order you like. 

每段声音你只能播放3次，
但你可以以任何顺序播放。''')

class Exp:
    def __init__(self):
        pad = 20
        root = tk.Tk()
        root.title('Sound Perception Experiment 声波感知实验')
        buttonA = tk.Button(root, text = 'Play Sound A\n播放声音A', command = self.playA, 
                            padx = pad, pady = pad, font = 'Verdana 20')
        buttonB = tk.Button(root, text = 'Play Sound B\n播放声音B', command = self.playB, 
                            padx = pad, pady = pad, font = 'Verdana 20')
        strVarA = tk.StringVar()
        strVarA.int = 3
        entryA = tk.Entry(root, justify = tk.CENTER, state = tk.DISABLED, 
                          textvariable = strVarA, font = 'Verdana 18')
        strVarA.set('Remaining: 3 plays')
        strVarB = tk.StringVar()
        strVarB.int = 3
        entryB = tk.Entry(root, justify = tk.CENTER, state = tk.DISABLED, 
                          textvariable = strVarB, font = 'Verdana 18')
        strVarB.set('Remaining: 3 plays')
        buttonHelp = tk.Button(root, text = 'Help\n帮助', command = greet, 
                            padx = 2*pad, font = 'Verdana 15')
        self.strVarA = strVarA
        self.strVarB = strVarB
        self.root = root
        buttonA.grid(row=0,column=0, pady = pad)
        buttonB.grid(row=0,column=1, pady = pad)
        entryA.grid(row=1,column=0, padx = pad)
        entryB.grid(row=1,column=1, padx = pad)
        buttonHelp.grid(row=2,column=0,columnspan=2, pady = pad)
        buttonA.focus_force()
        screenCenter(root)
        root.mainloop()
        del root, self.root
    
    def playA(self):
        self.play(self.strVarA)
    
    def playB(self):
        self.play(self.strVarB)
    
    def play(self, strVar):
        strVarA = self.strVarA
        strVarB = self.strVarB
        root = self.root
        if strVar.int > 0:
            strVar.int -= 1
            strVar.set('Playing...')
            root.update_idletasks()
            play()
            strVar.set('Remaining: %d plays ' % strVar.int)
            root.update_idletasks()
        if strVarA.int == 0 and strVarB.int == 0:
            root.quit()
            root.destroy()

class Ask:
    def __init__(self):
        self.result = 2
        pad = 20
        choice = tk.Tk()
        choice.title('Result 实验结果')
        buttonYes = tk.Button(choice, text = '''They sound different. 
听起来不一样''', 
                              font = 'Times 20', command = self.yes)
        buttonNo = tk.Button(choice, text = '''They sound the same. 
听起来没差别''', 
                              font = 'Times 20', command = self.no)
        buttonYes.pack(padx = pad, pady = pad)
        buttonNo.pack(padx = pad, pady = (0, pad))
        
        screenCenter(choice)
        choice.focus_force()
        self.choice = choice
        choice.mainloop()
        del choice, self.choice
    
    def yes(self):
        self.result = 1
        self.terminate()
    
    def no(self):
        self.result = 0
        self.terminate()
    
    def terminate(self):
        self.choice.quit()
        self.choice.destroy()

class Upload():
    def __init__(self, result):
        global group
        timestamp = format(time(), '.2f')
        self.string = '%s.%d.%d' % (timestamp, group, result)
        pad = 20
        root = tk.Tk()
        root.title('Upload the result 上传结果')
        
        label_1 = tk.Label(root, font = 'Verdana 20', 
                         text = 'Your result: \n实验结果：')
        label_1.pack(padx = pad, pady = (pad, 0))
        
        strVarResult = tk.StringVar()
        self.strVarResult = strVarResult
        strVarResult.trace('w', self.setResult)
        entryResult = tk.Entry(root, font = 'Verdana 12', 
                               textvariable = strVarResult)
        self.setResult(0, 0, strVarResult)
        entryResult.pack(padx = pad)
        
        label_2 = tk.Label(root, font = 'Verdana 20', 
                         text = '''Please send your result to this webpage: 
请把实验结果填写到这个网页：''')
        label_2.pack(padx = pad, pady = (pad, 0))
        
        self.Monkey = 'https://www.surveymonkey.com/r/J9NZ69N'
        
        strVarMonkey = tk.StringVar()
        self.strVarMonkey = strVarMonkey
        strVarMonkey.trace('w', self.setMonkey)
        self.setMonkey(0, 0, strVarMonkey)
        entryMonkey = tk.Entry(root, font = 'Verdana 12', width = len(self.Monkey), 
                              textvariable = strVarMonkey)
        entryMonkey.pack(padx = pad)
        
        buttonOpen = tk.Button(root, text = '''Open webpage in Browser
用浏览器打开网页''', 
                           command = self.openBrowser, font = 'Verdana 15')
        buttonOpen.pack(padx = pad, pady = pad)
        
        buttonOk = tk.Button(root, text = "Done it. \n完成了。", 
                           command = self.terminate, font = 'Verdana 12')
        buttonOk.pack(padx = pad, pady = (0, pad))
        
        self.root = root
        screenCenter(root)
        buttonOpen.focus_force()
        root.mainloop()
        del root, self.root
    
    def setResult(self, _, __, ___):
        strVarResult = self.strVarResult
        string = self.string
        if strVarResult.get != string:
            strVarResult.set(string)
    
    def setMonkey(self, _, __, ___):
        Monkey = self.Monkey
        strVarMonkey = self.strVarMonkey
        if strVarMonkey.get != Monkey:
            strVarMonkey.set(Monkey)
    
    def openBrowser(self):
        if platform.system() == WIN:
            os.startfile(self.Monkey)
        elif platform.system() == MAC:
            import subprocess
            subprocess.Popen(['open', self.Monkey])
        else:
            try:
                import subprocess
                subprocess.Popen(['xdg-open', self.Monkey])
            except OSError:
                msgbox('', 'Failed to open browser. 无法打开浏览器。')
    
    def terminate(self):
        root = self.root
        root.quit()
        root.destroy()

def thank():
    msgbox('','''Thank you for participating! 
I will appreciate it if you forward this app to another person. 
Click OK to quit the app. 

感谢您的参与！
诚希望您把这个程序转发给一个朋友。
单击OK来退出程序。''')

if __name__ == '__main__':
    main()
