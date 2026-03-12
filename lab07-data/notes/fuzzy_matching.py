import pandas as pd
import numpy as np
import difflib

from thefuzz import process 

df1 = pd.read_csv('../data/essential_indicators_messy.csv', index_col=0)
df2 = pd.read_csv('../data/country_codes.csv')#, index_col=0)

list1 = df1['Country']
list2 = df2['name']

# how many exact matches are there?
matches = list1.isin(list2).sum()
print(f"{matches} exact matches")

# Find names in list1 that aren't in list2
f = ~list1.isin(list2)
missing = list1[f]
print(f"{len(missing)} not matched")

# # find best match for Bolivia in list2
# process.extractOne("Bolivia", list2.to_list())

# find best matches for all missing 
matches = [process.extractOne(n,list2.to_list()) for n in missing]
matches, scores = zip(*matches)

match_table = pd.DataFrame({
    'Country':missing,
    "name":matches
})

fpath = '../data/matches.csv'
print(f"writing matches to {fpath}")
match_table.to_csv(fpath)