alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
decalage = int(input("Entrez le décalage:"))
mot = str(input("Entrez la chaîne de caractère:")).lower()
mot_code = []
mot_decode = []

for everyLetter in mot:
    extremum = 0
    if everyLetter in alphabet:
        if alphabet.index(everyLetter)+decalage > len(alphabet):
            extremum = len(alphabet)
        mot_code.append(alphabet[alphabet.index(everyLetter)+decalage-extremum])
        extremum = 0
        if alphabet.index(everyLetter)-decalage < 0:
            extremum = len(alphabet)
        mot_decode.append(alphabet[alphabet.index(everyLetter)-decalage+extremum])
    else:
        mot_code.append(everyLetter)
        mot_decode.append(everyLetter)


print("Votre chaîne de caractère codée:"+''.join(mot_code))
print("Votre chaîne de caractère décodée:"+''.join(mot_decode))

