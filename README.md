# ckodon-activities-emailer
Python program I wrote to email reviewed activities lists stored in Microsoft Word format to their intended recipients.  
 - The program extracts each recipient's email address from their activities document using the `docx2text` package and the `re` package from the standard library.
 - It then sends the document to the recipients as an email attachment using the `email` and `smtplib` packages of the standard library.