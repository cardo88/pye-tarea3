import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, stats

# Parámetro de la distribución de Poisson
lambda_poisson = 30

# Tamanos de muestra
tamanos_muestra = [10**2, 10**3, 10**4, 10**5]

# Generar muestras
muestras_poisson = {tamano: poisson.rvs(lambda_poisson, size=tamano) for tamano in tamanos_muestra}

# Crear diagramas de cajas
fig, ejes = plt.subplots(1, 4, figsize=(20, 5))

for i, tamano in enumerate(tamanos_muestra):
    ejes[i].boxplot(muestras_poisson[tamano])
    ejes[i].set_title(f'Muestra de tamano {tamano}')
    ejes[i].set_xlabel('Muestra')
    ejes[i].set_ylabel('Valor')

plt.tight_layout()
plt.show()

# Crear histogramas
fig, ejes = plt.subplots(2, 2, figsize=(12, 10))

for i, tamano in enumerate(tamanos_muestra):
    eje = ejes[i // 2, i % 2]
    eje.hist(muestras_poisson[tamano], bins=30, edgecolor='k', alpha=0.7)
    eje.set_title(f'Histograma de tamano {tamano}')
    eje.set_xlabel('Valor')
    eje.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Calcular mediana y moda
medianas_poisson = {tamano: np.median(muestras_poisson[tamano]) for tamano in tamanos_muestra}
modas_poisson = {}

for tamano in tamanos_muestra:
    resultado_moda = stats.mode(muestras_poisson[tamano])
    if isinstance(resultado_moda.mode, np.ndarray) and len(resultado_moda.mode) > 0:
        modas_poisson[tamano] = resultado_moda.mode[0]
    else:
        modas_poisson[tamano] = resultado_moda.mode

print("Medianas:", medianas_poisson)
print("Modas:", modas_poisson)

# Esperanza teórica
esperanza_teorica_poisson = lambda_poisson

# Media empírica
media_empirica_poisson = {tamano: np.mean(muestras_poisson[tamano]) for tamano in tamanos_muestra}

print("Media empírica:", media_empirica_poisson)
print("Esperanza teórica:", esperanza_teorica_poisson)

# Varianza teórica
varianza_teorica_poisson = lambda_poisson

# Varianza empírica
varianza_empirica_poisson = {tamano: np.var(muestras_poisson[tamano], ddof=1) for tamano in tamanos_muestra}

print("Varianza empírica:", varianza_empirica_poisson)
print("Varianza teórica:", varianza_teorica_poisson)