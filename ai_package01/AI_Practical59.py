# knn- algorithum

import numpy as np
from operator import itemgetter
import csv, os


class KNNClassifier(object):

    def __init__(self):
        self.training_features = None
        self.training_label = None
        self.test_feature = None
        self.elegantResult = 'most likely, {0} "{1}" is of type of "{2}".'

    def loadTrainigDtaFromFile(self, file_path):
        if (file_path is not None) and (os.path.exists(file_path)):
            tr_feature = []
            self.training_label = []
            with open(file_path, 'r') as training_data_file:
                reader = csv.DictReader(training_data_file)
                for row in reader:
                    if row['moviename'] != '?':
                        tr_feature.append([float(row['kicks']), float(row['kisses']) ])
                        self.training_label.append(row['movietype'])
                    else:
                        self.test_feature = np.array([float(row['kicks']), float(row['kisses'])])
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


def predictMOvieType():
    instance = KNNClassifier()
    instance.loadTrainigDtaFromFile('LgR_Movies_kNN_classifier.csv')
    print("*"*80)
    my_test_data = [50,50]
    classOfTestData = instance.classifyTestData(test_data=my_test_data, k=5)
    # classOfTestData = instance.classifyTestData(test_data=None, k=5)
    # print("predictMovieType ### classOfTestdata : ", classOfTestData)

    return instance.elegantResult.format('movie', str(instance.test_feature), classOfTestData)


if __name__ == '__main__':
    print(predictMOvieType())


