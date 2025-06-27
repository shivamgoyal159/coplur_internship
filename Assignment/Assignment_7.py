import pandas as pd

print("1) Explore more regex patterns \n")

df=pd.DataFrame(['$40.000*','$40000 condition attached'],
                columns=['one']
                )
print(df)

df['one']=df['one'].str.replace(r'\D+','',regex=True).astype('int')

df['one'] = df['one'].str.extract(r'(\d+\.\d+|\d+)')

df['one'] = df['one'].str.replace(r'[^a-zA-Z ]', '', regex=True)

df['one'] = df['one'].str.findall(r'[a-zA-Z]+').str.join(' ')

df['number'] = df['one'].str.extract(r'(\d+)')

df['after_number'] = df['one'].str.extract(r'\d+(.*)')

df['specials'] = df['one'].str.findall(r'[^a-zA-Z0-9\s]').str.join('')

df['one'] = df['one'].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
print(df)

print("\n 2) Explore more datetime functions and uses in Pandas \n")

df = pd.DataFrame({
    'Date': ['2025-06-01', '2025-06-15', '2025-07-01']
})

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.day_name()

df['Days_Since'] = (pd.Timestamp.today() - df['Date']).dt.days
print(df) 

print("\n 3) Import a meaningful CSV file, clean data, and analyze \n")

df = pd.read_csv("data.csv")

print(df.head())

df['Price'] = df['Price'].replace(r'[^0-9.]', '', regex=True).astype(float)

df['Date'] = pd.to_datetime(df['Date'])

df = df.dropna()

df['Total'] = df['Price'] * df['Quantity']

sales_summary = df.groupby('Product')['Total'].sum().sort_values(ascending=False)

print(sales_summary)

