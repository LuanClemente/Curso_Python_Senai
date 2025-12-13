#Conversor de temperatura de Celcius para Fahrenheit e kelvin

temperatura = float(input("Digite a temperatura em Celcius: "))
fahrenheit = (temperatura * 9/5) + 32
kelvin = temperatura + 273.15

print (f"Você digitou {temperatura}°C, em Fahrenheit fica {fahrenheit}°F e em Kelvin fica {kelvin}°K.")