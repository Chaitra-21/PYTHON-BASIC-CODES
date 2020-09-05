#get user email address
email= input("What is your email addr?: ").strip()

#slice user name
user=email[:email.index("@"):1]

#slice domain name
domain=email[email.index("@")+1:]

#format msg
output="Your username is {} and your domain name is {}".format(user,domain)

#display output msg
print(output)
