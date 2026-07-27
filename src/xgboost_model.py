import os
import joblib
import xgboost as xgb
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def train_xgboost(
    X_train,
    y_train
):
    """
    Train an XGBoost classifier.
    """

    model = xgb.XGBClassifier(
        objective="multi:softmax",
        eval_metric="mlogloss",
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model


def predict(model, X_test):
    """
    Predict activities.
    """

    predictions = model.predict(X_test)

    return predictions


def evaluate_model(
    y_test,
    predictions
):
    """
    Calculate model accuracy.
    """

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return accuracy


def save_model(
    model,
    filename="models/xgboost_model.pkl"
):
    """
    Save trained model.
    """

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, filename)

    print(f"\nModel saved to {filename}")


def load_model(
    filename="models/xgboost_model.pkl"
):
    """
    Load saved model.
    """

    return joblib.load(filename)
def plot_feature_importance(model, feature_names):
    """
    Display Feature Importance Graph.
    """

    importance = model.feature_importances_

    plt.figure(figsize=(8, 5))

    plt.bar(feature_names, importance)

    plt.title("XGBoost Feature Importance")

    plt.xlabel("Features")

    plt.ylabel("Importance Score")

    plt.tight_layout()
    import os

    plt.tight_layout()


    os.makedirs("output", exist_ok=True)

    plt.savefig("output/feature_importance.png")

    plt.close()

    print("Feature Importance graph saved successfully!")