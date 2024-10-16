"""
This module defines the following routines used by the 'ingest' step of the regression recipe:

- ``load_file_as_dataframe``: Defines customizable logic for parsing dataset formats that are not
  natively parsed by MLflow Recipes (i.e. formats other than Parquet, Delta, and Spark SQL).
"""

import logging
import pandas as pd

from pandas import DataFrame

_logger = logging.getLogger(__name__)

def read_csv_as_dataframe(location: str, file_format: str) -> DataFrame:
  patient = pd.read_csv(location)
  patient = patient.drop_duplicates()
  return patient