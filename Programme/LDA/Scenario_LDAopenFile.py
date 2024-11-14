#!/usr/bin/python3

#Measuring and Assessing the Resource- and Energy Efficiency of AIoT-Devices and Algorithms - Replication package

#Copyright (C) 2022 Achim Guldner, Julien Murach

#

#This program is free software: you can redistribute it and/or modify

#it under the terms of the GNU General Public License as published by

#the Free Software Foundation, either version 3 of the License, or

#(at your option) any later version.

#

#This program is distributed in the hope that it will be useful,

#but WITHOUT ANY WARRANTY; without even the implied warranty of

#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the

#GNU General Public License for more details.

#

#You should have received a copy of the GNU General Public License

#along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

import os, time
from datetime import datetime

import matplotlib.pyplot as plt

import tensorflow 

#from tensorflow import keras
from keras import initializers


##########   Für die LDA nötigen Importe
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


##########   Allgemeine Importe
import pandas as pd

from sklearn.model_selection import train_test_split  # Trennung der Daten in Trainings- und Testdaten
from sklearn.svm import SVC # import der suppoert-vector-machine

import random

import calculateTheQuality as cQ

from sklearn.linear_model import LogisticRegression

# *********************  Steuerparameter  ******************************  
VERBOSE = 1

print("sysargv:")
print(sys.argv[1][:])
filename = sys.argv[1][:]
#for row in sys.argv:
#    print(row)
df = pd.read_csv(filename)
lengthFileName = len(filename)
firstpart = filename[0:(lengthFileName-4)]
finalName = firstpart[10:]
print(finalName)


filename = "ActionLog_LDA_" + str(finalName) + ".txt"

scores = "Score_LDA_" + str(finalName) + ".txt"

scoresLogReg = "Score_LDA_LogReg_" + str(finalName) + ".txt"


numpy_array = df.to_numpy()
label = numpy_array[:,-1]
for element in label:
    element = int(element)

data = numpy_array[:,:-1]

iterations = 1


for counter in range(iterations):
    
    # **********************  setze Zufallszahl    ************************
    randomNumber = random.randint(1,100)

    if VERBOSE:

        print("Start")

    os.system("sudo sync")

    os.system("sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'")
   

    with open(filename,"a") as f:

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";startTestrun\n")

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";startAction;preprocessing\n")

        f.close()
         

        X = data
        y = label
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=randomNumber)

        

        

    

  

    with open(filename,"a") as f:

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";stopAction\n")

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";startAction;LDA transformation\n")
        f.close()
        # Daten transformieren und trennen

        LDA = LinearDiscriminantAnalysis(n_components=2)
        #Trainingsdaten fitten
        if VERBOSE: 
            print("Trainingsdaten fitten und transformieren - LDA")
        X_train_LDA = LDA.fit_transform(X_train, y_train)
        #testdaten transformieren
        X_test_LDA = LDA.transform(X_test)

    # --------------------------------------------------------------- SVM Start
    if int(finalName) < 1000000:
         
	    with open(filename,"a") as f:

             f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

             f.write(";stopAction\n")

             f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

             f.write(";startAction;LDA-SVM validation\n")

             f.close()

            
             #svm initialisieren
             svm_model_LDA = SVC()
             #svm fitten
             if VERBOSE: 
                print("SVM fitten")
                svm_model_LDA.fit(X_train_LDA,y_train)
                #Vorhersage treffen
             if VERBOSE: 
                print("Vorhersage SVM treffen")
                y_pred_train_LDA = svm_model_LDA.predict(X_train_LDA)#Vorhersage Trainingsdaten
                y_pred_test_LDA = svm_model_LDA.predict(X_test_LDA)#Vorhersage Testdaten


    # --------------------------------------------------------------- logistische Regression Start

    with open(filename,"a") as f:

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";stopAction\n")

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";startAction;LDA-LogReg validation\n")

        f.close()

        
        #svm initialisieren
        logReg_model_LDA = LogisticRegression(random_state=0).fit(X_train, y_train)
        #svm fitten
        if VERBOSE: 
            print("LogReg fitten")
        logReg_model_LDA.fit(X_train_LDA,y_train)
        #Vorhersage treffen
        if VERBOSE: 
            print("Vorhersage LogReg treffen")
        y_pred_logReg_train_LDA = logReg_model_LDA.predict(X_train_LDA)#Vorhersage Trainingsdaten
        y_pred_logReg_test_LDA = logReg_model_LDA.predict(X_test_LDA)#Vorhersage Testdaten


    with open(filename,"a") as f:

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";stopAction\n")

        f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        f.write(";stopTestrun\n")

        f.close()

    # --------------------------------------------------------------- LogReg Scores Start
        
    
    with open(scores,"a") as g:

        g.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

        g.write(", ")

        g.write(str(counter))

        g.write(": ")

        
        #Qualität berechnen
        accuracy_LogReg_train,precision_LogReg_train,specificity_LogReg_global_train,F1_score_LogReg_train = cQ.calculateTheQuality(y_train, y_pred_logReg_train_LDA)

        if VERBOSE:
            print("*********   Calculated Quality - _LogReg:   *********")
            print("Verfahren: LDA")
            print("accuracy: " + str(accuracy_LogReg_train))
            print("precision: " + str(precision_LogReg_train))
            print("specificity: " + str(specificity_LogReg_global_train))
            print("F1 Score: " + str(F1_score_LogReg_train))

        accuracy_LogReg_test,precision_LogReg_test,specificity_LogReg_global_test,F1_score_LogReg_test = cQ.calculateTheQuality(y_test, y_pred_logReg_test_LDA)

        if VERBOSE:
            print("*********   Calculated Quality - _LogReg:   *********")
            print("Verfahren: LDA")
            print("accuracy: " + str(accuracy_LogReg_test))
            print("precision: " + str(precision_LogReg_test))
            print("specificity: " + str(specificity_LogReg_global_test))
            print("F1 Score: " + str(F1_score_LogReg_test))



        qualityString =  str(accuracy_LogReg_train) + "," + str(precision_LogReg_train) + "," + str(specificity_LogReg_global_train) + "," + str(F1_score_LogReg_train) +  "," + str(accuracy_LogReg_test) + "," + str(precision_LogReg_test) + "," + str(specificity_LogReg_global_test) + "," + str(F1_score_LogReg_test)

        g.write(qualityString)

        g.write("\n")


        g.close()

    # --------------------------------------------------------------- SVM Scores Start
        
    if int(finalName) < 1000000:
        
	    with open(scoresLogReg,"a") as g:

             g.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

             g.write(", ")

             g.write(str(counter))

             g.write(": ")

            
             #Qualität berechnen
             accuracy_SVM_train,precision_SVM_train,specificity_SVM_global_train,F1_score_SVM_train = cQ.calculateTheQuality(y_train, y_pred_train_LDA)

             if VERBOSE:
                print("*********   Calculated Quality - SVM:   *********")
                print("Verfahren: LDA")
                print("accuracy: " + str(accuracy_SVM_train))
                print("precision: " + str(precision_SVM_train))
                print("specificity: " + str(specificity_SVM_global_train))
                print("F1 Score: " + str(F1_score_SVM_train))

             accuracy_SVM_test,precision_SVM_test,specificity_SVM_global_test,F1_score_SVM_test = cQ.calculateTheQuality(y_test, y_pred_test_LDA)

             if VERBOSE:
                print("*********   Calculated Quality - SVM:   *********")
                print("Verfahren: LDA")
                print("accuracy: " + str(accuracy_SVM_test))
                print("precision: " + str(precision_SVM_test))
                print("specificity: " + str(specificity_SVM_global_test))
                print("F1 Score: " + str(F1_score_SVM_test))



             qualityString =  str(accuracy_SVM_train) + "," + str(precision_SVM_train) + "," + str(specificity_SVM_global_train) + "," + str(F1_score_SVM_train) +  "," + str(accuracy_SVM_test) + "," + str(precision_SVM_test) + "," + str(specificity_SVM_global_test) + "," + str(F1_score_SVM_test)

             g.write(qualityString)

             g.write("\n")


             g.close()

    color={"red","green","blue","yellow","pink","black","purple"}

    # Plotting settings
    fig, ax = plt.subplots(figsize=(4, 3))
    x_min, x_max, y_min, y_max = -200, 200, -200, 200
    ax.set(xlim=(x_min, x_max), ylim=(y_min, y_max))

    scatter = ax.scatter(X_train_LDA[:, 0], X_train_LDA[:, 1], s=60, c=y_train, label=y, edgecolors="k")
    ax.legend(*scatter.legend_elements(), loc="upper right", title="Classes")
    ax.set_title("LDA")
    _ = plt.show()
