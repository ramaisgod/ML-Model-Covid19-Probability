"""
Features:
(1) Average fever - continuous variable
(2) Body pain - binary(0/1) 
(3) Age - discrete
(4) Runny Nose
(5) Difficulty breathing  - categorical variable -1/0/1
(6) Travel History (0/1)

Labels:
Probability of covid-19 infection
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle


def split_data(data, ratio):
    np.random.seed(0) # to seed reset (every time), the same set of numbers will appear every time.
    suffled_data = np.random.permutation(len(data))
    test_data_size = int(len(data) * ratio)
    test_indices = suffled_data[:test_data_size]
    train_indices = suffled_data[test_data_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


if __name__ == "__main__":
    # Data Reading
    df = pd.read_csv("data.csv")
    train, test = split_data(df, 0.2) # here ratio is 20%
    # collect features of train and test data
    x_train = train[['fever', 'body_pain', 'age', 'runny_nose', 'diff_breathing', 'travel_history']].to_numpy()
    x_test = test[['fever', 'body_pain', 'age', 'runny_nose', 'diff_breathing', 'travel_history']].to_numpy()
    # collect labels of train and test data
    y_train = train[['infection_prob']].to_numpy().reshape(len(train), )
    y_test = test[['infection_prob']].to_numpy().reshape(len(test), )
    clf = LogisticRegression()
    clf.fit(X=x_train, y=y_train)
    # Open a file to store train data
    file = open("model.pkl", "wb")
    pickle.dump(clf, file)
    file.close()
    
