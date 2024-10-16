"""
This module defines the following routines used by the 'transform' step of the regression recipe:

- ``transformer_fn``: Defines customizable logic for transforming input data before it is passed
  to the estimator during model inference.
"""

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


def transformer_fn():
    """
    Returns an *unfitted* transformer that defines ``fit()`` and ``transform()`` methods.
    The transformer's input and output signatures should be compatible with scikit-learn
    transformers.
    """

    categorical_columns = ["gender", "polyuria", "polydipsia", "sudden_weight_loss", "weakness", "polyphagia", "genital_thrush", "visual_blurring", "itching", "irritability", "delayed_healing", "partial_paresis", "muscle_stiffness", "alopecia", "obesity"]

    cat_pipeline = Pipeline(
        steps=[
            ("one_hot_encoder", OneHotEncoder()),
        ]
    )

    return ColumnTransformer(
                    [
                        ("cat_pipeline", cat_pipeline, categorical_columns)
                    ]
                )
