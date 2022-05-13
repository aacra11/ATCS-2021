# Alexandre Acra
# Ms. Namasivayam
# AT CS, Block B
# May 12, 2022

# Credit: Used techniques/some code from class to help build KNN models

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# reading and cleaning data, cutting down for quicker run time
crimes = pd.read_csv('bostoncrime/crime.csv',encoding="latin1")
crimes = crimes[["REPORTING_AREA","Lat","Long","HOUR","DAY_OF_WEEK","OFFENSE_CODE"]]
crimes.replace(" ",np.nan,inplace=True)
codes = pd.read_csv('bostoncrime/offense_codes.csv',encoding="latin1")
crimes.dropna(inplace=True)
crimes = crimes.head(100)

def predict_crime_categorized(crimes):
    crimelist = ["DRUGS", "ROBBERY", "RAPE", "BURGLARY", "MURDER", "MANSLAUGHTER", "FRAUD", "LARCENY"] # broad categories of crimes
    crimes["category"] = " "
    for i in range(len(crimes)): # only keeping rows which fall into these broad categories
        code = crimes.iloc[i]["OFFENSE_CODE"]
        for j in range(len(codes)):
            if codes.iloc[j]["CODE"] == code:
                name = codes.iloc[j]["NAME"]
                for val in crimelist:
                    if val in name:
                        crimes.at[i, "category"] = val
    crimes.replace(" ", np.nan, inplace=True)
    crimes.dropna(inplace=True)

    # same KNN model from here on, just for predicting a smaller list of categories --> higher accuracy
    feature_area = crimes["REPORTING_AREA"].values
    feature_latitude = crimes["Lat"].values
    feature_longitude = crimes["Long"].values
    feature_hour = crimes["HOUR"].values
    feature_dayofweek = crimes["DAY_OF_WEEK"].values
    class_offense = crimes["category"].values

    day_transformer = LabelEncoder().fit(feature_dayofweek)
    feature_dayofweek = day_transformer.transform(feature_dayofweek)

    features = np.array([feature_area, feature_latitude, feature_longitude, feature_hour, feature_dayofweek]).transpose()

    scaler = StandardScaler().fit(features)
    features = scaler.transform(features)

    feattrain, feattest, classtrain, classtest = train_test_split(features, class_offense, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=int(np.sqrt(len(crimes["category"])))).fit(feattrain, classtrain)
    classpred = model.predict(feattest)

    print("Accuracy: ", accuracy_score(classtest, classpred))

def crimemap_categorized(crimes):
    # map of crimes by latitude and longitude, colored by category of crime
    crimelist = ["DRUGS", "ROBBERY", "RAPE", "BURGLARY", "MURDER", "MANSLAUGHTER", "FRAUD", "LARCENY"]
    crimes["category"] = " "
    for i in range(len(crimes)):
        code = crimes.iloc[i]["OFFENSE_CODE"]
        for j in range(len(codes)):
            if codes.iloc[j]["CODE"] == code:
                name = codes.iloc[j]["NAME"]
                for val in crimelist:
                    if val in name:
                        crimes.at[i, "category"] = val
    crimes.replace(" ", np.nan, inplace=True)
    crimes.dropna(inplace=True)

    crimes = crimes[crimes["Lat"] >= 42] #filtering bad data
    longitudes = crimes["Long"]
    latitudes = crimes["Lat"]

    colors = {"DRUGS":"green", "ROBBERY":"blue", "RAPE":"red", "BURGLARY":"yellow", "MURDER":"black", "MANSLAUGHTER":"pink", "FRAUD":"gray", "LARCENY":"purple"}

    plt.scatter(longitudes, latitudes, s=1, c=crimes['category'].map(colors))
    plt.show()


def crimemap(crimes):
    # map of crimes by latitude and longitude
    crimes = crimes[crimes["Lat"] >= 42] # filtering bad data
    longitudes = crimes["Long"]
    latitudes = crimes["Lat"]
    plt.scatter(longitudes,latitudes,s=0.05)
    plt.show()

def predict_crime(crimes):
    # KNN model predicting the type of crime committed based on various factors
    feature_area = crimes["REPORTING_AREA"].values
    feature_latitude = crimes["Lat"].values
    feature_longitude = crimes["Long"].values
    feature_hour = crimes["HOUR"].values
    feature_dayofweek = crimes["DAY_OF_WEEK"].values
    class_offense = crimes[["OFFENSE_CODE"]].values

    day_transformer = LabelEncoder().fit(feature_dayofweek)
    feature_dayofweek = day_transformer.transform(feature_dayofweek)

    features = np.array([feature_area, feature_latitude, feature_longitude, feature_hour, feature_dayofweek]).transpose()

    scaler = StandardScaler().fit(features)
    features = scaler.transform(features)

    feattrain, feattest, classtrain, classtest = train_test_split(features, class_offense, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=24).fit(feattrain, classtrain)
    classpred = model.predict(feattest)

    print("Accuracy: ", accuracy_score(classtest, classpred))


def predict_crime_user(crimes,area,latitude,longitude,hour,dayofweek):
    # predicting the crime code based on several factors input by user
    # similar to KNN from class; outputs a value based on parameters rather than finding accuracy
    feature_area = crimes["REPORTING_AREA"].values
    feature_latitude = crimes["Lat"].values
    feature_longitude = crimes["Long"].values
    feature_hour = crimes["HOUR"].values
    feature_dayofweek = crimes["DAY_OF_WEEK"].values
    class_offense = crimes[["OFFENSE_CODE"]].values

    day_transformer = LabelEncoder().fit(feature_dayofweek)
    feature_dayofweek = day_transformer.transform(feature_dayofweek)
    dayofweek = day_transformer.transform([dayofweek])[0]

    features = np.array([feature_area, feature_latitude, feature_longitude, feature_hour, feature_dayofweek]).transpose()

    scaler = StandardScaler().fit(features)
    features = scaler.transform(features)

    feattrain, feattest, classtrain, classtest = train_test_split(features, class_offense, test_size=0.2)

    model = KNeighborsClassifier(n_neighbors=2).fit(feattrain, classtrain)
    value = model.predict([[area,latitude,longitude,hour,dayofweek]])
    print(value)

# predict_crime(crimes)
# predict_crime_user(crimes,417,42.2827822,-71.098342,11,"Friday")
# predict_crime_categorized(crimes)
# crimemap(crimes)
crimemap_categorized(crimes)