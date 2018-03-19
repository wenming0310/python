#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""主函数文件"""

import tkinter as tk
import tkinter.ttk as ttk
import buildgui
import serialctl
import configurationfile

if __name__=="__main__":
    root = tk.Tk()  #构建主窗体
    root.title(configurationfile.main_title)     # 标题
    root.geometry(configurationfile.main_window_size)        # 默认窗体大小
    # Tab Control introduced here --------------------------------------
    tabControl = ttk.Notebook(root)  # Create Tab Control
    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text=configurationfile.tool_tip_name_1)  # Add the tab
    tab2 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text=configurationfile.tool_tip_name_2)  # Make second tab visible
    tab3 = ttk.Frame(tabControl)  # Add a third tab
    tabControl.add(tab3, text=configurationfile.tool_tip_name_3)  # Make second tab visible
    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    app1 = buildgui.ApplicationGuiBuild(tab1) #主应用窗体构建在第一页

    root.mainloop()