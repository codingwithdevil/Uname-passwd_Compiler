import os
from time import sleep as wait
from subprocess import call

class colour:
    pallet = [
        '\033[1;31m',
        '\033[1;32m',
        '\033[1;33m',
        '\033[1;34m'
    ]
    mainlogo= """


    {0}  _____                      _ _           
    {0} / ____|                    (_) |          
    {0}| |     ___  _ __ ___  _ __  _| | ___ _ __ 
    {0}| |    / _ \| '_ ` _ \| '_ \| | |/ _ \ '__|
    {0}| |___| (_) | | | | | | |_) | | |  __/ |   
    {0} \_____\___/|_| |_| |_| .__/|_|_|\___|_|   
    {0}                      | |                  
    {0}                      |_|                 

                    {1}Coded by coding With Devil

    """.format(pallet[0],pallet[1])
    
    use = """ 
    {0}Usage :-
        {1}This tool is Help to easly combile username in wordlist [Password list], in openbullet,storm etc.
        {1}Useful for build Passwoard list[singleusername:pass],(this tool is only useful if u Dont have single target config)
        {1}eg:- 
        {1}     user:pass1
        {1}     user:pass2 
        {1}     .......... 
            
        """.format(pallet[3],pallet[1])

if __name__ == '__main__':

    try:
        call("clear")
        print(colour.mainlogo)
        wait(2)
        print(colour.use)
        wait(2)
        uname = input("\033[1;33mWhat is The username You want to add in password list: \033[1;34m")
        print(" ") 
        path = input("\033[1;33mPasswoard list path: \033[1;34m")
        print(" ")
        print("{0}Checking Passwordlist path".format(colour.pallet[3]))
        wait(2)
        if os.path.exists(path):
            info ="""

            {0}Password List path found 

            {0}Starting Process Please wait >>>
            """.format(colour.pallet[1])
            if len(open(path).readlines()) != 0:
                with open(path, "r") as f:
                    lines = f.readlines()
                with open(path, "w") as f:
                    for line in lines:
                        f.write(uname + ":" + line)
                    print("{0}Process Finished .... ".format(colour.pallet[1]))
            else:
                exit("{0}Password list is Empty".format(colour.pallet[0]))
        else:
            print("{0}Passwoard Path is not exist.. \n".format(colour.pallet[0]))
    except Exception as e:
        print(e)
        exit("{0}Error occured \n".format(colour.pallet[0]))
    except KeyboardInterrupt:
        exit("{0}Keyboard interrupt.. \n".format(colour.pallet[0]))