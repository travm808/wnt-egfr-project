def ParseReactions(reactions):
    Eqs = {}
    for i,r in enumerate(reactions):
        reactants,products = r
        temp = "k%i" %(i + 1)
        for species in reactants:
            temp = temp+ "*%s" %species
        for species in reactants:
            if species in Eqs:
                Eqs[species] = Eqs[species] + "-" + temp
            else:
                Eqs[species] = "-" + temp
        for species in products:
            if species in Eqs:
                Eqs[species] = Eqs[species] + "+" + temp
            else:
                Eqs[species] = temp
    return Eqs
