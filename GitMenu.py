import sys
import os


cwd = os.getcwd()

ans=True
while ans:
    print ("""
    1. Credenziali Iniziali
    2. Clone Javascript_Knockout_QUnit_Example
    3. Modifica ReadMe
    4. Commit
    5. Push
    6. Exit/Quit
    """)
    ans=input("What would you like to do? ")
    if ans=="1": 
      print("\n -----------------------------------------")
      print("\n Credenziali Iniziali")
      os.system("git config --global user.email 'domenicozinzi@gmail.com'")
      os.system("git config --global user.name 'xxx'")
      print("\n -----------------------------------------")
    elif ans=="2":
      print("\n -----------------------------------------")
      print("\n Javascript_Knockout_QUnit_Example")
      os.system("git clone https://github.com/thedom85/Javascript_Knockout_QUnit_Example.git")
    elif ans=="3":
      print("\n -----------------------------------------")
      print("\n Modifica ReadMe")
      os.system("git init")
      os.system("echo Test >> Javascript_Knockout_QUnit_Example/README.md")
    elif ans=="4":
      print("\n -----------------------------------------")
      print("\n Commit")
      os.system("git add .")
      os.system("git commit -m scheduledCommit")
      os.system("git push --all")
    elif ans=="5":
      print("\n -----------------------------------------")
      print("\n Push")
      os.system("git remote add origin https://github.com/thedom85/Javascript_Knockout_QUnit_Example.git ")
      os.system("git pull origin master")
      os.system("git push -f origin master")
    elif ans=="6":
      print("\n Goodbye") 
      quit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 