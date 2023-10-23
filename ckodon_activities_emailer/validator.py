"""Module for extracting and validating email addresses."""
from os import listdir
import docx2txt
import re


for filename in listdir("../data/activities/"):
    # define path to each activities document
    doc_path = "../data/activities/" + filename

    try:
        # extract all text from word document at path
        search_string = docx2txt.process(doc_path)

        # search for email in text
        pattern = "[A-Za-z0-9.+\-_]+@[A-Za-z0-9.+\-_]+[A-Za-z]{2,}"  # regular expression for email
        matches = re.search(pattern, search_string)
        email_address = matches.group(0)
        print(email_address, doc_path)

    except Exception as exception:
        print("Error found at:", filename)
