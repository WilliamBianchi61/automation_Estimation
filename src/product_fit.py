import numpy as np
import pandas as pd
import math
import os

csv = "<file_path>"

def bin_type_selector():

    autostore_bin_type = input("Input the Bin type: \n") # can make this into an automation type selector so GEEK and t-Sort can be included

    autoStore_bin_size = [3]
    
    unit_type = input("What unit for calculation: ")
    #bin type switch
    match autostore_bin_type:
        case "220":
            autoStore_bin_size = [220,400,600]
        case "330":
            autoStore_bin_size = [330,400,600]
        case "425":
            autoStore_bin_size = [425,400,600]
        case"geek":
            autoStore_bin_size = [573,240,315]
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
    df = pd.read_csv("data/test_data.csv")
    

    bin_dims = autoStore_bin_size

    sorted_bin_dims = sorted(bin_dims)

    item_dims = df[['Height','Width','Length']].to_numpy
    item_dims.sort(axis=1)

    mask =(
        (item_dims[:, 0] <= sorted_bin_dims[0]) &
        (item_dims[:, 1] <= sorted_bin_dims[1]) &
        (item_dims[:, 2] <= sorted_bin_dims[2]))

    df_filtered = df[mask]

    return df_filtered


def bin_count(df_filtered):
    print(df_filtered)