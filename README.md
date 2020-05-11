# ATP-assignment

# Overzicht

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

Why++ | Python equivalent | type
--- | --- | ----
[   |   + | Addition
\-   | -   | Subtraction
_   | * | Multiply
$ | / | Division
\: | = | Assignment
{ | < | Less than
} | \> | Greater than

## Voorbeeld:

```
B : 2 _ 53 [ 7 _ 1 [ 4 $ 2 [ 2
C : 5 _ 2
```

Python representatie:
```python
B = 2 * 53 + 7 * 1 + 4 / 2 + 2
C = 5 * 2
```

resulteert in:
```
Variables: {'B': '117', 'C': '10'}
```


## Must haves:
- Alles is type-annotated volgens Sectie 4.4 van de reader.
- Er is meerdere malen(meer dan de minimale 3 keer) gebruik gemaakt van map en filter. 
er is gebruikt gemaakt van zip.

## Should haves
- Een eigen taal is bedacht.
