"""Verify the four RMSE values reported for the improved-conditions joint inversion.

Uses only the Python standard library; does not perform an inversion.
Run from the repository root: python verify_reported_rmse.py
"""
from pathlib import Path
import csv
import math

ROOT = Path(__file__).resolve().parent / "Results" / "Improved_conditions"
COMPONENTS = [
    "joint_gravity_gz_obs_pred_residual",
    "joint_mag_gradiometry_bxx_obs_pred_residual",
    "joint_mag_gradiometry_byy_obs_pred_residual",
    "joint_mag_gradiometry_bzz_obs_pred_residual",
]


def load_rows(path):
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def main():
    for component in COMPONENTS:
        data = load_rows(ROOT / f"{component}_datos.csv")
        metrics = load_rows(ROOT / f"{component}_metricas.csv")
        assert len(metrics) == 1, f"Expected one metric record: {component}"
        assert len(data) == int(metrics[0]["n_data"]), f"Unexpected record count: {component}"
        squared_errors = [
            (float(row["observed"]) - float(row["predicted"])) ** 2
            for row in data
        ]
        rmse = math.sqrt(sum(squared_errors) / len(squared_errors))
        reported = float(metrics[0]["rmse"])
        assert math.isclose(rmse, reported, rel_tol=1e-10, abs_tol=1e-10), (
            f"RMSE mismatch for {component}: {rmse} vs {reported}"
        )
        print(f"PASS {component}: n={len(data)}, RMSE={rmse:.9f} {metrics[0].get('units', '')}")
    print("All four reported RMSE values verified.")


if __name__ == "__main__":
    main()
