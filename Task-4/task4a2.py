import pandas as pd

# method-1 read_csv()
df = pd.read_csv(
    "TV Shows - Netflix.csv"
)  # will import the csv file in a variable(dataframe)

# method-2 head(): will return the top n-number of rows of dataframe
df.head(5)

# method-3 tail(): will return the bottom n-number of rows in dataframe
df.tail(5)

# method-4 type(): will return the type of given dataframe or dataframe column
type(df)

# method-5 info(): will return the information about the dataframe
df.info()
