import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

qx = 0
sayac = 1
sayac2 = 1
data1 = []
data2 = []

print("-----------------------------------------")
while(sayac<6):
    
    verial = input(str(sayac)  + '. ip uzunlugunu giriniz(m):')
    sayac = sayac+1
    data1.append(float(verial))
print("-----------------------------------------")
while(sayac2<6):
    
    verial = input(str(sayac2)  + ". T'yi giriniz(s):")
    sayac2 = sayac2+1
    data2.append(float(verial)*float(verial))
print("-----------------------------------------")
gl = 0
temp = []
i = 0


while(i<5):
    g =(39.476*data1[i])/((data2[i]))
    temp.append(g)    
    i = i +1 
    print(g)


for i in temp:
    gl = i + gl

gl = gl/5

p = 0


data1 = np.array(data1
data2 = np.array(data2) 

x = data1.reshape(-1,1)
y = data2.reshape(-1,1)

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
plt.grid(True)





plt.scatter(y,x)
lr = LinearRegression()
lr.fit(x,y)
y_head = lr.predict(x)
plt.plot(y_head,x,color="red",label="linear")
plt.xlabel("Zaman(s² )  T²")
plt.ylabel("Uzunluk(m) L")

x1 =(y_head[1][0])
x2 =(y_head[2][0])

y1 =(x[1][0])
y2 =(x[2][0])

fig = plt.gcf()
fig.canvas.set_window_title('KTUN Fizik')
print("Eğim hesaplanıyor : ... y2 : {}  y1 : {}  x2 : {}  x1 : {}".format(y2,y1,x2,x1))


print('Deneysel ölçülen ortalama yer çekimi')
print(gl)
print("----------------------------------")
print('Gerçek yer çekimi : ')
print(((y2-y1)/(x2-x1))*39.478)
plt.title('Basit Harmonik Hareket')
print("-----------------------------------------")
print("Hata payı : ")
ou = ((((y2-y1)/(x2-x1))*39.478)-gl)/((((y2-y1)/(x2-x1))*39.478))
print(ou*100)
print('Created :Mehmet Değirmenci')
plt.show()

