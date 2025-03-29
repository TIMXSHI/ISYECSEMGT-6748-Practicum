import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


file_path = "Invoices_Mock_Data.csv"  
df = pd.read_csv(file_path)
print(df)

# df['Invoice Date'] = pd.to_datetime(df['Invoice Date'], errors='coerce')
# df.fillna({'True Value': 'Unknown'}, inplace=True)
# df.dropna(inplace=True)

# print(df)