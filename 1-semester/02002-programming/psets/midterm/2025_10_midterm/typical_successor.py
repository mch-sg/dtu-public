#
def typical_successor(text, letter):
    text = text.lower()
    ignore = [".", ",", ":", ";", "-", "?", "!"]
    arr = []
    c = []
    
    for j in range(len(text)): # Split teksten op i så den ignorerer ikke-bogstaver
        if text[j] in ignore:
            text = text[:j] + " " + text[j+1:]

    for i in range(len(text)): # append efterfølgeren, hvis det er lig letter, til et array
        if text[i] == letter:
            arr.append(text[i+1])

    for j in range(len(arr)): # append nyt array som er hvor mange gange de opstår
        c.append(arr.count(arr[j]))

    if c:
        typisk = arr[c.index(max(c))] # find indekset som er det maksimale af opståelse, og indsæt det i array for at finde typisk efterfølgenr
        return typisk
    else:
        return ' '