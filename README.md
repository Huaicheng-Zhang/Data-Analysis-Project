# Project Introduction
This challenge is aimed to explore the dataset, build a prediction model from it and then create a Python module that serves the model. There will be two main tasks:

1. A Jupyter Notebook containing all your experiments, analyzes, and results. In this notebook, you will perform all your visualizations, data normalizations, training and evaluation of your model.

2. A complete Python module ready to be used containing the model you trained. This module should contain usage instructions and a clear interface (generally speaking) to access your model.
# Data Summary
Kickstarter is one of the main online crowdfunding platforms in the world. This dataset contains more than 300,000 projects launched on the platform in 2018. The following columns are included in the file:
- ID
- name: name of the project
- category: project's category
- main_category: campaign's category
- currency: project's currency type
- deadline: project's deadline date
- goal: amount of fundraising goal
- launched: project's start date
- pledged: amount pledged by backers
- state: project's current state
- backers: amount of poeple that supported the project
- country: project's country
- usd pledged: amount pledged by backers converted to USD (conversion made by Kickstarter)
- usd_pledged_real: amount pledged by backers converted to USD (conversion made by fixer.io api)
- usd_goal_real: fundraising goal in USD
# Project Goal
The goal is to predict whether a project will be successful or not. It is entirely up to you which features you will use and which model. When it comes to performance metrics you should be able to say when the model is good enough. The purpose of this project is to evaluate how you handle an unknown dataset in a classification task and your ability to deliver the results.
# File List
Instructions.md —— Description and guideline of 'my_prediction' module  
Experiments.ipynb —— Analysis process of the project and related details   
Draft.ipynb —— Module instructions in Jupyter Notebook form   
