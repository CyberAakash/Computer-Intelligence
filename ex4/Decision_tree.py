import pandas as pd
import numpy as np

class DecisionTree:
    def __init__(self):
        self.root = None

    def fit(self, X, y):
        self.root = self._build_tree(X, y)

    def _build_tree(self, X, y):
        if len(np.unique(y)) == 1:
            return np.unique(y)[0]

        best_feature = self._find_best_split(X, y)
        return best_feature

    def _find_best_split(self, X, y):
        best_feature = None
        min_entropy = float('inf')

        for feature in range(X.shape[1]):
            entropy = self._calculate_entropy(X[:, feature], y)
            if entropy < min_entropy:
                min_entropy = entropy
                best_feature = feature
        return best_feature

    def _calculate_entropy(self, feature_column, labels):
        unique_values = np.unique(feature_column)
        entropy = 0

        for value in unique_values:
            value_indices = feature_column == value
            p_value = np.sum(value_indices) / len(labels)
            value_labels = labels[value_indices]
            unique_value_labels, counts = np.unique(value_labels, return_counts=True)
            p_label = counts / len(value_labels)
            entropy -= p_value * np.sum(p_label * np.log2(p_label + 1e-10))
        print(entropy)
        return entropy

    def get_root_node(self):
        return self.root

def main():
    csv_file_path = input("Enter the path to the CSV file: ")
    df = pd.read_csv(csv_file_path)
    column_names = df.columns[:-1]
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    model = DecisionTree()
    model.fit(X, y)
    root_node = model.get_root_node()
    if root_node is not None and root_node < len(column_names):
        root_column = column_names[root_node]
        print("Root Node:", root_column)
    else:
        print("Invalid root node or column name not found.")

if __name__ == "__main__":
    main()
