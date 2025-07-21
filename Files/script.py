# Let me check what files are currently available in the environment
import os
import json

# List all files in the current directory
current_files = os.listdir('.')
print("Current files in environment:")
for file in current_files:
    print(f"- {file}")
    
# Check if there are any zip files or markdown files from previous conversation
zip_files = [f for f in current_files if f.endswith('.zip')]
md_files = [f for f in current_files if f.endswith('.md')]

print(f"\nFound {len(zip_files)} zip files:")
for f in zip_files:
    print(f"- {f}")
    
print(f"\nFound {len(md_files)} markdown files:")
for f in md_files:
    print(f"- {f}")