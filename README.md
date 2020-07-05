## Project Overview

The goal of this project is to create a model that estimate the price of a used car based on different features.

## Resources And References

Python Version: 3.8.3

Packages used: pandas, numpy, sklearn, matplotlib, seaborn, scipy, statsmodels and bs4 (versions are reference in the requirements.txt file)

Data Source: [True Car Website](https://www.truecar.com/)

## Data Collection

The data was collected using web scrapping using the beautiful soup library ([Link to the script](./scripts/data_collection.py)). 

The data only include the listings within 15 milles of Jersey City, New Jersey.

After collecting and parsing the html elements, the data was saved as [raw_data](./data/raw_data.csv)


## Data Preparation

The data was cleaned and formmatted by:
 - Splitting the car_name into 3 columns: make, model and year.
 - Removing the dollar sign and comma from the price.
 - Removing the comma and the word "milles" from millage.
 - Extracting only the city and state from location.
 - Dividing the history into 3 columns: accidents, owner and use.
 
Other transformations were applied like handling missing values and outliers.
 
[Cleaning Script](scripts/cleaning.py)


## Exploratory Data Analysis

In this step I analyzed the data to discover any pattern or correlation between the variables.

![Correlation Matrix](images/corrMatrix.png)

I also checked for the distribution of some of the variables and their relationship with the label (price).

![](./images/boxplot.png)


## Model Selection and Evaluation

The data was split into training and test set. The training set was preprocessed by encoding the categorical variables and then applying standard scaler.

4 different regression models were tested and their evaluation scores based on their prediction were compare using 10 fold cross validation. The 4 models are:
- Lineal regression
- Ridge regression
- Lasso regression
- Elastic regression
- Random Forest regressor

Of all the models, the Random Forest Regressor had the best evaluation score. A grid search was performed on this model to find the best parameters.

The model was then saved as a pkl file for further deployment.


## Model Deployment# Car_Price_Prediction
