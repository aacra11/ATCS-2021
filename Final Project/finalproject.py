import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# https://www.topcoder.com/thrive/articles/python-for-image-recognition-opencv

data = pd.read_csv("data/sports.csv")
for i in range(len(data)):
    filepath = "data/"+data["filepaths"][i]
    