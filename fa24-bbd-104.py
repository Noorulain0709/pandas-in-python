#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df = pd.read_csv("melb_data.csv")


# In[55]:


import pandas as pd
df=pd.read_csv("melb_data.csv")

#1.	Identify columns with more than 20% missing values and drop them.
#Hint: In first step , create a variable missing_person and calculate it using df.isna().sum() and len(df). 
# Use simply process of calculating a percentage that is missing values/total values*100. 

missing_person=df.isna().sum()/len(df)*100
print(missing_person)

#2.	Fill missing values in the numerical columns using median instead of mean.
#Hint Use df.fillna and median commands 
#df.fillna(df.median(), inplace=True)

numeric_df = df.select_dtypes(include=['number'])
df.fillna(numeric_df.median(), inplace=True)

#3.	Fill missing values in the categorical columns using the most frequent value (mode).
#df["Column_Name"].fillna(df["Column_Name"].mode()[0], inplace=True)

df["SellerG"].fillna(df["SellerG"].mode()[0], )
df["Regionname"].fillna(df["Regionname"].mode()[0], )
df["Method"].fillna(df["Method"].mode()[0], )
df["Type"].fillna(df["Type"].mode()[0], )
df["Address"].fillna(df["Address"].mode()[0], )


# In[57]:


#Homework Task 2: Advanced Filtering and Indexing
#Activity Goal: Use filtering and indexing techniques to extract meaningful data subsets.Tasks:
#1.	Retrieve all properties located in "Richmond" with a price greater than $1,000,000.
#Hint: You should use is equal == command for location “Richmond” and greater than > for price. 
richmond_houses = df[(df["Suburb"] == "Richmond") & (df["Price"] > 1000000)]
print(richmond_houses.head())
#2.	Extract only the "Price", "Suburb", and "BuildingArea" columns for properties where the land size is above 500 square meters.
df_filtered = df.loc[df["Landsize"] > 500, ["Price", "Suburb", "BuildingArea"]]
#3.	Find the top 5 most expensive houses in the dataset using sorting.
#Hint: You should use sort option by Price and then print the top 5 rows.
df_sorted = df.sort_values(by="Price", ascending=False)
print(df_sorted.head(5))


# In[65]:


#Homework Task 3: Data Transformation & Feature Engineering
#Activity Goal: Apply transformation techniques to create new insights from the data.
#Tasks:
#1.	Create a new column that calculates the price per room (Price / Rooms).
df["Price_per_Room"] = df["Price"] / df["Rooms"]
print(df["Price_per_Room"])
#2.	Convert the "Date" column (if available) into a proper datetime format.
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
print(df["Date"])
#3.	Extract the year of sale from the date and create a new column Year_Sold.
df["Year_Sold"] = df["Date"].dt.year
print(df["Year_Sold"])


# In[67]:


#Homework Task 4: Aggregation and Grouping
#Activity Goal: Learn how to group and aggregate data for analysis.
#Tasks:
#1.	Find the average price of properties in each suburb.
suburb_avg_price = df.groupby("Suburb")["Price"].mean()
print(suburb_avg_price)
#2.	Find the total number of properties sold in each suburb.
#Hint: For properties sold, you should use the price column because the Price represent the price at which the properties are sold
# You can use groupby option
properties_per_suburb = df.groupby("Suburb")["Price"].count()
print(properties_per_suburb)
#3.	Identify the suburb with the highest average price.
most_expensive_suburb = suburb_avg_price.idxmax()
print("Most expensive suburb:", most_expensive_suburb)


# In[71]:


#📌 Homework Task 5: Exporting & Reporting Data
#✅ Goal: Save cleaned and processed data for further use.
#Tasks:
#1.	Save the cleaned dataset into a new CSV file.
import matplotlib.pyplot as plt
suburb_avg_price.head(10).plot(kind="bar")
plt.title("Average House Prices in Top 10 Suburbs")
plt.xlabel("Suburb")


# In[75]:


#🔹 Bonus Challenge (For Advanced Students)
#•	Use apply() to create a new column that classifies houses as "Expensive" or "Affordable", based on whether the price is above#
#or below the median price.
median_price = df["Price"].median()
df["Category"] = df["Price"].apply(lambda x: "Expensive" if x > median_price else "Affordable")
print(df["Category"])
#•	Find the correlation between price and the number of rooms using .corr().
# Find the correlation between price and the number of rooms
correlation = df["Price"].corr(df["Rooms"])
print("Correlation between Price and Rooms:", correlation)

