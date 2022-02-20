# -*- coding: utf-8 -*-
"""SpamEmailClassfier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cmUdy13PJgz-RgxJTjOFpO0EVQ5eL5Kl

##Support Vector Machine

# ***Modules***
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('notebook')
sns.set_style('white')
from scipy.io import loadmat
from sklearn import svm

"""# Read The Data"""

data1 = loadmat('/content/spamTrain.mat')

"""# Read the data as x and y

"""

y1 = data1['y']
X1 = data1['X']
print(X1.shape)

"""# Print the x data"""

print(X1)

"""# Print Y Data"""

print(y1)

"""# Make instance then fit the model to the data"""

svc = svm.SVC()
svc.fit(X1, y1)

"""# Print the trainng accuracy"""

print(f"The Train model accuracy is {round(svc.score(X1, y1)*100,2)}%")

"""# Load the test data """

data2 = loadmat('/content/spamTest.mat')

"""# Get the x test and y test"""

y_test = data2['ytest']
X_test = data2['Xtest']

"""# Print the accuracy of the model on the test data"""

print(f"The Test model accuracy is {round(svc.score(X_test, y_test)*100,2)}%")

"""# Try to see any example and perdict it """

email1=np.array(X1[1500])
email1=np.expand_dims(email1,-1)
svc.predict(email1.T)