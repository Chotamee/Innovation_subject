import numpy as np
import matplotlib.pyplot as plt

# Температура
T = np.array([100, 200, 300, 400, 500, 600])

# Формула бойынша жылу коэффициентін есептеу
k = 5.4e-3 * np.sqrt(T)

# Нәтижелерді шығару
for t, value in zip(T, k):
    print(f"T = {t} K, k = {value:.6f}")

# График
plt.plot(T, k, marker='o')

plt.xlabel('Температура, K')
plt.ylabel('Жылу коэффициенті, k')
plt.title('k температураға тәуелділігі')
plt.grid(True)
plt.show()