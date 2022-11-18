def KNN (x_train, x_test, y_train, y_test): 
    knn.fit(x_train,y_train) 
    yPred = knn.predict(x_test) 
    print (***KNeighborsClassifier***') 
    print('Confusion matrix') 
    print(confusion_matrix(y_test,yPred)) 
    print(classification_report(y_test,yPred))