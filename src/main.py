# import dump of packages
import numpy as np
import pandas as pd
import math
import os

#imports from

from product_fit import bin_type_selector
from product_fit import  unfit_product

# combine all functions here to start program

autoStore_bin_size = bin_type_selector()

unfit_product(autoStore_bin_size)

