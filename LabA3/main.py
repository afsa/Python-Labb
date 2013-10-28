#coding=latin1
'''
Created on 28 okt 2013

@author: MJ & YJ
'''

#Main class with UI and secret languages methods
class secretLanguages:
    vowels = "aeiouy���AEIOUY���"; #All vowels in the swedish alphabet.
    exceptions = " .,!?:;#%&$�@-_+*/";
    languages = None;
    
    #Menu toggles if a menu should be used and loop toggles if the script should loop
    def __init__ (self, menu = True, loop = True):
        if not menu: #If no menu opens do nothing on init
            return True;
        
        #Create list of languages
        self.languages  = [[1, "Viskspr�ket", self.whisper], [2, "R�varspr�ket", self.pirate],
                           [3, "Fyllespr�ket", self.drunk], [4, "Bebisspr�ket", self.baby],
                           [5, "Allspr�ket", self.all], [6, "Fikonspr�ket", self.fig], [7, "Avsluta"]];
        
        print("\nVilket spr�k vill du anv�nda?");
        print(self.createList());
        languageNr = input();
        if languageNr.isdigit() and int(languageNr) > 0 and int(languageNr) < 8: #Validate input
            languageNr = int(languageNr);
            if languageNr == 7: #If exit
                print("Applikationen avslutad.");
                exit();
            text = input("Skriv din mening: ");
            print(self.languages[languageNr-1][1] + ": " + self.languages[languageNr-1][2](text)); #Run language
        else:
            print("Error: Inv�rde m�ste vara en siffra mellan 1 och 7"); #Invalid input
            
        if loop:
            self.__init__(); #Do a loop
        
    #Create a list of languages to choose from
    def createList(self):
        output = ""
        for i in self.languages:
            output += str(i[0]) + " " + i[1] + "\n";
        return output;
    
    #Whisper language
    def whisper(self, text):
        output = "";
        tempList = list(text);
        
        for i in tempList:
            if not (i in self.vowels):
                output += i;
        return output;
    
    #Pirate language
    def pirate(self, text):
        output = "";
        tempList = list(text);
        
        for i in tempList:
            if i in self.vowels or i in self.exceptions:
                output += i;
            else:
                output += "O" + i.lower() + "o" if i.isupper() else "o" + i + "o"; #Add O if vowel is uppercase else o
        return output;
    
    #Drunk language
    def drunk(self, text):
        output = "";
        tempList = list(text);
        
        for i in tempList:
            if i in self.vowels:
                output += i + "f" + i.lower(); #No need for uppercase check
            else:
                output += i;
        return output;
    
    #Baby language
    def baby(self, text):
        output = "";
        tempList = text.split(" ");
        
        for i in tempList:
            output += " " if len(output) > 0 else ""; #Add space between words
            for j in range(len(i)):
                if i[j:j+1] in self.vowels:
                    output += 3 * i[0:j+1];
                    break;
        return output;
    
    #All language
    def all(self, text):
        output = "";
        tempList = text.split(" ");
        
        for i in tempList:
            output += " " if len(output) > 0 else ""; #Add space between words
            uppercase = False;
            for j in range(len(i)):
                if i[j:j+1].isupper():
                    uppercase = True;
                    
                if i[j:j+1] in self.vowels:
                    output += (i[j:j+1].upper() if uppercase else i[j:j+1]) + i[j+1:].lower() + i[:j].lower() + "all"; #Permute chars in word and add all in the end
                    break;
        return output;
    
    #Fig language
    def fig(self, text):
        output = "";
        tempList = text.split(" ");
        
        for i in tempList:
            output += " " if len(output) > 0 else ""; #Add space between words
            uppercase = False;
            for j in range(len(i)):
                if i[j:j+1].isupper():
                    uppercase = True;
                    
                if i[j:j+1] in self.vowels:
                    output += ("F" if uppercase else "f") + "i" + i[j+1:].lower() + i[:j+1].lower() + "kon"; #Permute chars in word, add fi in the beginning and kon in the end
                    break;
        return output;
        
if __name__ == "__main__":
    secretLanguages(); #Autostart