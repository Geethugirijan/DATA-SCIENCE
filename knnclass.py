import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

data=pd.read_csv('iris.csv')
# print(data.head())
x=data.iloc[:,:4]
# print(x.head())
y=data.iloc[:,-1]
# print(y.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.20, random_state=38)
# print(x_train.head())
# print(x_test.head())
sc=StandardScaler()
sc.fit(x_train)
x_train=sc.transform(x_train)
x_test=sc.transform(x_test)
classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
# print(y_pred)
# print(y_test)
from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
print(cm)
print(ac)
new_flower = [[5.9, 3.1, 4.4, 3.2]]

# Convert to DataFrame to match feature names (avoids warning)
new_flower_df = pd.DataFrame(new_flower, columns=x.columns)

# Scale new input using the same scaler
new_flower_scaled = sc.transform(new_flower_df)

# Predict the species
predicted_class = classifier.predict(new_flower_scaled)
print("Predicted class for new flower:", predicted_class[0])