import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

# importing the dataset
dataset = pd.read_csv('fruit_sample.csv', delimiter='\t')
X = dataset.iloc[:, [3,4,5,6]].values
y = dataset.iloc[:, 0].values

# Creating the training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)

# Applying feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

# Creating the classifier
# Logistic regression
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression(random_state=0)
log_reg.fit(X_train, y_train)
lr_pred = log_reg.predict(X_test)
print('Prediction for Logistic reg is: ', lr_pred)

cm_lr = confusion_matrix(y_test, lr_pred)
acc_lr = accuracy_score(y_test, lr_pred)
print('Confusion matrix is: ', cm_lr)
print('Accuracy score is: ', acc_lr)

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
dr = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dr.fit(X_train, y_train)
dr_pred = dr.predict(X_test)
print('Prediction for Decision tree is:', dr_pred)

cm_dr = confusion_matrix(y_test, dr_pred)
acc_dr = accuracy_score(y_test, dr_pred)
print('Confusion matrix is: ', cm_dr)
print('Accuracy score is: ', acc_dr)

# KNN
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)
print('Prediction for KNN is:', knn_pred)

cm_knn = confusion_matrix(y_test, knn_pred)
acc_knn = accuracy_score(y_test, knn_pred)
print('Confusion matrix is: ', cm_knn)
print('Accuracy score is: ', acc_knn)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_train, y_train)
nb_pred = nb.predict(X_test)
print('Prediction for Naive Bayes is:', nb_pred)

cm_nb = confusion_matrix(y_test, nb_pred)
acc_nb = accuracy_score(y_test, nb_pred)
print('Confusion matrix is: ', cm_nb)
print('Accuracy score is: ', acc_nb)

# SVM
from sklearn.svm import SVC
svm= SVC(kernel = 'linear', random_state=0)
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)
print('Prediction for SVM is:', svm_pred)

cm_svm = confusion_matrix(y_test, svm_pred)
acc_svm = accuracy_score(y_test, svm_pred)
print('Confusion matrix is: ', cm_svm)
print('Accuracy score is: ', acc_svm)
