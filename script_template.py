"""
This is the doc string for the module/script.
"""
import sys

# other imports  (standard library, standard non-library, local)
# import business logic from local modules
# constants (AKA global variables -- keep these to a minimum)

# main function
def wombat(args):
    """
    This is the docstring for the main() function

    :param args: Command line arguments.
    :return: None
    """
    print("Hi, Mom!!")
    function1()

# other functions
def function1():
    """
    This is the docstring for function1().

    :return: None
    """
    print("this is function1()")

    
    print(f"My name is {__name__}")

if __name__ == '__main__': # if this file is main script
    wombat(sys.argv[1:])  # Pass command line args (minus script name) to main()
