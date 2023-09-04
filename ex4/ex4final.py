import math
import pandas as pd

class DecisionTree:
    def calc_entropy(self, splits):
        total_count = sum(splits)
        if total_count == 0:
            return 0
        entropy = 0
        for split in splits:
            if split > 0:
                prob = split / total_count
                entropy -= prob * math.log2(prob)
        return round(entropy, 4)

    def info_gain(self, column, total_entropy):
        gain = 0
        for value in self.x_data[column].unique():
            subdata = self.data[self.x_data[column] == value]
            if self.y_data_dtype == 'object':
                entropy_splits = [sum(subdata[self.y_column].str.count(label)) for label in self.y_unique_labels]
            else:
                entropy_splits = [sum(subdata[self.y_column] == label) for label in self.y_unique_labels]

            print(f"Splits {entropy_splits}")

            if self.y_data_dtype == 'object':
                entropy = self.calc_entropy(entropy_splits)
            else:
                entropy = self.calc_entropy(entropy_splits)

            print(f"Entropy({value}) = {entropy}")

            gain += (len(subdata) / self.total_records) * entropy

        print(f"Total weighted entropy for {column} : {round(gain, 5)}")
        return round(total_entropy - gain, 5)

    def find_root(self, x_data, y_data):
        self.x_data = x_data
        self.y_data = y_data
        self.data = pd.concat([x_data, y_data], axis=1)
        self.total_records = len(x_data)
        self.y_column = y_data.columns[0]
        self.y_unique_labels = y_data[self.y_column].unique()
        self.y_data_dtype = y_data[self.y_column].dtype

        total_entropy_splits = [sum(y_data[self.y_column] == label) for label in self.y_unique_labels]
        total_entropy = self.calc_entropy(total_entropy_splits)

        print(f"Splits {total_entropy_splits}")
        print(f"Entropy(S) = {total_entropy}\n\n==================================\n")

        max_gain = -1
        root = None
        for column in x_data.columns:
            print(f"Feature = {column}\n")
            gain = self.info_gain(column, total_entropy)
            if gain > max_gain:
                max_gain = gain
                root = column
            print(f"\nInfo gain({column}) = {gain}\n\n==================================\n")

        print(f"Max gain = {max_gain}")
        return root

if __name__ == "__main__":
    filename = input("Enter the dataset filename: ")
    data = pd.read_csv(filename)
    x_data = data.iloc[:, 1:-1]
    y_data = data.iloc[:, -1:]
    model = DecisionTree()
    root_feature = model.find_root(x_data, y_data)
    print("Root feature =", root_feature)
