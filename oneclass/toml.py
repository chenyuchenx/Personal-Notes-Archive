import oneclass.toml as toml
import subprocess

# Load the current pyproject.toml file
with open('pyproject.toml', 'r') as f:
    pyproject = toml.load(f)

# Get the list of installed packages
result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
packages = result.stdout.decode('utf-8').split('\n')

# Parse the packages and add them to pyproject.toml
dependencies = pyproject.get('tool', {}).get('poetry', {}).get('dependencies', {})
for package in packages:
    if '==' in package:
        name, version = package.split('==')
        if name not in dependencies:
            dependencies[name] = version

# Update the pyproject.toml file
pyproject['tool']['poetry']['dependencies'] = dependencies
with open('pyproject.toml', 'w') as f:
    toml.dump(pyproject, f)

print("Dependencies have been added to pyproject.toml")
