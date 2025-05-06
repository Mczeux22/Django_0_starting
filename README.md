# Django_0_starting

# Formation Python - Django : Niveau 0 - Starting

Ce dépôt regroupe les exercices réalisés dans le cadre de la formation **Python-Django - 0 Starting**, visant à introduire les bases du langage Python et ses applications fondamentales en développement logiciel.

## 📚 Table des matières

- [Introduction](#introduction)
- [Notions clés abordées](#notions-clés-abordées)
- [Structure du dépôt](#structure-du-dépôt)
- [Pré-requis](#pré-requis)
- [Instructions de rendu](#instructions-de-rendu)
- [Auteurs](#auteurs)

---

## 🧠 Introduction

L'objectif de cette journée est de poser les fondations syntaxiques et sémantiques de Python à travers des exercices pratiques orientés vers la manipulation de données, la création de scripts, et la structuration du code de manière lisible et modulaire.

---

## ✅ Notions clés abordées

- **Types de données** : `int`, `str`, `float`, `bool`, `list`, `dict`, `tuple`, `set`
- **Manipulation de fichiers** : ouverture, lecture, traitement de contenu (`open`, `read`)
- **Dictionnaires** : création, recherche par clé et par valeur, regroupement, tri
- **Fonctions et scope** : encapsulation du code dans des fonctions (`def`), appel conditionnel via `if __name__ == '__main__'`
- **Traitement d'arguments en ligne de commande** (`sys.argv`)
- **Nettoyage et validation de l’entrée utilisateur** : casse, espaces, erreurs de format
- **Tri personnalisé de structures de données**
- **Génération de HTML** : création de pages web dynamiques à partir de données structurées (tableau périodique)
- **Respect des bonnes pratiques Python** : conformité au Zen of Python

---

## 🗂️ Structure du dépôt

Chaque exercice est situé dans un sous-dossier `exXX/`, et contient les fichiers suivants :

| Dossier   | Fichier                | Description |
|-----------|------------------------|-------------|
| `ex00/`   | `var.py`               | Déclaration et affichage de variables de différents types |
| `ex01/`   | `numbers.py`           | Lecture et affichage de nombres depuis un fichier texte |
| `ex02/`   | `var_to_dict.py`       | Transformation d'une liste de tuples en dictionnaire |
| `ex03/`   | `capital_city.py`      | Recherche de capitale à partir d’un état |
| `ex04/`   | `state.py`             | Recherche d’état à partir d’une capitale |
| `ex05/`   | `all_in.py`            | Détection automatique d’entrée utilisateur (état, capitale ou aucun) |
| `ex06/`   | `my_sort.py`           | Tri de dictionnaire selon critères multiples |
| `ex07/`   | `periodic_table.py`    | Génération d’un tableau périodique des éléments en HTML |

---

## 💡 Pré-requis

- Python 3.x
- Éditeur de texte ou IDE (Visual Studio Code, PyCharm, etc.)
- Environnement Linux ou WSL recommandé
- Machine virtuelle avec dossier partagé pour les rendus

---

## 🧾 Instructions de rendu

- Chaque script doit contenir un appel conditionnel à la fonction principale :
  ```python
  if __name__ == '__main__':
      your_function()
