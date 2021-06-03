import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv("C://Users//Prasaadh//Desktop//Data Science//Models//Customer Curn Prediction Using Random Forest//Data//train.csv")

test = pd.read_csv("C://Users//Prasaadh//Desktop//Data Science//Models//Customer Curn Prediction Using Random Forest//Data//test.csv")

#HANDLING CATEGORICAL VARIABLES 

train.area_code = train.area_code.map({'area_code_415':415,'area_code_408':408,'area_code_510':510})
test.area_code = test.area_code.map({'area_code_415':415,'area_code_408':408,'area_code_510':510})

train = train.replace({'voice_mail_plan':{'yes':1,'no':0}})
test = test.replace({'voice_mail_plan':{'yes':1,'no':0}})

train = train.replace({'international_plan':{'yes':1,'no':0}})
test = test.replace({'international_plan':{'yes':1,'no':0}})

train = train.replace({'churn':{'yes':1,"no":0}})
test = test.replace({'churn':{'yes':1,"no":0}})

train.state = train.state.astype('category')
test.state = test.state.astype('category')


#Building a churn prediction model

X = train.drop(['state','churn'],axis = 1)
y = train['churn']

X.columns
train.columns

#Feature Scaling

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_std = scaler.fit_transform(X)

type(X_std)

df = pd.DataFrame(X_std, index = train.index, columns = train.columns[1:15])

df['state'] = train['state']
df['churn'] = train['churn']

df.head()

X_new = df.drop(['state','churn'],axis = 1)
y_new = df['churn']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X_new,y_new,test_size = 0.3,random_state = 42)

X_train.shape

y_train.shape

#Random Forest Regressor Model

from sklearn.ensemble import RandomForestRegressor
for_reg = RandomForestRegressor(random_state = 42)
for_reg.fit(X_train,y_train)

predict = for_reg.predict(X_test)

from sklearn.metrics import mean_squared_error,accuracy_score

print(predict)

accuracy_score(predict.round(),y_test)

mse = mean_squared_error(predict.round(),y_test)

rmse = np.sqrt(mse)
print(rmse)

#Fine-Tune Model

from sklearn.model_selection import GridSearchCV

param_grid = [{'n_estimators':[10,100,1000] ,'max_features':[2,4,6,8,16]}] 
print(param_grid)
grid_search = GridSearchCV(for_reg,param_grid,cv = 3,scoring = 'neg_mean_squared_error',return_train_score = True,n_jobs = 3)
grid_search.fit(X_train,y_train)
y_pred = grid_search.predict(X_test)
y_pred = y_pred.round()
score = accuracy_score(y_pred,y_test)
print( "Accuracys is"+" "+ str(score*100),"%")






