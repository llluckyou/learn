import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.special import factorial

if __name__ == '__main__':
    N = 20
    x = np.linspace(0, N, 50)
    y = gamma(x+1)
    plt.figure(facecolor='w')
    plt.plot(x, y, 'r-', x, y, 'mo', lw=2, ms=7)
    z = np.arange(0, N+1)
    f = factorial(z, exact=True)
    print(f)
    plt.plot(z, f, 'go', markersize=9)
    plt.grid(b=True)
    plt.xlim(-0.1, N + 0.1)
    plt.ylim(0.5, np.max(y)*1.05)
    plt.xlabel('X', fontsize=15)
    plt.ylabel('Gamma(X)', fontsize=15)
    plt.show()
