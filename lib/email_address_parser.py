# your code goes here!
import re
class EmailAddressParser:

    def __init__(self, addresses):
        self.emails = addresses
        email_finder = re.compile(r'[, ]+')
        self.parsed_emails = sorted(email_finder.split(self.emails))
        email_validator = re.compile(r'\w+\.?\w*@\w+\.\w+')
        self.valid_emails = [email for email in self.parsed_emails if email_validator.match(email)]
        

    def parse(self):
        return self.valid_emails
    

test = re.findall(r'\w+\.?\w*@\w+\.\w+', "talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
print(sorted(test))