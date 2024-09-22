"""
Show resolved
This module defines the following routines used by the 'train' step of the regression recipe:
- ``estimator_fn``: Defines the customizable estimator type and parameters that are used
  during training to produce a model recipe.
"""
from typing import Dict, Any


def estimator_sgd_regressor_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from sklearn.linear_model import SGDRegressor

    return SGDRegressor(random_state=42, **estimator_params)

def estimator_random_forest_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from sklearn.ensemble import RandomForestRegressor

    return RandomForestRegressor(random_state=42, **estimator_params)


def estimator_linear_regression_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from sklearn.linear_model import LinearRegression

    return LinearRegression(**estimator_params)

def estimator_decision_tree_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from sklearn.tree import DecisionTreeRegressor

    return DecisionTreeRegressor(**estimator_params)

def estimator_gb_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from sklearn.ensemble import GradientBoostingRegressor

    return GradientBoostingRegressor(**estimator_params)

def estimator_xgb_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from xgboost import XGBRegressor

    return XGBRegressor(**estimator_params)

def estimator_catb_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from catboost import CatBoostRegressor

    return CatBoostRegressor(**estimator_params)

def estimator_adab_fn(estimator_params: Dict[str, Any] = None):
    """
    Returns an *unfitted* estimator that defines ``fit()`` and ``predict()`` methods.
    The estimator's input and output signatures should be compatible with scikit-learn
    estimators.
    """
    if estimator_params is None:
        estimator_params = {}
    from sklearn.ensemble import AdaBoostRegressor

    return AdaBoostRegressor(**estimator_params)

