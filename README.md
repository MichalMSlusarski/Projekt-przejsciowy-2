# Badanie korelacji między głównymi wskaźnikami optymalizacji stron internetowych a ich pozycją w wynikach wyszukiwania

### Cel projektu

Sprawdzenie jak parametry takie jak wydajność strony, dostępność, bezpieczeństwo i optymalizacja treści strony, wpływają na jej pozycję w wynikach wyszukiwania w Google.

### Zbieranie danych

Korzystając z biblioteki apify_client do automatycznego wykonywania zapytań na platformie Apify w celu pobrania wyników wyszukiwania dla określonego zapytania. automatyzujemy proces pobierania wyników wyszukiwania dla określonego zapytania, umożliwiając wielokrotne uruchomienie tego zadania w określonych odstępach czasu. Wyniki są zapisywane do plików JSON, a nazwy plików zawierają datę, godzinę i oryginalne zapytanie.

Badanym zapytaniem jest: "serwis rowerowy warszawa". ...

### Przekształcanie danych

Do uzupełnienia

### Google Lighthouse

Do zbadania parametrów strony korzystamy z API narzędzia Google Lighthouse. To otwarte narzędzie do analizy wydajności i jakości stron internetowych.

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

```{r, message = FALSE}
theme_set(theme_pubr())

wykres1 <- ggarrange(av1, av2, av3, av4, 
                    ncol = 2, nrow = 2)
```

#### Zmiana z linii regresji na linię trendu obliczoną na podstawie punktów na wykresach

```{r, message = FALSE}
wykres1.2 <- ggarrange(av1.2, av2.2, av3.2, av4.2, 
                     ncol = 2, nrow = 2) 
```

#### Wykresy punktowe zależności między zmienną weighted_position, a poszczególnymi zmiennymi

```{r, message = FALSE}
wykres2 <- ggarrange(we1, we2, we3, we4, 
                     ncol = 2, nrow = 2)
```

#### Zmiana z linii regresji na linię trendu obliczoną na podstawie punktów na wykresach

```{r, message = FALSE}
wykres2.2 <- ggarrange(we1.2, we2.2, we3.2, we4.2, 
                       ncol = 2, nrow = 2) 
```

### Konkluzje

Jak widać pomimo tego, że korelacja zachodzi tylko w przypadku zmiennej **best_practises_score**, to po wizualnej analizie wykresów można stwierdzić, że zmienna **seo_score** również ma znaczący wpływ na strony pozycjonowane najwyżej w wyszukiwaniach
