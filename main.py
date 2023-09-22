import tkinter as tk
from tkinter import ttk
from pymodbus.client.sync import ModbusTcpClient
import threading
import time

def read_modbus_data():
    # 从界面获取用户选择的地区
    selected_area = area_combobox.get()
    
    # 从配置文件中获取选定地区的Modbus参数
    modbus_parameters = config[selected_area]
    
    # 连接到Modbus服务器
    client = ModbusTcpClient(modbus_parameters['ip'], modbus_parameters['port'])
    
    # 读取Modbus寄存器数据
    response = client.read_holding_registers(modbus_parameters['register_address'],
                                             modbus_parameters['register_count'])
    
    if response.isError():
        result_label.config(text="Modbus读取错误")
    else:
        data = response.registers
        temperature_label.config(text=f"Temperature: {data[0]}")
        flux_label.config(text=f"Flux solaire: {data[1]}")
        puissance_injectee_label.config(text=f"Puissance injectée: {data[2]}")
        puissance_attendu_label.config(text=f"Puissance attendue: {data[3]}")
        alarmes_active_label.config(text=f"Code alarmes active: {data[4]}")
    
    # 断开与Modbus服务器的连接
    client.close()

def update_data_periodically():
    while True:
        read_modbus_data()
        # 定时器间隔（秒）
        time.sleep(10)  # 10秒钟更新一次数据

# 创建Tkinter窗口
root = tk.Tk()
root.title("Modbus数据读取")

# 创建下拉栏以选择地区
area_label = tk.Label(root, text="选择地区:")
area_label.pack()
area_combobox = ttk.Combobox(root, values=["地区1", "地区2", "地区3"])  # 你可以根据你的配置文件来添加更多地区
area_combobox.pack()

# 创建按钮来触发Modbus数据读取
read_button = tk.Button(root, text="读取数据", command=read_modbus_data)
read_button.pack()

# 创建用于显示Modbus数据的标签
temperature_label = tk.Label(root, text="Temperature:")
temperature_label.pack()
flux_label = tk.Label(root, text="Flux solaire:")
flux_label.pack()
puissance_injectee_label = tk.Label(root, text="Puissance injectée:")
puissance_injectee_label.pack()
puissance_attendu_label = tk.Label(root, text="Puissance attendue:")
puissance_attendu_label.pack()
alarmes_active_label = tk.Label(root, text="Code alarmes active:")
alarmes_active_label.pack()

# 从配置文件中加载地区参数
config = {
    "地区1": {
        "ip": "Modbus服务器IP1",
        "port": 502,
        "register_address": 0,
        "register_count": 5
    },
    "地区2": {
        "ip": "Modbus服务器IP2",
        "port": 502,
        "register_address": 10,
        "register_count": 5
    },
    # 添加更多地区的配置参数
}

# 创建一个定时器线程来定期更新数据
update_thread = threading.Thread(target=update_data_periodically)
update_thread.daemon = True
update_thread.start()

root.mainloop()
