import numpy as np
import pandas as pd
import math
import os

csv = "<file_path>"

def bin_type_selector():

    autostore_bin_type = input("Input the Bin type: \n") # can make this into an automation type selector so GEEK and t-Sort can be included

    autoStore_bin_size = [3]
    
    unit_type = input("What units: ")
    #bin type switch
    match autostore_bin_type:
        case "220":
            autoStore_bin_size = [220,400,600]
        case "330":
            autoStore_bin_size = [330,400,600]
        case "425":
            autoStore_bin_size = [425,400,600]
        case _:
            print("no bins type selected")
    #bin type switch
    match unit_type:
        case "mm":
            print("is mm")
        case "cm":
            t = autoStore_bin_size
            autoStore_bin_size = [x/10 for x in autoStore_bin_size]
        case "m":
            t = autoStore_bin_size
            autoStore_bin_size = [x/1000 for x in autoStore_bin_size]  
            
        case _:
            print("no unit selected")
    
    
    return autoStore_bin_size

def unfit_product(autoStore_bin_size):
    sorted_list = autoStore_bin_size.sort(False)
    print(sorted_list)

    df_main = pd.read_csv("data/test_data.csv")
    df_main.dropna # drops any null or N/A values from
    
    df_unfit = pd.DataFrame(columns=df_main.columns)
    
    
    df_unfit = df_main.loc[df.height]







