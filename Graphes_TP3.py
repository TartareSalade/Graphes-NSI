class Graphe:
    """
    Un graphe non orienté représenté par un dictionnaire d'adjadence
    """

    def __init__(self):
        self.adj = {}

    def ajouter(self,s):
        """
        Ajouter un sommet s au graphe
        :param s:
        :return None:
        """
        if s not in self.adj:
            self.adj[s] = []

    def ajouter_arete(self, s1,s2):
        """
        ajoute une arête entre les sommets s1 et s2. Si les sommets s1 et s2 ne sont pas dans le graphe, la méthode les ajoutera.
        :param s1:
        :param s2:
        :return None:
        """
        if s1 not in self.adj:
            self.ajouter(s1)
        if s2 not in self.adj:
            self.ajouter(s2)
        self.adj[s1].append(s2)
        self.adj[s2].append(s1)

    def successeurs(self,s):
        """
        retourne une liste contenant tous les voisins du sommet s
        :param s:
        :return list:
        """
        if s not in self.adj:
            return []
        return self.adj[s]

    def sommets(self):
        """
        renvoie la liste des sommets du graphe
        :return list:
        """
        liste_sommets = []
        for sommet in self.adj:
            liste_sommets.append(sommet)
        return liste_sommets





G = Graphe()
G.ajouter_arete('A', 'B')
G.ajouter_arete('A', 'D')
G.ajouter_arete('B', 'C')
G.ajouter_arete('D', 'E')
G.ajouter_arete("E", "B")
G.ajouter_arete("C", "E")
G.ajouter_arete("C", "F")
G.ajouter_arete("G", "C")

def parcours_profondeur(graphe, s_marques, s):
    """
    parcourt le graphe en profondeur depuis le sommet s
    :param graphe: le graphe à parcourir
    :param s_marques: liste des sommets marqués
    :param s: sommet de départ
    """
    s_marques.append(s)  # On marque s
    for voisin in graphe.successeurs(s):  # On parcourt les voisins de s
        if voisin not in s_marques:  # Si le voisin n'a pas encore été visité
            parcours_profondeur(graphe, s_marques, voisin)  # On continue le parcours à partir du voisin
    return s_marques

def existe_chemin(graphe, s1, s2):
    """
    Vérifie si il existe un chemin entre s1 et s2 dans le graphe
    :param graphe: graphe représenté par un dictionnaire d'adjacence
    :param s1: sommet de départ
    :param s2: sommet d'arrivée
    :return bool: True s'il existe un chemin, False sinon
    """
    sommets_atteints = []
    parcours_profondeur(graphe, sommets_atteints, s1)
    return s2 in sommets_atteints

test1 = existe_chemin(G, "G", "B")
print(test1)
test2 = existe_chemin(G, "G", "A")
print(test2)

sommets_atteints = []
print(parcours_profondeur(G, sommets_atteints, "A"))

