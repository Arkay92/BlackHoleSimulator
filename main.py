import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Constants
G = 6.674e-11  # gravitational constant in m^3 kg^-1 s^-2
c = 3.00e8  # speed of light in m/s

def schwarzschild_radius(M):
    """
    Calculate the Schwarzschild radius for a given mass.
    """
    return 2 * G * M / c**2

def create_figure(M):
    """
    Create a Plotly figure for a black hole with given mass.
    """
    rs = schwarzschild_radius(M)
    phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
    x = rs * np.sin(theta) * np.cos(phi)
    y = rs * np.sin(theta) * np.sin(phi)
    z = rs * np.cos(theta)
    
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Blackbody')])
    fig.update_layout(title=f'Visualization of a Schwarzschild Black Hole with Mass {M} kg', autosize=False,
                      width=800, height=800,
                      margin=dict(l=65, r=50, b=65, t=90))
    return fig

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='mass-input', type='number', value=1.989e30, step=1e29),
    dcc.Graph(id='black-hole-plot')
])

@app.callback(
    Output('black-hole-plot', 'figure'),
    [Input('mass-input', 'value')]
)
def update_figure(mass):
    return create_figure(mass)

if __name__ == '__main__':
    app.run_server(debug=True)
