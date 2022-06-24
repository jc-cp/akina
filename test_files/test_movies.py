# Test file to check a basic recommendation engine with some requests.#

import pandas as pd
import numpy as np
from ast import literal_eval
import os

print(os.getcwd())
path_parent = os.path.dirname(os.getcwd())
print(path_parent)
os.chdir(path_parent)


df = pd.read_csv('test_data/movies_metadata.csv', low_memory=False)

# Select just relevant features
relevant_features = ['title','genres', 'release_date', 'runtime', 'vote_average', 'vote_count']
df = df[relevant_features]

# Print the dataframe
df.head()