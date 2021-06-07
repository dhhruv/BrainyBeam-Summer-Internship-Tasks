## Task-5

### Task–5(A)

**Aim:** Clean data from csv file (train.csv).

-   Data cleaning : Data scientists spend a large amount of their time cleaning datasets and getting them down to a form with which they can work. In fact, a lot of data scientists argue that the initial steps of obtaining and cleaning data constitute 80% of the job.
Therefore, if you are just stepping into this field or planning to step into this field, it is important to be able to deal with messy data, whether that means missing values, inconsistent formatting, malformed records, or nonsensical outliers. We can clean the data using pandas and numpy.
-   We can do all below things using numpy and pandas.
    *   Dropping unnecessary columns in a DataFrame
    *   Changing the index of a DataFrame
    *   Using .str() methods to clean columns
    *   Using the DataFrame.applymap() function to clean the entire dataset, element-wise
    *   Renaming columns to a more recognizable set of labels
    *   Skipping unnecessary rows in a CSV file.


### Task–5(B)

**Aim:** Decision Tree Explanation.
-   Decision Tree:
    *   Decision tree is a predictive approach for modelling in statistics, data mining, and machine learning.
    *   It is mainly used for classification and regression.
    *   It is a non-parametric and supervised learning approach.
    *   Decision trees learn from data to approximate a sine curve with a set of if – then – else decision rule.
    *   The deeper the tree, the more complex the decision rules and the fitter the model is.

<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/120965573-b158e100-c782-11eb-91bd-03e5c1251654.png" />
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/120966756-4d371c80-c784-11eb-921d-df138c0dbb78.png" />
</p>


-   Terminologies of a decision tree:
    1.	Root Node: The node from which the decision tree starts is known as root node.
    2.	Leaf Node: Final output nodes are known as leaf nodes.
    3.	Splitting: The process of dividing a node into sub-nodes according to condition is known as splitting.
    4.	Branch/Sub Tree: The outcome of splitting i.e., a derived tree is known as sub – tree.
    5.	Pruning: The process of removing unwanted branches from a tree is known as pruning. There are two types of pruning: 
        *   Cost Complexity Pruning
        *   Reduced Error Pruning
    6.	Parent Node: The root node of any tree is known as parent node.
    7.	Child Node: Nodes other than root node are known as child nodes.

<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/120965692-d8afae00-c782-11eb-8214-86840b6bb107.png" />
</p>


-   Types of Decision Trees:
    1.	Classification Tree:
        *   This tree is of “YES/NO” type.
        *   In this kind of tree, the decision is based upon a decision variable. 
        *   For example, “Outlook” is a decision variable in first figure.
    2.	Regression Tree:
        *   This tree is of Continuous Data Types.
        *   In this tree, the decision variable is continuous 

-   Attribute Selection in a Decision Tree:
    *   The attribute selection in a decision tree is important as it gives better accuracy. 
    *   ASM (Attribute Selection Measure) is a technique which is used to select the best attribute for the nodes of decision tree. 
    *   Techniques of ASM are:
        1.	Information Gain
        2.	Gini Index

1.  **Information Gain:** It is an ASM which is used to decide the actual feature to split at each and every step-in decision tree. In this technique, the best split is chosen to obtain the purest results. Information is the measure which is a value and it measures how much information can be obtained by the class. The maximization of value of information gain is prior for a decision tree algorithm. This can be calculated with the help of the following formula:

    -   Entropy: Entropy is a metric which is used to measure the impurity of the attribute.  The randomness of the data is specified by entropy.

2.  **Gini Index:** Gini Index is used to create binary splits and it is a measure of purity/impurity. It is used during the creation of a decision tree in CART (Classification and Regression Tree). The attribute whose Gini Index is low is a preferable and high Gini Index is not preferable. The formula for Gini Index is as follows:

<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/120965784-f54be600-c782-11eb-874c-74421f1e9815.png" />
</p>


-   Advantages of Decision Tree:
    *   Useful in solving decision – related problems.
    *   Less requirement of data cleaning.

-   Disadvantages of Decision Tree:
    *   More layers make the decision tree complex.
    *   Overfitting may occur.

-   Construction of Decision Tree : A tree can be “learned” by splitting the source set into subsets based on an attribute value test. This process is repeated on each derived subset in a recursive manner called recursive partitioning. The recursion is completed when the subset at a node all has the same value of the target variable, or when splitting no longer adds value to the predictions. The construction of decision tree classifier does not require any domain knowledge or parameter setting, and therefore is appropriate for exploratory knowledge discovery. Decision trees can handle high dimensional data. In general decision tree classifier has good accuracy. Decision tree induction is a typical inductive approach to learn knowledge on classification.

-   Decision Tree representation: Decision trees classify instances by sorting them down the tree from the root to some leaf node, which provides the classification of the instance. An instance is classified by starting at the root node of the tree, testing the attribute specified by this node, then moving down the tree branch corresponding to the value of the attribute as shown in the above figure. This process is then repeated for the subtree rooted at the new node.

-   Like above shown as it is about weather , there are three attributes sunny overcast and rainy and it checks humidity for sunny ,if there are >75 humidity it is not best condition for playing , if it is about<75 then it is good for playing ,like wise there is also shown for rainy weather if it is windy then it is not suitable for playing outdoor games , if no windy weather then it is suitable for playing outdoor games. It predicts in which type of condition we can play outdoor games.

-   Strengths and Weakness of Decision Tree approach
    *   The strengths of decision tree methods are:
        *   Decision trees are able to generate understandable rules.
        *   Decision trees perform classification without requiring much computation.
        *   Decision trees are able to handle both continuous and categorical variables.
        *   Decision trees provide a clear indication of which fields are most important for prediction or classification.

-   The weaknesses of decision tree methods :
    *   Decision trees are less appropriate for estimation tasks where the goal is to predict the value of a continuous attribute.
    *   Decision trees are prone to errors in classification problems with many class and relatively small number of training examples.
    *   Decision tree can be computationally expensive to train. The process of growing a decision tree is computationally expensive.
    
-   At each node, each candidate splitting field must be sorted before its best split can be found. In some algorithms, combinations of fields are used and a search must be made for optimal combining weights. Pruning algorithms can also be expensive since many candidate sub-trees must be formed and compared.



### Task–5(C)
**Aim:** Random State Working.

-   Random State in Data Science:
    *   Whenever randomization is part of a scikit-learn library, a random – state parameter may be provided to control the random number generator used.
    *   The mere presence of random – state doesn’t mean that randomization is always used, as it may be dependent on another parameter, e.g. shuffle, being set.
    *   train_test_split() selects randomly the train and test size basing on the ratio given. 
    *   Every single time you run this function you will have a randomly selected train and test values based on the train and test size ratio. 
    *   This random selection every particular time you run this results in the "random-states". To avoid getting different values for train and test every time you select the random-state you want to use. 
    *   This will also have an impact on the evaluation metrics as if the random-state is not selected the values from the evaluation will differ. 
    *   The values 0, 1 are the most common values used. you can select your own value. Assume it as a shuffle of cards were, after the first shuffle that's random state 1 the after the second shuffle that's random state 2 etc.

-   **Why we use any integer for random_state, what it means?**
    *   This is to check and validate the data when running the code multiple times. Setting random_state a fixed value will guarantee that the same sequence of random numbers is generated each time you run the code.
    *   It takes nCr=n!/(n-r)!r! states by 70% and 30% and compare it and how many states we get , like we define 2 it gives the series which is in random_state 2.



