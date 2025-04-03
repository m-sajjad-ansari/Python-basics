email=input("Enter your email : ")
# index=email.index("@")
# username=email[:index]
# domain=email[index+1:]
print(f"Username is {email[:email.index("@")]}")
print(f"Domain is {email[email.index("@")+1:]}")