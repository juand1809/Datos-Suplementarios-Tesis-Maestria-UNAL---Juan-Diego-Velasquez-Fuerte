# Cerro Machín — datos suplementarios de entrada

Este paquete complementa el repositorio existente de datos y códigos de la tesis / manuscrito sobre inversión de gravimetría y gradiometría magnética en Cerro Machín.

## Contenido

- `Sinteticos/`: cinco escenarios (`denso_profundo`, `esquematico`, `falla_normal`, `liviano`, `multicuerpos`).
  - `datos_sinteticos_anom.csv`: observaciones sintéticas utilizadas como entrada en la configuración revisada de `inversion_sinteticos.txt`.
  - `modelo_mesh.csv`: propiedades y centros de celda del modelo sintético; el inversor revisado lo utiliza como modelo previo cuando `USE_PRIOR=True`.
  - `multicuerpos/datos_sinteticos.csv`: archivo adicional presente en el paquete original; se conserva sin adjudicarle una función en los experimentos definitivos.
- `Geologia/DEM_Machin_limite.tif`: modelo digital de elevación empleado por versiones de los códigos reales. Su procedencia probable y las limitaciones de trazabilidad se documentan a continuación.
- `Geologia/{crater_fixed,domo_fixed,flujos_sin_recortes,unidades_sin_flujos}.*`: conjuntos de datos vectoriales. Mantener juntos los componentes `.shp`, `.shx`, `.dbf`, `.prj`, `.cpg`.

## Procedencia del DEM y de la cartografía geológica

- **DEM (`DEM_Machin_limite.tif`).** Pedraza et al. (2022), *Gravity Studies at the Cerro Machín volcano, Colombia*, señalan que para su corrección topográfica utilizaron un modelo digital de elevación Copernicus DEM, citado como OpenTopography (2021). El autor de este repositorio participó en ese estudio y recuerda que el raster usado posteriormente en la tesis procede de aquella fuente. Por ello, **Copernicus DEM es la procedencia probable**, pero no se ha podido demostrar que este TIFF sea exactamente el mismo archivo utilizado en Pedraza et al. (2022) ni reconstruir sus parámetros de descarga, recorte o reproyección. No se atribuye aquí una variante específica (por ejemplo, GLO-30) sin verificar su procedencia.
- **Shapefiles.** Según la tesis de Velásquez-Fuerte, las geometrías vectoriales son **de elaboración propia**, basadas en la vista en planta de la Fig. 3 de Vesga-Ramírez et al. (2021). La disposición general de las unidades y los valores petrofísicos se apoyan además en Vesga-Ramírez et al. (2021) y Pedraza et al. (2022). Estos estudios deben citarse al reutilizar la interpretación geológica.
- **Uso y atribución.** Antes de redistribuir el DEM públicamente se deben comprobar las condiciones de reutilización y atribución aplicables al producto fuente. La identificación probable de Copernicus no equivale por sí sola a verificar la licencia del TIFF concreto. Conservar las referencias a los estudios originales y documentar cualquier transformación conocida.

**Referencias de procedencia para completar en la bibliografía formal:** Pedraza et al. (2022), *Gravity Studies at the Cerro Machín volcano, Colombia*; Vesga-Ramírez et al. (2021); OpenTopography (2021), fuente citada por Pedraza et al. (2022) para Copernicus DEM.

## Relación con los códigos existentes

El repositorio público contiene `inversion_sinteticos.txt`, `inversion_sinteticos_correccion_jurados.txt`, `inversion_reales.txt`, `inversion_reales_correccion_jurados.txt`, `inversion_treemesh_correccion_jurados.txt`, `inversiones_reales_treemesh.txt` y `modelo_litologico.txt`, así como datos de gravedad, gradiometría e interpolaciones.

**Nota:** esta entrega no sustituye ninguno de esos archivos. Se comprobaron nombres de dependencias con copias de código disponibles durante la preparación; aún no se han comparado las copias byte a byte con todos los scripts publicados en GitHub.

La configuración revisada del inversor sintético apunta a:

```python
DATA_SYN = os.path.join(SYN_DIR, ESCENARIO, "datos_sinteticos_anom.csv")
USE_PRIOR = True
PRIOR_MODEL = os.path.join(SYN_DIR, ESCENARIO, "modelo_mesh.csv")
```

Los códigos emplean rutas absolutas bajo `/content/drive/MyDrive/Tesis/` en Google Colab. Si se clona el repositorio o se reorganizan carpetas, se deben ajustar `BASE`, `SYN_DIR` y otras rutas antes de ejecutar. Los scripts no se han editado en este paquete.

## Límites de reproducibilidad

- Este paquete verifica la disponibilidad de entradas, no reproduce las inversiones.
- No se ha establecido qué configuración exacta produjo cada panel de la Figura 5, compuesta a partir de imágenes de diferentes ejecuciones.
- No se ha certificado la presencia o activación de `CrossGradient` en cada ejecución definitiva.
- Los resultados de misfit y modelos recuperados existentes en Drive no se incluyen aquí por ser salidas, no entradas. Su selección para archivo de resultados es independiente.
- `generador_sinteticos.py` no se incorpora como generador oficial porque su uso en la creación del conjunto definitivo no ha sido demostrado.
- La procedencia del DEM es probable, no plenamente verificada; confirmar licencia/atribución del raster antes de publicarlo. Las geometrías vectoriales se describen como elaboradas por el autor a partir de cartografía interpretativa publicada.
- No se incluye un entorno de dependencias fijado porque faltaría verificarlo contra las ejecuciones originales.

## Cómo integrar

Subir las carpetas `Sinteticos/` y `Geologia/` a la raíz del repositorio existente. Se puede agregar este README, pero si el repositorio ya tiene otro `README.md`, **combinar los contenidos en lugar de sobrescribirlo**. No eliminar ni reemplazar los códigos o datos actuales.
