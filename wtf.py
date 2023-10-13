
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_list_box_lnnaujmx = self.__tk_list_box_lnnaujmx(self)
        self.tk_button_lnnav42r = self.__tk_button_lnnav42r(self)
        self.tk_button_lnnawbqu = self.__tk_button_lnnawbqu(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 829
        height = 441
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)
    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
    
    def vbar(self,ele, x, y, w, h, parent):
        sw = 15 # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar,ele)
    def __tk_list_box_lnnaujmx(self,parent):
        lb = Listbox(parent)
        
        lb.insert(END, "列表框")
        
        lb.insert(END, "Python")
        
        lb.insert(END, "Tkinter Helper")
        
        lb.place(x=60, y=60, width=158, height=277)
        return lb
    def __tk_button_lnnav42r(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=250, y=140, width=57, height=103)
        return btn
    def __tk_button_lnnawbqu(self,parent):
        btn = Button(parent, text="Add", takefocus=False,)
        btn.place(x=90, y=360, width=83, height=38)
        return btn
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
    def LoadInfo(self,evt):
        print("<Button>事件未处理:",evt)
    def AddPlace(self,evt):
        print("<Button>事件未处理:",evt)
    def __event_bind(self):
        self.tk_button_lnnav42r.bind('<Button>',self.LoadInfo)
        self.tk_button_lnnawbqu.bind('<Button>',self.AddPlace)
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()