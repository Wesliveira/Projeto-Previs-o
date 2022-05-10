import requests

API_KEY = "973c9e58117124ef90e018351c156ffe"
cidade = "São Paulo"

link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

requi = requests.get(link)
requi_dic = requi.json()

descricao = requi_dic['weather'][0]['description']
temp = requi_dic['main']['temp'] - 273.15
print(descricao, temp)

