import os
import time
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

CLEANED_DATA_PATH = "/shared/cleaned_data.csv"
MODEL_PATH = "/shared/model.pkl"

def wait_for_file(path, timeout=300):
    # Wait up to 300s for file to appear
    start = time.time()
    while not os.path.exists(path):
        if time.time() - start > timeout:
            raise TimeoutError("Timeout waiting for cleaned data.")
        time.sleep(5)
    return True

def main():
    print("Waiting for cleaned_data.csv...")
    wait_for_file(CLEANED_DATA_PATH)
    print("cleaned_data.csv found. Starting training.")

    df = pd.read_csv(CLEANED_DATA_PATH)
    # Assuming last column is target again for simplicity
    X = df.select_dtypes(include=[float, int]).iloc[:, :-1]
    y = df.iloc[:, -1]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved to model.pkl.")

if __name__ == "__main__":
    main()
