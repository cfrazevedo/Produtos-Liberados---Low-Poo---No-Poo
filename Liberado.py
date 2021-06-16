def conferirLista(p, lista):
    s = 0
    for c in lista:
        if p in c:
            print(c.upper())
            s += 1
    if s != 0:
        y = str(input('\nAlguma das substâncias acima refere-se a que você está procurando? (S/N) ')).upper()
        while y[0] != 'S' and y[0] != 'N':
            y = str(input('\nResponda escrevendo "S" ou "N": ')).upper()
        if y[0] == 'S':
            return True
        else:
            print('_' * 80, '\n')


plp = ['mineral oil', 'paraffin', 'paraffinum liquidum', 'petrolatum', 'c10-11 isoparaffin',
       'c13-14 isoparaffin', 'c13-16 isoparaffin', 'c15-35 isoparaffin/isoalkylcycloalkanes',
       'c18-50 isoparaffin', 'c18-70 isoparaffin', 'c20-40 isoparaffin', 'chlorinated paraffin',
       'petrolatum red', 'petrolatum beta', 'methyl-cyclododecaneethanol',
       'diisocetyl dodecanedioate', 'dioctyldodecyl dodecanedioate', 'dodecane', 'decane',
       'dodecanedioic acid', 'dodecanedioic acid/cetearyl alcohol/glycol copolymer',
       'c7-8 isoparaffin', 'c8-9 isoparaffin', 'c9-13 isoparaffin', 'c9-14 isoparaffin',
       'c9-16 isoparaffin', 'c10-13 isoparaffin', 'c9-11 isoparaffin', 'c11-13 isoparaffin',
       'c11-14 isoparaffin', 'c9-12 isoparaffin', 'c10-12 isoparaffin', 'c11-12, isoparaffin',
       'c12-14 isoparaffin', 'c12-20 isoparaffin', 'vaseline', 'red petrolatum',
       'beta-methyl-cyclododecaneethanol', 'dodecanenitrile', 'epoxycyclododecane',
       'ethylene dodecanedioate', 'isododecane', 'isodecane', 'methoxycyclododecane',
       'tetramethyl-5-oxatricyclododecane', 'dodecene', 'decene', 'isododecene', 'isodecene',
       'alkane', 'alkene', 'alkine', '[x]cane', '[x]cene', '[x]cine', 'vaselin', 'tea lauryl sulfate',
       'ethyl peg-15 cocamine sulfate', 'sodium laureth sulfate', 'sodium lauryl ether sulfate',
       'sodium laurisulfate (sodium lauryl sulfate)', 'sodium myreth sulfate',
       'sodium trideceth sulfate', 'sodium coco-sulfonate', 'sodium sulfate coconut',
       'tridecyloxy', 'ethony', 'ethyl ester sulfate', 'hydrogen sulfate', 'sodium salt',
       'sodium tridecyl sulfate ether ethanol', 'sodium tridecyl tri (oxyethyl)',
       'sodium alkylbenzene sulfonate', 'alkylbenzene sulphonate', 'ammonium lauryl sulfate',
       'ammonium laureth sulfate', 'ammonium lauryl ether sulfate',
       'ammonium ou sodium xylenesulfonate', 'ammonium laureth',
       'tridecyl polyoxyethylene sodium sulfate', 'lauryl sulfate', 'myristal ether sulfate',
       'sulfonato de sódio olefina c14-16 (sodium c14-16 olefin sulfonate)',
       'tea dodecilbenzenosulfonate']

pnp = ['sodium cocyl isethionate', 'sodium lauryl sulfoacetate', 'sodium cocoyl glycinate',
       'sodium lauryl glucose carboxylate', 'sodium socoyl sarcosinate', 'lauryl/lauroyl sarcosinate',
       'ethyl peg-15 cocamine sulfate', 'dioctyl sodium sulfosuccinate (aerossol-ot, aot)',
       'decyl glucoside poly carboxylate', 'sodium methyl 2-sulfolaurate/disodium sulfolaurate',
       'methyl cocoyl', 'lauryl taurate', 'pluronic surfactant', 'tetronic surfactant',
       'polyglucosides', 'sodium lauryl sulfoacetate', 'disodium laureth sulfoccinate',
       'sodium lauroyl sarcosinate', 'distearoylethyl hydroxyethylmonium methosulfate',
       'cocobetaine', 'cocamidopropyl betaine', 'cocabetaine', 'cocoamphopropionate',
       'amodimethicone', 'cetearyl methicone', 'cetyl dimethicone', 'cyclomethicone',
       'cyclopentasiloxane', 'dimethicone crosspolymer', 'vinyl dimethicone',
       'vinyl dimethicone crosspolymer', 'dimethicone', 'methicone silsesquioxane crosspolymer',
       'crosspolymer dimethiconol', 'stearyl dimethicone', 'trimethylsilylamodimethicone',
       'simethicone', 'polydimethylsiloxane', 'methicone', 'phenyl trimethicone', 'dimethylpolysiloxane'
       'bis-aminopropyl dimethicone', 'dimethiconol', 'behenoxy dimethicone', 'stearoxy dimethicone',
       'propoxytetramethyl piperidinyl dimethicone (ptmpd)']

prb = ['4-(methoxycarbonyl)phenol', '4-hydroxy-', '4-hydroxybenzoic acid',
       '4-hydroxybenzoic acid methyl ester', 'aseptoform e', 'benzoic acid',
       'benzylparaben', 'bonomold oe', 'butoben', 'butyl 4-hydroxybenzoate',
       'butyl ester', 'butylparaben (e209)', 'easeptol', 'ethyl 4-hydroxybenzoate'
       'ethyl ester', 'ethyl parasept', 'ethylparaben (e214)', 'heptylparaben (e209)',
       'isobutylparaben', 'isopropylparaben', 'maseptol', 'metaben', 'methaben',
       'methyl 4-hydroxybenzoate', 'methyl butex', 'methyl chemosept', 'methyl ester',
       'methyl ester of p-hydroxybenzoic acid', 'methyl paraben',
       'methyl parahydroxybenzoate', 'methyl parasept', 'methyl p-hydroxybenzoate',
       'methyl p-oxybenzoate', 'methylben', 'methylparaben (e218)', 'metoxyde',
       'moldex', 'nipagin', 'nipagin m', 'paridol', 'p-carbomethoxyphenol',
       'p-hydroxy-', 'p-hydroxybenzoic acid methyl ester', 'p-methoxycarbonylphenol',
       'preserval', 'preserval m', 'propyl 4-hydroxybenzoate', 'propyl ester',
       'propyl paraben', 'propyl p-hydroxybenzoate', 'propylparaben (e216)',
       'septos', 'solbrol', 'solbrol m', 'tegosept e', 'tegosept m']

r = 'S'
while r == 'S':
    x = input('Insira o nome (ou parte) de uma substância: ').lower()
    print()
    if conferirLista(x, plp):
        print("\nSubstância proíbida para LOW POO e NO POO!")
    else:
        if conferirLista(x, pnp):
            print("\nSubstância proíbida para NO POO!")
        else:
            if conferirLista(x, prb):
                print("\nEssa substância é liberada, mas deve ser evitada (parabeno).")
            else:
                print('Substância liberada!')
    r = str(input('\nDeseja continuar? (S/N) ')).upper()
    while r[0] != 'S' and r[0] != 'N':
        r = str(input('\nResponda escrevendo "S" ou "N": ')).upper()
    print()
print('PROGRAMA ENCERRADO!')
