from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# Load the Iris dataset
iris = load_iris()

# Store the feature matrix (X) and response vector (y)
X = iris.data
y = iris.target

# Splitting X and y into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# Training the model on the training set
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = gnb.predict(X_test)

# Comparing actual response values (y_test) with predicted response values (y_pred)
accuracy = metrics.accuracy_score(y_test, y_pred) * 100
print("Gaussian Naive Bayes model accuracy (in %):", accuracy)
