def mapSquare(procedure, listt):
    resultlist = []
    [resultlist.append(procedure(item, item2)) for item in listt for item2 in listt]
    print "Confused"
    finalresultlist = []
    for item in range(len(listt)):
        finalresultlist.append([resultlist[item*(len(listt)):((item+1)*(len(listt)))])
    return finalresultlist
