guitar = {
	"E" : "022100",
	"F" : "133211",
	"F#" : "244322",
	"G" : "320003",
	"Ab" : "466544",
        "A" : "x02220",
        "A#" : "x13331",
        "Bb" : "x13331",
        "B" : "x24442",
        "C" : "x32010",
        "C#" : "x46664",
        "Db" : "x46664",
        "D" : "xx0232",
        "Eb" : "x68886",
        "x" : "xxxxxx",
        "Em" : "022000",
	"Fm" : "133111",
	"F#" : "244222",
	"Gm" : "355333",
	"Abm" : "466444",
        "Am" : "x02210",
        "A#m" : "x13321",
        "Bbm" : "x13321",
        "Bm" : "x24432",
        "Cm" : "x35543",
        "C#m" : "x46654",
        "Dbm" : "x46654",
        "Dm" : "xx0231",
        "Ebm" : "x68876",
        }

end_inputs = ["Nothing", "nothing", "Done", "done", "Finished", "finished", "stop", "Stop"]
def chords_func():
    while True:
        req=input("What guitar chord would you like to learn? \nPlease show me:")
        #normal input
        if req in guitar:
            print("\n  I know that one!!! \n ")
            print (req + ":     " + guitar[req])
            print ("\n")
            continue
        
        #For 7th Chords
        elif "7" in req:
            print("\n Sorry, no 7th chords in this version. \n Patience, please.\n")
            continue

        #for a joke
        elif "life" in req:
            print("\n   42, next question, please \n")
            continue

        #to stop the program
        elif req in end_inputs:
            print("\n  Thank you for trying my Python guitar chord program. \n       Have a good day!")
            break

        #for unknown input
        else:
            print("\nSorry, I don't recognize that one. \n \n")
            continue
        

