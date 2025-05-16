# Magister Add-on voor Home Assistant

Deze add-on maakt een REST API beschikbaar binnen Home Assistant waarmee je gegevens uit Magister kunt ophalen, zoals huiswerk.

## Installatie

1. Voeg deze repository toe aan Home Assistant als custom add-on repository:
   ```
   https://github.com/reiniertc/magister-addon
   ```

2. Installeer de add-on.
3. Voer je school-URL, gebruikersnaam en wachtwoord in bij de configuratie.
4. Start de add-on.

De API is beschikbaar op poort 8000, bijvoorbeeld:
```
http://homeassistant.local:8000/huiswerk
```
