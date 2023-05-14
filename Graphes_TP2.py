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

    def voisins(self,s):
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

graphe = Graphe()
graphe.ajouter("A")
graphe.ajouter("B")
graphe.ajouter_arete("A","B")
graphe.ajouter_arete("B","C")
graphe.ajouter_arete("D","C")
graphe.ajouter_arete("A","D")
graphe.ajouter_arete("D","B")
print("Liste d'adjacences", graphe.adj)
print("Voisins du sommet D: ", graphe.voisins("D"))
print("Sommet du graphe: ", graphe.sommets())
