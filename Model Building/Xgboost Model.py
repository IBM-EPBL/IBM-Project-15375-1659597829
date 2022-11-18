def xgboost(x_train, x_test, y_train, y_test):
xg = GradientBoostingClassifier() xg.fit(x_train,y_train)
yPred = xg.predict(x_test)
print(****Gradient BoostingClassifier****) print('Confusion matrix')
print(confusion_matrix(y_test,yPred)) print('Classification report')
print(classification_report (y_test, yPred))