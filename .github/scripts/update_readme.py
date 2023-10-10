import json
import pandas as pd
from tabulate import tabulate

# Load data
with open('data.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Convert to markdown table
md_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

# Update README.md
with open('README.md', 'w') as f:
    f.write("# My Prompt Library\n\n")
    f.write(md_table)