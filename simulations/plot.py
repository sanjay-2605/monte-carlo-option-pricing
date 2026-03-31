import matplotlib.pyplot as plt

def plot_paths(paths):
    plt.figure(figsize=(10,5))
    plt.plot(paths)
    plt.title("Monte Carlo Stock Price Simulation")
    plt.xlabel("Time Steps")
    plt.ylabel("Stock Price")
    plt.show()

def plot_payoff(payoff):
    plt.figure(figsize=(8,5))
    plt.hist(payoff, bins=50)
    plt.title("Option Payoff Distribution")
    plt.show()
