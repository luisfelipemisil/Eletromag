import plotly.graph_objects as go

Ns = [10, 20, 30, 40, 50]  # Lista de valores de N
d = 0.002  # Distância entre as placas em metros
L = 0.1  # Comprimento do lado maior do capacitor em metros
Vo = 10  # Diferença de potencial entre as placas em volts


for i in range(len(Ns)):
    N = Ns[i]
    dist = calculate_surface_charge_density(L, d, Vo, N)

    # Plotando a distribuição de cargas
    x = np.linspace(0, L, N)
    y = np.linspace(0, L, N)
    X, Y = np.meshgrid(x, y)
    Z = dist.T

    fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='viridis')])
    fig.update_layout(scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title=f'Cargas para N={N} (1e-8 C/m²)',
        camera=dict(
            eye=dict(x=-1.7, y=-1.7, z=0.5),
            up=dict(x=0, y=0, z=1),
        ),
    ))
    fig.show()
