import requests
from bs4 import BeautifulSoup
import re
import  csv
from janome.tokenizer import Tokenizer

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

    #レシピの説明文を取得
    sentence1= soup2.figcaption.p.string.replace(" ","").strip()
    sentence2=soup2.find_all("div",class_="content")[2].text.replace(" ","").replace("\n","").replace("ポイント","").strip()
    sentence=sentence1+sentence2

    #形態解析をして使われている名詞を頻出頻度の高い順に並べる
    t=Tokenizer()
    word_dic={}
    tokens=t.tokenize(sentence)
    for w in tokens :
        word=w.surface
        ps=w.part_of_speech
        if (re.match('名詞,(一般|固有名詞|サ変接続|形容動詞語幹)',ps)):

            if not word in word_dic:
                word_dic[word]=0
            word_dic[word]+=1

    keys=sorted(word_dic.items(),key=lambda x:x[1],reverse=True)
    for word1,cnt in keys[:3]:
        recipe.append(word1)

    # 収集した情報を格納
    information.append(recipe)

with open('recipe.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(['cooktime','ingredients','cookway','keyword'])
    writer.writerows(information)






















