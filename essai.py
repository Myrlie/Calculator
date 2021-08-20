def menu():
    print ("Ecrivez 'a' si vous voulez faire une addition \n Ecrivez 's' si vous voulez faire une soustraction \n Ecrivez 'm' si vous voulez faire une multiplication \n Ecrivez 'd' si vous voulez faire une division \n Ecrivez 'r' si vous voulez le reste de la division \n Ecrivez 'e' si vous voulez l\'exposant \n Ecrivez 'q' si vous voulez quitter le programme: ")

menu()
choix=input('faite votre choix: ')

def add(a,b):
    som = a+b
    return som

def sous(a,b):
    moins = a-b
    return moins

def mul(a,b):
    fois = a*b
    return fois

def div(a,b):
    quot = a/b
    return quot

def mol(a,b):
    reste = a%b
    return reste

def exp(a,b):
    expo = a**b
    return expo


while choix != 'a' or 's' or 'm' or 'd' or 'r' or 'e' or 'q':
    if choix == 'a':
        c = int(input('Entrer la premiere valeur: '))
        d = int(input('Entrer la seconde valeur: '))
        print('Le resultat est: ',add(c,d))
        break
    elif choix == "s":
        c = int(input('Entrer la premiere valeur: '))
        d = int(input('Entrer la seconde valeur: '))
        print ('Le resultat est: ',sous(c,d))
        break
    elif choix == 'm':
        c = int(input('Entrer la premiere valeur: '))
        d = int(input('Entrer la seconde valeur: '))
        print('Le resultat est: ',mul(c,d))
        break
    elif choix == 'd':
        c = int(input('Entrer la premiere valeur: '))
        d = int(input('Entrer la seconde valeur: '))
        print('Le resultat est: ',div(c,d))
        break
    elif choix == 'r':
        c = int(input('Entrer la premiere valeur: '))
        d = int(input('Entrer la seconde valeur: '))
        print('Le resultat est: ',mol(c,d))
        break
    elif choix == 'e':
        c = int(input('Entrer la premiere valeur: '))
        d = int(input('Entrer la seconde valeur: '))
        print('Le resultat est: ',exp(c,d))
        break
    elif choix == 'q':
        break
    else:
        print ('votre choix est incorrect veuillez essayer a nouveau ')
        menu ()
        choix= input('faite votre choix: ')
    
print('Merci et Au revoir')