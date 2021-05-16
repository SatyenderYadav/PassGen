from config.config import *



def check_password_strength(data=None):


    try:


        special = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        capital = re.compile('[A-Z]')
        small = re.compile('[a-z]')
        digit = re.compile('[0-9]')
        password = data['password']
        if(len(password)>=9):
            if(special.search(password) == None):
                
                session['password'] = "At Least One Special Character Nedded"
                return(0,"At Least One Special Character Nedded")
            
            
            else:
                if(capital.search(password) == None):
                    session['password'] ="At Least One Capital Character Nedded"
                    return(0,"At Least One Capital Character Nedded")
                
                
                else:
                    if(small.search(password) == None):
                        session['password'] ="At Least One Small Character Nedded"
                        return(0,"At Least One Small Character Nedded")
                    
                    
                    else : 
                        if(digit.search(password) == None):
                            session['password'] ="At Least One Digit Character Nedded"
                            return(0,"At Least One Digit Character Nedded")
                        
                        else:
                            session['password'] ="Strong Password"
                            return(1,"Strong Password")
                        
                        
        else :
            session['password'] ="Password Is Too Short at least 9 Character"
            return(0,"Password Is Too Short ")

    except :
        session['password'] ="Some Error Occurred"
        return(0,"Some Error Occurred")

# get random string password with letters, digits, and symbols
def get_random_password_string(length):

        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters) for i in range(length))
        return(password)


            
def password_generation(data=None):
    try:
        length = int(data['length'])
        if(length<15):
            password = get_random_password_string(length)
            session['password'] = f"Your password : {password}" 
            return(1,"password generated")
        else:
            session['password'] = "Some Error Occurred"
            return(0,"Some Error Occurred")
    except:
        session['password'] = "Some Error Occurred"
        return(0,"Some Error Occurred")



       
    
