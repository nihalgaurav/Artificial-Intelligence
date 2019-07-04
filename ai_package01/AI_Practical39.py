import numpy as np
import matplotlib.pyplot as plt


def estimate_coef(x, y):
    # numbers of observation/point
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # cal. cross deviation
    ss_xy = np.sum(x*y) - n* m_x * m_y
    ss_xx = np.sum(x*x) - n* m_x * m_x

    # cal regression coefficient
    m = ss_xy / ss_xx
    c = m_y - m * m_x
    return [m,c]


def plot_regression_line(x, y, b):
    # plotting the actual point as scatter plot
    plt.scatter(x, y, color='m', marker='o', s=30)

    # predict response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.scatter(x, y_pred, edgecolors='g')
    plt.plot(x, y_pred, color='b')

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    # function to show plot
    plt.show()


def main():
    # observation
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    # estmi. coffie
    m, c = estimate_coef(x,y)  # sender value
    print("estimated coefficients : \n")
    print("slope m = ", m)
    print("y-intercept c = ", c)

    # plotting regression line
    plot_regression_line(x, y, [c, m])


if __name__=='__main__':
    main()





