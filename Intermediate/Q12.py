# def cred(u,p1,p2):
#     if p1==p2:
#         return True
#     elif p1!=p2:
#         p2=input("Enter re pass Name:")
#         if p1==p2:
#             return True
#         elif p1!=p2:
#             p2=input("Enter re pass Name:")
#             if p1==p2:
#                 return True
#             elif p1!=p2:
#                 p2=input("Enter re pass Name:")
#                 if p1==p2:
#                     return True
#                 elif p1!=p2:
#                     print("reahced max no of password attempt")
#                     return False
                    

# u=input("Enter User Name:")
# p1=input("Enter password:")
# p2=input("Re-enter password:")
# result=cred(u,p1,p2)
# if result ==True:
#     print("You have succesfully login")
# elif result ==False:
#     print("You login failed")

user_credentials = {
    "user1": "password123",
    "user2": "securepass",
    "user3": "letmein"
}

def login():
    login_attempt =0
    
    while login_attempt<3:
        user=input("Enter User Name:")
        password=input("Enter User Password:")
        if user in user_credentials:
            if user_credentials[user]==password:
                print("Login successful!")
                break
            else:
                print("Incorrect password. Please try again.")
        else:
            print("Username not found. Please try again.")

        login_attempt += 1
    if login_attempt == 3:
        print("You have exceeded the maximum number of login attempts. Account locked.")

login()

