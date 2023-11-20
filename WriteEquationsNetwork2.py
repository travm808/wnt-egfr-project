compoundsplit = "_"
statesplit = "!"
def ProperOrder(A):
    if is_complex(A):
        name = A.split(compoundsplit)
        name.sort()
        return compoundsplit.join(name)
    else:
        return A
def is_complex(A):
    return len(A.split(compoundsplit)) > 1
def remove_state(A):
    if has_state(A):
        name = A[0 : (len(A) - 2)]
        return name
    else:
        return A
def has_state(A):
    return len(A.split(statesplit)) > 1
def NetworkToReactions(Network):
    reactions = []
    for edge in Network:
        A,B,rtype,C = edge
        A = ProperOrder(A)
        B = ProperOrder(B)
        if rtype == 1: #Activation with complex forming and unforming
            reactants = ["%s%sa" %(A,statesplit), "%s%si" %(B,statesplit)]
            product = "%s%s%s" %(A,compoundsplit,B)
            name = product.split(compoundsplit)
            name.sort()
            products = [compoundsplit.join(name)]
            reactions.append((reactants, products))
            reactions.append((products, reactants))
            new_products = ["%s%sa" %(A,statesplit), "%s%sa" %(B, statesplit)]
            reactions.append((products, new_products))
        if rtype == 2: #Inhibition with complex forming and unforming
            reactants = ["%s%sa" %(A,statesplit), "%s%sa" %(B, statesplit)]
            product = "%s%s%s" %(A,compoundsplit,B)
            name = product.split(compoundsplit)
            name.sort()
            products = [compoundsplit.join(name)]
            reactions.append((reactants, products))
            reactions.append((products, reactants))
            new_products = ["%s%sa" %(A,statesplit), "%s%si" %(B, statesplit)]
            reactions.append((products, new_products))
        if rtype == 3: #complex formed (always active)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%sa" % (A, statesplit), "%s%sa" % (B, statesplit)]
            product = "%s%s%s" %(A,compoundsplit,B)
            products = [ProperOrder(product) + "%sa" % statesplit]
            reactions.append((reactants, products))
            reactions.append((products, reactants))
        if rtype == 4: #complex formed (inactive)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%sa" % (A, statesplit), "%s%sa" % (B, statesplit)]
            product = "%s%s%s" %(A,compoundsplit,B)
            products = [ProperOrder(product) + "%si" % statesplit]
            reactions.append((reactants, products))
            reactions.append((products, reactants))
        '''if rtype == 5: #Phosphorylation (activate)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%sa" % (A, statesplit), "%s%si" % (B, statesplit)]
            products = ["%s%sa" % (A, statesplit), "%s%sa" % (B, statesplit)]
            reactions.append((reactants, products))
        if rtype == 6: #Dephosphorylation (inactivate)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%sa" % (A, statesplit), "%s%sa" % (B, statesplit)]
            products = ["%s%sa" % (A, statesplit), "%s%si" % (B, statesplit)]
            reactions.append((reactants, products))'''
        if rtype == 7: #unbinding of complex with other molecule (Ex: Dvl unbinding GSK3B)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%sa" % (A, statesplit), "%s%sa" % (B,statesplit)]
            remove_product = A.split(compoundsplit)
            remove_product.remove(C)
            product = compoundsplit.join(remove_product)
            products = ["%s%sa" % (product, statesplit), "%s%sa" % (B, statesplit), "%s%sa" % (C, statesplit)]
            reactions.append((reactants, products))
        if rtype == 8: #Activate itself (Ex. GSK3B and EGFR)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%si" % (A, statesplit)]
            products = ["%s%sa" % (A, statesplit)]
            reactions.append((reactants, products))
        if rtype == 9: #unbind from itself (Ex. Bcat from complex after Phosphorylation)
            A = remove_state(A)
            B = remove_state(B)
            reactants = ["%s%sa" % (A, statesplit)]
            remove_product = A.split(compoundsplit)
            remove_product.remove(B)
            product = compoundsplit.join(remove_product)
            products = ["%s%sa" % (product, statesplit), "%s%si" % (B,statesplit)]
            reactions.append((reactants, products))

    return reactions
