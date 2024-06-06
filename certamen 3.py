import matplotlib.pyplot as plt
import numpy as np
print(f"Inversion de un capital por medio de interes simple y compuesto")

dinero=int(input("ingrese capital inicial en pesos chilenos: " ))
i=float(input("ingrese tasa de interes mensual de su inversion: "))
meses=int(input("ingrese el periodo de ahorro en meses: "))

print(f"Resumen de la inversion:")
print(f"Monto de inversion: ${dinero}")
print(f"Interes mensual: {i}%")
print(f"Periodo de inversion: {meses} meses")

interessimple=(dinero*(1+i/100)*meses)  
interescompuesto=(dinero*(1+i/100)**meses)

plt.plot(meses,dinero)
plt.title(input("ingrese titulo del grafico: "))
plt.xlabel(input("ingrese etiqueta del eje x. "))
plt.ylabel(input("ingrese etiqueta del eje y: "))
plt.legend(['interes simple','interes compuesto'])
plt.grid()
plt.show()
