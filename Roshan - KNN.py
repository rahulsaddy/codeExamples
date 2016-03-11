
# Machine Learning 2 
# Implementing KNN 
# https://www.youtube.com/watch?v=7--b38oP5eg
#********************************************************************************
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
path = "data/adult.data"
columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "income"
    ]
csv_data = pd.read_csv(url, sep=", ", names=columns, nrows=20000)
csv_data.describe() # proc means

from pandas.tools.plotting import scatter_matrix
scatter_matrix(csv_data, alpha=0.05, figsize=(18, 18), diagonal='kde')
pass

plt.scatter(
    csv_data[csv_data['income']=='>50K']['education-num'],
    csv_data[csv_data['income']=='>50K']['age'],
    alpha=0.02,
    label='>50K',
    color='r'
    )

plt.scatter(
    csv_data[csv_data['income']=='<=50K']['education-num'],
    csv_data[csv_data['income']=='<=50K']['age'],
    alpha=0.02,
    label='<=50K',
    color='b'
    )

plt.legend()
plt.show()


# Making the chart above more pretty to look at
csv_data['education-num_rnd'] = csv_data['education-num'] + np.random.uniform(-0.5,0.5, len(csv_data))
plt.figure(figsize=(12,8))
plt.scatter(
    csv_data[csv_data['income']=='>50K']['education-num_rnd'],
    csv_data[csv_data['income']=='>50K']['age'],
    alpha=0.1,
    label='>50K',
    color='r'
    )

plt.scatter(
    csv_data[csv_data['income']=='<=50K']['education-num_rnd'],
    csv_data[csv_data['income']=='<=50K']['age'],
    alpha=0.1,
    label='<=50K',
    color='b'
    )

plt.xlabel('education-num')
plt.xticks(arange(17))
plt.xlim(0,17)
plt.ylabel('age')

#plt.legend()
plt.grid()
plt.title(u'From Census Data of 1994 (education-num \u00B10.5)')
plt.show()
csv_data = csv_data.drop('education-num_rnd', axis=1)


"""
Processing Text Feature
We have a lot of data that is not numerical. Most of machine learning algorithms use numerical data as features. We process text data according to what does the text represents. Commonly you will find:
None Organizable Categorical Text (City, Country, ...etc) 
Process it using Vectorizer. This finds each value and makes it into a separate feature. For example if you have three values for city where users live (London, New York, Toronto) it will make three features each indicating if the user lives in that city with with 0=False and 1=True.
Organizable Categorical Text (Rating, Income Brackets, ...etc) 
Convert to a series of numbers representing the value. For example (Excellence, Good, Average, Bad, Terrible) can be converted to (5,4,3,2,1).
Text Document 
Process it using CountVectorizer.
Special Values 
Email, URL, Phone number, Usernames process using Special Treatment."""

from sklearn.feature_extraction import DictVectorizer
vec = DictVectorizer()
features = vec.fit_transform(csv_data.dropna()\
                             .drop("capital-gain", axis=1)\
                             .drop("capital-loss", axis=1)\
                             .drop("income", axis=1)\
                             .drop("fnlwgt", axis=1).to_dict(outtype="records")).toarray()
results = csv_data["income"] == ">50K"

# Wenow split the data set into a traing and testing
# Develop cod eto do this at random
X_train = features[1000:]
Y_train = results[1000:]
X_test = features[:1000]
Y_test = results[:1000]

# Visualize one record
csv_data.to_dict(outtype="records")[8]


#Train Classification Model using kNN Algorithm
from  sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn = KNeighborsClassifier().fit(X_train, Y_train)

#Prediction
predictions = knn.predict(X_test)
accuracy = predictions == Y_test
print "Accuracy: %s%%" % (round(np.average(accuracy)* 100))

print "===============\nSamsple Data"
for counter in range(10):
    print "Prediction: %s is %s" % (predictions[counter], predictions[counter]==Y_test[counter])
	
#Improving Accuracy
target_names = ['<=50K', '>50K']
for kn in range(1,15):
    for method in ['uniform', 'distance']:
        knn = KNeighborsClassifier(n_neighbors=kn, weights=method).fit(X_train, Y_train)
        predictions = knn.predict(X_test)
        accuracy = predictions == Y_test
        print "Accuracy: %s%%, Neighbors: %s, Weights: %s" % (round(np.average(accuracy)* 100), kn, method)
        actual = pd.Series(Y_test).map({True: 1, False:0})
        predictions = pd.Series(predictions).map({True: 1, False:0})
        print(classification_report(actual.values, predictions.values, target_names=target_names))

#Inspecting Results
knn = KNeighborsClassifier(n_neighbors=11, weights='uniform').fit(X_train, Y_train)

predictions = knn.predict(X_test)

actual = pd.Series(Y_test).map({True: 1, False:0})
predictions = pd.Series(predictions).map({True: 1, False:0})
target_names = ['<=50K', '>50K']
print(classification_report(actual.values, predictions.values, target_names=target_names))

#Results
csv_data["prediction"] = pd.Series(predictions)	

#Quick Prediction
# Select values for a person to predict if They make more or less than 50K
person_features = {
 'age': 35,
 'education': 'Bachelors',
 'education-num': 14,
 'hours-per-week': 55,
 'marital-status': 'Never-married',
 'native-country': 'United-States',
 'occupation': 'Sales',
 'race': 'Black',
 'relationship': 'Not-in-family',
 'sex': 'Female',
 'workclass': 'Private'
}
person_features = vec.transform(person_features).toarray()

prediction = knn.predict(person_features)[0]

labels={True: '>50K', False: '<=50K'}

print labels[prediction]	

