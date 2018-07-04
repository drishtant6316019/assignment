''' Ques 1. Extract the user id, domain name and suffix from the following email addresses. 
emails = "mock26@facebook.com" , "gooli33@google.com" , "tiger42@amazon.com"
desired_output = [('mock26', 'facebook', 'com'), ('gooli33', 'google', 'com'), ('tiger42', 'amazon', 'com')] '''



import re
email_1="mock26@facebook.com"
email_2="gooli33@google.com"
email_3="tiger42@amazon.com"
p=re.compile(r"([a-zA-Z0-9]+)@([a-zA-Z]+).([a-z]+)")
def display(email):
    result=p.match(email)
    print(result[1],end=" ")
    print(result[2],end=" ")
    print(result[3])
display(email_1)
display(email_2)
display(email_3)
