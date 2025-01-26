# ANN Exercise

## Description:
Construct, train and test an artificial neural network using a dataset of your own choice. Try different settings for two or more hyperparameters and investigate the effect on learning. Write a Jupyter notebook which contains your python code and in which you describe your approach and results. In your notebook, you should describe your dataset and add a reference to the source of your dataset. Also, include references to any source code or tutorials that you used to write your code. If your neural network is aimed at classification, you should create a confusion matrix and discuss the results. Also reflect on the knowledge and skills you acquired on artificial neural networks.

## Deliverable:
Jupyter notebook converted to HTML

## Feedback:
Heart failure prediction.

There is a relatively high negative correlation (-0.5) between time and the target variable DEATH_EVENT. What is the meaning of time? Should this be included in the feature set?

If you look at the correlation matrix you can see there is a large correlation (0.4) between smoking and sex. It may worthwhile to investigate this.

You say that there are barely any correlations. This is not true. The features age, ejection_fraction, serum_creatine, serum_sodium and time are all correlated to DEATH_EVENT. They all have correlation values +/- 0.2 or higher.

What do the confusion matrices tell you in terms of precision and recall?

You experimented with number of hidden layers.

A neural network may not be the most appropriate machine learning algorithm for this dataset. Did you try other algorithms? Think of a decision tree for example.

In general, I think you should apply some feature selection for this dataset (but that may be considered out of scope for this exercise).

Exercise completed.