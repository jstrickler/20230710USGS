"""
Module documentation...
"""
def sample_function():
    """
    Sample function documentation...
    """
    print("sample {{cookiecutter.module_slug}} function")

class {{ cookiecutter.module_slug.split('_')|map('capitalize')|join }}:
    """
    Class documentation...
    """
    def sample_method(self):
        """
        Sample method documentation...
        """
        print("sample instance method")
