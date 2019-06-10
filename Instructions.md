# Welcome to use "my_prediction" module #

## Introduction

"My_prediction" is a machine learning prediction module based on Decision Tree and designed for predicting projects' state (successful/failed)
on Kickstarter platform.

There are two main functions "pred" and "pred_once" included in this Python module. You will learn how to use them quilckly through this instruction and apply them to prediction.

_Enjoy using it!_

## Running requirements

* Platform: Python 3 (version 3.7 recommended)
* Packages: numpy, pandas, sklearn and **my_prediction**

## Module guideline

### 1. Pred function

The function "Pred" is used for predicting projects' state with large amount of input data. So you can use it when your input data is saved in a csv file (or similar formats).

* __First step:__ import the packages we need and load the data set.


```python

import pandas as pd
from my_prediction import my_prediction

# load the file to python environment
data = pd.read_csv('put the location of your data file here')


```



* __Second step:__ use our module to implement the prediction.


```python

# predict and return the states with corresponding project ID
my_prediction.pred(data)



```



* __If you want to save the results for observation or analysis, type the following for the second step.__


```python

# output the results and save data in a csv file (choose 'True' for index if you want to display the labels)
prediction = my_prediction.pred(data)
prediction.to_csv("name for your saved file",index = False,sep = ',')

```


* __Now you may find your saved file in the same folder.__


#### Example:

```python

__In []: 

import pandas as pd
data = pd.read_csv('C:/Users/Desktop/task/data.csv')    # you can change the file reading path here
from my_prediction import my_prediction
my_prediction.pred(data)

```
```
__Out []:

 Brainstorming...
Prediction complete!

1000002330	failed
1000003930	failed
1000004038	failed
1000007540	failed
1000011046	failed
1000014025	successful
1000023410	successful
1000030581	failed
1000034518	failed
100004195	failed
100004721	failed
100005484	successful
1000055792	failed
1000056157	failed
1000057089	successful
...           ...
```
```python

__In []:

# use this code if you want to save the data
prediction = my_prediction.pred(data)
prediction.to_csv("test.csv",index = False,sep = ',')    # you may change the filename here


```




### 2. Pred_once function

If you only want to do prediction for once or several times, you can simply use function "Pred_once". Follow the instructions given and you will get the prediction you want.

* __First step:__ import the module we need and begin the prediction.

```python
from my_prediction import my_prediction
my_prediction.pred_once()

```


* __Second step:__ type in the required information (usd_pledged_real, usd_goal_real and backers) and get the result.

#### Example:

```python

__In []:

from my_prediction import my_prediction
my_prediction.pred_once()
```
```
__Out []:

Please type the amount pledged by backers converted to USD here ("usd_pledged_real"): 8000
Please type the fundraising goal in USD here ("usd_goal_real"): 6000
Please type the amount of poeple that backed the project here ("backers"): 200
usd_pledged_real: 8000.0 usd_goal_real: 6000.0 backers: 200.0
Check your input and press Enter to start prediction.
This project is likely to be: ['successful']

```


## Notes

* Don't forget to copy the whole "my_prediction" folder and put it together with your input data, because both the module and the trained machine learning model are included.


* If you want to see the detail of the module or make changes on it, you can find the "my_prediction.py" in "my_prediction" folder.


* You can find experiments and analysis related to this case in the notebook "experiments.ipynb".


* If you have questions about the module, feel free to contact me at hzhan723@uwo.ca or see more information in Python documentation ([Numpy](https://docs.scipy.org/doc/numpy-1.15.0/), [Pandas](https://pandas.pydata.org/pandas-docs/stable/) and [Sklearn](https://scikit-learn.org/stable/user_guide.html)).