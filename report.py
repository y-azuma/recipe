
import matplotlib.pyplot as plt
import numpy as np

#ファイルを開き読み込む
file=open('recipe.csv','r')
data=file.read()
file.close()
#リスト化する
information=[]
lines=data.split('\n')
for line in lines:
    recipe=line.split(',')
    information.append(recipe)

del information[0]
del information[-1]
#グラフ化しやすいように別々にリスト化する
cooktime=[]
ingredients=[]
cookway=[]
for infor in information:
    cooktime.append(int(infor[0]))
    ingredients.append(int(infor[1]))
    cookway.append(int(infor[2]))


#分布
plt.hist(cooktime,rwidth=0.5)
plt.xlabel('cooking_time')
plt.show()


plt.hist(ingredients,rwidth=0.5)
plt.xlabel('the_number_of_ingredients')
plt.show()

plt.hist(cookway,rwidth=0.5)
plt.xlabel('the_number_of_how_to_make_it')
plt.show()



#各々の相関
r1=np.corrcoef(cooktime,ingredients)
print("相関係数",r1[0][1])
plt.plot(cooktime,ingredients,'+')
plt.xlabel('cooking_time')
plt.ylabel('the_number_of_ingredients')
plt.show()

r2=np.corrcoef(cooktime,cookway)
print("相関係数",r2[0][1])
plt.plot(cooktime,cookway,'+')
plt.xlabel('cooking_time')
plt.ylabel('the_number_of_how_to_make_it')
plt.show()

r3=np.corrcoef(ingredients,cookway)
print("相関係数",r3[0][1])
plt.plot(ingredients,cookway,'+')
plt.xlabel('the_number_of_ingredients')
plt.ylabel('the_number_of_how_to_make_it')
plt.show()











