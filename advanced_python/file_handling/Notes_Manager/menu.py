def read_notes():
    with open("notes.txt","r") as file:
        return(file.read())
    
def append_note():
    with open("notes.txt","a") as file:
        (file.write(input("\n" + "enter the note :"))) 
    
def write_note():
    with open("notes.txt","w") as file:
        (file.write(input("enter the note :")))

running = True
while running :
    print("""Welcome to Notes Manager
      1. View Notes
      2. Add Notes
      3. Replace All Notes
      4. Exit""")
    try :
        x = int(input("Enter the Task Number :"))
    except ValueError :
        print("Invalid input")
        continue

    if x == 1 :
        notes=read_notes()
        print(notes)
    
    elif x == 2 :
        append_note()
        print("Appended")      
    
    elif x == 3 :
        write_note()
        print("Replaced")        
    
    elif x == 4 :
        print("Thanks for using Notes Manager!")
        break
    
    else :
        print("Invalid input")    