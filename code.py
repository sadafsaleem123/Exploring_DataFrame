#The dataset is available as event_details
-- Select the details and location of different events
SELECT 
	eventname AS event_name,
    catname AS category_name,
    catgroup AS category_group,
    venuecity AS city,
    caldate AS date,
    SUM(qtysold) AS total_sold,
    SUM(qtysold * pricepaid) AS total_sales
FROM event
INNER JOIN date USING(dateid)
INNER JOIN category USING(catid)
INNER JOIN venue USING(venueid)
INNER JOIN sales USING(eventid)
GROUP BY 1, 2, 3, 4, 5
ORDER BY total_sold DESC
LIMIT 1000


# Import libraries
import pandas as pd
import plotly.express as px

# Preview the data
event_details
event_details.info() #The .info() method prints a summary of a DataFrame. For each column, you can find its name, data type, and the number of non-null rows.
event_details.describe() #The .describe() method returns helpful descriptive statistics for your data, excluding null values.

# Create a boxplot of total sales by event category
fig = px.box(event_details, x="category_group", y="total_sales")
fig.show()

# Create a scatter plot of total sold versus total sales
fig = px.scatter(event_details, x="total_sold", y="total_sales", hover_data=["event_name"]) #Scatter plots are a great way to visualize the relationship between two (or more) numeric variables.
fig.show()
