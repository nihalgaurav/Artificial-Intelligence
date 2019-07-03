# import warnings
# warnings.filterwarnings(action="ignore")
#
# import pandas
# import urllib.request
# import  numpy as np
#
# hname = ['sepal-length','sepal-width','petal-lenght','petal-width','class']
#
# webpath = urllib.request.urlopen("https://goo.gl/QnHW4g")
#
# dataframe = pandas.read_csv(webpath, names= hname)
#
# #print(dataframe)
# #print(type(dataframe))
# mat = np.array(dataframe)
# #print(mat)
# mat_ar = mat[:, 0:4:]
# #print(mat_ar)
# # # broadcasting
# # print("broadcasting :", "*"* 60)
# # print(mat_ar + 2)
# # print("shape = ", mat_ar.shape)
# #
# # print("mean = ", mat_ar.mean())
# # print("median = ", np.median(mat_ar))
# # print("std = ",mat_ar.std())
# #
# # print("mat_ar.sum() = ", mat_ar.sum())
# # print("mat_ar.std() = ", mat_ar.std())
# # print("mat_ar.mean() = ", mat_ar.mean())
# # print("mat_ar.max() = ", mat_ar.max())
# # print("mat_ar.min() = ", mat_ar.min())
# # print("mat_ar.size : ", mat_ar.size)
# # print("dimension = ", mat_ar.ndim)
# # print("  axis 0 mean = \n", mat_ar.sum(axis=0))
# # print("axis 1 mean = \n", mat_ar.sum(axis=1))
# #print("na.transpose() = \n",mat_ar.transpose())
# print(mat_ar.transpose().shape)
# a = mat_ar[:,0]
# b = mat_ar[:,1]
# c = mat_ar[:,2]
# d = mat_ar[:,3]
# #print(a)
# a_sort = a.argsort()
# for x in a_sort:
#     print(a[x],"    ",b[x],"   ",c[x],"    ",d[x])






