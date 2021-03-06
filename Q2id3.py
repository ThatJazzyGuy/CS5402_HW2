from id3 import Id3Estimator, export_text
import numpy as np


def main():
    feature_names = ["outlook",
                 "temperature",
                 "humidity",
                 "windy"]

    X = np.array([['sunny', 'hot', 'high', 'false'],
            ['sunny', 'hot', 'high', 'true'],
            ['overcast', 'hot', 'high', 'false'],
            ['rainy', 'mild', 'high', 'false'],
            ['rainy', 'cool', 'normal', 'false'],
            ['rainy', 'cool', 'normal', 'true'],
            ['overcast', 'cool', 'normal', 'true'],
            ['sunny', 'mild', 'high', 'false'],
            ['sunny', 'cool', 'normal', 'false'],
            ['rainy', 'mild', 'normal', 'false'],
            ['sunny', 'mild', 'normal', 'true'],
            ['overcast', 'mild', 'high', 'true'],
            ['overcast', 'hot', 'normal', 'false'],
            ['rainy', 'mild', 'high', 'true']])

    y = np.array(["No",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No",
                  "Yes",
                  "No",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "Yes",
                  "No"])

    clf = Id3Estimator()
    clf.fit(X, y, check_input=True)
    print("Training:")
    print(export_text(clf.tree_, feature_names))
    print("Testing: rainy, hot, high, false")
    print(clf.predict([["rainy", "hot", "high", "false"]])) #Throws DeprecationWarning, ignore it

if __name__ == "__main__":
    main()