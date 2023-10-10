import pandas as pd
import json

# Load JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Convert DataFrame to Markdown Table
markdown_table = df.to_markdown()

# Read existing README
with open('README.md', 'r') as file:
    readme_content = file.read()

# Find a position to insert the table or define a marker in README.md
# For example, you can insert a comment <!-- DATA_TABLE --> in README.md where you want to insert the table
start_index = readme_content.find("<!-- DATA_TABLE -->")
if start_index != -1:
    end_index = start_index + len("<!-- DATA_TABLE -->")
    new_readme_content = (
        readme_content[:end_index] + "\n\n" + markdown_table + "\n" + readme_content[end_index:]
    )
else:
    new_readme_content = readme_content + "\n\n" + markdown_table

# Update README.md
with open('README.md', 'w') as file:
    file.write(new_readme_content)


