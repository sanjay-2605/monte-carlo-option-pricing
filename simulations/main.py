from simulations.monte_carlo import simulate_stock_paths
from pricing.option_pricing import european_call_option_price
from risk.risk_metrics import calculate_var, calculate_volatility
from utils.plot import plot_paths, plot_payoff
import numpy as np

# Parameters
S0 = 100
K = 105
r = 0.05
T = 1
mu = 0.1
sigma = 0.2
steps = 252
simulations = 10000

# Simulate paths
paths = simulate_stock_paths(S0, mu, sigma, T, steps, simulations)

# Option pricing
price, payoff = european_call_option_price(paths, K, r, T)

# Returns
returns = (paths[-1] - S0) / S0

# Risk metrics
var = calculate_var(returns)
volatility = calculate_volatility(returns)

print("Option Price:", price)
print("Value at Risk:", var)
print("Volatility:", volatility)

# Plot
plot_paths(paths)
plot_payoff(payoff)
