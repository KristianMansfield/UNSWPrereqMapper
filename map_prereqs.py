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
# Script Documentation                                                        #
###############################################################################
"""Map out the prerequisite chains for courses at UNSW Sydney.

This program pulls from the UNSW Sydney handbook found at
www.handbook.unsw.edu.au along with timetable.unsw.edu.au to get the
courses being offered in a given year and maps them together by their
prerequisite chains. A visualiser is to come.

Typical usage example:
    pipenv run ./map_prereqs.py
"""


###############################################################################
# Imports                                                                     #
###############################################################################
import argparse
import logging
from utils.setup_logger import logger


###############################################################################
# Classes                                                                     #
###############################################################################
##################
# Public classes #
##################
class Course:
    """A data structure to store a course.

    This class stores information about a course as detailed from the
    UNSW handbook. Note: this is not course offerings or instances, this
    is for the metadata about the course as a whole.

    Attributes:
        code (int):
            The unique course code as identified in the handbook.
        name (str):
            The name of the course as described in the handbook.
        corequisites:
            Courses that are prerequisites but can be taken alongside
            this course.
        prerequisites:
            Courses that are direct prerequisites before one can take
            this course.
        exclusions:
            Courses that have the same content and cannot be taken in
            the same program.
        other_prerequisites:
            Conditions of enrolment that are not courses.
        description (str):
            A description of the course as taken from the handbook.
        uoc (int):
            The number of Units of Credit this course represents.
        offering_faculty (str):
            The faculty offering the course.
        offering_school (str):
            The school offering the course.
        field_of_education (str):
            The field of education of the course as taken from the
            handbook.
        delivery_mode (str):
            The method of delivery for the course - usually in-person
    """

    # Static class attribute definitions
    # NONE

    # Dunders
    def __init__(self, code, name, prerequisites=None,
                 corequisites=None, exclusions=None):
        self.code = code
        self.name = name
        self.prerequisites = []
        self.corequesites = []
        self.exclusions = []

        for course in prerequisites:
            self.add_prereq(course)

        for course in corequisites:
            self.add_coreq(course)

        for course in exclusions:
            self.add_exclusion(course)

    # Public methods
    def add_prereq(self, course):
        """Add a course as a prerequisite to this course."""

        if course in self.prerequisites:
            logger.warning("Course {course.code} is already a prerequisite \
                           for {self.name}.")
        else:
            self.prerequisites.append(course)
            logger.info("Added {course.code} as a prerequisite for \
                        {self.name}.")

    def add_coreq(self, course):
        """Add a course as a corequisite to this course."""

        if course in self.corequesites:
            logger.warning("Course {course.code} is already a corequisite for \
                            {self.name}.")
        else:
            self.corequesites.append(course)
            logger.info("Added {course.code} as a corequisite for \
                        {self.name}.")

    def add_exclusion(self, course):
        """Add a course as an exclusion to this course."""

        if course in self.exclusions:
            logger.warning("Course {course.code} is already an exclusion for \
                           {self.name}.")
        else:
            self.exclusions.append(course)
            logger.info("Added {course.code} as an exclusion for {self.name}.")

    # Private methods


class Program:
    """A data structure to store an enrolment program.

    This class stores information about an enrolment program such as
    Computer Science and includes all the core courses one must
    complete.

    Attributes:
        name (str):
            The name of the enrolment program
        code (int):
            The UNSW program code as found on the handbook
        courses ():
            The core courses of which this program is comprised. This
            is optional at initilisation.
    """

    # Static class attribute definitions
    # NONE

    # Dunders
    def __init__(self, name: str, code: int, courses: list = None):
        self.name = name
        self.code = code
        self.courses = []
        for c in courses:
            self.add_course(c)

    # Public methods
    def add_course(self, course: Course):
        """Add a course to the program."""

        if course in self.courses:
            logger.warning("Course {course.code} is already in program \
                           {self.name}.")
        else:
            self.courses.append(course)
            logger.info("Added {course.code} to {self.name}.")

    # Private methods


###################
# Private classes #
###################


###############################################################################
# Functions                                                                   #
###############################################################################
####################
# Public functions #
####################


#####################
# Private functions #
#####################


###############################################################################
# Main                                                                        #
###############################################################################
def main():
    """Main function for python module"""
    # -----------------
    # Declare variables
    # -----------------

    # -----------------
    # Setup
    # -----------------
    logging.basicConfig(filename='prereq_map.log', encoding='utf-8',
                        level=logging.DEBUG)

    # -----------------
    # Run :)
    # -----------------

    # Return
    return


###############################################################################
# Entry point                                                                 #
###############################################################################
if __name__ == "__main__":
    # Parse arguments
    logger.debug("Parsing arguments.")
    parser = argparse.ArgumentParser()
    parser.parse_args()
    logger.debug("Arguments parsed.")

    # Perform setup

    # Run main
    main()
