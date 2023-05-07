MORSE_CODE = { ".-": "A","-...": "B","-.-.": "C","-..": "D",
    ".": "E","..-.": "F","--.": "G","....": "H","..": "I",
    ".---": "J","-.-": "K",".-..": "L","--": "M","-.": "N",
    "---": "O",".--.": "P","--.-": "Q",".-.": "R","...": "S",
    "-": "T","..-": "U","...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y","--..": "Z","-----": "0",".----": "1","..---": "2",
    "...--": "3","....-": "4",".....": "5","-....": "6","--...": "7",
    "---..": "8","----.": "9",".-.-.-": ".","--..--": ",","..--..": "?",
    "-.-.--": "!","-....-": "-",".----.": "'","-..-.": "/","-.--.": "(",
    "-.--.-": ")",".-...": "&","---...": ":","-.-.-.": ";","-...-": "=",
    ".-.-.": "+","..--.-": "_",".-..-.": "\"","...-..-": "$",
    ".--.-.": "@","... --- ...":"SOS"}
def decode_morse(morse_code):
    translation=""
    #remove possible whitespaces from start/end
    formatedstr= morse_code.strip()
    #create a list of the words
    words=formatedstr.split("   ")
    # iterate through the list
    for word in words:
        #for each word create a list containing the letters
        letters= word.split(" ")
        for letter in letters:
            #append the translated values in our final string 
            translation+= MORSE_CODE[letter]
        #seperate the words
        translation+=" "
    #return the final translation removing the whitespace at the end
    return translation.strip()

if __name__=="__main__":
    #get user input and then print the tranlation
    user= input(("Enter the morse code you would like to decypher!\n"))
    print(decode_morse(user))
