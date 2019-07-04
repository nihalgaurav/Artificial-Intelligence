import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model

import warnings
warnings.filterwarnings(action='ignore')


# function to get data
def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    print(dataframe)
    x_parameters = []
    y_parameters = []
    for single_square_feet, single_price_value in zip(
        dataframe['square_feet'], dataframe['price'] ):

        x_parameters.append([float(single_square_feet)])
        y_parameters.append(float(single_price_value))
    return x_parameters, y_parameters

# function for fitting data to linear model
def linear_model_main(x_parameters, y_parameters, quest_value):
    # create linear regression object
    regr = linear_model.LinearRegression()
    print("AREA : ", x_parameters)
    print("PRICE : ", y_parameters)
    regr.fit(x_parameters, y_parameters)
    predicted_ans = regr.predict([[quest_value]])
    predections = {}
    predections['coefficient'] = regr.coef_
    predections['intercept'] = regr.intercept_
    predections['predicted_ans'] = predicted_ans

    print('Output from machine = ', predicted_ans)

    plt.scatter(x_parameters, y_parameters, color='m', marker='o', s=30)
    all_predict_y = regr.predict(x_parameters)
    plt.scatter(x_parameters, all_predict_y, color='r')
    plt.plot(x_parameters, all_predict_y, color='r')
    plt.scatter(question_value, predicted_ans, color='g')
    plt.show()
    return predections


if __name__ == "__main__":
    x,y = get_data('LR_House_price.csv')
    question_value = 700
    result = linear_model_main(x, y, question_value)
    print('Intercept value ', result['intercept'])
    print('coefficient : ', result['coefficient'])
    print('predicted Hose Price value : ', result['predicted_ans'])


