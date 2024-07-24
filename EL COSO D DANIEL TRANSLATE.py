sentence = input("Enter the sentence: ")
clone = sentence.split()
final=[]


dic={"I" or "i":"me","He"or"he":"him","She"or"she":"her","They"or"they":"them","We"or"we":"us","you":"you"}
exo=[]


for i in clone:
    if i in dic:
        ad=clone.index(i)
        exo.append(ad)

clone[exo[0]], clone[exo[1]] = clone[exo[1]], clone[exo[0]]


for i in clone:
    if i in dic:
        final.append(dic[i])
    else:
        ad=clone.index(i)
        final.insert(ad,"is")
        final.append(i+"d by")


print(final)

