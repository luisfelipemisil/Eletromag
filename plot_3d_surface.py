import numpy as np
import plotly.graph_objects as go

# Definindo os parâmetros do capacitor
N = 100  # Número de segmentos em cada placa
d = 0.002  # Distância entre as placas em metros
L = 0.1  # Comprimento do lado maior do capacitor em metros
Vo = 10  # Diferença de potencial entre as placas em volts

# Calculando a distribuição de cargas
dist = calculate_surface_charge_density(L, d, Vo, N)

# Criando os eixos x e y
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

# Criando a figura
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=dist, colorscale='viridis')])

# Configurando o layout
fig.update_layout(
    title=f"Cargas para N={N} (1e-8 C/m²)",
    scene = dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='Carga (1e-8 C/m²)',
        camera=dict(
            eye=dict(x=1.5, y=-1.5, z=1)
        )
    ),
    margin=dict(l=0, r=0, b=0, t=50)
)

# Exibindo o gráfico
fig.show()