#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""final dissertation file .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QnyW4g8FmOniu78SxlxFhx9iI5T3Bc4v
"""

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:



# Load the dataset
data = pd.read_csv("payment-practices.csv")


# In[4]:


# Step 1: Evaluate the state of supply chain management in the UK
# Calculate some basic statistics
mean_time_to_pay = data["Average time to pay"].mean()
percentage_paid_within_30_days = data["% Invoices paid within 30 days"].mean()
percentage_paid_between_31_and_60_days = data["% Invoices paid between 31 and 60 days"].mean()
percentage_paid_later_than_60_days = data["% Invoices paid later than 60 days"].mean()


# In[5]:


# Display the results
print("Mean Time to Pay:", mean_time_to_pay)
print("Percentage Paid within 30 Days:", percentage_paid_within_30_days)
print("Percentage Paid between 31 and 60 Days:", percentage_paid_between_31_and_60_days)
print("Percentage Paid Later than 60 Days:", percentage_paid_later_than_60_days)


# In[6]:


# Step 2: Assess how the UK supply chain is implementing Industry 4.0 technologies
# Count the number of companies offering E-Invoicing and Supply-chain financing
e_invoicing_count = data["E-Invoicing offered"].sum()
supply_chain_financing_count = data["Supply-chain financing offered"].sum()


# In[7]:


# Step 2: Assess how the UK supply chain is implementing Industry 4.0 technologies
# Count the number of companies offering E-Invoicing and Supply-chain financing
e_invoicing_count = data["E-Invoicing offered"].sum()
supply_chain_financing_count = data["Supply-chain financing offered"].sum()


# In[8]:


# Display the results
print("Number of Companies Offering E-Invoicing:", e_invoicing_count)
print("Number of Companies Offering Supply-chain Financing:", supply_chain_financing_count)


# In[9]:


# Step 3: Visualize the impact of Industry 4.0 on innovation and efficiency
# Calculate the mean values for innovation-related columns
innovation_columns = ["% Invoices paid within 30 days", "% Invoices paid between 31 and 60 days", "% Invoices paid later than 60 days"]
innovation_means = data[innovation_columns].mean()


# In[10]:


# Plot the results
plt.figure(figsize=(10, 6))
innovation_means.plot(kind='bar', color='skyblue')
plt.title('Impact of Industry 4.0 on Innovation')
plt.xlabel('Invoice Payment Period')
plt.ylabel('Percentage')
plt.xticks(rotation=0)
plt.show()


# In[11]:


# Step 4: Investigate how partnerships and collaboration optimize supply chains
# Count the number of companies participating in payment codes
payment_codes_count = data["Participates in payment codes"].sum()


# In[12]:


# Display the results
print("Number of Companies Participating in Payment Codes:", payment_codes_count)


# In[13]:



# 5. Overview of the dataset
print("Dataset Overview:")
print(data.info())


# In[14]:



# 6. Summary statistics
print("\nSummary Statistics:")
print(data.describe())


# In[15]:


# 7. Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())


# In[16]:


# Plot histograms for numeric columns
numeric_columns = data.select_dtypes(include=['float64', 'int64'])
numeric_columns.hist(bins=15, figsize=(15, 10))
plt.suptitle('Numeric Columns Distribution', x=0.5, y=1.02, fontsize=16)
plt.show()


# In[17]:


# 9. Categorical data analysis

# Count the unique values in each categorical column
categorical_columns = data.select_dtypes(include=['object'])
for column in categorical_columns:
    print(f"\nUnique values in {column}:")
    print(data[column].value_counts())


# In[18]:


# 10. Correlation analysis for numeric columns
correlation_matrix = numeric_columns.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap', fontsize=16)
plt.show()


# In[19]:


# Payment Code Participation
plt.figure(figsize=(8, 6))
sns.countplot(x='Participates in payment codes', data=data)
plt.title('Payment Code Participation')
plt.xlabel('Participates in Payment Codes')
plt.ylabel('Count')
plt.show()


# In[20]:


# E-Invoicing and Supply-chain Financing Comparison
plt.figure(figsize=(10, 6))
sns.countplot(x='E-Invoicing offered', hue='Supply-chain financing offered', data=data)
plt.title('E-Invoicing vs. Supply-chain Financing')
plt.xlabel('E-Invoicing Offered')
plt.ylabel('Count')
plt.legend(title='Supply-chain Financing Offered', loc='upper right', labels=['No', 'Yes'])
plt.show()


# In[21]:


# Payment Term Changes
plt.figure(figsize=(8, 6))
sns.countplot(x='Payment terms have changed', data=data)
plt.title('Payment Term Changes')
plt.xlabel('Payment Terms Have Changed')
plt.ylabel('Count')
plt.show()


# In[22]:


# Payment Term Changes
plt.figure(figsize=(8, 6))
sns.countplot(x='Payment terms have changed', data=data)
plt.title('Payment Term Changes')
plt.xlabel('Payment Terms Have Changed')
plt.ylabel('Count')
plt.show()


# In[23]:


# Pie chart for the distribution of E-Invoicing offered
e_invoicing_distribution = data["E-Invoicing offered"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(e_invoicing_distribution, labels=e_invoicing_distribution.index, autopct='%1.1f%%', startangle=140)
plt.title('E-Invoicing Offered Distribution')
plt.show()


# In[ ]:




