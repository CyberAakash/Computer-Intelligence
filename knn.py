import pandas as pd
import numpy as np
from collections import Counter

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def knn_classify(X_train, y_train, X_new, k):
    y_pred = []
    for x in X_new:
        # Calculate distances from the current point to all points in the training set
        distances = [euclidean_distance(x, x_train) for x_train in X_train]
        
        # Get the indices of the k-nearest neighbors
        k_nearest_indices = np.argsort(distances)[:k]
        
        # Get the labels of the k-nearest neighbors
        k_nearest_labels = [y_train[i] for i in k_nearest_indices]
        
        # Predict the class by majority vote
        majority_vote = Counter(k_nearest_labels).most_common(1)[0][0]
        y_pred.append(majority_vote)
        
    return y_pred

def main():
    # Load data from CSV file
    filename = "Documents/Mepco/Lab/Computer Intelligence/data.csv"
    data = pd.read_csv(filename)
    
    # Assuming the last column contains the target labels and the rest are features
    X = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    
    # Splitting data into training and testing sets (you can use other methods like cross-validation)
    split_ratio = 0.8
    num_train_samples = int(len(data) * split_ratio)
    X_train, X_test = X[:num_train_samples], X[num_train_samples:]
    y_train, y_test = y[:num_train_samples], y[num_train_samples:]
    
    # Choose the value of k (number of neighbors)
    k = 5
    
    # Example usage of knn_classify to predict classes for the test set
    y_pred = knn_classify(X_train, y_train, X_test, k)
    
    # Calculate accuracy (for classification tasks)
    accuracy = np.mean(y_pred == y_test)
    print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
