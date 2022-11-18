from imblearn.combine import SMOTETomek
smote = SMOTETomek (0.90)
y = data['Loan_Status']
x = data.drop(columns=['Loan_Status'], axis=1)
x_bal,y_bal smote.fit_resample(x,y)
print(y.value_counts())
print(y_bal.value_counts())