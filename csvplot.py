import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

args = sys.argv
plt.style.use('ggplot') 

#url = args[1]
url = "bzip2_train.csv"
df = pd.read_csv(url,index_col=0, sep=';')
col = df.columns

df.plot(y=col[:4],figsize=(20,15),subplots=True,linestyle="none",marker="o",markersize=2,color="blue")
df.plot(y=col[4:-1],figsize=(20,15),subplots=True,linestyle="none",marker="o",markersize=2,color="blue")
plt.rcParams["font.size"] = 25
plt.show()
#plt.savefig('bzip2_performance.png')
