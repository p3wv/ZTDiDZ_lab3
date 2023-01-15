import string
import random
import enchant

dict = enchant.Dict("en_US")

password_list = []

def random_password_generator():

    character_list = ""

    character_list+=string.ascii_lowercase
    character_list+=string.ascii_uppercase
    character_list+=string.digits
    character_list+=string.punctuation

    while(len(password_list) < 8):
        password_list.append(random.choice(character_list))
        

if __name__ == "__main__":

    random_password_generator()
    # print(password_list)
    
    password = ''.join(str(i) for i in password_list)

    print(password)

    while (dict.check(password) == True):
        random_password_generator()
        print(password_list)
        print(password)



    
