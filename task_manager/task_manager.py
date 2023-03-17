import datetime
import os
import tkinter as tk

# プロジェクトファイルのパスをリストに格納
project_files = ['project1.py', 'project2.py', 'project3.py', 'project4.py', 'project5.py']

# 今日の日付を取得
today = datetime.datetime.today().strftime('%Y-%m-%d')

# 今日のタスクを格納するリスト
tasks = []

# 各プロジェクトファイルから今日のタスクを取得
for file in project_files:
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if today in line:
                tasks.append(line.strip())

# tkinterウィンドウの作成
root = tk.Tk()
root.title("今日のタスク")

# タスクリストを表示するラベルの作成
task_label = tk.Label(root, text="\n".join(tasks), font=("Helvetica", 12))
task_label.pack()


# クリックされたら、同じプロジェクトの次のタスクを表示する関数
def next_task(event):
    # クリックされたタスクのテキストを取得
    task_text = event.widget.cget("text")
    # クリックされたタスクのプロジェクトファイルを取得
    task_file = [file for file in project_files if file.startswith(task_text.split(":")[0])][0]
    # クリックされたタスクのインデックスを取得
    task_index = [i for i, line in enumerate(open(task_file, 'r')) if line.strip() == task_text][0]
    # 次のタスクを取得
    next_task_index = task_index + 1
    with open(task_file, 'r') as f:
        next_task_lines = f.readlines()[next_task_index:]
        next_task = [line.strip() for line in next_task_lines if today in line][0]
    # クリックされたタスクを更新
    event.widget.config(text=next_task)


# タスクラベルにクリックイベントを追加
for task in task_label.winfo_children():
    task.bind("<Button-1>", next_task)

root.mainloop()
