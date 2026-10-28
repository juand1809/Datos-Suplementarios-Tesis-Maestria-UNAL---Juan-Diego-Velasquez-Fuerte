# When joint inversion is insufficient: gravity and magnetic-gradient constraints at Cerro Machín volcano, Colombia

**Supplementary data and Python code** for the manuscript *When joint inversion is insufficient: gravity and magnetic-gradient constraints at Cerro Machín volcano, Colombia — Resolution assessment under sparse and uneven field coverage*, prepared for the *Journal of Applied Geophysics*.

**Authors:** Juan Diego Velásquez-Fuerte, Carlos Alberto Vargas-Jiménez, and Alexander Caneva-Rincón.

This study uses synthetic tests and field observations to assess the performance of individual and joint gravity and magnetic-gradient inversions at Cerro Machín volcano, Colombia.

## Repository contents

### Field observations and derived datasets

| File | Contents |
| --- | --- |
| `Gravimetría_VCM.xlsx` | Gravity dataset used in the field-data analyses. |
| `gradientes_filtrado_1.csv` – `gradientes_filtrado_5.csv` | Processed magnetic-gradient observations from five survey lines. |
| `gravimetria_interpolada_20x20.csv` | Interpolated gravity dataset used in gridded sensitivity experiments. |
| `gradientes_interpolados_20x20.csv` | Interpolated magnetic-gradient dataset used in gridded sensitivity experiments. |

The field dataset described in the manuscript contains **84 gravity stations** and **276 processed magnetic-gradient records**. Interpolated values are provided for numerical comparisons and are **not additional independent measurements**.

### Synthetic models

`Sinteticos/` contains five benchmark scenarios:

- `denso_profundo/`
- `esquematico/`
- `falla_normal/`
- `liviano/`
- `multicuerpos/`

Each scenario includes `datos_sinteticos_anom.csv` (synthetic potential-field observations) and `modelo_mesh.csv` (model-grid information and physical properties). The synthetic tests described in the manuscript use **441 regularly distributed observation locations** per scenario.

### Geological inputs

`Geologia/` contains:

- `DEM_Machin_limite.tif` — elevation raster used to define the field-modeling domain.
- `crater_fixed`, `domo_fixed`, `flujos_sin_recortes`, and `unidades_sin_flujos` — vector datasets supplied as multi-file shapefiles (`.shp`, `.shx`, `.dbf`, `.prj`, `.cpg`).

**DEM coverage:** The supplied clipped raster extends from **75.409306° W to 75.362917° W**, and from **4.465694° N to 4.504028° N** (WGS 84; EPSG:4326). Its pixel spacing is approximately 1 arc-second (about 30 m). These coordinates describe the extent of the supplied file, not necessarily the boundaries originally submitted for download.

**Data provenance:** The DEM was obtained through OpenTopography from Copernicus DEM data for the Cerro Machín area during the work associated with Pedraza et al. (2022); the file shared here is a clipped raster. The geological polygons were delineated by the author with reference to the interpretation of Vesga-Ramírez et al. (2021).

### Python scripts

The `.txt` files listed below contain Python source code. Their original filenames are retained.

**Scripts used to generate the figures presented in the manuscript:**

| Script | Purpose |
| --- | --- |
| `inversion_sinteticos.txt` | Synthetic-data inversions and figures. |
| `inversion_reales.txt` | Field-data inversions and figures. |
| `inversiones_reales_treemesh.txt` | Field-data inversions and figures under the *improved conditions* examined in the manuscript, using TreeMesh. |

**Scripts used for data-misfit analysis:**

| Script | Purpose |
| --- | --- |
| `inversion_sinteticos_correccion_jurados.txt` | Synthetic-data inversion misfit calculations and associated figures. |
| `inversion_reales_correccion_jurados.txt` | Field-data inversion misfit calculations and associated figures. |
| `inversion_treemesh_correccion_jurados.txt` | Misfit calculations and associated figures for the TreeMesh *improved-conditions* experiments. |

The `correccion_jurados` scripts were used to calculate data-fit metrics and generate additional diagnostic figures. The other inversion scripts were used to produce the figures presented in the manuscript. The TreeMesh implementations correspond to the experiments conducted under *improved modeling conditions*.

### Numerical diagnostics for the improved-conditions experiment

[`Results/Improved_conditions/`](Results/Improved_conditions/) contains the observed-versus-predicted tables and reported fit metrics for the **joint TreeMesh experiment** discussed in Section 4.3. The reported RMSE values can be checked without rerunning the inversion using:

```bash
python verify_reported_rmse.py
```

These diagnostics describe fits to interpolated data; they do not provide additional independent field observations.

## Using the code and data

1. **Preserve the repository structure.** Download or clone the repository. The inversion scripts are stored as `.txt` files containing Python code; their contents can be run in a Python notebook or saved as `.py` files.

2. **Prepare the Python environment.** The manuscript reports SimPEG v0.24.0. An initial dependency list is provided in [`requirements.txt`](requirements.txt); the other package versions have not been recovered from the original execution environment.

3. **Configure the data directory.** In the configuration section of the chosen script, set `BASE` to the directory containing the repository files. The original scripts contain the Google Colab/Drive path `/content/drive/MyDrive/Tesis/`, which must be changed if the files are stored elsewhere.

4. **Adjust geological input paths for field inversions.** The four field-inversion scripts currently look for the DEM and shapefiles directly inside `BASE`, whereas this repository stores them in `Geologia/`. Update `DEM` and the `shapefiles` dictionary accordingly:

   ```python
   DEM = os.path.join(BASE, "Geologia", "DEM_Machin_limite.tif")
   shapefiles = {
       "unidades": os.path.join(BASE, "Geologia", "unidades_sin_flujos.shp"),
       "flujos": os.path.join(BASE, "Geologia", "flujos_sin_recortes.shp"),
       "crater": os.path.join(BASE, "Geologia", "crater_fixed.shp"),
       "domo": os.path.join(BASE, "Geologia", "domo_fixed.shp"),
   }
   ```

5. **Run synthetic-data inversions.** In either synthetic script, select the scenario with `ESCENARIO`. The script loads `Sinteticos/<scenario>/datos_sinteticos_anom.csv`; when `USE_PRIOR=True`, it also uses `Sinteticos/<scenario>/modelo_mesh.csv` as the prior model.

6. **Run field-data inversions.** The `inversion_reales` scripts read `Gravimetría_VCM.xlsx` and the five `gradientes_filtrado_*.csv` files. The TreeMesh scripts, used for the improved-conditions experiments, read `gravimetria_interpolada_20x20.csv`, `gradientes_interpolados_20x20.csv`, and the five processed gradient-line files. Both groups also use the geological inputs described above.

7. **Select the calculations and diagnostics.** Review the inversion settings in each script's configuration section before running it. The `correccion_jurados` scripts include `RUN_GRAVITY`, `RUN_MAG_GRADIOMETRY`, and `RUN_JOINT` switches for selecting inversion types and produce data-fit diagnostics and associated figures.

For the current configuration defaults of each archived script, see [`EXPERIMENT_CONFIGURATIONS.md`](EXPERIMENT_CONFIGURATIONS.md). These defaults should not be assumed to identify every figure-producing run.

## Related studies

- **Pedraza et al. (2022)** — gravity investigation of Cerro Machín and the source study associated with the elevation data.
- **Vesga-Ramírez et al. (2021)** — geological interpretation used as a reference for the vector geometries.

Please refer to the manuscript and the cited studies for the scientific methodology, geological context, and interpretation.
