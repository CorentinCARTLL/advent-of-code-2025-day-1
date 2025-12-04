Bien sûr \! Voici le contenu du fichier `README.md` (version détente) directement ici, pour que tu puisses le copier-coller facilement sans passer par l'éditeur.

````markdown
# 🎄 Advent of Code 2025 - Day 01 🎅

## 🔐 The Secret Entrance (Cracking the Safe)

![Language](https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge&logo=python)
![Stars](https://img.shields.io/badge/Stars-⭐_2%2F2-yellow?style=for-the-badge)
![Vibe](https://img.shields.io/badge/Vibe-Chill-pink?style=for-the-badge)

### 📖 What's the deal with AoC?

So, [Advent of Code](https://adventofcode.com/) is basically this huge coding calendar that happens every December. It's made by this dude [Eric Wastl](http://was.tl/). Basically, you get puzzles, you solve 'em, you feel smart. Doesn't matter what language you code in, just get those stars! ⭐

---

### 🕵️‍♂️ The Challenge: Day 1

Okay, so the Elves are having a meltdown (classic). They wanna decorate the North Pole but the **Secret Entrance** is locked tight! 🛑
We gotta break into this safe that has a dial from `0` to `99`.

* **The Input:** Just a bunch of instructions like `R47`, `L37`.
* **The Mechanism:** The dial is a circle (wraps around 0-99).
    * `L` (Left) = Subtract numbers.
    * `R` (Right) = Add numbers.

#### ⭐ Part 1: The Decoy
First up, we just needed to count **how many times the dial lands EXACTLY on 0** when it stops spinning. Easy peasy.

#### 🌟 Part 2: The Real Password
Then it got real. The security is tighter than we thought! Now we gotta count **every single time the dial touches 0**, even while it's spinning past it. So if it goes from 90 to 10 (crossing 0), that counts!

---

### 📂 Repo Stuff
```text
advent-of-code-2025-day-01/
├── input.txt        # The secret instructions (shhh)
├── main1.py         # Code for the easy part
├── main2.py         # Code for the tricky part
└── README.md        # You are here lol
````

-----

### 🐍 How I Solved It

I grabbed **Python** cause it's chill. The main trick here is **Modulo Arithmetic**. Sounds fancy, but it's just clock math.

#### 💡 The Logic (Spinning in Circles)

Since the dial goes from 99 back to 0, I used the modulo operator `%` so the numbers don't go crazy:

```python
# Going Right (Adding stuff)
position = (position + valeur) % 100

# Going Left (Subtracting stuff)
position = (position - valeur) % 100
```

#### 🔍 Part 2 Logic (Did we cross the line?)

For the second star, just checking where we stopped wasn't gonna cut it. I had to calculate the distance to zero to see if we "lapped" it.

```python
# From main2.py
if sens == "R":
    distance_zero = 100 - position
    if valeur >= distance_zero:
        code += 1 # Ding! Crossed zero
        reste = valeur - distance_zero
        code += reste // 100 # Count any extra full spins
```

-----

### 🚀 Wanna Run It?

Just pop open your terminal and type this:

```bash
# Part 1
python main1.py

# Part 2
python main2.py
```

-----

*🎄 Happy Holidays & Happy Coding fam\!*

```
```
