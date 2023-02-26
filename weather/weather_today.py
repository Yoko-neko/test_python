import tkinter as tk
import requests

# tkinterは、主要なOSにも対応しているクロスプラットフォームなGUIライブラリ。
# Tkinterは、Tcl/Tk（古いけどとてもシンプルな言語）をベースにしている。
# Pythonで扱うためGUIライブラリで,
# Tk()関数を使用することで、メインウィンドウを作成することができる

# お天気APIを取得するためにimport requestsしたけど、要らないかも？
# requests普通に出るし、エラーの波線出てこない
# requests

# MainWindowの作成↓
canvas = tk.Tk()
canvas.geometry("700×500")
canvas.title("Today's weather")
a = ("Arial black", 20, "bold")
b = ("Arial black", 40, "bold")

# お天気情報を得るためのget_weather関数
def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q"+city+"&appid=ea16dc0452cab191865217b7b21c699d"

    json_data = requests.get(api).json()
    weather = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_min'] - 273.15)

    # アプリに表示する項目
    final_info = weather + "\n" + str(temp) + "°C"
    final_data = "\n"+ "最低気温: " + str(min_temp) + "°C" + "\n" + "最高気温: " + str(max_temp) + "°C"
    label1.config(text = final_info)
    label2.config(text = final_info)

# テキストボックス作成
textField = tk.Entry(canvas, justify='center', width = 20, font = b)
textField.pack(pady = 30)
# padyは外側の縦の隙間
textField.bind('<Return>', getWeather)
# APIの天気情報を表示する↑

label1 = tk.Label(canvas, font=b)
label1.pack()
label2 = tk.Label(canvas, font=a)
label2.pack()