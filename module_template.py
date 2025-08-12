#!/usr/bin/env python3

###############################################################################
# Licence Information                                                         #
###############################################################################
# Copyright © 2025 Kristian Mansfield
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


###############################################################################
# Module Documentation                                                        #
###############################################################################
"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  foo = ClassFoo()
  bar = foo.function_bar()
"""

# Package and Module Docstrings
# Package docstrings should be placed at the top of the package’s
# __init__.py file. This docstring should list the modules and
# sub-packages that are exported by the package.
#
# Module docstrings are similar to class docstrings. Instead of classes
# and class methods being documented, it’s now the module and any
# functions found within. Module docstrings are placed at the top of the
# file even before any imports. Module docstrings should include the
# following:
# * A brief description of the module and its purpose
# * A list of any classes, exception, functions, and any other objects
#   exported by the module
#
# The docstring for a module function should include the same items as a
# class method:
# * A brief description of what the function is and what it’s used for
# * Any arguments (both required and optional) that are passed including
#   keyword arguments
# * Label any arguments that are considered optional
# * Any side effects that occur when executing the function
# * Any exceptions that are raised
# * Any restrictions on when the function can be called
#
# From: https://realpython.com/documenting-python-code/
# ----------------------------------------------------------------------


###############################################################################
# Imports                                                                     #
###############################################################################


###############################################################################
# Classes                                                                     #
###############################################################################
##################
# Public classes #
##################
class MyClassTemplate:
    """A class used as a template to show good documentation.

    This example class shows how to build a class in python using the
    __init__ function with specifically defined variables. This is in
    contrast to a class that creates an instance from a dict. This
    method is preferred.

    Attributes:
        first (int):
            An integer to compare to second.
        second (int):
            An integer to compare to first.
        zeroth (string):
            An attribute that is shared across all class instances.
    """

    # Class Docstrings
    # Class method docstrings should contain the following:
    # * A brief description of what the method is and what it’s used for
    # * Any arguments (both required and optional) that are passed
    #   including keyword arguments
    # * Label any arguments that are considered optional or have a
    #   default value
    # * Any side effects that occur when executing the method
    # * Any exceptions that are raised
    # * Any restrictions on when the method can be called
    #
    # From: https://realpython.com/documenting-python-code/
    # ------------------------------------------------------------------

    # Static class attribute definitions
    zeroth = "Zero"

    # Dunders
    def __init__(self, first=None, second=None):
        self.first = first
        self.second = second

    # Public methods
    def set_first(self, new_first):
        """Set the variable called first in this instance of the class"""
        self.first = new_first

    # Private methods
    def _swap_first_and_second(self):
        temp = self.first
        self.first = self.second
        self.second = temp


class MyClassTemplateWithDict:
    """A class used as a template to show good documentation.

    This example class shows how to build a class in python using a dict
    instead of specific values in the __init__ function. While this
    method is not preferred, it can be used where classes need to be
    flexible or have None types.

    Attributes:
        name (str):
            A name attribute for the class instance.
        age (int):
            An age attribute for the class instance.
        city (str):
            The city for a class instance.
        zeroth (string):
            An attribute that is shared across all class instances.
    """

    # Static class attribute definitions
    zeroth = "Zero"

    # Dunders
    def __init__(self, data_dict):
        # Check if data_dict is indeed a dictionary
        if not isinstance(data_dict, dict):
            raise TypeError("Input must be a dictionary.")

        # Assign values from the dictionary to instance attributes
        self.name = data_dict.get(
            'name', 'Default Name'
            )   # Use .get() for safe access with defaults
        self.age = data_dict.get('age', 0)
        self.city = data_dict.get('city', 'Unknown')

        # Alternatively, you can also iterate through the dictionary
        # and set attributes dynamically
        for key, value in data_dict.items():
            setattr(self, key, value)

    # Public methods
    def set_name(self, new_name):
        """Set the name of this instance of the class"""
        self.name = new_name

    # Private methods
    def _happy_birthday(self):
        self.age = self.age + 1

###################
# Private classes #
###################


###############################################################################
# Functions                                                                   #
###############################################################################
####################
# Public functions #
####################
def check_digits(string_to_print: str, first: int, second: int = 0) -> bool:
    """Prints a string if given variables match.

    Compares variables first and second. If they match, return true and
    print the string. Otherwise return false and do not print.

    Args:
        string_to_print (str):
            The output string if the given variables are equal.
        first (int):
            The first number to compare with second.
        second (:obj:`int`, optional):
            The second number to compare with first. The default is 0.

    Returns:
        A boolean value of whether or not the given variables were
        equal.

    Raises:
        IOError: This is an example of an error occurring and raising
            an exception.
    """

    # Function Docstrings
    # The docstring for a function or method should summarize its
    # behavior and document its arguments and return values.
    # It should also list all the exceptions that can be raised and
    # other optional arguments.
    # From: https://www.programiz.com/python-programming/docstrings
    # ------------------------------------------------------------------

    if first == second:
        print(string_to_print)
        return True
    return False

#####################
# Private functions #
#####################


###############################################################################
# Main                                                                        #
# # DELETE IF NOT EXECUTABLE                                                  #
###############################################################################
def main():
    """Main function for python module"""
    # Declare variables

    # Create objects/connections

    # Do stuff :)

    # Return
    return


###############################################################################
# Entry point                                                                 #
# # DELETE IF NOT EXECUTABLE DIRECTLY                                         #
###############################################################################
if __name__ == "__main__":
    # Parse arguments

    # Perform setup if needed

    # Run main
    main()
