# ex at class 27/2/2024
# program to record the domain of email addresses from input then append to a list and print the list out with 
# the number of unique domains
def record_email_domain():
    email_list = []
    domain_list = []
    while True:
        email = input("Enter email address: ")
        if email == "done":
            break
        email_list.append(email)
    for email in email_list:
        domain = email.split("@")[1]
        if domain not in domain_list:
            domain_list.append(domain)
    print(domain_list)
    print(len(domain_list))