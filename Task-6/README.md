Task – 6(A)
Aim: Explain five parameters used in Decision Tree.
•	Parameters of DecisionTreeClassifier():

o	The signature of DecisionTreeClassifier() is as follows:

```
class sklearn.tree.DecisionTreeClassifier

DecisionTreeClassifier(*, criterion='gini',
splitter='best',
max_depth=None,
min_samples_split=2,
min_samples_leaf=1,
min_weight_fraction_leaf=0.0,
max_features=None,
random_state=None,
max_leaf_nodes=None,
min_impurity_decrease=0.0,
min_impurity_split=None,
class_weight=None,
ccp_alpha=0.0)
```

1.	criterion: {‘gini’, ‘entropy’}: The function to measure the quality of a split. Supported criteria are “gini” for the Gini impurity and “entropy” for the information gain. (default = ‘gini’)
2.	splitter: {‘best’,’random’}: The strategy used to choose the split at each node. Supported strategies are “best” to choose the best split and “random” to choose the best random split. (default = ‘best’)
3.	max_depth: int: The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples. (default = None)
4.	minimum_weight_fraction_leaf: float: The minimum weighted fraction of the sum total of weights (of all the input samples) required to be at a leaf node. Samples have equal weight when sample_weight is not provided. (default = 0.0)
5.	random_state: {int, RandomState instance, None}: Controls the randomness of the estimator. The features are always randomly permuted at each split, even if splitter is set to "best". When max_features < n_features, the algorithm will select max_features at random at each split before finding the best split among them. But the best found split may vary across different runs, even if max_features=n_features. That is the case, if the improvement of the criterion is identical for several splits and one split has to be selected at random. To obtain a deterministic behaviour during fitting, random_state has to be fixed to an integer.

Task – 6(B)
Aim: Mention data cleaning methods and its working.
•	Data Cleaning Methodology:
o	Data Cleaning mainly consists of two stages:
1.	Error Identification
2.	Error Solving
o	Identification of anomalies is necessary for data cleaning.

•	Methods of Data Cleaning:

1)	Obtain and fill – out missing values: One of the first steps of fixing errors in your dataset is to find incomplete values and fill them out. Most of the data that you may have can be categorized. In such cases, it is best to fill out your missing values based on different categories or create entirely new categories to include the missing values. If your data are numerical, you can use mean and median to rectify the errors. You can also take an average based on different criteria, — namely age, geographical location, etc., among others.

2)	Removing rows with missing columns: One of the simplest things to do in data cleansing is to remove or delete rows with missing values. This may not be the ideal step in case of a huge amount of errors in your training data. If the missing values are considerably less, then removing or deleting missing values can be the right approach. You will have to be very sure that the data you are deleting does not include information that is present in the other rows of the training data. 

3)	Removing Outliers: Sometimes a dataset can contain extreme values that are outside the range of what is expected and unlike the other data. These are called outliers and often machine learning modeling and model skill in general can be improved by understanding and even removing these outliers. In general, if you have a legitimate reason to remove an outlier, it will help your model’s performance.

4)	Fixing errors in the structure: Ensure there are no typographical errors or inconsistency in the upper or lower case. Go through your data set, identify such errors, and solve them to make sure that your training set is completely error-free. This will help you to yield better results from your machine learning functions. 

5)	Removal of duplicate observations: Duplicate data arises in the phase of data collection and may affect the accuracy. It can be faced as a result of combining datasets from multiple places or data scraping. Remove duplicate categorization from your data list and streamline your data.

6)	Reducing data for proper data handling: A downsized dataset can help you generate results that are more accurate. There are different ways of reducing data in your dataset. Whatever data records you have, sample them and choose the relevant subset from that data. This method of data handling is called Record Sampling. Apart from this method, you can also use Attribute Sampling. When it comes to the attribute sampling, select a subset of the most important attributes from the dataset.

o	Task 4: Make a diagram explaining decision tree parameters with titanic dataset with equation.
	Gini impurity : Used by the CART (classification and regression tree) algorithm for classification trees, Gini impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled if it was randomly labeled according to the distribution of labels in the subset.
	Information Gain:  the expected information gain is the change in information entropy Η from a prior state to a state that takes some information as given:
 
	Measure of goodness : the measure of "goodness" is a function that seeks to optimize the balance of a candidate split's capacity to create pure children with its capacity to create equally-sized children. This process is repeated for each impure node until the tree is complete. 
	max_features: int, float, string or None, optional (default=None)
