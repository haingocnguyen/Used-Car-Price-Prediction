import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/makid/OneDrive - VietNam National University - HCM INTERNATIONAL UNIVERSITY/3rd Year/2nd Sem/Stati Method/archive/CarPrice_Assignment.xlsx'
df = pd.read_excel(file_path, sheet_name="CylinderNumber", header=0)

#Frequency Bar Graph
print("Frequency Bar Graph")
plt.bar(df.CylinderNumber, df.Frequency, width=0.4)
plt.xlabel("Cylinder Number")
plt.ylabel("Frequency")
plt.title("Bar Graph for Cars' Cylinder Number Frequency")
# plt.xticks(rotation=90)
plt.show()

#Relative Creation
df['Relative_Frequency'] = None
for i in range(7):
    df['Relative_Frequency'] = df['Frequency']/sum(df['Frequency'])
print("Relative Frequency Table")
print(df)

#Relative Frequency Bar Graph
print("Relative Frequency Bar graph")
plt.bar(df.CylinderNumber, df.Relative_Frequency, width = 0.4)
plt.xlabel("Cylinder Number")
plt.ylabel("Relative Frequency")
plt.title("Bar Graph for Cars' Cylinder Number Relative Frequency")
# plt.xticks(rotation=90)
plt.show()



