# MAC
import os
os.chdir(os.path.dirname(__file__))

import subprocess
def play():
    subprocess.call(['afplay', 'temp'])

import Tkinter as tk
class Button(tk.Label):
    def __init__(self, master, **kw):
        command = kw.pop('command')
        if 'takefocus' not in kw:
            kw['takefocus'] = True
        if 'relief' not in kw:
            kw['relief'] = 'raised'
        tk.Label.__init__(self, master, **kw)
        self.command = command
        self.bind('<ButtonRelease-1>', self.mouseUp)
        self.bind('<space>', command)
        self.bind('<Enter>', self.highlight)
        self.bind('<FocusIn>', self.highlight)
        self.bind('<Leave>', self.lowlight)
        self.bind('<FocusOut>', self.lowlight)
        self.bind('<Button-1>', self.sink)
        self.saved_color = self.cget('background') 
        self.cursor_in = False
    
    def highlight(self, event):
        self.config(background = 'SystemHighlight')
        self.cursor_in = True
    
    def lowlight(self, event):
        self.config(background = self.saved_color)
        self.config(relief = 'raised')
        self.cursor_in = False
    
    def mouseUp(self, event):
        if self.cursor_in:
            self.command()
        else:
            self.config(relief = 'raised')
    
    def sink(self, event):
        self.config(relief = 'sunken')
    
tk.Button = Button

from sys import stdout
def p(sep = ' ', end = '\n', flush = True, *args):
    stdout.write(sep.join(args) + end)
    if flush:
        stdout.flush()
