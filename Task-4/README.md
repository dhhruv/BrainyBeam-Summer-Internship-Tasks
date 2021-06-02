## Task-4

### Task–4(A)

**Aim:** List out five methods of NumPy and pandas with output.
-   Methods of NumPy shown in [task4a.py]().
-   Methods of Pandas shown in [task4b.py]().


### Task–4(B)

**Aim:** reshape(-1,1) Explanation.
-   reshape() function:
    *   reshape() method is used to change the shape of an array.
    *   This method is capable of removing or modifying dimensions of any array.
    *   The syntax of reshape() is as follows:
        ```
        numpy.reshape(array_name, new_shape, order=’C’)
        ```
    *   The order attribute contains 3 values:
        1.	C – read/write the elements which are using C-like index.
        2.	F – read/write the elements which are using Fortran-index.
        3.	A - read/write the elements in C-like index, when array is not contiguous in memory, otherwise use Fortran-like order.

-   reshape(-1,1) function:
    *   reshape(-1,1) is used to flatten a multidimensional array.
    *   The argument ‘-1’ will flatten the multidimensional array into a 1-D array.
    *   The argument ‘1’ will make every element of 1-D array into a multidimensional array.

-   reshape(-1,1) example:
```sh
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
a = a.reshape(-1,1)
print(a)
```


### Task–4(C)

**Aim:** Linear Regression working with mathematical equation.

-   Linear Regression:
    *   Linear Regression is a model of ML (Machine Learning) which is used to find a relationship between two features or variables.
    *   The main aim to apply Linear Regression is to find the best fit for the data points on a graph which will help in further prediction of output of future values which are currently absent in dataset.
    *   The best fit is obtained on the basis of 2 type of variables:
        1.	Dependent Variables: The factor for which the equation is solved.
        2.	Independent Variables: The factors which are used to for prediction of dependent variables.
    *   Example of best fit line:

-   The formula for Linear Regression is as follows: y=a+bX
    Here, 
    a 	>>	Intercept
    b	>>	Slope
    X	>>	Datapoints 

-   This formula can also be derived as:
-   For obtaining the accuracy of the model that is developed for prediction via Linear Regression, “Cost Function” is used. 
-   It is used to obtain the error-rate that how wrong the model is during estimation.
-   The cost function is derived as follows i.e., Mean Square Error:
-   The Convergence Theorem is used to reach global minima in a curve that is defined by Cost Function.