# PyPoll mainfile
# Modules
import pandas as pd

# Define all of the variables for calculated values
df = pd.read_csv(r'Resources\election_data.csv')

print(df.head())

total_votes = df['Ballot ID'].count()
candidates = df['Candidate'].unique()
print(total_votes)

print(candidates)
candidate_votes = df['Candidate'].value_counts()
print(candidate_votes)

# Calculate the total number of months using pandas df
