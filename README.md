# Badanie korelacji między głównymi wskaźnikami optymalizacji stron internetowych a ich pozycją w wynikach wyszukiwania

### Cel projektu

Sprawdzenie jak parametry takie jak wydajność strony, dostępność, bezpieczeństwo i optymalizacja treści strony, wpływają na jej pozycję w wynikach wyszukiwania w Google.

### Zbieranie danych

Korzystając z biblioteki apify_client do automatycznego wykonywania zapytań na platformie Apify w celu pobrania wyników wyszukiwania dla określonego zapytania. automatyzujemy proces pobierania wyników wyszukiwania dla określonego zapytania, umożliwiając wielokrotne uruchomienie tego zadania w określonych odstępach czasu. Wyniki są zapisywane do plików JSON, a nazwy plików zawierają datę, godzinę i oryginalne zapytanie.

Badanym zapytaniem jest: "serwis rowerowy warszawa". ...

Proces agregacji danych podzielony jest na 4 etapy:
1. Zebranie 100 najlepszych wyników wyszukiwania na zadaną frazę. Powtórzenie wyszukiwania 100 razy, aby móc wyciągnąć średnią pozycję.
2. 

### Przekształcanie danych

Do uzupełnienia

|url                                                                                                                                                 |average_position|url_count|weight|weighted_position|
|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------|------|-----------------|
|https://wygodnyrower.pl/serwis/serwis-rowerowy-warszawa/                                                                                            |1               |100      |1     |1                |
|https://3gravity.pl/pl/                                                                                                                             |2.04            |100      |1     |2.04             |
|https://www.centrumrowerowe.pl/sklep-rowerowy-warszawa/                                                                                             |3.08            |100      |1     |3.08             |
|https://skleprowerowy.pl/                                                                                                                           |4.16            |100      |1     |4.16             |
|https://warszawa.naszemiasto.pl/serwisy-rowerowe-w-warszawie-lista-warsztatow-gdzie-mozna-naprawic-rower-lub-zrobic-jego-przeglad/ar/c15p1-21631935 |5.69            |100      |1     |5.69             |
|https://sklep-naszosie.pl/                                                                                                                          |6.36            |100      |1     |6.36             |
|https://beatbike.pl/                                                                                                                                |6.61            |100      |1     |6.61             |
|https://sportset.pl/                                                                                                                                |8.24            |100      |1     |8.24             |
|https://wygodnyrower.pl/aktualnosci/%F0%9F%91%8Bnowy-sklep-i-serwis-wygodnyrower-bielany/                                                           |8.76|99       |0.99  |8.8562           |
|https://www.rowerywarszawa.pl/                                                                                                                      |10.34           |100      |1     |10.34            |

### Google Lighthouse

Do zbadania parametrów strony korzystamy z API narzędzia Google Lighthouse. To darmowe narzędzie do analizy wydajności i jakości stron internetowych.

Działanie Google Lighthouse obejmuje kilka głównych obszarów analizy:

1. **Wydajność (Performance):** Lighthouse mierzy wydajność strony, oceniając takie czynniki jak czas ładowania strony, opóźnienie pierwszego buforowania (First Contentful Paint), czas renderowania pierwszego krytycznego elementu (First Meaningful Paint) i inne metryki związane z ładowaniem strony.

2. **Dostępność (Accessibility):** Narzędzie analizuje dostępność strony internetowej dla użytkowników z różnymi ograniczeniami, takimi jak osoby korzystające z czytników ekranowych. Ocena obejmuje np. używanie poprawnych etykiet dla elementów, dostępność kontrastu kolorów, czy zrozumiałe informacje dla asystentów głosowych.

3. **Najlepsze praktyki (Best Practices):** Lighthouse sprawdza, czy strona internetowa stosuje się do ogólnie przyjętych najlepszych praktyk w projektowaniu i programowaniu stron. Obejmuje to kwestie takie jak zabezpieczenia, używanie najnowszych standardów, optymalizacje dla urządzeń mobilnych i inne.

4. **SEO (Search Engine Optimization):** Narzędzie analizuje elementy związane z optymalizacją dla wyszukiwarek internetowych. Oceniane są takie aspekty, jak czy strona ma odpowiednie meta-tagi, czy adresy URL są przyjazne dla wyszukiwarek, czy strona jest zaindeksowana i wiele innych.

Po analizie, Lighthouse generuje raport z wynikami, w którym przedstawia wyniki w postaci punktów procentowych dla każdego z obszarów oceny. Dzięki bezpośredniemu wywołaniu narzędzia przy pomocy API, jesteśmy w stanie otrzymać wyniki dla wszystkich badanych adresów. Wyniki zapisujemy w tabeli `lighthouse-output-full.csv`.

### Analiza bazy danych

Przystępujemy do wytworzonej wcześniej bazy danych. Naszym celem, będzie sprawdzenie korelacji pomiędzy poszczególnymi zmiennymi. W wyniku analizy docelowo chcemy znaleźć zmienne, które będą znacząco decydujące o pozycji strony w wyszukiwarce.

Przyjmując istotność alfa = 0,05 możemy stwierdzić, że korelacja zachodzi jedynie w przypadku zmiennej **best_practises**

#### Wykresy punktowe zależności między zmienną average_position, a poszczególnymi zmiennymi

![img](Wykresy/average_position-regression-line.png)

#### Zmiana z linii regresji na linię trendu obliczoną na podstawie punktów na wykresach

![img](Wykresy/average_position-trend-line.png)

#### Wykresy punktowe zależności między zmienną weighted_position, a poszczególnymi zmiennymi

![img](Wykresy/weighted_position-regression-line.png)

#### Zmiana z linii regresji na linię trendu obliczoną na podstawie punktów na wykresach

![img](Wykresy/weighted_position-trend-line.png)

### Konkluzje

Jak widać pomimo tego, że korelacja zachodzi tylko w przypadku zmiennej **best_practises_score**, to po wizualnej analizie wykresów można stwierdzić, że zmienna **seo_score** również ma znaczący wpływ na strony pozycjonowane najwyżej w wyszukiwaniach
