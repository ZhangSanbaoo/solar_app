import tkinter as tk
from time import strftime
import random
from tkinter import font as tkFont
import pyglet
pyglet.font.add_file("CascadiaCodePLItalic.ttf")
pyglet.font.load("CascadiaCodePLItalic.ttf")
# 创建主窗口
# root = tk.Tk()
# root.title("App test")

# # 创建标签用于显示时间
# phi_label = tk.Label(root, font=("CASCADIA CODE PL", 1), text="")
# phi_label.pack(padx=400, pady=225) #软件界面的长宽

# # 更新时间的函数
# def update_test():
#     # phi = random.randint(1,10)
#     phi_label.config(text="phi",font=("CASCADIA CODE PL", 1))  # 更新标签文本
#     phi_label.after(1000, update_test)  # 每秒更新一次时间

# # 初始化并启动时间更新
# update_test()

# # 运行主循环
# root.mainloop()

root = tk.Tk()
available_fonts = tkFont.families()
print(available_fonts)
root.destroy()