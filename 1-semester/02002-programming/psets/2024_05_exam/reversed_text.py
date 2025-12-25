def reversed_text(text: str, option: str) -> str:
    res = ''
    if text[-1] == '.': text = text[:-1]
    lst = text.split(' ')
    if option == 'letters':
        # Reverse each word but same position
        for word in lst:
            res += word[-1::-1] + ' '
        return res.strip()
    
    if option == 'words':
        # Reverse word positioning
        for word in range(len(lst)-1,-1,-1):
            res += lst[word] + ' '
        return res.strip()
    
    return 'Invalid option'