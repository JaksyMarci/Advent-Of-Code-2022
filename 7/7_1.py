filesystem = {}
current_path = ''
size = 0


with open('example.txt', 'r') as f:
    for line in f:
        if (line[0] == '$'): #$
            if (line[2] == 'c'): #CD
                if (line[5] == '/'): #CD /
                    current_path = ''
                elif(line[5] == '.'): #CD ..
                    #delete entry from current_path
                    pass
                else: #CD <dirname>
                    #add the selected dir to path ??
                    pass

            elif (line[2] == 'l'): #LS
                #add the following lines until a command is read
                pass
        else: #some directory is being listed, this is the output
            if (48 <= ord(line[0]) <= 57): #this is a FILE with a SIZE
                pass
            else: #this is a DIRECTORY
                pass
