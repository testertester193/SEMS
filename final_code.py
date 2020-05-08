


# Import following Libraries
import pandas as pd 										# Pandas for initial data cleaning and training model
import numpy as np 											# Numpy is used for putting data in array 
import matplotlib.pyplot as plt 							# To plot graph matloblib is used
from sklearn.model_selection import train_test_split    	# From training model the data is splitted into train and test set
from sklearn.linear_model import LinearRegression 			# Import LinearRegression Model
from sklearn.metrics import r2_score 						# To check the performance of model r2_score is used


# Importing data and clean it

dataset = pd.read_csv('HeatDemand3year.csv')				# read data from csv file
dataset.dropna												# Drop the row is data is missing
dataset = dataset[(dataset['Outdoor Temperature'] <= 20) & (dataset['DH'] <= 300)]
															# The data is processed in such away that initail condition of 
															# turning DH ON is removed because it works as outlier.
															# Also, it can be assumed that over 22 degree DH wont be required.

outdoor_temp = dataset['Outdoor Temperature'].values.reshape(-1,1)
															# Defining X and y varibale for Model 

# Spliting the Data in ratio of 80% Training and 20% testing.

X_train, X_test, y_train, y_test = train_test_split(outdoor_temp,dh, test_size=0.2, random_state=0)
															# Spliting the data set for training and than testing the output.

# Linearregression Model from Scikit Learn

Model = LinearRegression()									# Defining the Linear Regression model in our case direct model is used
Model.fit(X_train, y_train)									# Fitting the model with training dataset
Model.score(X_train, y_train)								# Check how data fits on the model

# Testing the Trained Model

y_pred4 = Model.predict(X_test)								# Predicting values of test dataset 
r2_score(y_test, y_pred4)									# Comparing test data with predicted data

# Plotting the result

plt.scatter(X_test, y_test,  color='blue')					# Scatter plot of test dataset
plt.plot(X_test, y_pred4, color='#3bfb00', linewidth=2)		# Plot the predicted line
plt.show()

# Importing the weather data

weather_station_prediction =np.array([1, 2, 3, 4, 5, 6,7, 8, 9]).reshape(-1,1)		
															# Predicted weather data from weather station is converted into array

# Forecasting based on the weather data

Forecast_DH = Model.predict(s)								# Forcasted value of DH




