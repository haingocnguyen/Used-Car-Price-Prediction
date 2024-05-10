import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/makid/OneDrive - VietNam National University - HCM INTERNATIONAL UNIVERSITY/3rd Year/2nd Sem/Stati Method/archive/Used Car Dataset.xlsx'
df = pd.read_excel(file_path, sheet_name="Insurance Validity", header=0)

#Frequency Bar Graph
print("Frequency Bar Graph")
plt.bar(df.InsuranceValidity, df.Frequency, width=0.4)
plt.xlabel("Insurance Validity")
plt.ylabel("Frequency")
plt.title("Bar Graph for Used Car Insurance Validity")
plt.xticks(rotation=90)
plt.show()

#Relative Creation
df['Relative_Frequency'] = None
for i in range(5):
    df['Relative_Frequency'] = df['Frequency']/sum(df['Frequency'])
print("Relative Frequency Table")
print(df)

#Relative Frequency Bar Graph
print("Relative Frequency Bar graph")
plt.bar(df.InsuranceValidity, df.Relative_Frequency, width = 0.4)
plt.xlabel("Insurance Validity")
plt.ylabel("Relative Frequency")
plt.title("Bar Graph for Used Car Insurance Validity")
plt.xticks(rotation=90)
plt.show()

# #Pie Chart for Petrol type 
# df1 = pd.read_excel(file_path, sheet_name="Fuel Type", header=0)
# fig, ax = plt.subplots()
# ax.pie(df1['Frequency'], labels=df1['FuelType'], autopct='%1.1f%%')
# plt.title("Pie Chart for Used Cars' Fuel Types")
# plt.show()



