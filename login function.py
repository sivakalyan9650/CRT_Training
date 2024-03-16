#login function which accepts the user only when username and password are same
#display a msg login successful otherwise it keeps asking the user to enter credentians until they are corret

def login():
    
    while True:
        username=input("enter username:")
        password=input("enter password:")
        
        if(username==password):
            print("login successful")
            break
        
        else:
            print("login unsuccessful")
            
        
        
        
    

login()
    
