def phonebook_merge(phonebook: dict, second_phonebook: dict):
    for i, val in second_phonebook.items():
        if i not in phonebook:
            phonebook[i] = val

        if i in phonebook:
            for k in range(len(second_phonebook[i])):
                if val[k] not in phonebook[i]: phonebook[i].append(val[k])