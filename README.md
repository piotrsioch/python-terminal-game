**Autor:** Piotr Sioch

**Data:** 14.01.2022

**Platforma Sprzętowa:** Linux Fedora 35

**Sposób uruchamiania:** Należy wejść do folderu, w którym znajdują się pliki i uruchomić plik game.py za pomocą polecenia python3 game.py

**Zasada działania:** po włączeniu pliku w terminalu gracz musi wybrac jedna z trzech opcji, w tej wersji kodu do wyboru ma dwie dzialajace mozliwosci - grę oraz wyświetlanie najlepszych wynikow. Po wpisaniiu wartosci jeden wyswietli sie pole gry - 64 pola o współrzędnych (x,y), x, y c {1, 2, .., 8}. 
Niektóre z pól będą miały przypisaną wartość "+". Jest to pole zabronione, którego wartości nie da się zmienić w trakcie gry (liczba pól zabronionych jest 
losowo wybierana w trakcie uruchomienia programu, minimalnie jest ich 2, maksymalnie 6) Zadaniem gracza jest doprowadzić do sytuacji, w której żadne pole nie 
będzie miało wartości "O". W trakcie gry gracz kolejno wpisuje współrzędne pola, którego wartość chce zmienić. (najpierw wartość x, następnie wartość y). 
Oprócz punktu wybranego przez gracza, możliwa jest zmiana wartości punktów obok niego - jest to za każdym razem losowe. Minimalnie zmieni się jedno wybrane pole, 
maksymalnie dodatkowo 4 dookoła niego. W trakcie gry powyzej planszy gry po kazdym ruchu wyswietlany jest czas gry, ktory uplynal od momentu zaczecia rozgrywki oraz liczba punktow. Poczatkowo w tej wersji gry liczba punktow wynosi 50, nastepnie po kazdym ruchu od tej liczby odejmowane sa punkty w zaleznosci od ilosci czasu, ktory uplynal od rozpoczecia rozgrywki i liczby wykonanych ruchow. Dodatkowo, jesli gracz wybierze pole zabronione, liczba jego punktow zostanie zmniejszona o 2. Kiedy żadne pole nie będzie miało już wartośći "O" gra się kończy a na ekranie wyświetlana jest informacja o wygraniu gry, liczbie zdobytych punktow i 
o ilości ruchów, które były potrzebne do wygrania rozgrywki. Jesli wynik gracza kwalifikuje się do zapisu do listy najlepszych wyników, zostanie to zrobione pod koniec rozgrywki. 

**Algorytm:** 
Program działa w następujący sposób - na początku program czeka na wybor opcji. Jesli wybrana zostala liczba 2, wykonuje sie funkcja show_score_board, w ktorej otwierany jest plik scv z najlepszymi wynikami i parametrami tej gry (takiej jak czas, nickname, liczba ruchow), wartosci odczytane z pliku zapisywane sa do listy a nastepnie sa printowane na ekranie. Nastepnie program znowu oczekuje na wybor. Przy wybraniu opcji nr 1, czysczona jest konsola, a nastepnie wywolywana jest funkcja instruction, ktor wyswietla informacje odnosnie gry. Nastepnie wywoływana jest funkcja disturb_list, w trakcie której niektóre z pól mają zmienianą wartość na wartość zabronioną, czyli "+". Wartości takiego pola nie można zmienić w trakcie trwania gry. Liczba pól zabronionych jest generowana losowo, zawiera się w przedziale {2, 3, 4, 5, 6}. Następnie w pętli while wywoływane są po sobie funkcje print_board, change_field, check_status. Funkcja print_board wyświetla 
w konsoli pole gry. Domyślnie pola mają wartość "O", pola zabronione "+". W funkcji change_field wywoływana jest funkcja get_values, w której od gracza pobierane 
są współrzędne punktu, którego wartość ma być zmieniona. Dodatkowo w funkcji get_values, zliczany jest czas gry, po czym jest on wyswietlany w konsoli. Następnie punkt jest weryfikowany, najpierw przez pętle warunkową if (sprawdzenie, czy pole nie jest polem 
zabronionym) a następnie, jesli nie, generowana jest liczba od 1 do 5 i w zależności od niej wywoływana jest funkcja check_fields. Jeśli liczba wynosi 1, to f
unkcja ta wywoła się tylko raz - od punktów podanych przez gracza. Im większa jest liczba, tym więcej razy funkcja check_fields zostanie wykonana, czyli tym 
więcej wartości sąsiednich pól zostanie zmienionych. Następnei wywoływana jest funkcja check_status, w trakcie której sprawdzany jest stan gry, a dokładniej 
liczba znaków "O" w liście field_list. Jeśli wynosi ona 0 to zwracana jest wartosc 1. W glownym programie gry, jesli zwrocona wartosc == 1, to wykonywane sa funkcje save_score oraz win_game. W funkcji save_score otwierany jest plik csv z zapisanymi wartosciami w trybie odczytu, sa one odczytywane i zapisywane do tablicy. Nastepnie wynik z obecnej rozgrywki jest porownywany z wynikami z zapisanych rozgrywek. Jesli wynik aktualnej rozgrywki jest wiekszy od n-tego wyniku w pliku, n-ty wynik jest nadpisywany aktualnym. Jesli miejsce bylo pierwsze lub drugie odpowiednie wyniki zostaja przeniesione o jedno miejsce nizej. Nastepnie plik ten jest otwierany w trybie zapisu i wartosci zakutalizowanej listy zostaja do niego zapisane. Na koniec w funkcji win_game wyswietlana jest informacja o koncu gry a elemnty listy field_list maja przypisane domyslne wartosci - czyli znaki "O" i zostaje wykonane wyjscie z petli while, w ktorej byly wykonywane sekwencje instrukcji - program znowu czeka na wybor opcji.


**Wykaz zmiennych:**
- legal_fields - lista złożona z liczb od 0 do 7, wykorzystywana jest do pętli w funkcjach
- field_list - lista list, która przechowuje wartości pól
- move_number - zmienna, w której zapisywana jest liczba ruchów wykonanych przez gracza
- o_number - zmienna, do której zapisywana jest liczba znaków "O" w liście field_list
- x, y - zmienne, do których zapisywane są współrzędne punktów podanych przez gracza
- minutes, seconds - zmienne, w ktorych przechowywany jest czas gry
- start_time, end_time - zmienne, do ktorych zapisywane sa czasy wywolan funkcji time.perf_counter a nastepnie roznica tych wartosci przypisywana jest do zmiennej seconds
- i, j, n, k - zmienne pomocnicze w funkcjach do instrukcji warunkowych.
- player - lista, w ktorej zostaja zapisane wartosci najlepszych rozgrywek (w funkcjach operujacych na plikach)
- player_statistics - lista z zapisanymi wartosciami aktualnej gry (takimi jak czas, liczba punktow etc.)



**Wykaz funkcji:**
- instruction() - funkcja, ktora wyswietla informacje odnosnie gry
- win_game() - funkcja, ktora wyswietla informacje o zakonczeniu gry i przywraca domyslne wartosci pol w liscie field_list
- clear_console() - funkcja, która przy każdym wywołaniu czyści konsole
- show_scoreboard() - funkcja, w ktorej otwierany jest plik csv, gdzie zapisane sa najlepsze wyniki wraz z innymi parametrami a nastepnie sa one wyswietlane na ekranie
- save_score() - funkca, ktora otwiera plik csv z najlepszymi wynikami i sprwadza, czy liczba punktow gracza jest wieksza od ktorejs z zapisanych wartosci - jesli tak, to wynik ten wraz z nickiem gracza zostanie zapisany do pliku
- disturb_list() - funkcja, która przy wywołaniu zmienia kilka wartości pól na zabronione (od 2 do 6 pól)
- print_board() - funkcja, która przy wywołaniu wyświetla tablice gry
- get_values() - funkcja, która pobiera od gracza współrzędne punktu, którego stan ma być zmieniony. Dodatkowo w funkcji tej zliczany jest czas gry (poniewaz czas mija podczas pobierania wartosci od gracza)
- check_fields() - funkcja, która weryfikuje współrzędne punktu podanego przez gracza. Jeśli punkt ma którąś ze współrzędnych <0lub >7, to nie robione jest nic. 
W pozostałych przypadkach jeśli pole ma wartość "O" to zamieniane jest na "X"
- change_field() - funkcja, w której wywoływana jest funkcja get_values a następnie sprawdzany jest punkt podany przez gracza. Jeśli ma on wartość "+" to 
wyświetlana jest informacja o niemożności zmiany wartości pola zabronionego. W pozostałych przypadkach generowana jest liczba od 1 do 5 i w zależności od niej 
zmieniane są wartości x pól.
- check_status() - funkcja, w której sprawdzany jest status gry. Jeśli liczba znaków "O" w list_fields jest równa 0, to funkcja zwraca wartość 1. 
