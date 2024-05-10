import pandas as pd
# from sklearn.linear_model import LinearRegression 
import statsmodels.api as sm

file_path = 'C:/Users/makid/OneDrive - VietNam National University - HCM INTERNATIONAL UNIVERSITY/3rd Year/2nd Sem/Stati Method/archive/CarPrice_Assignment.xlsx'
df = pd.read_excel(file_path, sheet_name="CarPrice_Assignment", header=0)

#Find dummies from Insurance Validity
categori_col = ['enginesize']
dummies = pd.get_dummies(df[categori_col], prefix=categori_col)
dummies = dummies.astype(int)
df = pd.concat([df, dummies], axis=1)
df.drop(categori_col, axis=1, inplace=True)
print(df)

#Regression from dummy variables to Y - price
target_col = ['price']
x = dummies
y = df[target_col]
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())