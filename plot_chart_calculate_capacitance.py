# Definindo os parâmetros do capacitor
L = 0.1  # Comprimento do lado maior do capacitor em metros
d = 0.002  # Distância entre as placas em metros
Vo = 10  # Diferença de potencial entre as placas em volts
Ns = [10, 20, 30, 40]  # Lista de valores de N

caps = [calculate_capacitance(L, d, Vo, N) for N in Ns]

plt.plot(Ns, caps)
plt.xlabel('N')
plt.ylabel('Capacitância (F)')
plt.show()
