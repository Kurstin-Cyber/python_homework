import pandas as pd


#Sample DataFrame with missing values

data = {'Name': ['Amara', 'Yulia', 'None', 'David'],
        'Age': [24, 27, 22, None],
        'Score': [85, None, 88, 76]}

df = pd.DataFrame(data)

# Find rows with missing data
df_missing = df[df.isnull().any(axis=1)]
print(df_missing)

# Remove rows with missing data
df_dropped = df.dropna()
print(df_dropped)

# Replace missing data with default values
df_filled =df.fillna({'Age': 0, 'Score': df['Score'].mean()})
print(df_filled)



# Sample DataFrame with mixed data types
data = {'Name': ['Amara', 'Yulia', 'Charlie'],
      'Age': ['24', '27', '22'],
      'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}

df = pd.DataFrame(data)

# Convert 'Age' column to integers
df['Age'] = df['Age'].astype(int)

# Convert 'JoinDate' column to datetime
df['JoinDate'] = pd.to_datetime(df['JoinDate'])

print(df.dtypes)
print(df) # Verify data types

data = {
    'Name': ['Amara', 'Yulia', 'Amara', 'David'],
    'Age': [24, 27, 24, 32],
    'Score': [85, 92, 85, 76]
}

df = pd.DataFrame(data)

# Identify and remove duplicates
df_cleaned = df.drop_duplicates()
print(df_cleaned)

# Remove duplicates based on 'Name' column
df_cleaned_by_name = df.drop_duplicates(subset='Name')
print(df_cleaned_by_name)

data = {'Name': ['Amara', 'Yulia', 'Charlie'],
        'Location': ['LA', 'LA', 'NY'],
        'JoinDate': ['2023-01-15', '2022-12-20', '2023-03-01']}

df =pd.DataFrame(data)

# Convert 'Location' abbreviations into full names
df['Location'] = df['Location'].map({'LA': 'Los Angeles', 'NY': 'New York'})

print(df)

df = pd.DataFrame({
    'City': ['LA', 'NY', 'Chicago']
})

option_a = df['City_A'] = df['City'].map({
    'LA': 'Los Angeles', 'NY': 'New York'
})

option_b = df['City_B'] = df['City'].replace({'LA': 'Los Angeles', 'NY': 'New York'})

print(df)
print(option_a)
print(option_b)


data = {'Name': ['Tomas', 'Priya', 'Taiwo', 'Mary'],
        'Phone': [3212347890, '(212)555-8888', '752-9103', '8659134568']}

df = pd.DataFrame(data)
df['Correct Phone'] = df['Phone'].astype(str)

def fix_phone(phone):
    if phone.isnumeric():
        out_string = phone
    else:
        out_string = '' 
        for c in phone:
            if c in '0123456789':
                out_string += c
    if len(out_string) == 10:
        return out_string
    return None

print(df)
         