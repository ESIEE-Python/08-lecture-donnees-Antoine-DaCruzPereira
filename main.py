'''
Import des modules random et csv
'''
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """
    Retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='utf8') as f:
        d = csv.reader(f, delimiter=';')
        lb = list(d)
        l = []
        for i in range(len(lb)):
            l.append([])
            for j in lb[i]:
                l[i].append(int(j))
    return l

def get_list_k(data, k):
    """
    Retourne la liste k de la liste data

    Args:
        data, k : liste et indice

    Returns:
        l : la liste au k-ième indice
    """
    l = data[k]
    return l

def get_first(l):
    """
    Retourne le premier élément d'une liste

    Args:
        l : liste prédéterminé

    Returns:
        first : le premier nombre de la liste
    """
    first = l[0]
    return first

def get_last(l):
    """
    Retourne le dernier élément d'une liste

    Args:
        l : liste prédéterminé

    Returns:
        last : le dernier nombre de la liste
    """
    last = l[-1]
    return last

def get_max(l):
    """
    Retourne le nombre max d'une liste

    Args:
        l : liste prédéterminé

    Returns:
        mx : le maximum de la liste
    """
    mx = max(l)
    return mx

def get_min(l):
    """
    Retourne le nombre min d'une liste

    Args:
        l : liste prédéterminé

    Returns:
        mn : le minimum de la liste
    """
    mn = min(l)
    return mn

def get_sum(l):
    """
    Retourne la somme des nombre d'une liste

    Args:
        l : liste prédéterminé

    Returns:
        s : somme d'élément dde la liste
    """
    s = 0
    for i in l:
        s += i
    return s


#### Fonction principale


def main():
    '''
    Fonction de test pour les fonction secondaire

    Arg : None

    Return : None
    '''
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
