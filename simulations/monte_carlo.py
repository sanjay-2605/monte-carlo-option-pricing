import numpy as np

def simulate_stock_paths(S0, mu, sigma, T, steps, simulations):
    dt = T / steps
    paths = np.zeros((steps, simulations))
    paths[0] = S0

    for t in range(1, steps):
        Z = np.random.standard_normal(simulations)
        paths[t] = paths[t-1] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)

    return paths
