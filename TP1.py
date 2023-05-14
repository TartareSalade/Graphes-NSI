class Graphe_or:
    def __init__(self,n):
        """"
        Un graphe représenté par sa matrice d'adjacence.
        Les sommets sont représentés par les entiers 0,1,...,n-1
        """
        self.nombre = n
        self.adj = [n*[False] for i in range(n)]

    def ajouter_arc(self, s1, s2):
        """
        ajoute un arc du sommet  s1 vers le sommet  s2
        :param s1:
        :param s2:
        :return None:
        """
        self.adj[s1][s2] = True

    def successeur(self, s):
        """
        retourne  une  liste  contenant  tous  les  successeurs  du sommet  s.
        :param s:
        :return list:
        """
        liste_succes = []
        for i in range(self.nombre):
            if self.adj[s][i]:
                liste_succes.append(i)
        return liste_succes

    def predecesseur(self,s):
        """
        retourne  une liste contenant  tous les prédécesseurs  du sommet  s.
        :param s:
        :return list:
        """
        liste_pred = []
        for i in range(self.nombre):
            if self[i][s]:
                liste_pred.append(i)
        return liste_pred

    def ajouter(self,s):
        """
        ajoute un sommet  s au graphe
        :param s:
        :return None:
        """
        self.nombre += 1
        for i in range(self.nombre-1):
            self.adj[i].append(False)
        self.adj.append(self.nombre*[False])

    def supprimer_arc(self, s1, s2):
        """
        supprime l’arc du sommet  s1 vers le sommet  s2
        :param s1:
        :param s2:
        :return None:
        """
        self.adj[s1][s2] = False





graphe = Graphe_or(4)
graphe.ajouter_arc(0, 1)
graphe.ajouter_arc(0, 2)
graphe.ajouter_arc(1, 3)
graphe.ajouter_arc(2, 3)
graphe.ajouter(4) # ajout du sommet 4
graphe.ajouter_arc(3, 4) # ajout de l'arc (3, 4)

# Affichage de la matrice d'adjacence
for ligne in graphe.adj:
    print(ligne)

# Affichage des successeurs du sommet 3
print(graphe.successeur(3))
graphe.supprimer_arc(2,1)