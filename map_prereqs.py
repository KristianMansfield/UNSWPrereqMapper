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
https://www.handbook.unsw.edu.au along with timetable.unsw.edu.au to get
the courses being offered in a given year and maps them together by
their prerequisite chains. A visualiser is to come.

This script should have several stages, with each run independently:
1. Query network and store information.
    Gather information from the urls and store the html to disk.
2. Build a model built on classes.
    Open the stored information from disk and build the relevant class
    structures. Store these classes to disk in an importable method for
    usage later.
3. Visualise the graph.
    Open a graph so that one can view the prerequisite chains. This
    should also have some visualisation differences to show corequisites
    and exclusionary courses

Typical usage example:
    pipenv run ./map_prereqs.py

TODO:
    * Write more documentation. Adhere to the PEP257 regarding using the
    docstring as the usage output of the scripts invocation.
    * Put the type inference on all function definitions.
"""


###############################################################################
# Imports                                                                     #
###############################################################################
from __future__ import annotations
import argparse
import logging
import os
import json
import re
from urllib.parse import urlparse

import matplotlib.pyplot as plt
import networkx as nx
import requests
from bs4 import BeautifulSoup

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
        name:
            The name of the course as described in the handbook.
        code:
            The unique course code as identified in the handbook.
        postgrad:
            Whether or not this course is a postgraduate course.
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

    TODO:
        Add the following attributes:
            description (str, optional):
                A description of the course as taken from the handbook.
            uoc (int, optional):
                The number of Units of Credit this course represents.
            offering_faculty (str, optional):
                The faculty offering the course.
            offering_school (str, optional):
                The school offering the course.
            field_of_education (str, optional):
                The field of education of the course as taken from the
                handbook.
            delivery_mode (str, optional):
                The method of delivery for the course - usually
                in-person
        Provide docstring for method listing
    """

    # Static class attribute definitions
    # NONE

    # Dunders
    def __init__(self, name: str, code: str, postgrad: bool = False) -> None:
        """Create a new Course for visualisation maps.

        Args:
            name (str): The name of the course.
            code (str): The course code.
            postgrad (bool, optional):
                Whether this course is offered for postgrad students
                instead of undergrad students. Defaults to False.
        """

        self.code: str = code
        self.name: str = name
        self.prerequisites: list[Course] = []
        self.corequesites: list[Course] = []
        self.exclusions: list[Course] = []

        if postgrad:
            self.handbook_url = "https://www.handbook.unsw.edu.au/" \
                + "postgraduate/courses/2025/" + code
        else:
            self.handbook_url = "https://www.handbook.unsw.edu.au" \
                + "undergraduate/courses/2025/" + code

    def __str__(self) -> str:
        return f"Course \"{self.name}\" with course code {self.code}"

    # Public methods
    def add_prereq(self, course: Course) -> None:
        """Add a course as a prerequisite to this course."""
        if course in self.prerequisites:
            logger.warning("Course %s is already a prerequisite for %s.",
                           course, self.name)
        else:
            self.prerequisites.append(course)
            logger.info("Added %s as a prerequisite for %s.", course,
                        self.name)

    def add_coreq(self, course: Course) -> None:
        """Add a course as a corequisite to this course."""
        if course in self.corequesites:
            logger.warning("Course %s is already a corequisite for %s.",
                           course.code, self.name)
        else:
            self.corequesites.append(course)
            logger.info("Added %s as a corequisite for %s.", course,
                        self.name)

    def add_exclusion(self, course: Course) -> None:
        """Add a course as an exclusion to this course."""
        if course in self.exclusions:
            logger.warning("Course %s is already an exclusion for %s.",
                           course, self.name)
        else:
            self.exclusions.append(course)
            logger.info("Added %s as an exclusion for %s.", course,
                        self.name)

    # Private methods
    # NONE


# class Program:
#     """A data structure to store an enrolment program.

#     This class stores information about an enrolment program such as
#     Computer Science and includes all the core courses one must
#     complete.

#     Attributes:
#         name (str):
#             The name of the enrolment program
#         code (str):
#             The UNSW program code as found on the handbook
#         courses ():
#             The core courses of which this program is comprised. This
#             is optional at initilisation.
#     """

#     # Static class attribute definitions
#     # NONE

#     # Dunders
#     def __init__(self, name: str, code: str, courses: list = None):
#         self.name = name
#         self.code = code
#         self.courses = []

#         if courses:
#             for c in courses:
#                 self.add_course(c)

#     def __str__(self):
#         out_str = f"Program \"{self.name}\" \nwith course code " \
#             + f"{self.code} \nhas the following courses:"

#         course_string = "\n\t".join(x.code for x in self.courses)

#         return f"{out_str}\n\t{course_string}"

#     # Public methods
#     def add_course(self, course: Course):
#         """Add a course to the program."""

#         if course in self.courses:
#             logger.warning("Course %s is already in program %s.",
#                            course.code, self.name)
#         else:
#             self.courses.append(course)
#             logger.info("Added %s to %s.", course.code, self.name)

#     # Private methods


class GraphVisualisation:
    """A graph visualisation class for the course prerequisite chains.

    View prerequisites, corequisites, and exclusionary courses based
    on the Course class defined elsewhere. This generates a graph for
    visually checking prerequisites chains.

    Attributes:
        prerequisites (list[Course]):
            The list of connected edges between courses. Entries are in
            the form (a, b) where a is a Course that has a prerequisite
            of Course b.
    """

    # Static class attribute definitions
    # NONE

    # Dunders
    def __init__(self) -> None:
        """Creates a new visualisation mapper for course chains."""
        self.prerequisites: list[Course] = []

    # Public methods
    def add_edge_prerequisite(self, a: Course, b: Course) -> None:
        """Appends a vertex pair to the visual list."""
        temp = [a, b]
        self.prerequisites.append(temp)

    def visualise(self) -> None:
        """Opens a visual graph of the verticies."""
        G = nx.Graph()
        G.add_edges_from(self.prerequisites)
        nx.draw_networkx(G)
        plt.show()

    # Private methods
    # NONE


###################
# Private classes #
###################


###############################################################################
# Functions                                                                   #
###############################################################################
####################
# Public functions #
####################
# --- Primary runner functions --- #
def store_data_to_disk(timetable_link: str) -> list[str]:
    """Get all courses from the timetable website.

    Get a list of courses from the timetable website, store their HTML,
    and return the list of courses as a list of URLs.

    Parameters:
        timetable_link (str):
            A url to the timetable page.

    Returns:
        list[str]: A list of urls representing the found courses."""

    logger.info("Starting stage 1: gathering courses.")

    timetable_content = query_url(timetable_link)
    courses_listed = get_courses_list_from_timetable(timetable_content)

    for course_url in courses_listed:
        # Make a request for that course
        query_url(course_url)

    return courses_listed


# --- Secondary functions --- #
def query_url(url: str, use_cache: bool = True) -> str:
    """Get HTML content for a url from internet or local storage."""
    if use_cache:
        # Check if there is a cache
        try:
            logger.debug("Attempting to open file for url %s", url)
            return open_contents(url)
        except FileNotFoundError:
            logger.info("No cached file for url %s", url)
            return make_request(url)


def make_request(url: str, save_response: bool = True) -> str:
    """Make a request to the given URL and return the HTML content."""
    logger.info("Making request for %s", url)
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
    except requests.HTTPError as e:
        logger.error("URL %s returned a status code of %d.",
                     e.request.url, e.response.status_code)

    if save_response:
        logger.info("Saving HTML response for url %s.", url)
        save_contents(url, resp.text)

    return resp.text


def open_contents(url: str) -> str:
    """Get contents from cached results for given URL query."""
    logger.info("Searching for cached response for %s.", url)

    domain = urlparse(url)

    # This has static file locations. Should probs be a global.
    file_location = "sites/" + domain.netloc + "/" + domain.path + ".html"

    try:
        with open(file_location, 'r', encoding='utf-8') as f:
            logger.info("Content found. Returning.")
            html_content = f.read()
            return html_content
    except FileNotFoundError as exc:
        logger.error("File not found for url %s.", url)
        raise FileNotFoundError from exc


def save_contents(url: str, html_content: str) -> None:
    """Save the given HTML content to a file in a structured manner."""
    domain = urlparse(url)

    # TODO This has static file locations. Should probs be a global.
    save_location = "sites/" + domain.netloc + "/" + domain.path + ".html"

    # Make sure the path for this file exists
    os.makedirs(os.path.dirname(save_location), exist_ok=True)

    soup = BeautifulSoup(html_content, "html.parser")

    with open(save_location, 'w', encoding='utf-8') as f:
        logger.info("Saving content for url %s to disk.", url)
        f.write(soup.prettify())


def get_courses_list_from_timetable(content: str) -> list[str]:
    """Get list of urls that point to courses found in given content."""
    soup = BeautifulSoup(content, "html.parser")
    table_headers = soup.find_all("td", class_="classSearchSectionHeading")
    identified_courses = []

    for th in table_headers:
        logger.debug("Parsing table headers: %s", th)
        # Remember if this is iterating through postgrad or undergrad courses
        # This depends on there being a visiable line titled "Undergraduate"
        # in the html content - otherwise it will default to postgrad.
        if "Undergraduate" in th.parent.parent.parent.parent.previous_sibling\
                .previous_sibling.text:
            logger.debug("Undergrad found.")
            url_course_string = "undergraduate"
        else:
            logger.debug("No undergrad found. Assuming postgraduate.")
            url_course_string = "postgraduate"

        # Find the first table and get all the rows of that table.
        course_entries = th.parent.parent.find("table").find_all("tr")

        # Remove the first entry as this is a header row
        course_entries.pop(0)

        for c in course_entries:
            logger.debug("Parsing course entry: %s", c)

            # Skip row spacers
            if c.find("td", class_="rowSpacer"):
                logger.debug("Entry skipped.")
                continue

            course_code = c.find_all("td")[0].text
            course_handbook_url = "https://www.handbook.unsw.edu.au/" \
                + url_course_string \
                + "/courses/2025/" \
                + course_code

            if course_handbook_url not in identified_courses:
                logger.debug("Adding course %s to list.", course_code)
                identified_courses.append(course_handbook_url)
            else:
                logger.debug("Course %s already found.", course_code)

    return identified_courses


def get_all_data(content: str) -> dict[str, any]:
    """Get the important data out of the given content."""
    course_data = {}
    course_data['prerequisites'] = _get_prerequisites(content)
    course_data['name'] = _get_name_from_content(content)
    course_data['code'] = _get_code_from_content(content)
    course_data['is_postgrad'] = _get_postgrad_from_content(content)

    return course_data


#####################
# Private functions #
#####################
def _content_to_json(content: str) -> dict[any, any]:
    """Get the json data out of the HTML response"""
    soup = BeautifulSoup(content, "html.parser")
    data_script = soup.find("script", id="__NEXT_DATA__").text
    logger.debug("Found data script.")
    return json.loads(data_script)


def _get_prerequisites(content: str) -> list[str]:
    """Get prerequisite data out of given HTML content"""
    course_data = _content_to_json(content)
    try:
        page_content = course_data['props']['pageProps']['pageContent']
        # TODO: handle the case where the course has multiple rules
        prerequisite_info = page_content['enrolment_rules'][0]['description']
        logger.debug("Successfully parsed enrolment rules.")
    except TypeError:
        logger.warning("Could not parse enrolment rules. "
                       + "Assuming no conditions of enrolment.")
        return []
    except IndexError:
        logger.warning("Could not parse enrolment rules. "
                       + "Assuming no conditions of enrolment.")
        return []

    prerequisites = re.findall(r"COMP\d\d\d\d", prerequisite_info,
                               re.IGNORECASE)
    logger.debug("Regex match for courses: %s", prerequisites)

    return prerequisites


def _get_name_from_content(content: str) -> str:
    """Get the course name from the content given by parsing HTML."""
    course_data = _content_to_json(content)
    try:
        page_content = course_data['props']['pageProps']['pageContent']
        course_name = page_content['title']
        logger.debug("Successfully parsed course name.")
        return course_name
    except TypeError:
        logger.error("Could not parse course name.")
        return ""


def _get_code_from_content(content: str) -> str:
    """Get the course code from the content given by parsing HTML."""
    course_data = _content_to_json(content)
    try:
        page_content = course_data['props']['pageProps']['pageContent']
        course_code = page_content['cl_code']
        logger.debug("Successfully parsed course code.")
        return course_code
    except TypeError:
        logger.error("Could not parse course code.")
        return ""


def _get_postgrad_from_content(content: str) -> bool:
    """Get the course code from the content given by parsing HTML."""
    course_data = _content_to_json(content)
    try:
        page_content = course_data['props']['pageProps']['pageContent']
        # TODO: handle the case where the course is offered at multiple
        # levels
        course_pgrd = page_content['study_level'][0]['label']
        logger.debug("Successfully parsed course level.")

        if course_pgrd == "Postgraduate":
            return True
        else:
            return False

    except TypeError:
        logger.error("Could not parse course level.")
        return True


###############################################################################
# Main                                                                        #
###############################################################################
def main(parsed_args):
    """Main function for python module"""

    # -----------------
    # Setup
    # -----------------
    timetable_link = ''.join(["https://timetable.unsw.edu.au/",
                              parsed_args.year,
                              "/",
                              parsed_args.school,
                              parsed_args.campus,
                              ".html"
                              ])

    # -----------------
    # Run :)
    # -----------------
    # --- STAGE ONE ---#
    # --- Query the network and store information to disk ---#
    courses_found = store_data_to_disk(timetable_link)

    # --- STAGE TWO ---#
    # --- Open content from disk and create class structures ---#
    courses = []
    for course_url in courses_found:
        course_html = open_contents(course_url)
        course_data = get_all_data(course_html)

        new_course = Course(course_data.get('name'),
                            # TODO Change this to be parsing from html
                            course_data.get('code'),
                            course_data.get('is_postgrad'))

        # Add the prerequisites to the course class and visualiser
        for prereq in course_data.get('prerequisites'):
            new_course.add_prereq(prereq)

        courses.append(new_course)

    # --- STAGE THREE ---#
    # --- Create a graph from class structures and visualise ---#
    visualiser = GraphVisualisation()

    for course in courses:
        for prereq in course.prerequisites:
            visualiser.add_edge_prerequisite(course.code, prereq)

    # Show the graph
    visualiser.visualise()


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
                        help="The logfile location.")
    parser.add_argument("--use-cache", nargs=1, default=True,
                        help="Default to local storage if it exists.")
    parser.add_argument("--offline", nargs=1, default=False,
                        help="If this option is set, use only locally stored \
                            HTML responses.")
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
