# My_prediction: a Python module to predict the state of projects launched on Kickstater

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

# Prediction model for data saved in a file.
def pred(data):

	
	# remove the missing value or wrong entries
	data = data.dropna()

	# show the brief information of your input data
	print('Baisc information of your data:')
	data.info()

	# select the features we need for prediction
	x = data[[ 'usd_pledged_real', 'usd_goal_real', 'backers']].values
	

	# load our trained model from saved file
	clf = joblib.load('my_prediction/trained_model.m')

	# perform the prediction on given data
	print('\n Brainstorming...')
	prediction = clf.predict(x)
	print('Prediction complete!')

	# match each prediction state with its project ID
	num = data['ID'].values
	predictions = pd.DataFrame(prediction, num)
	

	return predictions


# Use this one for single prediction.
def pred_once():

	# First input required, check if it's a number
	usd_pledged_real = input('Please type the amount pledged by backers converted to USD here ("usd_pledged_real"): ')
	if usd_pledged_real.isdigit():
		usd_pledged_real = float(usd_pledged_real)
	else:
		print('Invalid input! Please restart and type number here.')
		return

	# Second input required, check if it's a number
	usd_goal_real = input('Please type the fundraising goal in USD here ("usd_goal_real"): ')
	if usd_goal_real.isdigit():
		usd_goal_real = float(usd_goal_real)
	else:
		print('Invalid input! Please restart and type number here.')
		return

	# Third input required, check if it's a number
	backers = input('Please type the amount of poeple that backed the project here ("backers"): ')
	if backers.isdigit():
		backers = float(backers)
	else:
		print('Invalid input! Please restart and type number here.')
		return


	print('usd_pledged_real:', usd_pledged_real, 'usd_goal_real:', usd_goal_real, 'backers:', backers)
	input('Check your input and press Enter to start the prediction.')
	
	# data for prediction
	x = [[usd_pledged_real, usd_goal_real, backers]]

	# load our trained model from saved file
	clf = joblib.load('my_prediction/trained_model.m')

	# perform the prediction on given data
	prediction = clf.predict(x)

	print('This project is likely to be:', prediction)



