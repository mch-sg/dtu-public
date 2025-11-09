def dice_fairness(throws):
    arr = []
    for i in throws: # Nyt array tal til antallet af gange vi lander på x
        arr.append(throws.count(i))
    #
    hyppigst_forekomst = max(arr) # den side vi lander på flest gange
    mindst_forekomst = min(arr) # den side vi lander på mindst gange
    hyppigst_tal = throws[arr.index(hyppigst_forekomst)] # det tal som kommer flest gange
    diff = hyppigst_forekomst - mindst_forekomst # forskellen
    #
    return (hyppigst_tal, hyppigst_forekomst, diff)