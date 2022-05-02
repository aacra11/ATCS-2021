import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

crimes = pd.read_csv('bostoncrime/crime.csv',encoding="latin1")
crimes = crimes.replace("",np.nan,inplace=True)
codes = pd.read_csv('bostoncrime/offense_codes.csv',encoding="latin1")
crimes.dropna(inplace=True)

def predict_crime(area,latitude,longitude,hour,dayofweek):
    feature_area = crimes["REPORTING_AREA"].astype(float).values
    feature_latitude = crimes["Lat"].values
    feature_longitude = crimes["Long"].values
    feature_hour = crimes["HOUR"].values
    feature_dayofweek = crimes["DAY_OF_WEEK"].values
    class_offense = crimes["OFFENSE_CODE_GROUP"].values

    day_transformer = LabelEncoder().fit(feature_dayofweek)
    feature_dayofweek = day_transformer.transform(feature_dayofweek)

    features = np.array([feature_area, feature_latitude, feature_longitude, feature_hour, feature_dayofweek]).transpose()

    class_labels = np.unique(crimes["OFFENSE_CODE"])

    scaler = StandardScaler().fit(features)
    features = scaler.transform(features)

    feattrain, feattest, classtrain, classtest = train_test_split(features, class_offense, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=2).fit(feattrain, classtrain)

    value = model.predict([area,latitude,longitude,hour,dayofweek])
    print(value)

    # print("Accuracy: ", accuracy_score(classtest, classpred))
    #
    # cm = confusion_matrix(classtest, classpred, labels=class_labels)
    # cmd = ConfusionMatrixDisplay(cm, display_labels=class_labels)
    # cmd.plot()


# def predict_crime(latitude, longitude, hour, dayofweek): # checking for redundancy of area with physical location

predict_crime(808,42.357,-71.14,13,"Sunday")