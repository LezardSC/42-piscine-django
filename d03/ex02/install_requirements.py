import subprocess

# Read the requirements.txt file
with open('requirement.txt', 'r') as file:
    requirements = file.readlines()

# Iterate over each line in the file
for requirement in requirements:
    # Remove any leading or trailing whitespace and split the line into package name and version
    package, version = requirement.strip().split('==')
    
    # Use subprocess to run pip install command
    subprocess.run(['pip', 'install', f'{package}=={version}'])
