# Gestionnaire de Tâches avec Tkinter et ttkthemes

Ce projet est un gestionnaire de tâches simple créé en utilisant Tkinter pour l'interface utilisateur et `ttkthemes` pour appliquer un thème esthétique. Les tâches peuvent être ajoutées, marquées comme terminées, supprimées, enregistrées dans un fichier JSON et chargées à partir d'un fichier JSON existant.

## Prérequis

Pour exécuter ce programme, vous aurez besoin de Python installé sur votre machine. Vous aurez également besoin des bibliothèques Tkinter et ttkthemes. Vous pouvez installer ttkthemes en utilisant pip :

```bash
pip install ttkthemes
```

## Fonctionalités

* Ajouter des Tâches: Vous pouvez ajouter des tâches avec une description et une date d'échéance.
* Marquer les Tâches comme Terminées: Les tâches peuvent être marquées comme terminées, ce qui ajoutera un symbole de vérification à côté de la description de la tâche.
* Supprimer des Tâches: Vous pouvez supprimer des tâches de la liste.
* Enregistrer et Charger des Tâches: Les tâches peuvent être enregistrées dans un fichier JSON et chargées à partir d'un fichier JSON.


## Interface utilisateur

L'interface utilisateur contient les composants suivants:

* Champs de saisie: Pour la description et la date d'échéance des tâches.
* Boutons: Pour ajouter des tâches, marquer des tâches comme terminées, supprimer des tâches, enregistrer et charger des tâches.
* Liste des Tâches: Affiche toutes les tâches avec leur état (terminé ou non).
