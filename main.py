import numpy as np
import plotly.graph_objects as go
import argparse

# Constants
G = 6.674e-11  # gravitational constant in m^3 kg^-1 s^-2
c = 3.00e8  # speed of light in m/s

def schwarzschild_radius(M):
    """
    Calculate the Schwarzschild radius for a given mass.
    
    Parameters:
    - M: Mass of the black hole in kilograms.
    
    Returns:
    - Schwarzschild radius in meters.
    """
    return 2 * G * M / c**2

def plot_black_hole(M):
    """
    Plot a 3D representation of a black hole for a given mass.
    
    Parameters:
    - M: Mass of the black hole in kilograms.
    """
    # Calculate Schwarzschild radius
    rs = schwarzschild_radius(M)

    # Create a sphere
    phi, theta = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
    x = rs * np.sin(theta) * np.cos(phi)
    y = rs * np.sin(theta) * np.sin(phi)
    z = rs * np.cos(theta)

    # Plot using Plotly
    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Blackbody')])
    fig.update_layout(title=f'Visualization of a Schwarzschild Black Hole with Mass {M} kg', autosize=False,
                      width=800, height=800,
                      margin=dict(l=65, r=50, b=65, t=90))
    fig.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualize a Schwarzschild Black Hole for a given mass.')
    parser.add_argument('mass', type=float, help='Mass of the black hole in kilograms')
    
    args = parser.parse_args()

    # Plotting the Schwarzschild black hole for the given mass
    plot_black_hole(args.mass)