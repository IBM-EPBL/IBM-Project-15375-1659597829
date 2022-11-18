from sklearn.model_selection import cross_val_score
# Random forest model is selected
rf = RandomForestClassifier()
rf.fit(x_train,y_train)
yPred rf.predict(x_test)
f1_score(yPred,y_test, average='weighted')
cv = cross_val_score(rf,x,y,cv=5)
np.mean(cv)
pickle.dump(model, open('rdf.pk1','wb'))