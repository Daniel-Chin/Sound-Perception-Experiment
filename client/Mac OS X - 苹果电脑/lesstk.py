from platform_specific import tk
from os import system
import platform
MAC = 'Darwin'

def screenCenter(root):
    root.update_idletasks()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    size = tuple(int(_) for _ in root.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    root.geometry("%dx%d+%d+%d" % (size + (x, y)))

class Msgbox():
    def __init__(self, title = '', msg = ''):
        root = tk.Tk()
        root.title(title)
        
        label = tk.Label(root, text=msg, font='Verdana 20') 
        label.pack(padx = 20, pady = 10)
        
        button = tk.Button(root, text='OK', command=self.terminate, 
                           font = 'Verdana 12', padx = 10, pady = 5)
        button.bind('<Return>', self.terminate)
        button.pack(pady = (0, 10))
        
        screenCenter(root)
        self.root = root
        if platform.system() == MAC:
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        button.focus_force()
        root.mainloop()
    
    def terminate(self, event = None):
        root = self.root
        root.quit()
        root.destroy()

def msgbox(title = '', msg = ''):
    Msgbox(title, msg)

if __name__ == '__main__':
    msgbox('Title', 'Test Message. ')
