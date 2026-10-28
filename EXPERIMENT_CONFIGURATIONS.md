# Execution configurations and source-file mapping

This document records the **configuration values currently present in the archived Python scripts** accompanying the study. These defaults are not, by themselves, evidence that any particular figure was generated with exactly these settings. Figure-specific run provenance is only established when logs or saved configurations are available.

## Script inventory

| Script | Intended role | Default configuration in the archived script |
| --- | --- | --- |
| `inversion_sinteticos.txt` | Synthetic inversion and manuscript figures | `ESCENARIO="liviano"`; `USE_PRIOR=True`; gravity, magnetic-gradient and joint routines called in sequence; `DH=150`, `NZ=40` |
| `inversion_sinteticos_correccion_jurados.txt` | Synthetic inversions, fit diagnostics and associated figures | `ESCENARIO="multicuerpos"`; `USE_PRIOR=True`; `RUN_GRAVITY=True`, `RUN_MAG_GRADIOMETRY=False`, `RUN_JOINT=False`; `DH=150`, `NZ=40` |
| `inversion_reales.txt` | Field-data inversion and manuscript figures | `USE_PRIOR=False`; gravity data from `Gravimetría_VCM.xlsx`; five processed magnetic-gradient files |
| `inversion_reales_correccion_jurados.txt` | Field-data inversion, fit diagnostics and associated figures | `USE_PRIOR=False`; `RUN_GRAVITY=False`, `RUN_MAG_GRADIOMETRY=False`, `RUN_JOINT=True`; `JOINT_USE_CROSS_GRADIENT=False` |
| `inversiones_reales_treemesh.txt` | Adaptive-mesh field-data inversion and improved-conditions figures | `USE_PRIOR=False`; `USE_CROSS_GRADIENT=True`, `WEIGHT_XGRAD=1e2` |
| `inversion_treemesh_correccion_jurados.txt` | Adaptive-mesh field-data diagnostics and associated figures | `USE_PRIOR=False`; `USE_CROSS_GRADIENT=True`, `WEIGHT_XGRAD=1e2`; `RUN_GRAVITY=False`, `RUN_MAG_GRADIOMETRY=False`, `RUN_JOINT=True` |

## Input files

**Synthetic inversions:** Set `BASE` to the local repository root and choose `ESCENARIO` in the configuration block. Each of the five scenarios under `Sinteticos/` contains `datos_sinteticos_anom.csv` and `modelo_mesh.csv`. The latter is used when `USE_PRIOR=True`.

**Field inversions (TensorMesh):** `Gravimetría_VCM.xlsx`, `gradientes_filtrado_1.csv` through `gradientes_filtrado_5.csv`, and the geological inputs under `Geologia/`.

**Field inversions (TreeMesh, improved conditions):** `gravimetria_interpolada_20x20.csv` and a `MAG_GRAD_FILES` list that includes **both** `gradientes_interpolados_20x20.csv` **and** the five processed line files `gradientes_filtrado_1.csv` through `gradientes_filtrado_5.csv`. These scripts also use the geological inputs under `Geologia/`.

The four field-inversion scripts currently construct `DEM` and shapefile paths immediately below `BASE`. With the public directory structure, those paths must include `Geologia/` (see the repository's main README).

## Python environment

`requirements.txt` lists the directly imported third-party packages and the Excel engine required to read the gravity workbook. The manuscript identifies **SimPEG 0.24.0**; the originally installed versions of other libraries and the original Python interpreter version were not recovered. This list has **not** been validated by rerunning all inversions. A complete version-locked environment should only be published after obtaining it from a known working environment.

## Traceability limits

- Default values in a distributed script may differ from those used for a particular displayed figure if its configuration was changed between runs.
- The manuscript's synthetic figure was assembled from selected panels rather than exported from one single documented run. A definitive per-panel configuration mapping has not been reconstructed.
- The TreeMesh scripts expose structural-coupling options, but the appearance of a setting in the archived source is not proof that it was active in every result presented in the manuscript.
- The `correccion_jurados` variants produce data-fit diagnostics **and** additional figures, not diagnostics exclusively.
- This audit reflects copies of the scripts archived with the project materials; byte-for-byte equality against the current GitHub repository was not established.

No inversion algorithms, datasets or published figures are modified by this documentation.
