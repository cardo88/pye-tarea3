import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom, stats

# Parámetro de la distribución geométrica
p_geom = 0.08

# Tamanos de muestra
tamanos_muestra = [10**2, 10**3, 10**4, 10**5]

# Generar muestras
muestras_geom = {tamano: geom.rvs(p_geom, size=tamano) for tamano in tamanos_muestra}

# Crear diagramas de cajas
fig, ejes = plt.subplots(1, 4, figsize=(20, 5))

for i, tamano in enumerate(tamanos_muestra):
    ejes[i].boxplot(muestras_geom[tamano])
    ejes[i].set_title(f'Muestra de tamano {tamano}')
    ejes[i].set_xlabel('Muestra')
    ejes[i].set_ylabel('Valor')

plt.tight_layout()
plt.show()

# Crear histogramas
fig, ejes = plt.subplots(2, 2, figsize=(12, 10))

for i, tamano in enumerate(tamanos_muestra):
    eje = ejes[i // 2, i % 2]
    eje.hist(muestras_geom[tamano], bins=30, edgecolor='k', alpha=0.7)
    eje.set_title(f'Histograma de tamano {tamano}')
    eje.set_xlabel('Valor')
    eje.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()

# Calcular mediana y moda
medianas_geom = {tamano: np.median(muestras_geom[tamano]) for tamano in tamanos_muestra}
modas_geom = {}

for tamano in tamanos_muestra:
    resultado_moda = stats.mode(muestras_geom[tamano])
    if isinstance(resultado_moda.mode, np.ndarray) and len(resultado_moda.mode) > 0:
        modas_geom[tamano] = resultado_moda.mode[0]
    else:
        modas_geom[tamano] = resultado_moda.mode

print("Medianas:", medianas_geom)
print("Modas:", modas_geom)

# Esperanza teórica
esperanza_teorica_geom = (1 / p_geom)

# Media empírica
media_empirica_geom = {tamano: np.mean(muestras_geom[tamano]) for tamano in tamanos_muestra}

print("Media empírica:", media_empirica_geom)
print("Esperanza teórica:", esperanza_teorica_geom)

# Varianza teórica
varianza_teorica_geom = (1 - p_geom) / (p_geom**2)

# Varianza empírica
varianza_empirica_geom = {tamano: np.var(muestras_geom[tamano], ddof=1) for tamano in tamanos_muestra}

print("Varianza empírica:", varianza_empirica_geom)
print("Varianza teórica:", varianza_teorica_geom)
