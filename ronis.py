import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import plotly.express as px

aprilFile = pd.read_csv('april_2024.csv')
mayFile = pd.read_csv('may_2024.csv')
juneFile = pd.read_csv('june_2024.csv', encoding='latin-1') #this one had some sort of issue when reading, but encoding='latin-1' fixes it
julyFile = pd.read_csv('july_2024.csv')
augustFile = pd.read_csv('august_2024.csv')
septemberFile = pd.read_csv('september_2024.csv')
octoberFile = pd.read_csv('october_2024.csv')

#april - 30
#Order # - indx 0 	Sent Date - indx 1	Modifier - indx 2	Option Group Name - indx 3 	Parent Menu Selection - indx 4 	Order ID - indx 5 
#april_rows = [list(row) for row in aprilFile.values]
#print(april_rows)

#   APRIL
# Total orders:
aprilFile['Sent Date'] = pd.to_datetime(aprilFile['Sent Date']) #to_datetime changes it to a format where we can read the day, month, and year by using pandas day month and year keywords
total_orders_april = aprilFile['Order ID'].nunique() #.nunique() returns the number of unique values in a series, so this will give us the total number of orders

# Monthly Data:
#Add day month and hour properties to our file
aprilFile['Day'] = aprilFile['Sent Date'].dt.dayofweek  #.dayofweek gets the number of the day of the week with 0 = Monday -> 6 = Sunday, need .dt in front because that is how we access those time/date properties of our datetimelike values
aprilFile['Hour'] = aprilFile['Sent Date'].dt.hour #.hout gets the hour 

april_days = aprilFile.groupby('Day')['Order ID'].nunique() #.groupby groups the data by Day, then we can use ['Order ID'].nunique() to get the number of orders for each day
#print(april_days)


# Most Popular:
april_popular = aprilFile['Parent Menu Selection'].value_counts() #.value_counts computes a histogram of a 1D array of values - so it will count the number of times each menu item appears
#print(april_popular)
april_modifiers = aprilFile['Modifier'].value_counts()
#print(april_modifiers)

#   MAY
# Total orders:
mayFile['Sent Date'] = pd.to_datetime(mayFile['Sent Date']) 
total_orders_may = mayFile['Order ID'].nunique() 

# Date Data:
mayFile['Day'] = mayFile['Sent Date'].dt.dayofweek  
mayFile['Hour'] = mayFile['Sent Date'].dt.hour 

may_days = mayFile.groupby('Day')['Order ID'].nunique()

# Most Popular
may_popular = mayFile['Parent Menu Selection'].value_counts() 
may_modifiers = mayFile['Modifier'].value_counts()

#   JUNE
# Total orders:
juneFile['Sent Date'] = pd.to_datetime(juneFile['Sent Date'])
total_orders_june = juneFile['Order ID'].nunique()

# Date Data:
juneFile['Day'] = juneFile['Sent Date'].dt.dayofweek
juneFile['Hour'] = juneFile['Sent Date'].dt.hour

june_days = juneFile.groupby('Day')['Order ID'].nunique()

# Most Popular
june_popular = juneFile['Parent Menu Selection'].value_counts() 
june_modifiers = juneFile['Modifier'].value_counts()

#   JULY
# Total orders:
julyFile['Sent Date'] = pd.to_datetime(julyFile['Sent Date'])
total_orders_july = julyFile['Order ID'].nunique()

# Date Data:
julyFile['Day'] = julyFile['Sent Date'].dt.dayofweek
julyFile['Hour'] = julyFile['Sent Date'].dt.hour

july_days = julyFile.groupby('Day')['Order ID'].nunique()

# Most Popular
july_popular = julyFile['Parent Menu Selection'].value_counts() 
july_modifiers = julyFile['Modifier'].value_counts()

#   AUGUST
# Total orders:
augustFile['Sent Date'] = pd.to_datetime(augustFile['Sent Date'])
total_orders_august = augustFile['Order ID'].nunique()

# Date Data:
augustFile['Day'] = augustFile['Sent Date'].dt.dayofweek
augustFile['Hour'] = augustFile['Sent Date'].dt.hour

august_days = augustFile.groupby('Day')['Order ID'].nunique()

# Most Popular
august_popular = augustFile['Parent Menu Selection'].value_counts() 
august_modifiers = augustFile['Modifier'].value_counts()

#   SEPTEMBER
# Total orders:
septemberFile['Sent Date'] = pd.to_datetime(septemberFile['Sent Date'])
total_orders_september = septemberFile['Order ID'].nunique()

# Date Data:
septemberFile['Day'] = septemberFile['Sent Date'].dt.dayofweek
septemberFile['Hour'] = septemberFile['Sent Date'].dt.hour

september_days = septemberFile.groupby('Day')['Order ID'].nunique()

# Most Popular
september_popular = septemberFile['Parent Menu Selection'].value_counts() 
september_modifiers = septemberFile['Modifier'].value_counts()

#   OCTOBER
# Total orders:
octoberFile['Sent Date'] = pd.to_datetime(octoberFile['Sent Date'])
total_orders_october = octoberFile['Order ID'].nunique()

# Date Data:
octoberFile['Day'] = octoberFile['Sent Date'].dt.dayofweek
octoberFile['Hour'] = octoberFile['Sent Date'].dt.hour

october_days = octoberFile.groupby('Day')['Order ID'].nunique()

# Most Popular
october_popular = octoberFile['Parent Menu Selection'].value_counts() 
october_modifiers = octoberFile['Modifier'].value_counts()

#   ALL
# Total Time
total_days = april_days + may_days + june_days + july_days + august_days + september_days + october_days

total_days.index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Plot the sales by day of the week
total_days.plot(kind='bar', color='skyblue')
plt.title("Sales by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Order Count")
plt.show()

# Output the results to check:
print(f"Total Orders in April: {total_orders_april}")
print(f"Total Orders in May: {total_orders_may}")
print(f"Total Orders in June: {total_orders_june}")
print(f"Total Orders in July: {total_orders_july}")
print(f"Total Orders in August: {total_orders_august}")
print(f"Total Orders in September: {total_orders_september}")
print(f"Total Orders in October: {total_orders_october}")

#print(aprilFile)

x = np.array(["April", "May", "June", "July", "August", "September", "October"])
y = np.array([total_orders_april, total_orders_may, total_orders_june, total_orders_july, total_orders_august, total_orders_september, total_orders_october])
plt.plot(x, y)
plt.ylim(0, 5000)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Order ID")
#plt.show()

# Step 1: Load Data
data = pd.read_csv('april_2024.csv')
data['Sent Date'] = pd.to_datetime(data['Sent Date'])
data['Month'] = data['Sent Date'].dt.month
data['Day'] = data['Sent Date'].dt.day

# Step 2: Create an Interactive Plot (Example: Orders by Day)
fig = px.bar(data, x='Day', title="Orders by Day of the Month", color='Month')

# Step 3: Add Streamlit Widgets (Dropdown)
selected_month = st.selectbox('Select Month', options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Step 4: Filter Data Based on Selected Month
filtered_data = data[data['Month'] == selected_month]
fig_filtered = px.bar(filtered_data, x='Day', title=f"Orders for Month {selected_month}")

# Step 5: Display Graph and Text
st.title("Roni's Mac Bar - Interactive Dashboard")
st.write(f"Showing orders for the selected month ({selected_month})")
st.plotly_chart(fig_filtered)