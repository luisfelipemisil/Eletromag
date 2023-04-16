import numpy as np
import plotly.express as px

# Permissividade elétrica do vácuo
EPSILON_0 = 8.8541878176e-12

def calculate_surface_charge_density(length, distance, voltage, num_points):
    """Calcula a densidade superficial de carga em uma placa com tensão aplicada.
    
    Args:
        length : comprimento da placa em metros
        distance : distância entre as placas em metros
        voltage : diferença de potencial aplicada entre as placas em volts
        num_points : número de pontos em cada dimensão da grade
    
    Returns:
        dist : densidade superficial de carga em coulombs por metro quadrado
    """
    delta = length / num_points

    # Gerando coordenadas x e y dos pontos de carga
    x = np.zeros(2 * num_points ** 2)
    y = np.zeros(2 * num_points ** 2)
    count = 0
    for k1 in range(2):
        for k2 in range(num_points):
            for k3 in range(num_points):
                if not (k2 > num_points/2 and k3 > num_points/2):
                    x[count] = delta * (k2+1 - 0.5)
                    y[count] = delta * (k3+1 - 0.5)
                    count += 1
    
    # Gerando coordenada z dos pontos de carga
    z = np.zeros(count)
    z[:int(count/2)] = 0
    z[int(count/2):] = distance

    # Gerando vetor coluna de tensão V
    V = np.zeros(count)
    V[:int(count/2)] = voltage
    V[int(count/2):] = 0

    # Gerando matriz de impedância Z
    Z = np.zeros((count, count))
    for i in range(count):
        for j in range(count):
            if i == j:
                Z[i, j] = (delta/(np.pi*EPSILON_0))*np.log(1+np.sqrt(2))
            else:
                R = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2 + (z[i] - z[j])**2)
                Z[i, j] = (1/(4*np.pi*EPSILON_0))*((delta**2)/R)

    # Resolvendo o sistema linear Z * A = V
    A = np.linalg.solve(Z, V)

    # Gerando matriz de densidade superficial a partir da função impulso
    dist = np.empty((num_points, num_points))
    dist[:] = np.nan
    n = 0
    for k2 in range(num_points):
        for k3 in range(num_points):
            if not (k2 > num_points/2 and k3 > num_points/2):
                dist[k2][k3] = A[n]
                n += 1

    return dist
