import smtplib
from string import Template

filename = "contacts.txt"

smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)

smtp.starttls

# put into env var
smtp.login('MY_ADDRES', 'PASSWORD')

# read contacts and emails
def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', enconding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
        return names, emails

# read template and returns template object with content
def read_template(filename):
    with open(filename, 'r', enconding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.login("eliot643@densebpoqq.com", "a371b6bf76a74041a4e9d7f01b528e7d")
# message = "teste"
# server.sendmail("eliot643@densebpoqq.com", "reric10909@eilnews.com", message)
# server.quit()