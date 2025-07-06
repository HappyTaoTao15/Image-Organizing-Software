import os
import datetime
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


def organize_files_by_date(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # 获取文件的修改时间
            modified_time = os.path.getmtime(os.path.join(directory, filename))
            # 将修改时间转换为datetime对象
            date_obj = datetime.datetime.fromtimestamp(modified_time)
            # 提取datetime对象的年份和月份
            year_month = date_obj.strftime('%Y-%m')
            # 构造新的文件夹路径
            new_folder = os.path.join(directory, year_month)
            # 如果新文件夹不存在，则创建它
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            # 将文件移动到新文件夹中
            shutil.move(os.path.join(directory, filename), os.path.join(new_folder, filename))


def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files_by_date(directory)
        messagebox.showinfo("成功", "图片整理完成！")


def main():
    # 创建主窗口
    root = tk.Tk()
    root.geometry("300x200")
    root.title("图片整理工具3.0")

    label = tk.Label(root, text="图片整理工具-快乐的涛涛")
    label.pack()

    # 创建一个按钮
    button = tk.Button(root, text="选择文件夹", command=browse_directory)
    button.pack(pady=20)

    label = tk.Label(root, text="使用教程:  1,点击[选择文件夹后]")
    label.pack()

    label = tk.Label(root, text="2,该文件夹下的图片便会自动整理")
    label.pack()

    label = tk.Label(root, text="3,整理后文件夹的格式为年份+月份，如2024-02")
    label.pack()

    label = tk.Label(root, text="4,当有弹窗显示（图片整理完成）时便完成图片整理")
    label.pack()

    # 运行主循环
    root.mainloop()


if __name__ == "__main__":
    main()