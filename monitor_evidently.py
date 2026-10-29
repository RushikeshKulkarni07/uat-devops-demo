"""Evidently data-drift monitoring (dry run with sample data)."""
import os

import pandas as pd
from sklearn.datasets import load_iris
from evidently import Report
from evidently.presets import DataDriftPreset

os.makedirs("reports", exist_ok=True)

iris = load_iris(as_frame=True).frame.drop(columns=["target"])
reference = iris.iloc[:75]      # baseline data
current = iris.iloc[75:]        # new/production data

report = Report([DataDriftPreset()])
snapshot = report.run(current_data=current, reference_data=reference)
snapshot.save_html("reports/evidently_report.html")
print("Evidently report generated: reports/evidently_report.html")
