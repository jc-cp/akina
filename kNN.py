# This file consists of a kNN classifier that matches the best scores to optimize the final recommendation.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
#from sklearn.neighbors import KNeighborsClassifier
#from sklearn.metrics import classification_report, confusion_matrix


class kNN:

    def read_data(self):
        # url = ## INSERT DATABASE FROM MONGO
        # dataset = pd.read_csv(url, names=names)
        # dataset.head()
        pass

    def process_data(self):
        # Split dataset in labels and data
        # X = dataset.iloc[:, :-1].values
        # y = dataset.iloc[:, 4].values
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
        pass

    def scaling(self):
        # scaler = StandardScaler()
        # scaler.fit(X_train)

        # X_train = scaler.transform(X_train)
        # X_test = scaler.transform(X_test)
        pass

    def classifier(self):
        # classifier = KNeighborsClassifier(n_neighbors=5)
        # classifier.fit(X_train, y_train)
        # y_pred = classifier.predict(X_test)
        pass

    def evaluation(self):
        # print(confusion_matrix(y_test, y_pred))
        # print(classification_report(y_test, y_pred))

        error = []

        # Calculating error for K values between 1 and 40
        # for i in range(1, 40):
        #    knn = KNeighborsClassifier(n_neighbors=i)
        #    knn.fit(X_train, y_train)
        #    pred_i = knn.predict(X_test)
        #    error.append(np.mean(pred_i != y_test))
        # plt.figure(figsize=(12, 6))
        # plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
        #         markerfacecolor='blue', markersize=10)
        # plt.title('Error Rate K Value')
        # plt.xlabel('K Value')
        # plt.ylabel('Mean Error')
        pass

    def run(self):
        pass