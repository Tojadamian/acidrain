import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#generowanie danych symulacyjnych ilości opadu (X) i pH opadu (y)
np.random.seed(0)
n_samples = 100
X = np.random.uniform(low=0, high=50, size=(n_samples,1))
# ilość opadu w mm
true_slope = -0.1 #Prawdziwa wartość współczynnika nachylenia
true_intercept = 7 #Prawdziwa wartość przesunięcia
noise = np.random.normal(loc=0, scale=2, size=(n_samples,1)) #Szum
y = true_slope * X + true_intercept + noise #pH opadu

# Dopasowanie modelu regresji liniowej
model = LinearRegression()
model.fit(X, y)

#wyświetlenie wyników
print('Współczynnik nachylenia:', model.coef_[0][0])
print('Przesunięcie:', model.intercept_[0])

#rysoanie wykresu
plt.scatter(X, y, color='blue', label='Dane')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regresja liniowa')
plt.xlabel('Ilość opadu (mm)')
plt.ylabel('pH opadu')
plt.title('Regresja liniowa dla ilości opadu i pH opadu')
plt.legend()
plt.show()
