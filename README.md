````markdown
# 🎄 Advent of Code 2025 - Jour 1 : L'Entrée Secrète 🎅

Bienvenue dans mon dépôt pour le **Jour 1** de l'Advent of Code 2025 ! Cette année, les elfes ont (encore) des problèmes de gestion de projet, et nous devons les aider à décorer le Pôle Nord. Mais d'abord... il faut ouvrir un coffre-fort.

![Language](https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge&logo=python)
![Stars](https://img.shields.io/badge/Stars-⭐_2%2F2-yellow?style=for-the-badge)

## 📖 Le Défi : Ouvrir le Coffre

Nous sommes devant une entrée secrète, mais le mot de passe a changé. Pour l'obtenir, nous devons manipuler un cadran numéroté de **0 à 99**.

* **Le mécanisme :** Un cadran circulaire (comme une horloge, mais de 0 à 99).
* **Les instructions :** Une liste de rotations, par exemple `R47` (Droite 47 crans) ou `L37` (Gauche 37 crans).
* **Départ :** Le cadran commence toujours sur la position **50**.

### ⭐ Partie 1 : Le Leurre
La première consigne nous demandait de suivre les instructions et de compter **combien de fois le cadran s'arrête exactement sur 0** à la fin d'une rotation.

### 🌟 Partie 2 : Le Vrai Mot de Passe
La sécurité a été renforcée (ou plutôt, mal comprise au début). Pour le vrai mot de passe, il faut compter **chaque "clic" sur le 0**, même si le cadran ne fait que passer dessus pendant qu'il tourne.

Cela inclut :
1.  Les fois où il s'arrête sur 0.
2.  Les fois où il traverse le 0 en passant de 99 à 0 (ou inversement).

---

## 📂 Structure du Projet

```text
advent-of-code-2025-day-01/
├── input.txt        # Les instructions données par l'Advent of Code
├── main1.py         # Solution pour la Partie 1 (Arrêts sur 0)
├── main2.py         # Solution pour la Partie 2 (Passages par 0)
└── README.md        # Ce fichier
````

-----

## 🐍 Ma Solution et Ma Logique

J'ai choisi **Python** pour résoudre ce problème. La clé de ce défi réside dans l'arithmétique modulaire (le fameux `%`), car le cadran est un cercle qui boucle sur lui-même.

### Logique Globale (Modulo)

Puisque le cadran va de 0 à 99, dès qu'on dépasse 99 ou qu'on descend sous 0, on doit revenir dans l'intervalle. L'opérateur `% 100` est parfait pour ça :

  * `position = (position + valeur) % 100` (pour la droite)
  * `position = (position - valeur) % 100` (pour la gauche)

### 🧠 Logique Partie 2 (Calcul de distance)

Pour la deuxième étoile, simuler chaque clic un par un aurait pu fonctionner, mais j'ai opté pour une approche plus mathématique dans `main2.py`.

Au lieu de faire une boucle pour chaque mouvement, je calcule la **distance restante jusqu'à zéro** :

1.  **Vers la Gauche (L) :** La distance vers 0 est simplement la valeur actuelle de la position.
2.  **Vers la Droite (R) :** La distance vers 0 est `100 - position`.

Si la valeur de rotation est supérieure ou égale à cette distance, cela signifie qu'on a croisé le zéro au moins une fois. On ajoute alors 1 au code, puis on regarde combien de tours complets (100 crans) on a fait en plus avec le reste de la rotation.

Extrait de `main2.py` :

```python
if sens == "R":
    distance_zero = 100 - position
    # Est-ce qu'on tourne assez pour atteindre ou dépasser 0 ?
    if valeur >= distance_zero:
        code += 1             # On a touché 0 une première fois
        reste = valeur - distance_zero
        code += reste // 100  # On ajoute les tours complets supplémentaires
    
    # Mise à jour de la position finale
    position = (position + valeur) % 100
```

-----

## 🚀 Comment lancer le code

Assurez-vous d'avoir Python installé, puis lancez simplement les scripts dans votre terminal :

```bash
# Pour obtenir la réponse de la partie 1
python main1.py

# Pour obtenir la réponse de la partie 2
python main2.py
```

-----

*Bon code et Joyeuses Fêtes \!* 🎄

```
```
