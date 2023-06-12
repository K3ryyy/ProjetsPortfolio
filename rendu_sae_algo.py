from operator import itemgetter

import time

##############################################

"""
Création de l'echiquier en fonction de la taille demandé
"""            

def voisin(nb_ligne,nb_col):
    
    
    """
    Creation de clé et de valeur sous forme de liste pour chaque cle
    dic[(1,1)] = [], dic[(1,2)] = [] ...
    """
    dic = {}
    for i in range(1,nb_ligne + 1):
        for j in range(1,nb_col + 1):
            dic[(i,j)] = []
    
    """
    Ajout des voisins de chaque cle
    dic[(1,1)] = [(2,3),(3,2)], dic[(1,2)] = [(3,1),(2,4),(3,3)] ...
    """
    for i in range(1,nb_ligne + 1):
        for j in range(1,nb_col + 1):
            
            ligne = i + 1
            col = j - 2
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
            ligne = i - 2
            col = j + 1
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
                
            ligne = i + 1
            col = j + 2
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
            ligne = i + 2
            col = j + 1
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
               
            ligne = i - 1
            col = j - 2
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
            ligne = i - 2
            col = j - 1
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
                
            ligne = i - 1
            col = j + 2
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
            ligne = i + 2
            col = j - 1
            if 1 <= ligne <= nb_ligne and 1 <= col <= nb_col:
                dic[(i,j)].append((ligne,col))
    return dic

################################################################


"""
Algorithme backtracking

ajoute le case_depart de départ dans un chemin
    si la longueur de la chemin correspond à un chemin qui a traversé tout le plateau
        retourne la chemin qui est le chemin
    sinon si case_depart a des voisin pas encore visité
        il ajoute ce case_depart à la chemin
        et dans les sommets visités on ajoute un voisin au valeur de la clef case_depart
    sinon
        on recule d'une case_depart
        si apres avoir reculé le case_depart en question n'a plus de voisin
            les case_departs visités de ce case_depart sont supprimés
            on recule encore d'un case_depart
"""

def parcour_backtracking(graphe, case_depart):
    chemin = [] #represente le potentiel chemin qui traversera l'echiquier
    chemin.append(case_depart) #ajout du case_depart de départ choisi
    
    """
    case_departs_visites est un dictionnaire
    il a pour cle un case_depart et en valeur les case_departs que cette cle à visité
    si il existe :
        case_departs_visites[(2,2)] = [(3,4)]
    alors dans la chemin (3,4) ne pourra pas être le case_depart suivant (2,2)
    mais (3,4) pourra suivre (1,5)
    """
    case_departs_visites = {} #dictionnaire avec comme cle un case_depart et comme valeur --> 
    while chemin != []:
        case_depart_en_cour = chemin[-1]
        if case_depart_en_cour not in case_departs_visites.keys(): #si la clef case_depart n'a pas deja ete ajouté danscase_departs_visitess
              case_departs_visites[case_depart_en_cour] = [] # on ajoute la clef case_depart_en_cour et une liste pour les prochaines cases que le case_depart va visté
              
        voisin = []
        for x in graphe[case_depart_en_cour]: #voisins du dernier élément de la chemin
            if( x not in case_departs_visites[case_depart_en_cour]) and (x not in chemin): # si le dernier élément de la chemin n'a pas déja visité et n'est pas présent dans la chemin
                voisin = voisin + [x] # ajout de x dans les voisin
        listo_somm = [] # liste temporaire [(voisin_en_question, nombre_de_voisins_du_veq)]
        for i in voisin :
            
            listo_somm.append((i,len([ u for u in graphe[(i)] if u not in chemin ]))) # ajout à listo_somm (i,nb voisin de i) 
                              
        liste_sommet_trier = sorted(listo_somm, key=itemgetter(1)) # tri liste_sommet_trier sur 
        voisin = liste_sommet_trier
        
        if len(chemin)==len(graphe): # si le chemin possede toutes les cases de l'echiquier
            return chemin
              
        elif voisin: # si voisin n'est pas vide
            i = voisin[0][0] #on prend le prmier voisin de la liste voisin
            case_departs_visites[case_depart_en_cour] =  case_departs_visites[case_depart_en_cour] + [i] # on dit que case_depart_en_cour visite i
            chemin = chemin + [i] # ajoute de i au chemin
            
        else:
            a = case_depart_en_cour #on stock le case_depart en cour dans a
            del chemin[-1] # on recule d'une case car il n'y a plus de possibilite pour case_depart_en_cour
            case_depart_en_cour = chemin[-1] # le case_depart en cour n'est plus le même, on le change
            if chemin != []: # si il reste des éléments dans chemin
                voisin_case_depart_en_cour = [y for y in graphe[case_depart_en_cour] if y not in case_departs_visites[case_depart_en_cour] and y not in chemin] #après avoir reculé d'une case on creer une liste des cases que la nouvelle case actuelle n' pas visité
                
                """
                apres avoir reculé d'une case, on vérifie que la case suivant il lui reste des voisins
                si non :
                    on supprimer les cases visité de la nouvelle case actuelle
                    on recule d'une case
                    et on supprime les cases visite par a, car le chemin a changé
                """
                
                if voisin_case_depart_en_cour == []:
                    

                    
                    case_departs_visites[case_depart_en_cour] = [] # cases visites par le case_depart_en_cour sont supprimé
                    del chemin[-1]
                    case_departs_visites[a] = [] # cases visites par a sont supprimé

    return chemin
      
################################################################

"""
Algorithme trouve chemin
il ajoute a chemin case_depart
il consiste à réalisé une liste de voisin de case_depart.
La liste est trier en fonction de chaque voisin, en effet moin un voisin possède lui même de voisin, plus il sera prit avant les autres
si case_depart (soit la dernière case de chemin) n'a plus de voisin on la supprime de chemin
  
"""

    
def trouve_chemin(graphe,case_depart):
    chemin = [] # represente le potentiel chemin qui traversera l'echiquier
    def parcour(case_depart):
        
        chemin.append(case_depart) #ajout case_depart au chemin
        if len(chemin) == len(echiquier) :  # si le chemin possede toutes les caces de l'echiquier
            gagne = True
            
        else :
            """
            Creation d'une liste 'voisins' avec les voisins de case_depart n'étant pas déjà dans chemin
            Ensuite on creer une liste qui aura pour valeur un couple, sous la forme --> (sommet,nbr de voisin possible du sommet)
            cette liste sera ensuite trier en fonction de la deuxième valeur de chaque couple
            On aura alors une liste de sommet trier en fonction du nombre de voisin que ce sommet possède
            ( le voisin qui aura le moin de sommet ensuite sera en premiere position dans  liste_sommet_trier)
            """
            
            gagne = False    
            voisins = [ u for u in graphe[(case_depart)] if u not in chemin ] # création d'une liste de voisin qui ne sont pas dans voisin
            
            listo_somm = [] # liste temporaire [(voisin_en_question, nombre_de_voisins_du_veq)]
            for i in voisins :
                
                listo_somm.append((i,len([ u for u in graphe[(i)] if u not in chemin ]))) # ajout à listo_somm (i,nb voisin de i) 
                                  
            liste_sommet_trier = sorted(listo_somm, key=itemgetter(1)) # tri liste_sommet_trier sur 
            
            for i in liste_sommet_trier : # pour chaque sommet de liste_sommet_trier
                
                if gagne : break
            
                else : gagne = parcour( i[0] ) # fonction recursive avec la partie gauche du couple i
            
            
            if not gagne :
                chemin.pop() #  case est supprimée de chemin si elle a mené à une impasse
        return gagne
    parcour(case_depart)
    return chemin     

#############################################################
"""
Définition de la taille de l'échiquier puis sa création
"""  
lignes = int(input("Quelle nombre de lignes vous voulez pour le plateau : "))
colonnes = int(input("Quelle nombre de colonnes vous voulez pour le plateau : "))

echiquier = voisin(lignes,colonnes)


################################################################

"""
utilisation des différents graphes et le temps d'éxécution d'algorithme

"""

debut = time.time()

print(parcour_backtracking(echiquier,(1,1))) # aappel de la fonction avec pour paramètres l'echiquier et la case de départ
#print(trouve_chemin(echiquier,(1,1)))
#verif(parcour_backtracking(echiquier,(1,1)))
fin = time.time()

duree_execution = fin - debut

print("L'algorithme choisi à durée ",duree_execution, "s")










