import os
import logging
import copy
import random

import numpy as np
import pandas as pd
import pickle as pkl

from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

from help.helper import getSensorInformation
from data.preprocessingFunc import getValueColumnsNames


def calcPCA(df, components):
    columns = df.columns.tolist()
    columns = getValueColumnsNames(columns)

    y = df["Measurements"].values
    X = (df[columns].apply(pd.to_numeric)).values
    dfPCA = copy.deepcopy(df)

    # PCA berechnen
    try:
        pca = PCA(n_components=components)
        principalComponents = pca.fit_transform(X)
    except Exception as e:
        logging.exception("PCA could not be calculate:\n %s", e)
        return pd.DataFrame()

    # Datenframe erzeugen
    if components == 3:
        principalDf = pd.DataFrame(data=principalComponents, columns=["_component 1", "_component 2", "_component 3"],)
    else:
        principalDf = pd.DataFrame(data=principalComponents, columns=["_component 1", "_component 2"])

    dfPCA = pd.concat([dfPCA , principalDf], axis=1)
    dfPCA = dfPCA.drop(columns,axis=1)
    return dfPCA

def createPCA(inputFolder, sensor, profiles, components, exportFolder):
    sensorInformation = getSensorInformation(sensor)
    ai = sensorInformation["ai"]

    if(ai) != True:
        return

    if not os.path.exists(exportFolder):
        os.makedirs(exportFolder)

    try:
        files = os.listdir(inputFolder)
    except:
        files =[]

    if(len(profiles) ==0):
        for i in range(0, len(files)):
            try:
                df = pd.read_csv(inputFolder + files[i], header=0, index_col=None)
                df = copy.deepcopy(df).sort_values(["_time"])
                df.reset_index(inplace=True, drop=True)
                df.fillna(0, inplace=True)
            except Exception as e:
                logging.exception("Dataframe could not be read:\n %s", e)
                df =  pd.DataFrame()
            if(len(df)> 0):
                df =calcPCA(df, components)
                fileName = files[i].replace(".csv", "")
                file = exportFolder + fileName  + "_HP" + str(i) +".csv" 
                df.to_csv(file, mode="w", header=True, index=False)
    
    if(len(profiles) > 0):
        for i in range(0, len(profiles)):
            dfPCA = pd.DataFrame()
            file = profiles[i][0]
            underLineIndex = file.rfind("_")
            file = file[:underLineIndex]
            
            for j in range(0, len(profiles[i])):
                file2 = profiles[i][j]
                underLineIndex = file2.rfind("_")
                file = file + "_" + file2[underLineIndex + 1:]

                try:
                    df = pd.read_csv(inputFolder + file2 + ".csv" , header=0, index_col=None)
                    df = copy.deepcopy(df).sort_values(["_time"])
                    df.reset_index(inplace=True, drop=True)
                    df.fillna(0, inplace=True)
                except Exception as e:
                    logging.exception("Dataframe could not be read:\n %s", e)
                    df =  pd.DataFrame()
                if(len(df)> 0):
                    #dfPCA.loc[len(dfPCA):len(dfNew)+len(df)] = df
                    dfPCA = pd.concat([dfPCA, df], ignore_index=True, axis =0 )
                    #dfPCA.reset_index(inplace=True, drop=True)
            if(len(dfPCA)> 0):
                df =calcPCA(dfPCA, components)
                fileName = file.replace(".csv", "")
                file = exportFolder + fileName  + "_HP" + str(i) + ".csv" 
                df.to_csv(file, mode="w", header=True, index=False)
    return

def calcLDA(df, components):
    columns = df.columns.tolist()
    columns=getValueColumnsNames(columns)

    y = df["_substance"].values
    X = (df[columns].apply(pd.to_numeric)).values
    dfLDA = copy.deepcopy(df)

    # LDA berechnen
    try:
        lda = LinearDiscriminantAnalysis(n_components=components)
        X = lda.fit_transform(X, y)
    except Exception as e:
        logging.exception("LDA could not be calculate:\n %s", e)
        return pd.DataFrame()
    
    # Datenframe erzeugen
    if components == 3:
        principalDf = pd.DataFrame(data=X, columns=["_component 1", "_component 2", "_component 3"],)
    else:
        principalDf = pd.DataFrame(data=X, columns=["_component 1", "_component 2"])

    dfLDA = pd.concat([dfLDA , principalDf], axis=1)
    dfLDA = dfLDA.drop(columns,axis=1)
    return dfLDA

def createLDA(inputFolder, sensor, profiles, components, exportFolder):
    sensorInformation = getSensorInformation(sensor)
    ai = sensorInformation["ai"]

    if(ai) != True:
        return

    if not os.path.exists(exportFolder):
        os.makedirs(exportFolder)
    
    try:
        files = os.listdir(inputFolder)
    except:
        files =[]

    if(len(profiles) ==0):
        for i in range(0, len(files)):
            try:
                df = pd.read_csv(inputFolder + files[i], header=0, index_col=None)
                df = copy.deepcopy(df).sort_values(["_time"])
                df.reset_index(inplace=True, drop=True)
                df.fillna(0, inplace=True)
            except Exception as e:
                logging.exception("Dataframe could not be read:\n %s", e)
                df =  pd.DataFrame()
            if(len(df)> 0):
                df =calcLDA(df, components)
                fileName = files[i].replace(".csv", "")
                file = exportFolder + fileName  + "_HP" + str(i) +".csv" 
                df.to_csv(file, mode="w", header=True, index=False)
    
    if(len(profiles) > 0):
        for i in range(0, len(profiles)):
            dfLDA = pd.DataFrame()
            file = profiles[i][0]
            underLineIndex = file.rfind("_")
            file = file[:underLineIndex]
            
            for j in range(0, len(profiles[i])):
                file2 = profiles[i][j]
                underLineIndex = file2.rfind("_")
                file = file + "_" + file2[underLineIndex + 1:]

                try:
                    df = pd.read_csv(inputFolder + file2 + ".csv" , header=0, index_col=None)
                    df = copy.deepcopy(df).sort_values(["_time"])
                    df.reset_index(inplace=True, drop=True)
                    df.fillna(0, inplace=True)
                except Exception as e:
                    logging.exception("Dataframe could not be read:\n %s", e)
                    df =  pd.DataFrame()
                if(len(df)> 0):
                    #dfLDA.loc[len(dfLDA):len(dfLDA)+len(df)] = df
                    dfLDA = pd.concat([dfLDA, df], ignore_index=True, axis =0 )
                    #dfLDA.reset_index(inplace=True, drop=True)
            if(len(dfLDA)> 0):
                df =calcLDA(dfLDA, components)
                fileName = file.replace(".csv", "")
                file = exportFolder + fileName  + "_HP" + str(i) + ".csv" 
                df.to_csv(file, mode="w", header=True, index=False)
    return

def calcSVM(df, exportFolder , fileName):
    columns = df.columns.tolist()
    columns=getValueColumnsNames(columns)

    y = df["_substance"].values
    X = (df[columns].apply(pd.to_numeric)).values


    # 70% Trainingsdaten  30% Testdaten
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=109)

    # SVM durchführen
    try:
        model = SVC()
        clf = OneVsOneClassifier(model)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
    
    except Exception as e:
        logging.exception("LDA could not be calculate:\n %s", e)
        return

    acc_decision_svm = round(clf.score(X_test, y_test) * 100)
    sk_report = classification_report(digits=6, y_true=y_test, y_pred=y_pred, output_dict=True)

    # Ergebnisse speichern
    df_classification_report = pd.DataFrame(sk_report).transpose()

    text_file = open(exportFolder  + "report/"+ fileName +  ".html", "w")
    text_file.write(df_classification_report.to_html())
    text_file.close()

    print("Accuracy", acc_decision_svm)
    print(sk_report)
    f1score = f1_score(y_test, y_pred, average="weighted")
    pkl.dump(f1score, open(exportFolder + "f1/"+ fileName + ".pkl", "wb"),)
    print(f1score)
    pkl.dump(clf, open(exportFolder + "clf/"+ fileName + ".pkl", "wb"),)
    
    return

def createSVM(inputFolder, sensor, profiles, exportFolder):
    sensorInformation = getSensorInformation(sensor)
    ai = sensorInformation["ai"]
    profiles = []
    
    if(ai) != True:
        return

    if not os.path.exists(exportFolder):
        os.makedirs(exportFolder)
    if not os.path.exists(exportFolder + "report/"):
        os.makedirs(exportFolder + "report/")
    if not os.path.exists(exportFolder + "f1/"):
        os.makedirs(exportFolder + "f1/")
    if not os.path.exists(exportFolder + "clf/"):
        os.makedirs(exportFolder + "clf/")
    
    try:
        files = os.listdir(inputFolder)
    except:
        files =[]

    if(len(profiles) ==0):
        for i in range(0, len(files)):
            try:
                df = pd.read_csv(inputFolder + files[i], header=0, index_col=None)
                df = copy.deepcopy(df).sort_values(["_time"])
                df.reset_index(inplace=True, drop=True)
                #df.fillna(0, inplace=True)
            except Exception as e:
                logging.exception("Dataframe could not be read:\n %s", e)
                df =  pd.DataFrame()
            if(len(df)> 0):
                fileName = files[i].replace(".csv", "")
                calcSVM(df, exportFolder , fileName  + "_HP" + str(i))
    
    if(len(profiles) > 0):
        for i in range(0, len(profiles)):
            dfSVM = pd.DataFrame()
            file = profiles[i][0]
            underLineIndex = file.rfind("_")
            file = file[:underLineIndex]
            
            for j in range(0, len(profiles[i])):
                file2 = profiles[i][j]
                underLineIndex = file2.rfind("_")
                file = file + "_" + file2[underLineIndex + 1:]

                try:
                    df = pd.read_csv(inputFolder + file2 + ".csv" , header=0, index_col=None)
                    df = copy.deepcopy(df).sort_values(["_time"])
                    df.reset_index(inplace=True, drop=True)
                    #df.fillna(0, inplace=True)
                except Exception as e:
                    logging.exception("Dataframe could not be read:\n %s", e)
                    df =  pd.DataFrame()
                if(len(df)> 0):
                    #dfdfSVMLDA.loc[len(dfdfSVMLDA):len(dfdfSVMLDA)+len(df)] = df
                    dfdfSVMLDA = pd.concat([dfSVM, df],  axis =0 )
            if(len(dfSVM)> 0):
                fileName = file.replace(".csv", "")
                calcSVM(df, exportFolder , fileName  + "_HP" + str(i))
                
    return
