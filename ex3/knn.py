import pandas as pd
import numpy as np


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))




sime cha
def knn(train_data, test_point, k=3):
    distances = []
    for train_point in train_data:

        dist = euclidean_distance(test_point, train_point[:-1])

        distances.append((dist, train_point[-1]))
    distances.sort()

    k_nearest_species = [species for _, species in distances[:k]]

    prediction = max(set(k_nearest_species), key=k_nearest_species.count)
    return prediction


def main():

    data = pd.read_csv('./iris.csv').values

    np.random.shuffle(data)

    train_size = int(0.8 * len(data))
    train_data, test_data = data[:train_size], data[train_size:]

    print("Details of Test Data:")
    print("----------------------")
    for test_point in test_data:
        sepal_length, sepal_width, petal_length, petal_width, species = test_point
        print(f"Sepal Length: {sepal_length:.1f}, Sepal Width: {sepal_width:.1f}, Petal Length: {petal_length:.1f}, Petal Width: {petal_width:.1f}, Species: {species}")

    k = int(input("Enter the value of k (number of neighbors): "))

    sepal_length = float(input("Enter the sepal length: "))
    sepal_width = float(input("Enter the sepal width: "))
    petal_length = float(input("Enter the petal length: "))
    petal_width = float(input("Enter the petal width: "))

    test_point = np.array(
        [sepal_length, sepal_width, petal_length, petal_width])

    prediction = knn(train_data, test_point, k)

    print(f"The predicted species for the given flower is: {prediction}")


if __name__ == "__main__":
    main()
