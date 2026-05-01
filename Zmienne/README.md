# Lekcja 1: Zmienne

W tej lekcji poznałem podstawowe rodzaje zmiennych w Pythonie. Python posiada wiele wbudowanych typów danych, ale na ten moment najważniejsze są cztery z nich.

## Rodzaje zmiennych:
* **Integer** (int) – liczby całkowite.
* **Float** – liczby zmiennoprzecinkowe (rzeczywiste).
* **Boolean** (bool) – wartości logiczne (`True` lub `False`).
* **String** (str) – ciągi znaków (tekst).

### Jak powinna wyglądać zmienna?
1. **W Pythonie dążymy do tego, aby kod był jak najbardziej czytelny i prosty!** (Zgodnie z filozofią *The Zen of Python*).
2. Zmienna musi mieć jasną, opisową nazwę, np. `flowers_count` zamiast `fc`. Jest to szczególnie przydatne w większych projektach, gdzie łatwo zapomnieć, co oznaczają poszczególne skróty, oraz podczas pracy w zespole.
3. Nazwy zmiennych powinny być pisane małymi literami. Słowa oddzielamy znakiem podkreślenia `_` (jest to styl zwany **snake_case**). Spacja w nazwie spowodowałaby błąd składniowy, a brak jakichkolwiek odstępów utrudniłby czytanie.
4. Python jest językiem **typowanym dynamicznie**. Oznacza to, że nie musimy deklarować typu zmiennej (w przeciwieństwie do np. języka C). Python sam rozpoznaje typ na podstawie przypisanej wartości: `nazwa = dane`.

### Przykład:
```python
students_count = 1000          # Liczba całkowita (Integer)
rating = 4.99                  # Liczba zmiennoprzecinkowa (Float)
is_published = True            # Wartość logiczna (Boolean)
course_name = "Python Kurs"    # Ciąg znaków (String)
