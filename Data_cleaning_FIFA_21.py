import pandas as pd
import numpy as np
from openpyxl import Workbook

df = pd.read_csv("FIFA 21.csv")

#Q1. Convert the height and weight columns to numerical forms. [2 marks]
#Converting height to cm, feet and inches to cm
def convert_to_cm(height):
    if 'cm' in height:
        return height[:3]
    elif "'" in height and '"' in height:
        height = str(height).replace('"', '')
        feet, inches = map(int,height.split("'"))
        total_inches = feet * 12 + inches
        return round(float(total_inches * 2.54),2)
    else:
        return np.nan

print("Before converting values in Height column:\n",df['Height'].head())
df['Height'] = df['Height'].apply(convert_to_cm)
df['Height'] = df['Height'].astype(float)
print("After converting values in Height column:\n",df['Height'].head())

#Converting weight to lbs, Kg to lbs
def convert_to_lbs(weight):
    if 'kg' in weight:
        return round(float(weight[:-2]) * 2.20462,2)
    elif 'lbs' in weight:
        return round(float(weight[:-3]),2)
    else:
        return np.nan

print("Before converting values in Weight column:\n",df['Weight'].head())
df['Weight'] = df['Weight'].apply(convert_to_lbs)
df['Weight'] = df['Weight'].astype(float)
print("After converting values in Weight column:\n",df['Weight'].head())

#Q2. Remove the unnecessary newline characters from all columns that have them. [3 marks]
#Check columns for instance of string and strip them of widespace and unnecessary newline characters
for column in df.columns:
    df[column] = df[column].apply(lambda x: x.strip() if isinstance(x,str) else x)

#Q3. 'Value', 'Wage' and "Release Clause' are string columns. Convert them to numbers.
#For eg, "M" in value column is Million, so multiply the row values by 1,000,000, etc. [3 marks]
def convert_value_appropriately(value):
    if value[-1] == 'K':
        return float(value[1:-1]) * 1000
    elif value[-1] == 'M':
        return float(value[1:-1]) * 1000000
    else:
        return float(value[1:])
    
print("Before converting values in Value column:\n",df['Value'].head())
df['Value'] = df['Value'].apply(convert_value_appropriately)
df['Value'] = df['Value'].astype(float)
print("After converting values in Value column:\n",df['Value'].head())

print("Before converting values in Wage column:\n",df['Wage'].head())
df['Wage'] = df['Wage'].apply(convert_value_appropriately)
df['Wage'] = df['Wage'].astype(float)
print("After converting values in Wage column:\n",df['Wage'].head())

print("Before converting values in Release Clause column:\n",df['Release Clause'].head())
df['Release Clause'] = df['Release Clause'].apply(convert_value_appropriately)
df['Release Clause'] = df['Release Clause'].astype(float)
print("After converting values in Release Clause column:\n",df['Release Clause'].head())

#The Hits column also has values like 1.3k so converting to numeric  values appropriately
def convert_Hits_to_numeric(value):
    if isinstance(value, float):
        return value
    elif value.endswith('K'):
        return float(value[:-1]) * 1000
    else:
        return float(value)
    
print("Before converting values in Hits column:\n",df['Hits'].head())
df['Hits'] = df['Hits'].apply(convert_Hits_to_numeric)
df['Hits'] = df['Hits'].astype(float)
print("After converting values in Hits column:\n",df['Hits'].head())


#Q4. Some columns have 'star' characters.
#Strip those columns of these stars and make the columns numerical. [3 marks]
def remove_stars_convert_to_numeric(value):
    return int(value[0])
    
print("Before converting values in W/F column:\n",df['W/F'].head())
df['W/F'] = df['W/F'].apply(remove_stars_convert_to_numeric)
df['W/F'] = df['W/F'].astype(int)
print("After converting values in W/F column:\n",df['W/F'].head())

print("Before converting values in SM column:\n",df['SM'].head())
df['SM'] = df['SM'].apply(remove_stars_convert_to_numeric)
df['SM'] = df['SM'].astype(int)
print("After converting values in SM column:\n",df['SM'].head())

print("Before converting values in IR column:\n",df['IR'].head())
df['IR'] = df['IR'].apply(remove_stars_convert_to_numeric)
df['IR'] = df['IR'].astype(int)
print("After converting values in IR column:\n",df['IR'].head())

#The following columns are of type object so converting for good measure
df['Name'] = df['Name'].astype(str)
df['LongName'] = df['LongName'].astype(str)
df['photoUrl'] = df['photoUrl'].astype(str)
df['playerUrl'] = df['playerUrl'].astype(str)
df['Nationality'] = df['Nationality'].astype(str)
df['Club'] = df['Club'].astype(str)
df['Contract'] = df['Contract'].astype(str)
df['Positions'] = df['Positions'].astype(str)
df['Preferred Foot'] = df['Preferred Foot'].astype(str)
df['Contract'] = df['Contract'].astype(str)
df['Best Position'] = df['Best Position'].astype(str)
df['A/W'] = df['A/W'].astype(str)
df['D/W'] = df['D/W'].astype(str)

#These columns were converted to uppercase to avoid a flawed analysis.
columns_to_convert = ['Name', 'LongName', 'photoUrl', 'playerUrl', 'Nationality', 'Club', 
                      'Contract', 'Positions', 'Preferred Foot', 'Best Position', 'A/W', 'D/W']
df[columns_to_convert] = df[columns_to_convert].apply(lambda x: x.str.upper())
print(df[columns_to_convert].head())

#The odd character was removed from OVA column name
df.rename(columns={'↓OVA': 'OVA'}, inplace=True)

#Extract year from different formats of contract
def extract_contract_dates(contract):
    if 'ON LOAN' in contract:
        contract_end = contract.split(',')[1].strip()[:4]  # Extracting the year part after the comma
        contract_start = None
    elif contract == 'FREE':
        contract_start = None
        contract_end = None
    elif ' ~ ' in contract:
        contract_dates = contract.split(' ~ ')
        contract_start = contract_dates[0]
        contract_end = contract_dates[1] if len(contract_dates) > 1 else None
    return pd.Series([contract_start, contract_end], index=['contract_start', 'contract_end'])

#Split contract column using ~ into start and end of contract
df[['contract_start', 'contract_end']] = df['Contract'].apply(extract_contract_dates)

#df.to_csv("Cleaned_FIFA_21.csv", date_format='%Y-%m-%d %I:%M:%S %p', index=False)
df.to_excel("Cleaned_FIFA_21.xlsx", index=False)
#print(df.dtypes)