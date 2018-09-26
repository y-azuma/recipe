import requests
from bs4 import BeautifulSoup
import re
import  csv
information=[]
html=requests.get('http://recipe.hacarus.com/')
soup=BeautifulSoup(html.text,'html.parser')
for news in soup.findAll('li'):
    # 各メニューのURLを取得する
    html2=requests.get('http://recipe.hacarus.com'+news.a.get("href"))
    soup2=BeautifulSoup(html2.content,'html.parser')
    header=soup2.header.p.string
    #調理時間を取得する
    cooktime=header.replace(" ","").replace("(","").replace(")","").strip()
    recipe=re.split('[\n分]', cooktime)
    del recipe[0::2]
    #時間表記の場合、分表記に変換する
    m=re.search('時間',recipe[0])
    if m:
        b=recipe[0].strip("時間以上")
        recipe[0]=int(b)*60
    #調理時間を数値整数型に変換
    recipe[0]=int(recipe[0])
    #材料数を取得する
    ingredient=len(soup2.tbody.findAll('tr'))
    soup2.tbody.name="tbody1"
    recipe.append(ingredient)
    #作り方の手順の数を取得する
    cookway=len(soup2.tbody.findAll('tr'))
    recipe.append(cookway)
    #収集した情報を格納
    information.append(recipe)

with open('recipe.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(['cooktime','ingredients','cookway'])
    writer.writerows(information)






















