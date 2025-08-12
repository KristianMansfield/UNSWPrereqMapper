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
    # TODO Make arguments a dict
    def __init__(self, name, code, prerequisites=None,
                 corequisites=None, exclusions=None):
        self.code = code
        self.name = name
        self.prerequisites = []
        self.corequesites = []
        self.exclusions = []

        if prerequisites:
            for course in prerequisites:
                self.add_prereq(course)

        if corequisites:
            for course in corequisites:
                self.add_coreq(course)

        if exclusions:
            for course in exclusions:
                self.add_exclusion(course)

    def __str__(self):
        return f"Course \"{self.name}\" with course code {self.code}"

    # Public methods
    def add_prereq(self, course):
        """Add a course as a prerequisite to this course."""

        if course in self.prerequisites:
            logger.warning("Course %s is already a prerequisite for %s.",
                           course.code, self.name)
        else:
            self.prerequisites.append(course)
            logger.info("Added %s as a prerequisite for %s.", course.code,
                        self.name)

    def add_coreq(self, course):
        """Add a course as a corequisite to this course."""

        if course in self.corequesites:
            logger.warning("Course %s is already a corequisite for %s.",
                           course.code, self.name)
        else:
            self.corequesites.append(course)
            logger.info("Added %s as a corequisite for %s.", course.code,
                        self.name)

    def add_exclusion(self, course):
        """Add a course as an exclusion to this course."""

        if course in self.exclusions:
            logger.warning("Course %s is already an exclusion for %s.",
                           course.code, self.name)
        else:
            self.exclusions.append(course)
            logger.info("Added %s as an exclusion for %s.", course.code,
                        self.name)

    # Private methods


class Program:
    """A data structure to store an enrolment program.

    This class stores information about an enrolment program such as
    Computer Science and includes all the core courses one must
    complete.

    Attributes:
        name (str):
            The name of the enrolment program
        code (str):
            The UNSW program code as found on the handbook
        courses ():
            The core courses of which this program is comprised. This
            is optional at initilisation.
    """

    # Static class attribute definitions
    # NONE

    # Dunders
    def __init__(self, name: str, code: str, courses: list = None):
        self.name = name
        self.code = code
        self.courses = []

        if courses:
            for c in courses:
                self.add_course(c)

    def __str__(self):
        out_str = f"Program \"{self.name}\" \nwith course code " \
            + f"{self.code} \nhas the following courses:"

        course_string = "\n\t".join(x.code for x in self.courses)

        return f"{out_str}\n\t{course_string}"

    # Public methods
    def add_course(self, course: Course):
        """Add a course to the program."""

        if course in self.courses:
            logger.warning("Course %s is already in program %s.",
                           course.code, self.name)
        else:
            self.courses.append(course)
            logger.info("Added %s to %s.", course.code, self.name)

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
def make_request(url):
    """Make a request to the given URL and return the HTML content."""

    # TODO


def get_courses(content):
    """Get the list of courses out of the given content."""

    # TODO


def get_all_data(content):
    """Get the important data out of the given content."""

    # TODO


#####################
# Private functions #
#####################
def _get_prerequisites(content):
    """Get prerequisite data out of given HTML content"""

    # TODO


###############################################################################
# Main                                                                        #
###############################################################################
def main(parsed_args):
    """Main function for python module"""

    # -----------------
    # Declare variables
    # -----------------
    timetable_link = ''.join(["https://timetable.unsw.edu.au/",
                              parsed_args.year,
                              "/",
                              parsed_args.school,
                              parsed_args.campus,
                              ".html"
                              ])
    # https://www.handbook.unsw.edu.au/undergraduate/courses/2025/COMP6441

    # -----------------
    # Setup
    # -----------------

    # -----------------
    # Run :)
    # -----------------
    course1 = Course("Intro Course", "101")
    course2 = Course("Intro Course", "102", prerequisites=[course1])
    program_a = Program("BestProgram", "001", courses=[course1, course2])

    print(course1)
    print(course2)
    print(program_a)
    print(timetable_link)


###############################################################################
# Entry point                                                                 #
###############################################################################
if __name__ == "__main__":
    # Parse arguments
    logger.debug("Parsing arguments.")
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--school", nargs=1, default="COMP",
                        help="The school to scrape.")
    parser.add_argument("-y", "--year", nargs=1, default="2025",
                        help="The year to scrape.")
    parser.add_argument("-c", "--campus", nargs=1, default="KENS",
                        help="The campus to scrape.")
    parser.add_argument("-l", "--logfile", nargs=1, default="prereq_map.log",
                        help="The logfile location")
    parser.add_argument("-v", "--log-verbosity", nargs=1, default=1, type=int,
                        choices=[0, 1, 2, 3],
                        help="The depth to which we are logging. \n\t0 = \
                            DEBUG\n\t1 = INFO\n\t2 = WARNING\n\t3 = ERROR")
    # parser.add_argument - save HTML responses
    # parser.add_argument - online vs local storage
    args = parser.parse_args()   # Parse the arguments here

    # Set debug level correctly
    if args.log_verbosity == 0:
        LOG_LEVEL = logging.DEBUG
    elif args.log_verbosity == 1:
        LOG_LEVEL = logging.INFO
    elif args.log_verbosity == 2:
        LOG_LEVEL = logging.WARNING
    elif args.log_verbosity == 3:
        LOG_LEVEL = logging.ERROR
    else:
        logging.basicConfig(filename=args.logfile, encoding='utf-8',
                            level=logging.DEBUG)
        logger.warning("Invalid argument given to --log-verbosity."
                       + "Resetting to default.")
        LOG_LEVEL = logging.INFO

    logging.basicConfig(filename=args.logfile, encoding='utf-8',
                        level=LOG_LEVEL)

    logger.info("Arguments parsed.")
    logger.info("Using logfile: %s", args.logfile)
    logger.info("Starting main")

    # Run main
    main(args)

    logger.debug("Main terminated.")
