import os,sys
import time
import compileall

def encode1 () :
    import os

    mesaage =input(str("enter the text for encode >> "))
    tranzlated = str('')

    i = len(mesaage) - 1
    while i >= 0 :
        tranzlated =str(tranzlated + mesaage [i])
        i = i - 1

    f = open ('encode.txt','a')
    f.write (str(tranzlated)+'\n')
    f.close ()


def encode2 () :
    import compileall

    print ("1- for encode file ")
    print ("2- for encode dir ")

    e = input (">>> ")

    if e == '1' :
        w = input(str("enter name of file for encode >> "))
        compileall.compile_file (w)
    elif e == '2' :
        k = input(str('enter name of dir for encode >> '))
        compileall.compile_dir (k)

def styel () :
    text = '''


\033[1;31m
 __  __ _____ ____  _  __    ___     ___    _____ ____  
|  \\/  | ____|  _ \\| |/ /   / \\ \\   / / \\  |_   _/ ___|
| |\/| |  _| | |_) | ' /   / _ \\ \\ / / _ \\   | | \\___ \\
| |  | | |___|  _ <| . \\  / ___ \\ V / ___ \\ _| |  ___) |
|_|  |_|_____|_| \\_\\_|\\_\\/_/   \\_\\_/_/   \\_(_)_| |____/

\033[1;35m
         _____           ____            _   _
        |_   _|         / ___|          | \ | |
          | |    _____  \___ \   _____  |  \| |
          | |   |_____|  ___) | |_____| | |\  |
          |_|           |____/          |_| \_|

\033[1;33m
         C7 TEAM / BLACK SHADOW / PROJECT SEGMA 
          
       
\033[1;32m

'''
    print (text)

def encode3 () :
    print ("1- for encode file ")
    print ("2- for decode file ")
    print ("")
    lll = input (">>> ")
    if lll == "1" :
        os.system ("""
echo 'enter name of file >> '
read g

gpg -c $g

""")

    elif lll == "2" :
        os.system ("""
echo 'enter name of file >> '
read g

gpg $g

""")













  
os.system ("c")
styel ()
print ("")
print ("1- encode text ")
print ("2- encode file/dir ")
print ("3- encode file with passeword && decode it ")
print ("#- exit ")
print ("")

kl = input (">>> ")
if kl == "1" :
    os.system ("c")
    styel ()
    encode1 ()
elif kl == "2" :
    os.system ("c")
    styel ()
    encode2 ()
elif kl == "3" :
    os.system ("c")
    styel ()
    encode3 ()

elif kl == "#" :
    sys.exit ()
