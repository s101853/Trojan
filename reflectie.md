## GitHub Trojan

[GitHub Repository](https://github.com/s101853/Trojan)  
[Panopto Video](https://ap.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=09ea4a73-771b-498e-94a1-b26100ab7427)

### Reflectie

#### Welke technieken waren het meest effectief?
- **Exploitmodules:** 
  - **Screenshot Capturing:** Het onopgemerkt vastleggen van scherminhoud om gevoelige informatie te verkrijgen.
  - **DDOS Attacks:** Het succesvol uitvoeren van gedistribueerde denial-of-service-aanvallen om systemen te verstoren.
  - **Bash & Reverse Shell Execution:** Het verkrijgen van toegang tot een machine voor verdere exploitatie en het uitvoeren van commando’s wanneer gewenst.

#### Hoe kan dit in een realistisch scenario misbruikt worden en hoe kun je zulke aanvallen voorkomen?
- **Misbruikmogelijkheden:**
  - **Screenshot Capturing:** Kan worden gebruikt om gevoelige informatie zoals wachtwoorden of persoonlijke gegevens vast te leggen.
  - **DDOS Attacks:** Kan kritieke diensten verstoren, wat kan leiden tot uitval of overbelasting van systemen.
  - **Reverse Shell Execution:** Kan worden ingezet om volledige controle over een systeem te krijgen voor kwaadaardige activiteiten.

- **Preventie:** 
  - **Endpoint Protection:** Gebruik van antivirussoftware en intrusion detection/prevention systems (IDS/IPS) om verdachte activiteiten te detecteren en te blokkeren.
  - **Rate Limiting and Firewalls:** Bescherming tegen DDOS-aanvallen door het beperken van de hoeveelheid toegestane verzoeken en het gebruik van firewalls.
  - **Access Control:** Beperken van toegang en het regelmatig bijwerken van wachtwoorden en systeemupdates om reverse shells te voorkomen.

#### Jouw eigen leerproces tijdens de opdracht
- **Uitdagingen:** Het waarborgen van de functionaliteit door middel van grondige tests, het omgaan met uitzonderingen, en het verifiëren van de compatibiliteit met de evoluerende GitHub-data.
- **Verbeteringen:** Regelmatige updates en het oplossen van bugs die tijdens het testen zijn ontdekt, waren essentieel om het programma operationeel te houden.

### Reflectieverslag

#### Beschrijf je bevindingen
Tijdens deze opdracht probeerde ik zoveel mogelijk functionaliteit in het script te integreren, zodat het meerdere vormen van input kon afhandelen. Dit omvatte het versturen van DDOS-aanvallen, het maken van screenshots, en het uitvoeren van commando's. Hoewel het script niet volledig is geoptimaliseerd om elke mogelijke invoer te verwerken met uitgebreide foutafhandeling, zijn de kernfunctionaliteiten aanwezig en operationeel.

#### Keuzes
- **Gebruik van GitHub API, dynamische configuratie en taakuitvoering:** Het script maakt gebruik van de GitHub API om configuratieveranderingen te detecteren en uit te voeren. Dit zorgt voor een dynamische en flexibele uitvoering van opdrachten op basis van wijzigingen in de repository.

#### Uitdagingen
- **Foutafhandeling en compatibiliteit:** Het consistent houden van de code was een grote uitdaging, vooral omdat veel functies afhankelijk waren van elkaar. Een voorbeeld hiervan was de **execute_bash_command**-functie, die initieel werkte met de standaard **sh**-shell, terwijl ik **/bin/bash** nodig had voor de reverse shell. Dit vereiste aanpassingen in de foutafhandelingslogica om correct te reageren op verschillende soorten commando’s.

#### Ethische inzichten
- **Overwegingen rondom het gebruik van dergelijke scripts:** Deze opdracht gaf me waardevolle inzichten in de mogelijkheden en de complexiteit van exploitatie. Hoewel we technieken zoals reverse shells en DDOS-aanvallen gebruikten, die vaak worden misbruikt, bood dit project een educatief perspectief op hoe dergelijke aanvallen werken en hoe ze kunnen worden tegengegaan.

### Demo

#### Korte uitleg bij de handelingen in de demovideo
1. Alle programma's worden opgestart, waarbij ze hun ID en systeeminformatie doorzenden.
2. De **Screenshot-module** wordt uitgevoerd en de gemaakte screenshots worden naar GitHub geüpload.
3. De **DDOS-module** voert een aanval uit op een lokaal draaiende webserver, wat resulteert in een storing en tijdelijke uitval van de website.
4. Tot slot voeren we een **reverse shell-command** uit via GitHub. Dit commando arriveert op de Linux-machine en activeert de shell op Kali. Op Windows gebeurt er niets, maar de module kan worden uitgebreid om ook op Windows een reverse shell te activeren.
