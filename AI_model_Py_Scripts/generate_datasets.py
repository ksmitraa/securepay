import pandas as pd
import numpy as np

def generate_fraud_detection_dataset(n_samples=10000, seed=42, output_file="fraud_detection_dataset.csv"):
    np.random.seed(seed)
    data = {
        "Transaction Amount": np.random.exponential(scale=500, size=n_samples),
        "Transaction Frequency": np.random.poisson(lam=3, size=n_samples),
        "Recipient Verification Status": np.random.choice(
            ["verified", "recently_registered", "suspicious"], n_samples, p=[0.6, 0.3, 0.1]
        ),
        "Recipient Blacklist Status": np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        "Device Fingerprinting": np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        "VPN or Proxy Usage": np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        "Geo-Location Flags": np.random.choice(
            ["normal", "high-risk", "unusual"], n_samples, p=[0.7, 0.2, 0.1]
        ),
        "Behavioral Biometrics": np.random.normal(loc=0, scale=1, size=n_samples),
        "Time Since Last Transaction": np.random.uniform(0, 30, n_samples),
        "Social Trust Score": np.random.uniform(0, 100, n_samples),
        "Account Age": np.random.uniform(0, 5, n_samples),
        "High-Risk Transaction Times": np.random.choice([0, 1], n_samples, p=[0.75, 0.25]),
        "Past Fraudulent Behavior Flags": np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        "Location-Inconsistent Transactions": np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        "Normalized Transaction Amount": np.random.normal(loc=0.5, scale=0.2, size=n_samples),
        "Transaction Context Anomalies": np.random.normal(loc=0, scale=1, size=n_samples),
        "Fraud Complaints Count": np.random.poisson(lam=0.5, size=n_samples),
        "Merchant Category Mismatch": np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        "User Daily Limit Exceeded": np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
        "Recent High-Value Transaction Flags": np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
    }
    df = pd.DataFrame(data)

    def label_transaction(row):
        fraud_score = 0
        fraud_score += row["Recipient Blacklist Status"] * 3
        fraud_score += row["Device Fingerprinting"] * 2
        fraud_score += row["VPN or Proxy Usage"] * 2
        fraud_score += 1 if row["Geo-Location Flags"] == "high-risk" else 0
        fraud_score += row["Past Fraudulent Behavior Flags"] * 3
        fraud_score += row["Location-Inconsistent Transactions"] * 2
        fraud_score += row["Merchant Category Mismatch"] * 1.5
        fraud_score += row["User Daily Limit Exceeded"] * 1.5
        return 1 if fraud_score > 4 else 0

    df["Label"] = df.apply(label_transaction, axis=1)
    df.to_csv(output_file, index=False)
    print(f"Dataset saved to {output_file}")
    print(df["Label"].value_counts())


def generate_refined_fraud_dataset(n_samples=20000, fraud_ratio=0.5, seed=42, output_csv="refined_fraud_dataset.csv"):
    np.random.seed(seed)
    data = {
        "Transaction Amount": np.abs(np.random.exponential(scale=500, size=n_samples)),
        "Transaction Frequency": np.random.poisson(lam=3, size=n_samples),
        "Recipient Verification Status": np.random.choice(
            ["verified", "recently_registered", "suspicious"], n_samples, p=[0.7, 0.2, 0.1]
        ),
        "Recipient Blacklist Status": np.random.choice([0, 1], n_samples, p=[0.95, 0.05]),
        "Device Fingerprinting": np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        "VPN or Proxy Usage": np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        "Geo-Location Flags": np.random.choice(
            ["normal", "high-risk", "unusual"], n_samples, p=[0.8, 0.15, 0.05]
        ),
        "Behavioral Biometrics": np.abs(np.random.normal(loc=0, scale=1, size=n_samples)),
        "Time Since Last Transaction": np.random.uniform(0, 30, n_samples),
        "Social Trust Score": np.random.uniform(0, 100, n_samples),
        "Account Age": np.random.uniform(0, 5, n_samples),
        "High-Risk Transaction Times": np.random.choice([0, 1], n_samples, p=[0.8, 0.2]),
        "Past Fraudulent Behavior Flags": np.random.choice([0, 1], n_samples, p=[0.95, 0.05]),
        "Location-Inconsistent Transactions": np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        "Normalized Transaction Amount": np.abs(np.random.normal(loc=0.5, scale=0.2, size=n_samples)),
        "Transaction Context Anomalies": np.abs(np.random.normal(loc=0, scale=1, size=n_samples)),
        "Fraud Complaints Count": np.random.poisson(lam=0.5, size=n_samples),
        "Merchant Category Mismatch": np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        "User Daily Limit Exceeded": np.random.choice([0, 1], n_samples, p=[0.85, 0.15]),
        "Recent High-Value Transaction Flags": np.random.choice([0, 1], n_samples, p=[0.85, 0.15])
    }
    df = pd.DataFrame(data)
    caps = {"Transaction Amount": 5000, "Behavioral Biometrics": 3, "Time Since Last Transaction": 30}
    for feature, cap in caps.items():
        df[feature] = df[feature].clip(upper=cap)

    def label_transaction(row):
        fraud_score = 0
        fraud_score += row["Transaction Amount"] / 1000
        fraud_score += row["Recipient Blacklist Status"] * 2
        fraud_score += row["Past Fraudulent Behavior Flags"] * 2
        fraud_score += row["VPN or Proxy Usage"]
        fraud_score += 2 if row["Geo-Location Flags"] == "high-risk" else 0
        return 1 if fraud_score > 5 else 0

    df["Label"] = df.apply(label_transaction, axis=1)
    fraud_cases = df[df["Label"] == 1]
    non_fraud_cases = df[df["Label"] == 0]
    n_fraud = int(n_samples * fraud_ratio)
    n_non_fraud = n_samples - n_fraud
    fraud_cases = fraud_cases.sample(n=n_fraud, replace=True, random_state=seed)
    non_fraud_cases = non_fraud_cases.sample(n=n_non_fraud, replace=True, random_state=seed)
    balanced_df = pd.concat([fraud_cases, non_fraud_cases]).sample(frac=1, random_state=seed).reset_index(drop=True)
    balanced_df.to_csv(output_csv, index=False)
    print(f"Refined dataset saved to {output_csv}")
    return balanced_df


if __name__ == '__main__':
    generate_fraud_detection_dataset(n_samples=10000, output_file="AI_model_Py_Scripts/fraud_detection_dataset.csv")
    generate_refined_fraud_dataset(n_samples=20000, fraud_ratio=0.5, output_csv="AI_model_Py_Scripts/refined_fraud_dataset.csv")
