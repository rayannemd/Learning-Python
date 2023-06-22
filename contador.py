from datetime import date
import datetime

ano = int(input("Insira o ano (Ex: 2020): "))      
mes = int(input("Insira o mês (Ex: 01): "))  
dia = int(input("Insira o dia (Ex: 02): "))

datapadrao = datetime.date(ano, mes, dia)
dataatual = datetime.date.today()

if datapadrao > dataatual:
    cont = datapadrao - dataatual
    print("Faltam", cont,"dias para essa data")

elif datapadrao <= dataatual:
    cont = dataatual - datapadrao
    print("Se passaram", cont,"dias dessa data")
    
else: 
    cont = 0
