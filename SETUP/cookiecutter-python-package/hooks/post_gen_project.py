import sys
from subprocess import run

print("Installing module in editable mode")
run([sys.executable, '-m', 'pip', 'install', '-e', '.'])
print()
print("""
Add your code to src/{{cookiecutter.module_slug}}.py.


The following tasks may be run from the command line in the project (top level) folder:

Run all tests:
    pytest
   
Generate documentation:
    cd docs
    make latexpdf

    or
    
    cd docs
    make html
    
""")
