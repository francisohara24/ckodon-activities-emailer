"""Module for validating email adresses."""
from os import listdir
import helpers

email_addresses = []  # list of email addresses to be validated.

# Extract the path to each word document and extract addresses
for filename in listdir("../data/activities/"):
    # concatenate file name with directory path
    path = "../data/activities/" + filename

    # extract email address from word document at path
    email_address = helpers.extract_address(path)

    # validate email address
    is_valid = helpers.validate(email_address)

    print(is_valid, email_address)
