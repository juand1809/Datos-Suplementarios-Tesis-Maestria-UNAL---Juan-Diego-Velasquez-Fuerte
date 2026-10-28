# Improved-conditions numerical diagnostics

These eight CSV files document the **joint TreeMesh inversion** results used for the numerical RMSE values discussed in Section 4.3 of the accompanying Cerro Machín manuscript. They were taken from the project archive folder named `misfit_observado_predicho_residual_treemesh`.

| Component | Units | Records | RMSE |
| --- | --- | ---: | ---: |
| Gravity (gz) | mGal | 400 | 1.3885793798542518 |
| Magnetic gradient (bxx) | nT/m | 400 | 1405.4651596207552 |
| Magnetic gradient (byy) | nT/m | 400 | 1687.3197415810437 |
| Magnetic gradient (bzz) | nT/m | 400 | 497.09303021197013 |

- Files ending in `_datos.csv` contain coordinates, observed values, predicted values, residuals, uncertainties, and normalized residuals.
- Files ending in `_metricas.csv` contain the reported statistics (sample count, RMSE, MAE, mean residual, normalized RMS, and data-misfit term).
- The reported metrics were independently checked against the paired observed/predicted values. The recalculated RMSE agrees to floating-point precision.
- These 400-point grids contain **interpolated values**, not 400 new independent field observations. They must not be conflated with the original gravity stations or processed gradient-line records.
- Other archived runs have different statistics; the values in this folder correspond specifically to the results cited above. These files do not assert the exact parameter settings used during the historic run.

Run `python verify_reported_rmse.py` from the repository root to recalculate the four RMSE values from these CSV files (no third-party packages required).
