def TimeConverter(Seconds):
    Day = Seconds // (24*3600)
    Seconds = Seconds % (24*3600)
    Hour = Seconds // 3600
    Seconds = Seconds % 3600
    Minute = Seconds // 60
    Seconds = Seconds % 60
    if Day == 1:
        a = "Day"
        print("The result is: " + "%d" % Day, a, "%02d:%02d:%02d." % (Hour, Minute, Seconds))
    elif Day == 0:
        print("The result is: %02d:%02d:%02d" % (Hour, Minute, Seconds))
    else:
        a = "Days"
        print("The result is: " + "%d" % Day, a, "%02d:%02d:%02d." % (Hour, Minute, Seconds))
    return 

try:
    Variable = input("Insert the desired second: ")
    Seconds = int(Variable)
    if Seconds < 0:
        print("Invalid input, your input must be greater than or equal to 0!")
    else:    
        TimeConverter(Seconds)
except:
    print("Invalid input, your input must be in INTEGER format!")
 