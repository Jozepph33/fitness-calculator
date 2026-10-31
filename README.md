# Fitness Calculator

# Leírás

Python alkalmazás alapvető fitneszhez kapcsolódó értékek kiszámítására és a felhasználói adatok mentésére.

# Funkciók

- EU és USA mértékegységrendszer kiválasztása
- BMI számítás
- BMR számítás
- Ideális testsúly számítás
- Testsúly átváltása kilogramm és font között
- Magasság átváltása centiméter és inch/láb között
- Adatok mentése CSV fájlba
- Statisztikák számítása a mentett adatok alapján
- Az aktuális eredmények összehasonlítása az átlaggal
- Grafikus felhasználói felület Tkinterrel
- Alapvető hibakezelés és adatellenőrzés

# Fájlok

- `main.py` – a program fő fájlja és a grafikus felület
- `szjb_sajat_modul.py` – saját modul, amely az osztályt és a függvényeket tartalmazza
- `fitness_data.csv` – automatikusan létrejövő fájl a mentett adatokkal

# Használt modulok

- `tkinter`
- `math`
- `csv`
- `os`

# Saját osztály

- `SZJBFitnessCalculator`

# Monogramot tartalmazó saját függvény

- `szjb_round_down()`

# Program indítása

`python main.py`