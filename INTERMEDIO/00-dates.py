"""
Dates: fechas- representa una hora, un día o tiempo.
"""
from datetime import datetime # agrupa las dos tiempo y fechas
from datetime import time # agrupa el tiempo(la parte de la hora)
from datetime import date # agrupa las fechas
from datetime import timedelta # nos va a permitir operar con diferentes fechas

now = datetime.now()
"""
print(now.day)
print(now.hour)
print(now.minute)
print(now.year)
print(now.month)
print(now.second)
"""
timestamp = now.timestamp()
print(timestamp)
"""
timestap: se toma como medida de tiempo el número de segundos transcurridos 
desde el primero de enero de 1970 a las 0 horas UTC hasta el momento a representar
"""

# función manipulando las fechas
def print_date(date):
    print("segundos:",date.second)
    print("minutos:",date.minute)
    print("hora:",date.hour)
    print("dias:",date.day)
    print("mes:",date.month)
    print("año:",date.year)
    print(date.timestamp())
    
print(now)    
    
year_2023 = datetime(2023,1,1,12,15) 
print_date(year_2023)    

current_time = time(21,5,6) # colocar primero la hora, despues minutos y luego segundos
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

#current_date = date(current_date.year,current_date.month + 8, current_date.day)
#print(current_date.month)

# cuando son objetos del mismo tipo si se los puede restar
# primer los objetos son datetime
diferente = year_2023 - now
print(diferente)

 #luego son date
diferente = year_2023.date() - current_date
print(diferente)

start_delta = timedelta(200,10,15,weeks=200)
end_delta = timedelta(15,19,21, weeks=100)
print(end_delta - start_delta)
print(end_delta + start_delta)