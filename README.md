# ATP-assignment

## Introductie Why++
Ik heb de taal Why++ genoemd. Voornamelijk om de onlogische on onduidelijke operators en manier van programmeren.

## Stappen
Grofweg zijn dit de stappen.

1. Als eerste wordt een file ingelezen, die returned een lijst met tokens terug.
2. Deze lijst met tokens worden omgezet tot één waarde en/of assignment aan een variable
3. De ProgramState wordt geupdate met geupdate met de variabelen en waarde die daarbij hoort.
4. De ProgramState wordt gereturned. 


## Stappen in detail.
1. in de **interpreter.py**, functie **tokenize** 
leest character voor character in en returned een token. 
Deze functie roept recursief **tokenize** aan.
Afhankelijk van de character returned hij een type token. 
Hieronder een kort overzicht van de tokens in inheritance.
  
 ![inheritance_tokens](https://user-images.githubusercontent.com/31653244/81508624-69f4ec80-9305-11ea-962f-8c4019a8a939.png)


2. De tokens worden omgezet tot één waarde en/of assignment aan een variable. 
Dit gebeurd in de **execute** functie. Allereerst worden first_precedence tokens uitgevoerd (zoals multiply en divide).
Vervolgens worden second_precedence tokens uitgevoerd(addition en subtraction).
Uiteindelijk is één token het resultaat (een IntegerToken met een waarde, of een Variable token met een waarde en identifier)

3. Daarna wordt de variable aan de programstate toegevoegd. Dit gebeurd in de **insert_variable** functie.

4. De ProgramState wordt uiteindelijk gereturned.



## Operators

Why++ | Python equivalent | type | Precedence
--- | --- | ---- | ----
_   | * | Multiply | First
$ | / | Division | First
[   |   + | Addition | Second
\-   | -   | Subtraction | Second
\: | = | Assignment | No precedence
{ | < | Less than | Third
} | \> | Greater than | Third

## Voorbeeld:

### orde van operaties:
De tokens zijn opgedeeld in first, second en third precedence tokens.
In volgorde van first, second en third worden de operaties uitgevoerd.

```
C:5 _ 2
C :5 _ 3
D : 5 } 3 [ 3
number113:2 _ 53 [ 7 _ 1 [ 4 $ 2 [ 2
F : number113 [ 7
multiplyCwithF : C _ F
```

Python representatie:
```python
C=5 * 2
C =5 * 3
D = 5 > 3 + 3
number113=2 * 53 + 7 * 1 + 4 / 2 + 2
F = number113 + 7
multiplyCwithF = C * F

```



resulteert in:
```
{'C': '15', 'D': 'False', 'number113': '113', 'F': '120', 'multiplyCwithF': '1800'}
```


## Must haves:
- Alles is type-annotated volgens Sectie 4.4 van de reader.
- Er is gebruik gemaakt van inheritance voor de tokens. Dit is te zien in het klassendiagram.
- Er is meerdere malen(meer dan de minimale 3 keer) gebruik gemaakt van map en filter. 
er is gebruikt gemaakt van zip.

## Should haves
- Een eigen taal is bedacht.
