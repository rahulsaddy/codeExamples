"""
https://www.youtube.com/watch?v=ymOQLNnTBds

Roshan ML Regression
"""


import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

csv_data = pd.read_csv("data/temp_data_features.csv")

#Visualizing the data - Scatter chart
plt.figure(figsize=(20,5))
plt.scatter(x=csv_data["Year"], y=csv_data["Average"], marker="o", s=50, c=csv_data["Average"])
plt.plot(csv_data["Year"], csv_data["Average"], label="Annual Global Average Anomaly", alpha=0.4, linewidth=2, c="grey")
plt.hlines(0,min(csv_data["Year"])-3,max(csv_data["Year"])+5)

plt.legend(loc="best")
plt.xlim(min(csv_data["Year"])-3, max(csv_data["Year"])+5)
plt.ylabel(u"CRUTEM4 Temperature Anomaly (\u00B0C)")
plt.colorbar()
plt.grid()
plt.show()

#Visualizing the data - Bar chart
plt.figure(figsize=(20,5))
plt.bar(
    csv_data["Year"],
    csv_data["Average"],
    width=0.7,
    edgecolor="none",
    color=(csv_data["Average"]>0).map({True: 'r', False: 'b'}),
    label="Annual Average Global Anomaly",
    )
plt.hlines(0,min(csv_data["Year"])-3,max(csv_data["Year"])+5)
plt.legend(loc="best")
plt.xlim(min(csv_data["Year"])-3, max(csv_data["Year"])+5)
plt.ylabel(u"CRUTEM4 Temperature Anomaly (\u00B0C)")
plt.grid()
plt.show()

# Visualize Monthly data
# Prepare monthly data
monthly_temp = csv_data.drop("Year", 1).drop("Average", 1).drop("TSI", 1).drop("CO2", 1).drop("CH4", 1)
monthly_temp = pd.Series(np.ravel(monthly_temp)).dropna()
month_index = list((monthly_temp.index/12.) + 1851)

plt.figure(figsize=(15,8))
plt.scatter(
    x=month_index,
    y=monthly_temp,
    marker="o",
    label="Monthly Average Global Anomaly",
    c=monthly_temp,
    alpha=0.6
    )
plt.colorbar()
plt.legend(loc="lower right")
plt.xlim(min(month_index)-3,max(month_index)+5)
plt.ylim(min(monthly_temp),max(monthly_temp))
plt.ylabel(u"CRUTEM4 Temperature Anomaly (\u00B0C)")
plt.grid()
plt.show()



# LINEAR REGRESSION
annual_temp = csv_data["Average"]
annual_index = list(csv_data["Year"].values)
annual_index_feature = list(csv_data[["Year"]].values)
prediction_annual_index = [[item] for item in range(min(annual_index_feature),max(annual_index_feature)+10)]



# Predicting Annual Temperature
# Code source: Jaques Grobler
# License: BSD 3 clause

from sklearn import linear_model

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(annual_index_feature, annual_temp)

# The coefficients
print 'Coefficients:', regr.coef_
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(annual_index_feature) - annual_temp) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(annual_index_feature, annual_temp))

# Plot outputs
plt.figure(figsize=(20,5))
plt.bar(annual_index, annual_temp,  width=0.7, edgecolor="none", color=(annual_temp>0).map({True: 'r', False: 'b'}),
        label="Annual Average Global Anomaly", alpha=0.3)

plt.plot(prediction_annual_index[:], regr.predict(prediction_annual_index[:]), color='green',
        linewidth=3, alpha=1.0, label="Linear Regression")

plt.grid()
plt.xlim(np.min(annual_index_feature), np.max(annual_index_feature)+5)
plt.ylabel(u"CRUTEM4 Temperature Anomaly (\u00B0C)")
plt.legend(loc="best")
plt.show()


# Predicting Monthly Temperature
# Code source: Jaques Grobler
# License: BSD 3 clause
month_index_feature = [[item] for item in month_index]
prediction_month_index = [[item[0] + 5] for item in month_index_feature]

from sklearn import linear_model

regr = linear_model.LinearRegression()

# # The coefficients
print 'Coefficients:', regr.coef_
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(month_index_feature) - monthly_temp) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(month_index_feature, monthly_temp))

# Plot outputs
plt.figure(figsize=(20,5))
plt.bar(month_index, monthly_temp,  width=0.1, edgecolor="none", color=(monthly_temp>0).map({True: 'r', False: 'b'}),
        label="Monthly Average Global Anomaly", alpha=0.1)

plt.plot(month_index, regr.predict(month_index_feature), color='black',
        linewidth=3, alpha=0.5, label="Linear Regression")
plt.plot(prediction_month_index[-5*12:], regr.predict(prediction_month_index[-5*12:]), color='green',
        linewidth=3, alpha=1.0, label="Linear Regression Prediction")

plt.grid()
plt.xlim(np.min(month_index_feature), np.max(month_index_feature)+5)
plt.ylabel(u"CRUTEM4 Temperature Anomaly (\u00B0C)")
plt.legend(loc="best")
plt.show()Train the model using the training sets
regr.fit(month_index_feature, monthly_temp)


#SVM
from sklearn.svm import SVR

# Create linear regression object
regr_linear = SVR(kernel="linear")
regr_rbf_1 = SVR(kernel="rbf", C=100.0, gamma=0.004, epsilon=0.01)
regr_rbf_2 = SVR(kernel="rbf", C=10.0, gamma=0.0001, epsilon=0.01)
regr_rbf_3 = SVR(kernel="rbf", C=1.0, gamma=0.0002, epsilon=0.1)

# Train the model using the training sets
regr_linear.fit(annual_index_feature, annual_temp)
regr_rbf_1.fit(annual_index_feature, annual_temp)
regr_rbf_2.fit(annual_index_feature, annual_temp)
regr_rbf_3.fit(annual_index_feature, annual_temp)


# The coefficients
#print 'Coefficients:', regr.coef_
# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr_rbf_1.predict(annual_index_feature) - annual_temp) ** 2))
# Explained variance score: 1 is perfect prediction
print('score1: %.2f' % regr_rbf_1.score(annual_index_feature, annual_temp))
print('score2: %.2f' % regr_rbf_2.score(annual_index_feature, annual_temp))
print('score3: %.2f' % regr_rbf_3.score(annual_index_feature, annual_temp))

# Plot outputs
plt.figure(figsize=(20,5))
plt.bar(annual_index, annual_temp,  width=0.7, edgecolor="none", color=(annual_temp>0).map({True: 'r', False: 'b'}),
        label="Annual Average Global Anomaly", alpha=0.3)

plt.plot(prediction_annual_index[:], regr_linear.predict(prediction_annual_index[:]), color='green',
        linewidth=3, alpha=0.5, label="Linear Prediction")
plt.plot(prediction_annual_index[:], regr_rbf_1.predict(prediction_annual_index[:]), color='blue',
        linewidth=3, alpha=0.5, label="RBF1 Prediction")
plt.plot(prediction_annual_index[:], regr_rbf_2.predict(prediction_annual_index[:]), color='orange',
        linewidth=3, alpha=0.5, label="RBF2 Prediction")
plt.plot(prediction_annual_index[:], regr_rbf_3.predict(prediction_annual_index[:]), color='red',
        linewidth=3, alpha=0.5, label="RBF3 Prediction")

plt.grid()
plt.xlim(np.min(annual_index_feature), np.max(annual_index_feature)+10)
plt.xticks(np.arange(np.min(annual_index_feature), np.max(annual_index_feature)+10, 10))
plt.ylabel(u"CRUTEM4 Temperature Anomaly (\u00B0C)")
plt.legend(loc="best")
plt.show()


from sklearn.svm import SVR
from sklearn.grid_search import GridSearchCV

regr_rbf = SVR(kernel="rbf")
C = [100, 10, 1]
gamma = [0.005, 0.004, 0.003, 0.002, 0.001]
epsilon=[0.01]
parameters = {"C":C, "gamma":gamma, "epsilon":epsilon}

gs = GridSearchCV(regr_rbf, parameters, scoring="r2")

gs.fit(annual_index_feature, annual_temp)

print "Best Estimator:\n%s"  % gs.best_estimator_




