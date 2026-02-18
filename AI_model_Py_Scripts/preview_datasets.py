import pandas as pd

def preview(path, n=5):
    df = pd.read_csv(path)
    print('\n' + '='*40)
    print(f'Preview for: {path}')
    print('='*40)
    print('\nHead:')
    print(df.head(n).to_string(index=False))
    print('\nDescribe:')
    print(df.describe(include='all').to_string())

if __name__ == '__main__':
    preview('AI_model_Py_Scripts/fraud_detection_dataset.csv', n=5)
    preview('AI_model_Py_Scripts/refined_fraud_dataset.csv', n=5)
