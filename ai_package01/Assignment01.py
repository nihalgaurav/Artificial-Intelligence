# knn- algorithum

import numpy as np
from operator import itemgetter
import csv, os
import  pandas as pd


class KNNClassifier(object):

    def __init__(self):
        self.training_features = None
        self.training_label = None
        self.test_feature = None
        self.elegantResult = 'most likely, {0} "{1}" is of type of "{2}".'


    def loadTrainigDtaFromWeb(self, file_path):
        tr_feature = []
        self.training_label = []
        reader = pd.read_csv(file_path)
        reader = np.array(reader)
        print(reader)
        print(type(reader))
        for row in reader:
            if row[4] != '?':
                tr_feature.append([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
                self.training_label.append(row[4])
            else:
                self.test_feature = np.array([float(row[0]), float(row[1]), float(row[2]), float(row[3])])
        print(self.training_features)
        if(len(tr_feature)>0):
            self.training_features = np.array(tr_feature)
            print("self.training_features : \n", self.training_features)
            print("self.training_label: \n",self.training_label)
            print("self.test_feature : \n", self.test_feature)

    def classifyTestData(self, test_data = None, k=0):
        print("classifyTestData : testData : ", test_data)
        if test_data is not None:
            self.test_feature = np.array(test_data, dtype=float)
        print("classifyTestData : self.test_features : ", self.test_feature)


        if self.test_feature is not None and self.training_features is not None and self.training_label is not None and k>0:

            print("classifyTestData says self.test_features : ", self.test_feature)
            print("self.training_features : \n", self.training_features)
            print("self.training_label", self.training_label)
            featureVectorSize = self.training_features.shape[0]
            print("featureVectorSize : ", featureVectorSize)
            tileOfTestData = np.tile(self.test_feature, (featureVectorSize, 1))
            print("after tileOfTestData :", tileOfTestData)
            diffmat = self.training_features - tileOfTestData
            print("diffmat : \n", diffmat)
            sqDiffMat = diffmat**2
            print("sqDiffMat : \n", sqDiffMat)
            sqDistance = sqDiffMat.sum(axis=1)
            print("row wise sum of sqDiffmat : ", sqDistance)
            distances = sqDistance ** .5
            print("distance (square root of distance : )", distances)
            sortedDistanceIndies = distances.argsort()
            print("sortedDistanceIndies : ", sortedDistanceIndies)
            print("self.training_label : ", self.training_label)
            classcount = {}
            for i in range(k):
               print("sortedDistanceIndices['i'] : ", sortedDistanceIndies[i])
               voteILabel = self.training_label[sortedDistanceIndies[i]]
               print("voteILabel : ", voteILabel)
               classcount[voteILabel] = classcount.get(voteILabel, 0) + 1
            # classCount = {"action " : 2, "romance" : 3}

            print("classCount : ", classcount)
            sortedClassCount = sorted(classcount.items(), key=itemgetter(1), reverse=True)

            print("sortedClassCount : ", sortedClassCount)
            print("sortedClassCount[0] : ", sortedClassCount[0])
            print("sortedClassCount[0][0]", sortedClassCount[0][0])
            return sortedClassCount[0][0]
        else:
            return "can't determine result for empty test-data"

def predictElementType():
    instance = KNNClassifier()
    instance.loadTrainigDtaFromWeb("https://goo.gl/QnHW4g")
    print("*"*80)
    my_test_data = [6.2, 2.7, 4.6, 1.8]
    classOfTestData = instance.classifyTestData(test_data=my_test_data, k=5)
    # classOfTestData = instance.classifyTestData(test_data=None, k=5)
    # print("predictMovieType ### classOfTestdata : ", classOfTestData)

    return instance.elegantResult.format('Element', str(instance.test_feature), classOfTestData)
if __name__ == '__main__':
    print(predictElementType())


