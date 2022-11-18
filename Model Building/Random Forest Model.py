def randomForest (x_train, x_test, y_train, y_test): 
    rf = RandomForestClassifier() 
    rf.fit(x_train,y_train) 
    yPred = rf.predict(x_test) 
    print (***RandomForestClassifier****) 
    print('Confusion matrix') 
    print(confusion_matrix(y_test,yPred)) 
    print('Classification report')
    print(classification_report (y_test,yPred))