from scipy.optimize import curve_fit
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

print('Plotting and fitting the function y=a*sen(b*x + c)')
def seno(x,a,b,c):
  return a*np.sin(b*x + c) 
x = np.linspace(-10,10,1000)
y = seno(x,1,1,1)
ruido = 0.5*np.random.normal(y)
y = y + ruido  

fig, graf = plt.subplots()
graf.scatter(x,y,color='#00b3b3',label='Dados Experimentais')

popt, pcov =  curve_fit(seno,x,y)
graf.plot(x,seno(x,*popt),linestyle='--', linewidth=2, color='black',label='Ajuste da curva')
graf.set_xlabel("x")
graf.set_ylabel("y")
graf.legend()
graf.set_title('y=a*sen(b*x + c)')

print('Plotting and fitting the function a /( (x - b)**2 + c )')
def funcao(x,a,b,c):
  return a /( (x - b)**2 + c )
x = np.linspace(-10,10,1000)
y = funcao(x,1,1,1) 
ruido = 0.06*np.random.normal(y)
y = y + ruido

fig, graf = plt.subplots()
graf.scatter(x,y,color='#00b3b3',label='Dados Experimentais')

popt, pcov =  curve_fit(funcao,x,y)
graf.plot(x,funcao(x,*popt),linestyle='--', linewidth=2, color='black',label='Ajuste da curva')
graf.set_xlabel("x")
graf.set_ylabel("y")
graf.legend()
graf.set_title('a /( (x - b)**2 + c )')

print('Plotting and fitting the function a*sin(b*x)*sqrt(x+c)')
def funcao(x,a,b,c):
  return a*np.sin(b*x)*np.sqrt(x + c)
x = np.linspace(-10,10,1000)
y = funcao(x,1,1,1) 
ruido = 0.5*np.random.normal(y)
y = y + ruido

fig, graf = plt.subplots()
graf.scatter(x,y,color='#00b3b3',label='Dados Experimentais')

x = np.nan_to_num(x)
y = np.nan_to_num(y)

popt, pcov = curve_fit(funcao,x,y)
graf.plot(x,funcao(x,*popt),linestyle='--', linewidth=2, color='black',label='Ajuste da curva')
graf.set_xlabel("x")
graf.set_ylabel("y")
graf.legend()
graf.set_title('a*sin(b*x)*sqrt(x+c)')
