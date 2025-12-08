import numpy as np
import pandas as pd
import math
import os

csv = "<file_path>"

def bin_type_selector():

    autostore_bin_type = input("Input the Bin type: \n") # can make this into an automation type selector so GEEK and t-Sort can be included

    autoStore_bin_size = [3]
    
    unit_type = input("What units: ")

    match autostore_bin_type:
        case "220":
            autoStore_bin_size = 220,400,600
        case "330":
         autoStore_bin_size = 330,400,600
        case "425":
            autoStore_bin_size = 425,400,600
        case _:
            print("no bins type selected")

    match unit_type:
        case "mm":
            print("is mm")
        case "cm":
            t = autoStore_bin_size
            t2 = tuple(t/10 for ti in t)
            autoStore_bin_size = t2
            print("is cm")

        case "m":
            autoStore_bin_size /1000 , print('is m')

    

    print(autoStore_bin_size)
