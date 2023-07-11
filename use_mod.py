import script_template
import sys

script_template.function1()

#  PYTHONPATH="C:\myfolder\modules;d:\other_modules"

# module search order:
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in sys.prefix (installation folder)
for path in sys.path:
    print(path)
print()



print(globals())
