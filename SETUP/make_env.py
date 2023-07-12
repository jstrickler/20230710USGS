"""Create a .env file that points to EXAMPLES/tests so that the 
    pytest tools in VSCode will work correctly
"""
import os

root_folder = os.path.dirname(os.getcwd())
test_folder = os.path.join(root_folder, "EXAMPLES", "tests")


env_filename = os.path.join(root_folder, ".env")
print(f"env_filename: {env_filename}")

with open(env_filename, "w") as env_out:
    env_out.write(f"PYTHONPATH={test_folder}\n")

