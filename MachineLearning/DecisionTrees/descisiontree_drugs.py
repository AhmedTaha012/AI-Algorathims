# -*- coding: utf-8 -*-
"""DescisionTree-Drugs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jmPStdITM_YksNzv1iynA60bdq942D3r

##Import Used Modules
"""

import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

"""##Download The Patiens Data From Ibm Cloud"""

!wget -O drug200.csv https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/drug200.csv

"""##Read the data using pandas"""

data=pd.read_csv("drug200.csv")

"""##Print the first 5 rows of data """

data.head()

"""##More Information about the data"""

print(f"The data conatins :{data.shape[0]} rows ")
print(f"The data conatins :{data.shape[1]} colums ")
print(f"The data conatins :{len(list(data.columns))-1} features")
print(f"The Features in the data are :{list(data.iloc[:,:-1].columns)}")
print(f"The labels that data conatins is {set(data['Drug'])} there are {len(set(data['Drug']))} labels")

"""##Read the data into X and Y"""

x=data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
y=data['Drug'].values

"""##Show the first 5 rwos to know if it needs to encoding"""

print(data.iloc[:5])

"""The Sex ,BP and Cholesterol need to encodeing

Print what every one of the sex, BP,Cholesterol Contains to can encode them
"""

print(f"The Sex Colums contains{set(data['Sex'])}")
print(f"The Sex Colums contains{set(data['BP'])}")
print(f"The Sex Colums contains{set(data['Cholesterol'])}")

"""##Use the sklearn to preprocssing them """

from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
x[:,1] = le_sex.transform(x[:,1]) 


le_BP = preprocessing.LabelEncoder()
le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
x[:,2] = le_BP.transform(x[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
x[:,3] = le_Chol.transform(x[:,3]) 

x[0:5]

"""## Now we will divid the data to train and test"""

from sklearn.model_selection import train_test_split
X_trainset, X_testset, y_trainset, y_testset = train_test_split(x, y, test_size=0.3, random_state=3)

"""##The size of Train and test data """

print(f"The x Train shape is {X_trainset.shape}")
print(f"The y Train shape is {y_trainset.shape}")
print(f"The x Train shape is {X_testset.shape}")
print(f"The y Train shape is {y_testset.shape}")

"""--------------------------------------------------------
##NOW WE GO TO MODEL THE DATA

##**NOTE**
The Depth is the number of featuers -1
"""

drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree.fit(X_trainset,y_trainset)

"""Perdict the x test"""

predTree = drugTree.predict(X_testset)

"""##The module accuracy """

print("DecisionTrees's Accuracy: ", round(metrics.accuracy_score(y_testset, predTree)*100,2),"%")

"""##The Reuslt in Image """

# Commented out IPython magic to ensure Python compatibility.
from  io import StringIO
import pydotplus
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn import tree
# %matplotlib inline

dot_data = StringIO()
filename = "drugtree.png"
featureNames =data.columns[0:5]
out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img,interpolation='nearest')