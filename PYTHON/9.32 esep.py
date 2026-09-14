import numpy as np
import matplotlib.pyplot as plt


k = 9e9
q = 5e-9
R = 0.10

L = np.array([0, 0.05, 0.08, 0.10, 0.15])
E = k * q * L / (R**2 + L**2)**1.5

print("L (см):", L*100)
print("E (В/м):", E)




k = 9e9
q = 5e-9
R = 0.10

L = np.array([0, 0.05, 0.08, 0.10, 0.15])
E = k * q * L / (R**2 + L**2)**1.5

L_plot = np.linspace(0, 0.20, 500)
E_plot = k * q * L_plot / (R**2 + L_plot**2)**1.5

plt.plot(L_plot*100, E_plot); plt.plot(L*100, E, 'ro'); plt.title('E(L)'); plt.xlabel('L, см'); plt.ylabel('E, В/м'); plt.grid()
plt.show()