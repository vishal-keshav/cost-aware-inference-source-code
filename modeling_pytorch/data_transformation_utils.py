import numpy as np
from scipy.signal import resample
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

def standardizer_z_score(data, verbose=False):
    """
    data is a time seriese sequence (nd_array) numpy data
    normalize the data across time series by calculating mean and variance
    print the mean and variance if verbose is true.
    Here we standardize the data with z-score normalization.
    This is supposedly work only if data has gaussian distribution.

    Other normalization procedure to explore:
    * Median normalization
    * Sigmoid normalization
    * Tanh normalization
    """
    scaler = StandardScaler()
    scaler.fit(data)
    scaled_data = scaler.transform(data)
    if verbose:
        print("mean: ", scaler.mean_, " var: ", scaler.var_)
    return scaled_data


def normalizer_min_max(data, verbose=False):
    """
    Normalize the data in range 0 to 1. Supresses the scaler variations,
    but do not assume any gaussian distribution (this assumption is with
    standardization)
    """
    scaler = MinMaxScaler()
    scaler.fit(data)
    scaled_data = scaler.transform(data)
    if verbose:
        print("min: ", scaler.data_min_, " max: ", scaler.data_max_)
    return scaled_data


def normalizer_median_quantiles(data, verbose=False):
    """
    Normalize the data in range 75th and 25th percentile
    This normalization is robust to outliers
    """
    scaler = RobustScaler()
    scaler.fit(data)
    scaled_data = scaler.transform(data)
    if verbose:
        print("center: ", scaler.center_, " scale: ", scaler.scale_)
    return scaled_data

# #################################### Test ###################################



if __name__ == "__main__":
    pass
