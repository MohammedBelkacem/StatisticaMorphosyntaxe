import csv
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
corpora="data/corpus-kab.txt"
def  tagset (corpora):
    tags=[]
    for sentence in open(corpora,encoding='utf-8'):
        tagged_sentence=sentence.replace('\ufeff',"").replace('\n',"").split()
        for tagged_word in tagged_sentence:
            tag=tagged_word.split("/")[1]
            if tag not in tags:
                tags.append(tag)
    return tags

tags=tagset(corpora)


header = tags
data=[]

def initilialize (tags):
    words=[]
    for i in tags:
        words.append(0)
    return words



for sentence in open(corpora,encoding='utf-8'):
        words=initilialize (tags)

        tagged_sentence=sentence.replace('\ufeff',"").replace('\n',"").split()
        for tagged_word in tagged_sentence:
            word=tagged_word.split("/")[0]
            words[tags.index(tagged_word.split("/")[1])]=words[tags.index(tagged_word.split("/")[1])]+1
        data.append(words)
#print (data)


with open('data/postag.csv', 'w', encoding='UTF8', newline='\n') as f:
    writer = csv.writer(f,delimiter='\t')

    # write the header
    writer.writerow(header)
    for i in data:
      writer.writerow(i)


df = pd.read_csv ('data/postag.csv',delimiter='\t')
#display(df)

Verbs=['VAF',   #aoriste futur
    'VAI',    # aoriste impératif
    'VAIT',   #aoriste intensif
    'VII',   #impératif intensif
    'VP',    # prétérit
    'VPN',   # prétérit négatif
    'VPA',   #participe aoriste
    'VPAIN', #participe aoriste intensif négatif
    'VPAIP', #participe aoriste intensif positif

    'VPPN',  #participe prétérit négatif
    'VPPP',  # participe prétérit positif

    ]
occurences=[]
for i in Verbs:

     occurences.append(df[i].sum())

patches, texts, autotexts = plt.pie(occurences,
                                        labels=Verbs, autopct='%.0f%%',
                                        shadow=False, radius=1)
for t in texts:
        t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Imyagen s tmeẓri')

plt.show()



##noms Verbes

Verbes=['VAF',   #aoriste futur
    'VAI',    # aoriste impératif
    'VAIT',   #aoriste intensif
    'VII',   #impératif intensif
    'VP',    # prétérit
    'VPA',   #participe aoriste
    'VPAIN', #participe aoriste intensif négatif
    'VPAIP', #participe aoriste intensif positif
    'VPN',   # prétérit négatif
    'VPPN',  #participe prétérit négatif
    'VPPP',  # participe prétérit positif
    ]

Verbs=['Imyagen','Ismawen']

occurences=[]
nb=0
for i in Verbes:
    nb=nb+df[i].sum()


occurences.append(nb)

Names=['NMC',   #nom commun
       'NMP',    # nom propre
       'NCM',   #nom cardinal
]

nb=0
for i in Names:
    nb=nb+df[i].sum()


occurences.append(nb)


patches, texts, autotexts = plt.pie(occurences,
                                        labels=Verbs, autopct='%.0f%%',
                                        shadow=False, radius=1)
for t in texts:
        t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Ismawen/Imyagen')

plt.show()


occurences=[]
Tanila=['PDP',   #nom commun
       'PDS']

nb=0
for i in Tanila:
    nb=nb+df[i].sum()
    occurences.append(nb)


patches, texts, autotexts = plt.pie(occurences,
                                        labels=Tanila, autopct='%.0f%%',
                                        shadow=False, radius=1)
for t in texts:
        t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Tazelɣa n tnila')

plt.show()

#
occurences=[]
PAV=['PSV',   #nom commun
       'PPV']

nb=0
for i in PAV:
    nb=nb+df[i].sum()
    occurences.append(nb)


patches, texts, autotexts = plt.pie(occurences,
                                        labels=PAV, autopct='%.0f%%',
                                        shadow=False, radius=1)
for t in texts:
        t.set_size('smaller')
autotexts[0].set_color('y')

plt.xlabel('Imqimen iwsilen n umyag')

plt.show()