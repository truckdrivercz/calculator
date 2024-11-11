a = float(input("Zadejte první číslo: "));
operace = input("Zvolte znamínko: ");
b = float(input("Zadejte druhé číslo: "));

def scitani (a, b):
    return a + b;

def odcitani (a, b):
    return a - b;

def nasobeni (a, b):
    return a * b;

def deleni (a, b):
    return a / b;

def error (a, b):
    if b == 0:
        return "Chyba, nelze dělit nulou";
        return a / b;

match operace:
    case "+":
        vysledek = scitani(a, b);

    case "-":
        vysledek = odcitani(a, b);

    case "*":
        vysledek = nasobeni(a, b);

    case "/":
        vysledek = deleni(a, b);

    case _:
        vysledek = "Neplatná operace";

print("Výsledek je: ", vysledek);