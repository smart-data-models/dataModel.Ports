<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: SeaportFacilities  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Das Datenmodell dient der Bereitstellung von Informationen über Häfen, die der Freizeitschifffahrt, dem Handel oder der Personenbeförderung dienen können. Es ermöglicht die Darstellung der Parameter jedes Hafens, seines Standorts, seiner Liegeplatzkapazitäten und der damit verbundenen kostenlosen oder kostenpflichtigen Dienstleistungen, die direkt vom Hafen oder von Fachleuten, die im oder in der Nähe des Hafens arbeiten, erbracht werden.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedPropulsion[array]`: A Antriebsart, die zum Einlaufen in den Hafen zugelassen ist. Eine Kombination aus Motor, Segel, Elektroantrieb, Ruder, Nuklearantrieb, Flüssiggas, Flüssiggas, andere  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatSupplyingServices[array]`: Beschreibung der ergänzenden Versorgungsdienste für das Schiff, die von Fachleuten angeboten werden, die im oder in der Nähe des Hafens arbeiten. Eine Kombination aus Bewachung, FuelStation, FuelTankerTruck, TrinkwasserTankerTruck, Proviantierung, DryFairing, WaterFairing, Reparatur, Expertise, Gangways, LiftCranes, Schleppen, WasteWaterPumping, BoatConveying, BoatTransfer, Sonstiges  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `contactPoint[object]`: https://schema.org/ContactPoint  - `contractingAuthority[string]`: Name des öffentlichen Auftraggebers  . Model: [https://schema.org/Text](https://schema.org/Text)- `contractingCompany[string]`: Die für die Verwaltung des Hafens zuständige Vertragsgesellschaft  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `currencyAccepted[array]`: Eine Kombination aus einer Liste aktiver Codes, die im Modell [Norm ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Kryptowährungen](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Börsenhandelssystem](https://en.wikipedia.org/wiki/Local_exchange_trading_system  . Model: [https://schema.org/currenciesAccepted, .Currency accepted for payment](https://schema.org/currenciesAccepted, .Currency accepted for payment)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateLastReported[date-time]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem ein Fluss erfolgreich Daten gemeldet hat. Das Datum und die Uhrzeit dieses Repositorys im ISO8601 UTC-Format  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `electricTransport[array]`:  Liste der verschiedenen von der Stadt vorgeschlagenen Arten von Elektrofahrzeugen. Eine Kombination aus Elektroauto, Elektrofahrrad, Elektromotorrad und Elektroroller  . Model: [http://schema.org/Text](http://schema.org/Text)- `endDate[date-time]`: Datum und Uhrzeit des Endes der Sendung (im Datumsformat ISO 8601).  . Model: [https://schema.org/endDate](https://schema.org/endDate)- `facilities[array]`: Beschreibung der vorgeschlagenen Einrichtungen im Hafen. Eine Kombination aus: Toiletten, Duschen, Wäscherei, Telefon, Mülltonnen, Müllcontainer, Container, Mülltrennung, Stromanschluss, Wasseranschluss, Zimmerreservierung, WiFi, Sonstiges  . Model: [http://schema.org/Text](http://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxDraft[number]`: A Höchstzulässiger Tiefgang für den Zugang zum Hafen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  . Model: [http://schema.org/Number](http://schema.org/Number)- `maxTonnage[number]`: Maximale Tonnage, die für den Zugang zum Hafen zugelassen ist. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **TNE** für Tonne Metrisch  . Model: [http://schema.org/Number](http://schema.org/Number)- `maxWidth[number]`: A Maximal zulässige Breite für den Zugriff auf den Hafen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  . Model: [http://schema.org/Number](http://schema.org/Number)- `maximumLength[number]`: A Maximal zulässige Länge für den Zugriff auf den Hafen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  . Model: [http://schema.org/Number](http://schema.org/Number)- `minimumLength[number]`: A Mindestlänge für den Zugriff auf den Hafen. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben. Zum Beispiel steht **MTR** für Meter  . Model: [http://schema.org/Number](http://schema.org/Number)- `name[string]`: Der Name dieses Artikels  - `nearbyServices[array]`: Beschreibung der zusätzlichen Dienstleistungen in dem geografischen Gebiet am oder in der Nähe des Hafens. Eine Kombination aus: Fremdenverkehrsbüro, Einrichtungsgeschäften, Reisebüro, Wechselstube, Arztpraxis, Apotheke, Lebensmittelgeschäften, Restaurants, Druckereien, Bar, Geschäften, Meeresausflügen, Stadtrundfahrten, touristischen Ausflügen, anderen  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `numberOfPlace[number]`: Gesamtzahl der Plätze im Hafen  . Model: [http://schema.org/Number](http://schema.org/Number)- `openingHours[string]`: Die allgemeinen Öffnungszeiten für ein Unternehmen. Die Öffnungszeiten können als wöchentliche Zeitspanne angegeben werden, beginnend mit Tagen, dann Zeiten pro Tag. Mehrere Tage können mit Kommas ',' zwischen den einzelnen Tagen angegeben werden. Tages- oder Zeitbereiche werden mit einem Bindestrich '-' angegeben. Tage werden mit den folgenden Kombinationen aus zwei Buchstaben angegeben: Mo, Di, We, Do, Fr, Sa, So. Zeiten werden im 24:00-Format angegeben. So wird beispielsweise 15 Uhr als 15:00 Uhr und 10 Uhr als 10:00 Uhr angegeben. Hier ist ein Beispiel: <time itemprop='openingHours' datetime='Di,Do 16:00-20:00'>Dienstags und donnerstags 16-20 Uhr</time>. Wenn ein Geschäft 7 Tage in der Woche geöffnet ist, kann es als <time itemprop='openingHours' datetime='Mo-So'>Montag bis Sonntag, den ganzen Tag</time> angegeben werden.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `openingHoursSpecification[array]`: Ein strukturierter Wert, der Informationen über die Öffnungszeiten eines Ortes oder einer bestimmten Dienstleistung an einem Ort liefert  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `paymentAccepted[array]`: Akzeptierte Zahlung. Eine Kombination aus einer Liste aktiver Codes, die im Modell definiert sind: Bargeld, Kreditkarte, CryptoCurrency, andere  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `portServicesProvided[array]`: Beschreibung der Dienstleistungen, die direkt vom Hafen angeboten werden. Eine Kombination aus: harborOffice, weather, customsServices, porters, boatRingRental, mooringAssistance, handlingAssistance, publicWifi, privateWifi, other  . Model: [http://schema.org/Text](http://schema.org/Text)- `refBoatAuthorized[array]`: Verweis auf eine Liste von [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md)  - `refBoatPlaceAvailable[array]`: Verweis auf eine Liste von [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)  . Model: [https://schema.org/URL](https://schema.org/URL)- `refBoatPlacePricing[array]`: Verweis auf eine Liste von [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)  . Model: [https://schema.org/URL](https://schema.org/URL)- `refDevice[*]`: Verweis auf die Haupteinheit [Gerät] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) bei Verwendung als zweite Verbindung  - `refPointOfInterest[*]`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit dem Repository verknüpft ist  - `rentalSaleServices[array]`: ADie Beschreibung der Dienstleistungen, die von professionellen Verkaufs- oder Vermietungsagenturen im geografischen Gebiet am oder in der Nähe des Hafens angeboten werden. Eine Kombination aus : Bootsvermietung, Bootsverkauf, JetSkiVermietung, JetSkiVerkauf, AutoVermietung, LuxusAutoVermietung, VanVermietung, FahrradVermietung, MotorrollerVermietung, Caddie, PalettenTransport, Sonstiges  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `routeType[array]`: Liste der verschiedenen Arten von Nahverkehrsmitteln (U-Bahn, Bus, Straßenbahn, ...) aus dem GFTS-Standard für Nahverkehrsmittel [STOP] (https://developers.google.com/transit/gtfs/reference/#stopstxt). Eine Kombination von Werten, die nur aus dem Attribut "Beschreibung" bestehen Straßenbahn(0), U-Bahn(1), Zug(2), Bus(3), Fähre(4), CableTram(5), CableCar(6), Standseilbahn(7), Oberleitungsbus(11), Einschienenbahn(12)  . Model: [http://schema.org/Text](http://schema.org/Text)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `startDate[date-time]`: Datum und Uhrzeit des Beginns der Sendung (im Datumsformat ISO 8601).  . Model: [https://schema.org/startDate](https://schema.org/startDate)- `transportServices[array]`: Beschreibung der Dienstleistungen im Bereich der Sondertransporte und Shuttle-Dienste. Eine Kombination aus: Parken, ShuttlesZumFlughafen, ShuttlesZurEisenbahn, interneShuttles, Taxis, Hubschrauberlandeplatz, Sonstiges  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `type[string]`: Es muss SeaPortFacilities sein  - `typeOfPort[array]`: Ein Hafentyp. Eine Kombination aus: Jachthafen, Warenverkehr, Kreuzfahrt, Fähre, Passagiere, Yachting, Fischerei, Militär, Fluss, Sonstiges  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `webSite[string]`: Link zur offiziellen Website des Hafens für weitere Informationen  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `dateLastReported`  - `id`  - `location`  - `type`  - `typeOfPort`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SeaportFacilities:    
  description: 'The Data Model is intended to provide information about ports that can accommodate pleasure craft, commerce or passenger  transport. It permit to represent the parameters of each port, its location, its mooring capacities and the free or paid services associated with it provided directly by the port or by professionals working on or near the port.'    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    authorizedPropulsion:    
      description: 'A Type of propulsion authorized to enter in the harbor. A combination of motor, sail, electric, oar, nuclear, lng, lpg, other'    
      items:    
        enum:    
          - motor    
          - sail    
          - electric    
          - oar    
          - nuclear    
          - lng    
          - lpg    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    boatSupplyingServices:    
      description: 'Description of the complementary supplying services for the boat offered by professionals working on or near the harbor. A combination of guarding, fuelStation, fuelTankerTruck , drinkingWaterTankerTruck, provisioning, dryFairing, waterFairing, repair, expertise, gangways, liftingCranes, towing, wasteWaterPumping, boatConveying, boatTransfer, other'    
      items:    
        enum:    
          - boatConveying    
          - boatTransfer    
          - drinkingWaterTankerTruck    
          - dryFairing    
          - expertise    
          - fuelStation    
          - fuelTankerTruck    
          - gangways    
          - guarding    
          - liftingCranes    
          - provisioning    
          - repair    
          - towing    
          - waterFairing    
          - wasteWaterPumping    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    contactPoint:    
      description: https://schema.org/ContactPoint    
      type: object    
      x-ngsi:    
        type: Property    
    contractingAuthority:    
      description: Name of the contracting authority    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contractingCompany:    
      description: The Contracting Company responsible of the management of the port    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    currencyAccepted:    
      description: 'A combination of a list of active codes defined in the model [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system'    
      items:    
        enum:    
          - AUD    
          - GBP    
          - EUR    
          - JPY    
          - CHF    
          - USD    
          - AFN    
          - ALL    
          - DZD    
          - AOA    
          - ARS    
          - AMD    
          - AWG    
          - AUD    
          - ATS (EURO)    
          - BEF (EURO)    
          - AZN    
          - BSD    
          - BHD    
          - BDT    
          - BBD    
          - BYR    
          - BZD    
          - BMD    
          - BTN    
          - BOB    
          - BAM    
          - BWP    
          - BRL    
          - GBP    
          - BND    
          - BGN    
          - BIF    
          - XOF    
          - XAF    
          - XPF    
          - KHR    
          - CAD    
          - CVE    
          - KYD    
          - CLP    
          - CNY    
          - COP    
          - KMF    
          - CDF    
          - CRC    
          - HRK    
          - CUC    
          - CUP    
          - CYP (EURO)    
          - CZK    
          - DKK    
          - DJF    
          - DOP    
          - XCD    
          - EGP    
          - SVC    
          - EEK (EURO)    
          - ETB    
          - EUR    
          - FKP    
          - FIM (EURO)    
          - FJD    
          - GMD    
          - GEL    
          - DMK (EURO)    
          - GHS    
          - GIP    
          - GRD (EURO)    
          - GTQ    
          - GNF    
          - GYD    
          - HTG    
          - HNL    
          - HKD    
          - HUF    
          - ISK    
          - INR    
          - IDR    
          - IRR    
          - IQD    
          - IED (EURO)    
          - ILS    
          - ITL (EURO)    
          - JMD    
          - JPY    
          - JOD    
          - KZT    
          - KES    
          - KWD    
          - KGS    
          - LAK    
          - LVL (EURO)    
          - LBP    
          - LSL    
          - LRD    
          - LYD    
          - LTL (EURO)    
          - LUF (EURO)    
          - MOP    
          - MKD    
          - MGA    
          - MWK    
          - MYR    
          - MVR    
          - MTL (EURO)    
          - MRO    
          - MUR    
          - MXN    
          - MDL    
          - MNT    
          - MAD    
          - MZN    
          - MMK    
          - ANG    
          - NAD    
          - NPR    
          - NLG (EURO)    
          - NZD    
          - NIO    
          - NGN    
          - KPW    
          - NOK    
          - OMR    
          - PKR    
          - PAB    
          - PGK    
          - PYG    
          - PEN    
          - PHP    
          - PLN    
          - PTE (EURO)    
          - QAR    
          - RON    
          - RUB    
          - RWF    
          - WST    
          - STD    
          - SAR    
          - RSD    
          - SCR    
          - SLL    
          - SGD    
          - SKK (EURO)    
          - SIT (EURO)    
          - SBD    
          - SOS    
          - ZAR    
          - KRW    
          - ESP (EURO)    
          - LKR    
          - SHP    
          - SDG    
          - SRD    
          - SZL    
          - SEK    
          - CHF    
          - SYP    
          - TWD    
          - TZS    
          - THB    
          - TOP    
          - TTD    
          - TND    
          - TRY    
          - TMM    
          - USD    
          - UGX    
          - UAH    
          - UYU    
          - AED    
          - VUV    
          - VEB    
          - VND    
          - YER    
          - ZMK    
          - ZWD    
        type: string    
      type: array    
      x-ngsi:    
        model: 'https://schema.org/currenciesAccepted, .Currency accepted for payment'    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastReported:    
      description: A timestamp which denotes the last time when a flow successfully reported data. The date and time of this Repository in ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    electricTransport:    
      description: ' List of the different types of electric transport proposed by the city. A combination of electricCar, electricBycicle, electricMotorBike, electricScooter '    
      items:    
        enum:    
          - electricBycicle    
          - electricCar    
          - electricMotorBike    
          - electricScooter    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    endDate:    
      description: The end date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/endDate    
        type: Property    
    facilities:    
      description: 'Description of the proposed facilities on the harbor. A combination of : toilets, showers, laundry, telephone, dustbins, dumpsters, container, selectiveSortingWaste, electricTerminal, waterTerminal, indoorRoomReservation, wifi, other'    
      items:    
        enum:    
          - container    
          - dustbins    
          - dumpsters    
          - electricTerminal    
          - 'indoorRoomReservation '    
          - laundry    
          - selectiveSortingWaste    
          - showers    
          - telephone    
          - toilets    
          - waterTerminal    
          - wifi    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    maxDraft:    
      description: 'A Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    maxTonnage:    
      description: 'Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: TNE    
    maxWidth:    
      description: 'A Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    maximumLength:    
      description: 'A Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    minimumLength:    
      description: 'A Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nearbyServices:    
      description: 'Description of the additional services on the geographical area on or near the harbor. A combination of :touristOffice, fittingsStores, travelAgency, exchangeOffice, medicalOffice, pharmacy, groceryStores, restaurants, presses, bar, shops, seaExcursions, cityTour, touristicExcursions, others'    
      items:    
        enum:    
          - bar    
          - cityTour    
          - fittingsStores    
          - groceryStores    
          - exchangeOffice    
          - medicalOffice    
          - pharmacy    
          - presses    
          - restaurants    
          - seaExcursions    
          - shops    
          - touristicExcursions    
          - touristOffice    
          - travelAgency    
          - others    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    numberOfPlace:    
      description: Total number of place in the harbor    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    openingHours:    
      description: 'The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas '','' separating each day. Day or time ranges are specified using a hyphen ''-''. Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su. Times are specified using 24:00 format. For example, 3pm is specified as 15:00, 10am as 10:00. Here is an example: <time itemprop=''openingHours'' datetime=''Tu,Th 16:00-20:00''>Tuesdays and Thursdays 4-8pm</time>. If a business is open 7 days a week, then it can be specified as <time itemprop=''openingHours'' datetime=''Mo-Su''>Monday through Sunday, all day</time>'    
      type: string    
      x-ngsi:    
        model: https://schema.org/openingHours    
        type: Property    
    openingHoursSpecification:    
      description: A structured value providing information about the opening hours of a place or a certain service inside a place    
      items:    
        properties:    
          closes:    
            description: ' 	The closing hour of the place or service on the given day(s) of the week'    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          dayOfWeek:    
            anyOf:    
              - description: Array of days of the week    
                enum:    
                  - Monday    
                  - Tuesday    
                  - Wednesday    
                  - Thursday    
                  - Friday    
                  - Saturday    
                  - Sunday    
                  - PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
              - description: Array of days of the week    
                enum:    
                  - https://schema.org/Monday    
                  - https://schema.org/Tuesday    
                  - https://schema.org/Wednesday    
                  - https://schema.org/Thursday    
                  - https://schema.org/Friday    
                  - https://schema.org/Saturday    
                  - https://schema.org/Sunday    
                  - https://schema.org/PublicHolidays    
                type: string    
                x-ngsi:    
                  type: Property    
            description: 'The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)'    
            type: string    
            x-ngsi:    
              model: http://schema.org/dayOfWeek    
              type: Property    
          opens:    
            description: The opening hour of the place or service on the given day(s) of the week    
            format: time    
            type: string    
            x-ngsi:    
              type: Property    
          validFrom:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            x-ngsi:    
              type: Property    
          validThrough:    
            anyOf:    
              - description: ""    
                format: date    
                type: string    
                x-ngsi:    
                  model: http://schema.org/Date    
                  type: Property    
              - description: ""    
                format: date-time    
                type: string    
                x-ngsi:    
                  model: http://schema.org/DateTime    
                  type: Property    
            description: 'The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format'    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    paymentAccepted:    
      description: 'Accepted payment. A combination of a list of active codes defined in the model : Cash, CreditCard, CryptoCurrency, other'    
      items:    
        enum:    
          - Cash    
          - CreditCard    
          - CryptoCurrency    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    portServicesProvided:    
      description: 'Description of the services provided directly by the harbor. A combination of : harborOffice, weather, customsServices, porters, boatRingRental, mooringAssistance, handlingAssistance, publicWifi, privateWifi, other'    
      items:    
        enum:    
          - harborOffice    
          - weather    
          - customsServices    
          - porters    
          - boatRingRental    
          - mooringAssistance    
          - handlingAssistance    
          - publicWifi    
          - privateWifi    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    refBoatAuthorized:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md)'    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Relationship    
    refBoatPlaceAvailable:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)'    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    refBoatPlacePricing:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)'    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refDevice:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
      x-ngsi:    
        type: Relationship    
    refPointOfInterest:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository'    
      x-ngsi:    
        type: Relationship    
    rentalSaleServices:    
      description: 'ADescription of services provided by professional sales or rental agencies on the geographical area on or near the harbor. A combination of : boatRental, boatSale, jetSkiRental, jetSkiSale, carRental, luxuryCarRental, vanRental, bikeRental, scooterRental, Caddie, palletTransport, other'    
      items:    
        enum:    
          - bikeRental    
          - boatRental    
          - boatSale    
          - Caddie    
          - carRental    
          - jetSkiRental    
          - jetSkiSale    
          - luxuryCarRental    
          - palletTransport    
          - scooterRental    
          - vanRental    
          - Others    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    routeType:    
      description: "List of the different types of urban transport Mode (Metro, Bus, Tram, ...) from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values composed only of the attribute 'description' tram(0), metro(1), train(2), bus(3), ferry(4), cableTram(5), cableCar(6), funicular(7), trolleybus(11), monorail(12)"    
      items:    
        enum:    
          - bus    
          - cableCar    
          - cableTram    
          - ferry    
          - funicular    
          - metro    
          - monorail    
          - train    
          - tram    
          - trolleybus    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    startDate:    
      description: The start date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/startDate    
        type: Property    
    transportServices:    
      description: 'Description of the services provided for dedicated transport and shuttle services. A combination of : parking, shuttlesToAirport, shuttlesToRailway, internalShuttles, taxis, heliport, other'    
      items:    
        enum:    
          - heliport    
          - internalShuttle    
          - parking    
          - shuttlesToAirport    
          - shuttlesToRailway    
          - taxis    
          - Others    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    type:    
      description: It has to be SeaPortFacilities    
      enum:    
        - SeaPortFacilities    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfPort:    
      description: 'A Type of harbor. A combination of : marina, merchandise, cruise, ferry, passengers, yachting, fishing, military, river, other'    
      items:    
        enum:    
          - cruise    
          - ferry    
          - fishing    
          - marina    
          - merchandise    
          - military    
          - passengers    
          - river    
          - yachting    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    webSite:    
      description: Link to the official website of the harbor for more information    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - typeOfPort    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.Ports/SeaPortFacilities/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### SeaportFacilities NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine SeaportFacilities im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
  "type": "SeaPort",  
  "name": "Riviera-Port-NCE-SP-001",  
  "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
  "description": "Harbor Description and services provided",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Port",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "refBoatAuthorized": [  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
  ],  
  "refBoatPlaceAvailable": [  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
  ],  
  "refBoatPlacePricing": [  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
  ],  
  "owner": [  
    "Departement_06", "CCI06", "MNCA", "Ville_de_Nice"  
  ],  
  "contractingAuthority": "CCI",  
  "contractingCompany": "Régie Autonome des ports",  
  "contactPoint": "Capitainerie",  
  "webSite": "https://riviera-ports.com/ports/port-de-nice",  
  "typeOfPort": [  
    "marina",  
    "merchandise",  
    "cruise",  
    "ferry",  
    "yatching"  
  ],  
  "authorizedPropulsion": [  
    "motor",  
    "electric",  
    "lng"  
  ],  
  "maxTonnage": 30000,  
  "numberOfPlace": 120,  
  "minLength": 6,  
  "maxLength": 180,  
  "maxWidth": 25,  
  "maxDraft": 9.65,  
  "portServicesProvided": [  
    "harborOffice",  
    "weather",  
    "customsServices",  
    "porters"  
  ],  
  "boatSupplyingServices": [  
    "fuelStation",  
    "fuelTankerTruck",  
    "drinkingWaterTankerTruck",  
    "dryFairing",  
    "repair",  
    "expertise",  
    "gangways",  
    "liftingCranes",  
    "towing",  
    "wasteWaterPumping",  
    "boatConveying"  
  ],  
  "facilities": [  
    "wifi",  
    "telephone",  
    "toilets",  
    "selectiveSortingWaste",  
    "electricTerminal",  
    "waterTerminal",  
    "dustbins",  
    "dumpsters",  
    "container"  
  ],  
  "nearbyServices": [  
    "groceryStores",  
    "presses",  
    "exchangeOffice",  
    "touristicExcursions"  
  ],  
  "rentalSaleServices": [  
    "boatRental",  
    "boatSale",  
    "carRental"  
  ],  
  "transportServices": [  
    "parking",  
    "shuttlesToAirport",  
    "taxis"  
  ],  
  "routeType": [  
    "tram",  
    "metro",  
    "train",  
    "bus",  
    "ferry"  
  ],  
  "electricTransport": [  
    "electricBycicle",  
    "electricMotorBike"  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR",  
    "USD"  
  ]  
}  
```  
</details>  
#### SeaportFacilities NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine SeaportFacilities im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
	"type": "SeaPort",  
	"name": {  
		"type": "Property",  
		"value": "Riviera-Port-NCE-SP-001"  
	},  
	"alternateName": {  
		"type": "Property",  
		"value": "Riviera Port - Main harbor - Commerce & Passengers"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Harbor Description and services provided"  
	},  
	"seeAlso": {  
		"type": "Property",  
		"value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "point",  
				"coordinates": [43.664810, 7.196545]  
			}  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Port"  
	},  
	"dateLastReported": {  
		"type": "DateTime",  
		"value": "2020-03-17T08:45:00Z",  
		"metadata": {  
			"TimeInstant": {  
				"type": "Text",  
				"value": "2020-03-17TT08:45:00Z"  
			}  
		}  
	},  
	"refBoatAuthorized": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
		]  
	},  
	"refBoatPlaceAvailable": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
		]  
	},  
	"refBoatPlacePricing": {  
		"type": "Relationship",  
		"Object": ["urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
		]  
	},  
	"owner" : {  
		"type": "Property",  
		"value": ["Departement_06", "CCI06", "MNCA", "Ville_de_Nice"]  
	},  
	"contractingAuthority": {  
		"type": "Property",  
		"value": "CCI"  
	},  
	"contractingCompagny": {  
		"type": "Property",  
		"value": "Régie Autonome des ports"  
	},  
	"contactPoint": {  
		"type": "Property",  
		"value": "Capitainerie"  
	},  
	"webSite": {  
		"type": "Property",  
		"value": "https://riviera-ports.com/ports/port-de-nice"  
	},  
	"typeOfPort": {  
		"type": "Property",  
		"value": ["marina", "merchandise", "cruise", "ferry", "yatching"]  
	},  
	"authorizedPropulsions": {  
		"type": "Property",  
		"value": ["motor", "electric","lng"]  
	},  
	"maxTonnage": {  
		"type": "Property",  
		"value": 30000  
	},  
	"numberOfPlace": {  
		"type": "Property",  
		"value": 120  
	},  
	"minLength": {  
		"type": "Property",  
		"value": 6  
	},  
	"maxLength": {  
		"type": "Property",  
		"value": 180  
	},  
	"maxWidth": {  
		"type": "Property",  
		"value": 25  
	},  
	"maxDraft": {  
		"type": "Property",  
		"value": 9.65  
	},  
	"portServicesProvided": {  
		"type": "Property",  
		"value": ["harborOffice", "weather", "customsServices", "porters"]  
	},  
	"boatSupplyingServices": {  
		"type": "Property",  
		"value": ["fuelStation", "fuelTankerTruck", "drinkingWaterTankerTruck", "dryFairing", "repair", "expertise", "gangways", "liftingCranes", "towing", "wasteWaterPumping", "boatConveying"]  
	},  
	"facilities": {  
		"type": "Property",  
		"value": ["wifi", "telephone", "toilets", "selectiveSortingWaste", "electricTerminal", "waterTerminal", "dustbins", "dumpsters", "container"]  
	},  
	"nearbyServices": {  
		"type": "Property",  
		"value": ["groceryStores", "presses", "exchangeOffice", "touristicExcursions"]  
	},  
	"rentalSaleServices": {  
		"type": "Property",  
		"value": ["boatRental", "boatSale", "carRental"]  
	},  
	"transportServices": {  
		"type": "Property",  
		"value": ["parking", "shuttlesToAirport", "taxis"]  
	},  
	"routeType": {  
		"type": "Property",  
		"value": ["tram", "metro", "train", "bus", "ferry"]  
	},  
	"electricTransport": {  
		"type": "Property",  
		"value": ["electricBycicle", "electricMotorBike"]  
	},  
	"paymentAccepted": {  
		"type": "Property",  
		"value": ["Cash", "CreditCard"]  
	},  
	"currencyAccepted": {  
		"type": "Property",  
		"value": ["EUR", "USD"]  
	}  
}  
```  
</details>  
#### SeaportFacilities NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine SeaportFacilities im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
    "type": "SeaPort",  
    "alternateName": {  
        "type": "Property",  
        "value": "Riviera Port - Main harbor - Commerce & Passengers"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Port"  
    },  
    "authorizedPropulsions": {  
        "type": "Property",  
        "value": [  
            "motor",  
            "electric",  
            "lng"  
        ]  
    },  
    "boatSupplyingServices": {  
        "type": "Property",  
        "value": [  
            "fuelStation",  
            "fuelTankerTruck",  
            "drinkingWaterTankerTruck",  
            "dryFairing",  
            "repair",  
            "expertise",  
            "gangways",  
            "liftingCranes",  
            "towing",  
            "wasteWaterPumping",  
            "boatConveying"  
        ]  
    },  
    "contactPoint": {  
        "type": "Property",  
        "value": "Capitainerie"  
    },  
    "contractingAuthority": {  
        "type": "Property",  
        "value": "CCI"  
    },  
    "contractingCompagny": {  
        "type": "Property",  
        "value": "R\u00e9gie Autonome des ports"  
    },  
    "currencyAccepted": {  
        "type": "Property",  
        "value": [  
            "EUR",  
            "USD"  
        ]  
    },  
    "dateLastReported": {  
        "type": "DateTime",  
        "value": "2020-03-17T08:45:00Z",  
        "metadata": {  
            "TimeInstant": {  
                "type": "Text",  
                "value": "2020-03-17TT08:45:00Z"  
            }  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Harbor Description and services provided"  
    },  
    "electricTransport": {  
        "type": "Property",  
        "value": [  
            "electricBycicle",  
            "electricMotorBike"  
        ]  
    },  
    "facilities": {  
        "type": "Property",  
        "value": [  
            "wifi",  
            "telephone",  
            "toilets",  
            "selectiveSortingWaste",  
            "electricTerminal",  
            "waterTerminal",  
            "dustbins",  
            "dumpsters",  
            "container"  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "point",  
            "coordinates": [  
                43.66481,  
                7.196545  
            ]  
        }  
    },  
    "maxDraft": {  
        "type": "Property",  
        "value": 9.65  
    },  
    "maxLength": {  
        "type": "Property",  
        "value": 180  
    },  
    "maxTonnage": {  
        "type": "Property",  
        "value": 30000  
    },  
    "maxWidth": {  
        "type": "Property",  
        "value": 25  
    },  
    "minLength": {  
        "type": "Property",  
        "value": 6  
    },  
    "name": {  
        "type": "Property",  
        "value": "Riviera-Port-NCE-SP-001"  
    },  
    "nearbyServices": {  
        "type": "Property",  
        "value": [  
            "groceryStores",  
            "presses",  
            "exchangeOffice",  
            "touristicExcursions"  
        ]  
    },  
    "numberOfPlace": {  
        "type": "Property",  
        "value": 120  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "Departement_06",  
            "CCI06",  
            "MNCA",  
            "Ville_de_Nice"  
        ]  
    },  
    "paymentAccepted": {  
        "type": "Property",  
        "value": [  
            "Cash",  
            "CreditCard"  
        ]  
    },  
    "portServicesProvided": {  
        "type": "Property",  
        "value": [  
            "harborOffice",  
            "weather",  
            "customsServices",  
            "porters"  
        ]  
    },  
    "refBoatAuthorized": {  
        "type": "Relationship",  
        "Object": [  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
            "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
        ]  
    },  
    "refBoatPlaceAvailable": {  
        "type": "Relationship",  
        "Object": [  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
            "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
        ]  
    },  
    "refBoatPlacePricing": {  
        "type": "Relationship",  
        "Object": [  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
            "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
        ]  
    },  
    "rentalSaleServices": {  
        "type": "Property",  
        "value": [  
            "boatRental",  
            "boatSale",  
            "carRental"  
        ]  
    },  
    "routeType": {  
        "type": "Property",  
        "value": [  
            "tram",  
            "metro",  
            "train",  
            "bus",  
            "ferry"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
    },  
    "transportServices": {  
        "type": "Property",  
        "value": [  
            "parking",  
            "shuttlesToAirport",  
            "taxis"  
        ]  
    },  
    "typeOfPort": {  
        "type": "Property",  
        "value": [  
            "marina",  
            "merchandise",  
            "cruise",  
            "ferry",  
            "yatching"  
        ]  
    },  
    "webSite": {  
        "type": "Property",  
        "value": "https://riviera-ports.com/ports/port-de-nice"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SeaportFacilities NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine SeaportFacilities im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
    "type": "SeaPort",  
    "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
    "areaServed": "Nice Port",  
    "authorizedPropulsion": [  
        "motor",  
        "electric",  
        "lng"  
    ],  
    "boatSupplyingServices": [  
        "fuelStation",  
        "fuelTankerTruck",  
        "drinkingWaterTankerTruck",  
        "dryFairing",  
        "repair",  
        "expertise",  
        "gangways",  
        "liftingCranes",  
        "towing",  
        "wasteWaterPumping",  
        "boatConveying"  
    ],  
    "contactPoint": "Capitainerie",  
    "contractingAuthority": "CCI",  
    "contractingCompany": "R\u00e9gie Autonome des ports",  
    "currencyAccepted": [  
        "EUR",  
        "USD"  
    ],  
    "dateLastReported": "2020-03-17T08:45:00Z",  
    "description": "Harbor Description and services provided",  
    "electricTransport": [  
        "electricBycicle",  
        "electricMotorBike"  
    ],  
    "facilities": [  
        "wifi",  
        "telephone",  
        "toilets",  
        "selectiveSortingWaste",  
        "electricTerminal",  
        "waterTerminal",  
        "dustbins",  
        "dumpsters",  
        "container"  
    ],  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "maxDraft": 9.65,  
    "maxLength": 180,  
    "maxTonnage": 30000,  
    "maxWidth": 25,  
    "minLength": 6,  
    "name": "Riviera-Port-NCE-SP-001",  
    "nearbyServices": [  
        "groceryStores",  
        "presses",  
        "exchangeOffice",  
        "touristicExcursions"  
    ],  
    "numberOfPlace": 120,  
    "owner": [  
        "Departement_06",  
        "CCI06",  
        "MNCA",  
        "Ville_de_Nice"  
    ],  
    "paymentAccepted": [  
        "Cash",  
        "CreditCard"  
    ],  
    "portServicesProvided": [  
        "harborOffice",  
        "weather",  
        "customsServices",  
        "porters"  
    ],  
    "refBoatAuthorized": [  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
        "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
    ],  
    "refBoatPlaceAvailable": [  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
        "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
    ],  
    "refBoatPlacePricing": [  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
        "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
    ],  
    "rentalSaleServices": [  
        "boatRental",  
        "boatSale",  
        "carRental"  
    ],  
    "routeType": [  
        "tram",  
        "metro",  
        "train",  
        "bus",  
        "ferry"  
    ],  
    "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
    "transportServices": [  
        "parking",  
        "shuttlesToAirport",  
        "taxis"  
    ],  
    "typeOfPort": [  
        "marina",  
        "merchandise",  
        "cruise",  
        "ferry",  
        "yatching"  
    ],  
    "webSite": "https://riviera-ports.com/ports/port-de-nice",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
