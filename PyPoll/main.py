# PyPoll mainfile
# Modules
import pandas as pd

# Define all of the variables for calculated values
df = pd.read_csv(r'Resources\election_data.csv')

# ballot total counts
total_votes = df['Ballot ID'].count()

# canidate names
candidates = df['Candidate'].unique()

# counts per canidate
candidate_votes = df['Candidate'].value_counts()

# percentage for counted votes
percentage = (candidate_votes/total_votes) * 100

# winner of the election
president = candidate_votes.idxmax()

# Print Statements
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")

# for loop to loop through candidates list
for candidate in candidates:
    print(
        (f"{candidate}: {percentage[candidate]:.3f}% ({candidate_votes[candidate]})"))
print("----------------------------")
print(f"Winner: {president}")
print("----------------------------")

# Write file to analysis folder
path = (r'Analysis\election_analysis.txt')
with open(path, "w") as file:

    # Write file to analysis folder
    file.write(f'''Election Results:
----------------------------
Total Votes: {total_votes}
----------------------------''')

    for candidate in candidates:
        file.write(
            (f"\n{candidate}: {percentage[candidate]:.3f}% ({candidate_votes[candidate]})"))

    file.write(f'''
----------------------------
Winning Results:
----------------------------
Winner: {president}
----------------------------
               ''')
