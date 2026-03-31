import numpy as np

def european_call_option_price(paths, K, r, T):
    payoff = np.maximum(paths[-1] - K, 0)
    price = np.exp(-r * T) * np.mean(payoff)
    return price, payoff
