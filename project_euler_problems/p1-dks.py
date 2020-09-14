from joblib import Parallel, delayed
import multiprocessing
from random import seed
from random import random
import pandas as pd
# seed random number generator
seed(1)
# generate random numbers between 0-1

# what are your inputs, and what operation do you want to
# perform on each input. For example...

og_names = ["John", "Michael", "Jim", "Cindy", "Jeff", "Ron"]

name_df = pd.DataFrame(columns=["Name","Name Length"])

inputs = og_names

def processInput(name):
    name_length = len(name)
    name_details_dict = {'Name': name,'Name Length': name_length}
    return name_details_dict

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(processInput)(name) for name in inputs)

final_df = pd.DataFrame(results)
print(final_df.head(2))


print(results)
