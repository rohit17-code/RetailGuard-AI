import pandas as pd
#for importing dataset
df = pd.read_excel("data/products_10000.xlsx")
#to see top 5 rows of data
print(df.head())
# to know how many rows and columns are there
print("shape:", df.shape)

#to get information about dataset
print(df.info())

#to see statistics
print(df.describe())

# to see date column
print(df["Launch_Date"].head(10))


# to convert date from string to actual datetme
df["Launch_Date"] = pd.to_datetime(df["Launch_Date"])

# to see info abot data
print(df.info())

# to check null values
print(df.isnull().sum())

# check duplicates
print(df.duplicated().sum()) 

# Business question 1: which category has the most products?

print(df["Category"].value_counts())

# Business question 2: which  brand has the most products?

print(df["Brand"].value_counts())

# Business question 3: what is a average selling price?

print(df["Selling_Price"].mean())

# Business question 4:what is highest selling price ?

print(df["Selling_Price"].max())

## Business question 5: what is lowest selling price ?

print(df["Selling_Price"].min())

#  show all electronics produts.

Electronics = df[df["Category"] == "Electronics"]
print(Electronics)

# show all active status products.

Status = df[df["Status"] == "Active"]
print(Status)


#show active status products and whose sellin price is greater than 10000.

df[(df["Status"] == "active") & (df["Selling_Price"] >= 10000)]


# show all the products that belongs to either elecronics or 
#sports category


Electronics_or_Sports = df[
       (df["Category"] == "Electronics") 
     |                      
       (df["Category"] == "Sports")
                           ]
print(Electronics_or_Sports)

# show all products that are not discontineud.

Active_products = df[df["Status"] != "Discontinued"]
print(Active_products)
print(df["Status"].value_counts())

# 5 most xpensive products.

Expensive_products = df.sort_values(by="Selling_Price",ascending=False)

print(Expensive_products[["Product_ID","Product_Name","Selling_Price"]].head(5))
#Show the 5 cheapest products.
Cheapest_pro = df.sort_values(by= "Selling_Price", ascending=True)
print(Cheapest_pro[["Product_ID","Product_Name","Selling_Price"]].head(5))

# Business Question:
# What is the average selling price for each category?

Category_avg = df.groupby("Category")["Selling_Price"].mean()
print(Category_avg)

# How many products do we have in each category?

Category_count = df.groupby("Category")["Product_ID"].count()
print(Category_count)


# Business Question:
# What is the total selling price of products in each category?
Category_total = df.groupby("Category")["Selling_Price"].sum().round(2)
print(Category_total)

Category_report = df.groupby("Category").agg({
    "Product_ID" : "count",
    "Selling_Price" : ["sum","mean","median"]
})
print(Category_report)

#Business Question:
#For each category, what is the most expensive product price and the 
#cheapest product price?

Product_exp = df.groupby("Category").agg({
    "Product_ID" : "count",
    "Selling_Price" : ["min","max"]
    })
print(Product_exp)


print(df.loc[5, ["Product_Name", "Selling_Price"]])