# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:28:00 2020

@author: Shrita
"""

'''
AI steps common for all models
 # Select the model appropriate for the task
model = DecisionTreeClassifier()

# Train the model
model.fit(X=X_train, y=y_train)

# Generate predictions
prediction_results = model.predict(X=X_test) 

# Test the model
evaluate_predictions(y_true=y_test,
                     y_pred=prediction_results)
'''