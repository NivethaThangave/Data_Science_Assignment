import pandas as pd
import seaborn as sbn
import plotly.express as px
import matplotlib.pyplot as plt

# reading the CSV file 
NHS_Data = pd.read_csv("NHS_Expenditures.csv")
plt.style.use('default')
print(NHS_Data)
# Creating a Data Frame
NHS_Expense = pd.DataFrame({'Year': ["1955","1965","1975","1985","1995","2005","2015"],
                           'NHS_Expenses' : [10,22,26,45,59,113,140]})

print(NHS_Expense)

# Using Seaborn for plotting the graph 

sbn.lineplot(x="Year", y="NHS_Expenses", data=NHS_Expense)
plt.show()

# By plotting the graph using plotly
fig = px.line(NHS_Expense, x = 'Year', y = ['NHS_Expenses'], title = 'NHS Budget')
fig.show()
