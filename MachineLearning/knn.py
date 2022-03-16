import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

data = pd.read_csv('data/weather.csv')
graph = sns.relplot(data=data, x="weather", y="temp",hue="outerwear")
plt.grid()

feature_weather = data["weather"].values
feature_temp = data["temp"].values
classes = data["outerwear"].values

weather_transformer = LabelEncoder().fit(feature_weather)
feature_weather = weather_transformer.transform(feature_weather)

features = np.array([feature_weather,feature_temp]).transpose()

class_labels = np.unique(data["outerwear"])

scaler = StandardScaler().fit(features)
features = scaler.transform(features)

feattrain, feattest, classtrain, classtest = train_test_split(features,classes,test_size=0.2)

model = KNeighborsClassifier(n_neighbors=2).fit(feattrain, classtrain)

classpred = model.predict(feattest)

print("Accuracy: ", accuracy_score(classtest, classpred))

cm = confusion_matrix(classtest, classpred, labels=class_labels)
cmd = ConfusionMatrixDisplay(cm,display_labels=class_labels)
cmd.plot()
plt.show()