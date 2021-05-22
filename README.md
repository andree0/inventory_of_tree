Tree Inventory System (TIS)
---------------------

**Technologies used:** Python 3.x, Django, Django Rest Framework, Web Scrapping, \
PostgreSQL, OpenStreetMap, pytest, Bootstrap

**Description app:** This is application for landscape architects \
and dendrologist to inventory of green places.
# Tree Inventory System (TIS)


### Aplikacja ta powinna umożliwiać:

* wyświetlać listę wszystkich inwenatryzacji
* przeglądanie szczegółów inwenatryzacji oraz zinwentaryzowanych drzew
* dodawanie inwentaryzacji terenów zieleni z określeniem geolokalizacji na mapie
* dodawanie drzew do inwentaryzacji z określeniem ich stanu zdrowotnego
* edytować inwentaryzację tylko autorowi oraz użytkownikom którym została udostępniona
* generowanie raportów w formacie xls, pdf oraz wniosków urzędowych
* dołączanie do drzewa dokumentacji fotograficznej
* dołączanie do inwentaryzacji plików dwg

### Opis kroków realizacji inwentaryzacji:

1. Tworzenie nowej inwentaryzacji: nadanie nazwy inwentaryzacji, określenie autora, zleceniodawce, lokalizację
2. Inwenatryzacja o statusie "otwarta" będzie składać sie z 3 etapów: inwentaryzacja --> waloryzacja --> gospodarka drzewostanem
3. Etap "inwentaryzacja": spisanie drzew (gatunek, obwód pnia, zasięg korony, wysokość drzewa, skala reloffa)
4. Etap "waloryzacja": określenie stanu drzew
5. Etap "gospodarka drzewostanem": określenie zabiegów dla drzewa, przeznaczenie do wycinki lub pozostawienie
6. W każdym etapie możliwość generowania i podpinania plików
7. Zamknięcie inwentaryzacji
