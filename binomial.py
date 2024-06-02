import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, stats

# Parámetros de la distribución binomial
n = 100
p = 0.35

# Tamanos de muestra
tamanos_muestra = [10**2, 10**3, 10**4, 10**5]

# Generar muestras
muestras_binom = {tamano: binom.rvs(n, p, size=tamano) for tamano in tamanos_muestra}

# Crear diagramas de cajas
fig, ejes = plt.subplots(1, 4, figsize=(20, 5))

for i, tamano in enumerate(tamanos_muestra):
    ejes[i].boxplot(muestras_binom[tamano])
    ejes[i].set_title(f'Muestra de tamano {tamano}')
    ejes[i].set_xlabel('Muestra')
    ejes[i].set_ylabel('Valor')

plt.tight_layout()
plt.show()

# Crear histogramas
fig, ejes = plt.subplots(2, 2, figsize=(12, 10))

for i, tamano in enumerate(tamanos_muestra):
    eje = ejes[i // 2, i % 2]
    eje.hist(muestras_binom[tamano], bins=30, edgecolor='k', alpha=0.7)
    eje.set_title(f'Histograma de tamano {tamano}')
    eje.set_xlabel('Valor')
    eje.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Calcular mediana y moda
medianas_binom = {tamano: np.median(muestras_binom[tamano]) for tamano in tamanos_muestra}
modas_binom = {}

for tamano in tamanos_muestra:
    resultado_moda = stats.mode(muestras_binom[tamano])
    if isinstance(resultado_moda.mode, np.ndarray) and len(resultado_moda.mode) > 0:
        modas_binom[tamano] = resultado_moda.mode[0]
    else:
        modas_binom[tamano] = resultado_moda.mode

print("Medianas:", medianas_binom)
print("Modas:", modas_binom)

# Esperanza teórica
esperanza_teorica_binom = n * p

# Media empírica
media_empirica_binom = {tamano: np.mean(muestras_binom[tamano]) for tamano in tamanos_muestra}

print("Media empírica:", media_empirica_binom)
print("Esperanza teórica:", esperanza_teorica_binom)

# Varianza teórica
varianza_teorica_binom = n * p * (1 - p)

# Varianza empírica
varianza_empirica_binom = {tamano: np.var(muestras_binom[tamano], ddof=1) for tamano in tamanos_muestra}

print("Varianza empírica:", varianza_empirica_binom)
print("Varianza teórica:", varianza_teorica_binom)
