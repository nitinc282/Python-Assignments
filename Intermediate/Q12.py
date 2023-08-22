def cred(u,p1,p2):
    if p1==p2:
        pass
        return True
    elif p1!=p2:
        p2=input("Enter re pass Name:")
        if p1==p2:
            pass
        elif p1!=p2:
            p2=input("Enter re pass Name:")
            if p1==p2:
                pass
            elif p1!=p2:
                p2=input("Enter re pass Name:")
                if p1==p2:
                    pass
                elif p1!=p2:
                    return False
                    print("reahced max no of password attempt")


u=input("Enter User Name:")
p1=input("Enter password:")
p2=input("Re-enter password:")
result=cred(u,p1,p2)
if result ==True:
    print("You have succesfully login")
elif result ==False:
    print("You login failed")
