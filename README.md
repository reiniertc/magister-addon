# Magister Add-on voor Home Assistant

## let op: dit is in ontwikkeling, er is geen enkele garantie dat dit werkt
## ik stop er af en toe wat uurtjes in, als het eenmaal werkt zal ik het
## hier vermelden

Deze add-on maakt een REST API beschikbaar binnen je Home Assistant-installatie waarmee je gegevens uit [Magister](https://mijn.magister.net) kunt ophalen, zoals:

- Huiswerk (komende 5 dagen)

In de toekomst kun je deze add-on uitbreiden met rooster, cijfers, aanwezigheid, enz.

## ðŸ”§ Installatie

1. Voeg deze repository toe aan Home Assistant als **custom add-on repository**:
   ```
   https://github.com/<jouw-gebruikersnaam>/magister-addon
   ```

2. Installeer de add-on `Magister Add-on` via de Add-on Store.
3. Vul tijdens de installatie je Magister-accountgegevens in:
   - School-URL (bijv. `https://jouwschool.magister.net`)
   - Gebruikersnaam
   - Wachtwoord
4. Start de add-on.

De add-on draait op poort `8000` en biedt een endpoint aan:

```
http://homeassistant.local:8000/huiswerk
```

## ðŸ“¡ Gebruik in Home Assistant

### Sensor in `configuration.yaml`:

```yaml
sensor:
  - platform: rest
    name: Magister Huiswerk
    resource: http://homeassistant.local:8000/huiswerk
    value_template: "{{ value_json.aantal_opdrachten }}"
    json_attributes:
      - opdrachten
    scan_interval: 3600
```

### Lovelace weergave (voorbeeld):

```yaml
type: markdown
title: Huiswerk komende 5 dagen
content: >
  {% for item in state_attr('sensor.magister_huiswerk', 'opdrachten') %}
  **{{ item.vak }}** â€“ {{ item.beschrijving }}  
  Deadline: {{ item.datum }}  
  {% endfor %}
```

## ðŸ” Veiligheid

Je gebruikersnaam en wachtwoord worden **lokaal opgeslagen** in Home Assistant (niet in GitHub). Je hoeft dus geen gevoelige gegevens in deze repository te zetten.

## ðŸ“¦ Toekomstplannen

- [ ] Rooster ophalen via `/rooster`
- [ ] Cijfers ophalen via `/cijfers`
- [ ] Pushmeldingen bij nieuwe cijfers of wijzigingen

---

## ðŸ’¬ Feedback of bijdragen?

Open gerust een issue of pull request. Feedback en uitbreidingen zijn welkom!
