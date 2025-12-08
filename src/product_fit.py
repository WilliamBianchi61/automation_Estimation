import numpy as np
import pandas as pd
import math
import os

csv = "<file_path>"

autostore_bin_type = input("Input the Bin type: \n") # can make this into an automation type selector so GEEK and t-Sort can be included

autoStore_bin_size = [3]

match autostore_bin_type:
    case "220":
        autoStore_bin_size = 220,400,600
    case "330":
        autoStore_bin_size = 330,400,600
    case "425":
        autoStore_bin_size = 425,400,600
    case _:
        print("no bins type selected")
    




print(autoStore_bin_size)