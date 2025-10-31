# Balanced Pairs - Level 1

#A journey begins with a single step. This is step one.

## Purpose
The purpose of this program is to ensure that every **grouping character** (parentheses, brackets, braces, etc.) has a matching **opening symbol**.  
This is similar to how an IDE might check for code inside brackets.

---

## Methodology
- A **stack** is used to track opening symbols.
- A **hash map (dictionary)** dynamically maps closing symbols to their corresponding opening symbols.
- User inputs a string of symbols and the BalanceStack method will check for closing symbols first by popping the them off the stack first
- if the closing symbol is found, the key pair is added to the dictionary with its corresponding opening symbol.
- if a opening symbol is found, the program will check the hash map if a closing key exists and continue if true
- Otherwise the program will return invalid

---

## Incorporating Invariants
An **invariant** is a property that must always be true about an object.  

- In this program, the invariant is:  
  > If a closing symbol is encountered, the **top of the stack must match** its corresponding opening symbol.
- Due to the **LIFO nature** of stacks, only the closing symbols need mapping in the hash map.  
- There is no need to create key-value pairs for opening symbols inside the stack itself.

---



## Improvements / Future Work
- **Readability**: Current `if` / `match-case` statements are cumbersome; a cleaner implementation is possible.
- **Robustness**: Handle all consecutive pairs and extra openings correctly.
- **Extensibility**: Generalize to support any type of grouping symbols beyond `()[]{}`.

