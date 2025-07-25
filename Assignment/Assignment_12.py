# Databricks notebook source
# MAGIC %pip install pandas
# MAGIC %restart_python

"""This code reads a CSV file from the specified path and header is true because we #want first row as column names and then we displayed it"""

df = spark.read.csv("/Volumes/workspace/default/sales_v", header=True , inferSchema=True)
display(df)


"""here the data is filtered where sales is greater than 1000 by using .filter()##function"""
df_filtered = df.filter((df['SALES']>1000))
display(df_filtered)


"""here we only selected specific columns from table and named this as df_select by #using select() function"""
df_select = df.select('ORDERNUMBER','QUANTITYORDERED','PRICEEACH','ORDERLINENUMBER','SALES','ORDERDATE','STATUS','QTR_ID')
display(df_select)


"""here we used aggregate function sum with group by to group the data by #ORDERNUMBER and renamed the column as total_sales"""
df_group = df.groupBy('ORDERNUMBER').agg(sum('SALES').alias('total_sales'))
display(df_group)


"""here we saved the data in delta format and mode we used is append because we want to append the data in table """
df_group.write.format("delta").mode("append").saveAsTable("default.agg_sales_data")


"""here we used describe history to get the history of the table to track what changes have been made to it """
df_history = spark.sql("describe history default.agg_sales_data")
display(df_history)


"""This code reads version 1 of the Delta table default.agg_sales_data using time #travel, allowing you to view the table's state at that specific version."""
version_number=1
df_specific_version=spark.read.format("delta").option("versionAsOf",version_number).table("default.agg_sales_data")
display(df_specific_version)


"""filter the data where status is disputed and price of each is >95"""
df_filtered1 = df.filter((df['STATUS'] == 'Disputed') & (df['PRICEEACH']>95))
display(df_filtered1)


"""code filters rows where STATUS is 'Disputed' and PRICEEACH is greater than 95, #selects relevant columns, 
and writes the result in Delta format, partitioned by #STATUS, to the specified path"""
df_transformed1 = df.filter((df['STATUS'] == 'Disputed') & (df['PRICEEACH'] > 95)
).select(
    "ORDERNUMBER", "QUANTITYORDERED", "PRICEEACH",
    "ORDERLINENUMBER", "SALES", "ORDERDATE", "STATUS", "QTR_ID"
)
df_transformed1.write.format("delta")\
    .mode("overwrite")\
    .partitionBy("STATUS")\
    .save("/Volumes/workspace/default/sales_v/transformed1_data")