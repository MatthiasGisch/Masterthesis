
# Hilfsprogramm zum Berechnen der Qualitätskriterien

from sklearn.metrics import precision_score, accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.svm import SVC
import numpy as np

TEST = 1
VERBOSE = 0


def calculateTheQuality(ylabel, ypredicted):
    accuracy = accuracy_score(ylabel,ypredicted)
    precision = precision_score(ylabel, ypredicted,average="micro")

    conf_matrix = confusion_matrix(ylabel, ypredicted)
    num_classes = conf_matrix.shape[0]
    specificity = []
    for i in range(num_classes):
        tn = sum(conf_matrix[j, j] for j in range(num_classes) if j != i)
        fp = sum(conf_matrix[j, i] for j in range(num_classes) if j != i)
        if VERBOSE:
            print("Tn + fp:")
            print(tn)
            print(fp)
        specificity.append(tn / (tn + fp))
    specificity_global = np.sum(specificity)/num_classes

    F1_score = f1_score(ylabel, ypredicted,average="micro")

    if VERBOSE:
        print("accuracy: " + str(accuracy))
        
        print("precision: " + str(precision))
      
        print("specificity_global: " + str(specificity_global))
        
        print("F1_score: " + str(F1_score))
        





    return accuracy,precision,specificity_global,F1_score