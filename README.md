# Symulowane wyżarzanie w Pythonie

Mały projekt, który szuka minimum albo maksimum funkcji jednej lub dwóch zmiennych za pomocą algorytmu symulowanego wyżarzania (simulated annealing). Funkcję wpisujesz sam w terminalu, a na końcu dostajesz wykres z zaznaczonym znalezionym punktem.

## Jak to działa

Algorytm startuje z losowego punktu i w każdej iteracji robi mały, losowy krok w jego okolicy. Potem decyduje, czy ten nowy punkt przyjąć:

- jeśli nowy punkt jest lepszy (mniejsza wartość dla minimum, większa dla maksimum), przyjmuje go od razu,
- jeśli jest gorszy, to czasem też go przyjmie, z prawdopodobieństwem zależnym od aktualnej temperatury.

Na początku temperatura jest wysoka, więc algorytm chętnie łazi po całej funkcji i może "wyskoczyć" z lokalnego minimum. Z każdą iteracją temperatura spada (mnożona przez współczynnik chłodzenia), algorytm robi się coraz ostrożniejszy i w końcu osiada w jednym miejscu.

## Wymagania

- Python 3.8 lub nowszy
- numpy
- matplotlib

Instalacja bibliotek:

```bash
pip install numpy matplotlib
```

## Uruchomienie

Zapisz kod jako np. `main.py` i odpal:

```bash
python main.py
```

Program zapyta o trzy rzeczy:

1. liczbę wymiarów funkcji (1 lub 2),
2. samą funkcję,
3. czy szukasz minimum, czy maksimum (wpisz dokładnie `minimum` albo `maksimum`).

### Przykład sesji

```
Podaj liczbę wymiarów funkcji (1 lub 2): 1
Wprowadź funkcję jednowymiarową f(x): x**2 + 5*np.sin(x)
Czy chcesz wyliczyć minimum czy maksimum funkcji? (minimum/maksimum): minimum
```

Po chwili pojawi się wykres, a w konsoli zobaczysz znalezione rozwiązanie.

## Jak wpisywać funkcje

Funkcja jest wczytywana przez `eval`, więc zapisujesz ją jak zwykłe wyrażenie w Pythonie, używając zmiennych `x` (i `y` w wersji 2D). Dostępne są `math` i `np`.

| Co chcesz | Jak wpisać |
|-----------|------------|
| potęga | `x**2` |
| sinus | `np.sin(x)` |
| e do x | `np.exp(x)` |
| dwie zmienne | `x**2 - y**3 + 7*y` |

Wskazówka: do wykresów 3D używaj funkcji z `np` (np. `np.sin`), a nie z `math`. Funkcje z `math` nie radzą sobie z tablicami, więc wykres 2D może się wysypać.

W kodzie są też gotowe przykładowe funkcje `one_dimensional_function` i `two_dimensional_function`, których możesz użyć do testów.

## Parametry algorytmu

Ustawiane na sztywno w bloku `if __name__ == "__main__"`:

| Parametr | Wartość | Znaczenie |
|----------|---------|-----------|
| `initial_temperature` | 100.0 | temperatura startowa |
| `cooling_rate` | 0.95 | mnożnik temperatury w każdej iteracji |
| `num_iterations` | 1000 | liczba iteracji |

Rozmiar kroku to losowa liczba z przedziału od -0.5 do 0.5 w każdym wymiarze, a punkt startowy jest losowany z przedziału od -10 do 10.

## Struktura kodu

- `simulated_annealing` - sam algorytm,
- `get_user_function` - wczytuje funkcję od użytkownika,
- `plot_function` - rysuje wykres 2D albo powierzchnię 3D z zaznaczonym wynikiem,
- `one_dimensional_function`, `two_dimensional_function` - przykładowe funkcje celu.

## Znane ograniczenia

- **Wynik jest losowy.** Każde uruchomienie może dać trochę inną odpowiedź, bo algorytm jest probabilistyczny. Nie ma gwarancji znalezienia globalnego optimum.
- **Funkcje nieograniczone.** Dla funkcji bez minimum albo maksimum (np. `x**2 - y**3 + 7*y` ma w y nieskończone wartości w obie strony) algorytm będzie po prostu dryfował w kierunku, w którym wartość rośnie lub maleje.
- **Warunek akceptacji dla maksimum.** Prawdopodobieństwo przyjęcia gorszego punktu liczone jest tym samym wzorem dla obu trybów, więc przy szukaniu maksimum algorytm zachowuje się inaczej niż można by oczekiwać. Prawidłowo różnicę w wartościach trzeba tam odwrócić (albo szukać minimum funkcji `-f`).
- **Bezpieczeństwo.** Użycie `eval` do wczytywania funkcji jest wygodne, ale wykona każdy wpisany kod. Nie wystawiaj tego programu na cudze dane wejściowe.
- **Zakres wykresu.** Wykres pokazuje otoczenie znalezionego punktu (plus minus 10), więc nie zawsze widać całą funkcję.

## Pomysły na rozwój

- wczytywanie parametrów (temperatura, liczba iteracji) od użytkownika,
- zapamiętywanie najlepszego rozwiązania z całego przebiegu, a nie tylko ostatniego,
- wykres zbieżności (wartość funkcji w kolejnych iteracjach),
- bezpieczniejszy parser funkcji zamiast `eval`.
