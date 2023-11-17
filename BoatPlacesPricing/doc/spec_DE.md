<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: BoatPlacesPricing    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Zweck des Datenmodells ist es, Informationen über die Preisgestaltung von Festmachern nach Kategorie (Länge/Breite) zu liefern. Die erhaltenen Informationen beziehen sich nur auf Freizeitboote und schließen gewerbliche Boote und Boote zur Personenbeförderung aus. Die Informationen über die Spot-Kategorien für Boote sind der Norm ISO 8666 entnommen.**    
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
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateLastReported[date-time]`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, zu dem das Gerät erfolgreich Daten gemeldet hat. Das Datum und die Uhrzeit dieser Beobachtung im ISO8601 UTC-Format  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `fairing[object]`: Ticketpreis des Platzes für Verkleidungsboote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 3 Untereigenschaften, wobei jedes Element eine Zeichenkette im Format `Schlüssel` : `Preis` in Euro € ist  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `day`:       
	- `month`:       
- `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxDraft[number]`: Maximal zulässiger Tiefgang für den Zugriff auf die Stelle. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLength[number]`: Maximal zulässige Länge für den Zugriff auf den Punkt. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben.  . Model: [https://schema.org/number](https://schema.org/number)- `maxWidth[number]`: Maximal zulässige Breite für den Zugriff auf den Spot. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben.  . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: Mindestlänge für den Zugriff auf die Stelle. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben  . Model: [https://schema.org/number](https://schema.org/number)- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `passage[object]`: Fahrpreis des Platzes für durchfahrende Boote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 3 Untereigenschaften, wobei jedes Element eine Zeichenkette im Format `Schlüssel` : `Preis` in Euro € ist  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `day`:       
	- `month`:       
- `period[string]`: Art des Zeitraums definiert das Datum von und bis: Ein freier Text oder ein eindeutiger Wert der verschiedenen zulässigen Kombinationen 'Saison / Nebensaison' - 'Sommer / Winter' - 'niedrig / mittel / hoch'. enum:'hoch, niedrig, mittel, Nebensaison, Saison, Sommer, Winter'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `refPointOfInterest[*]`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit dem Repository verknüpft ist  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[*]`: Verweis auf die Entität [Seehafen] (https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md) zur Verwendung als Hauptlink  . Model: [https://schema.org/URL](https://schema.org/URL)- `resident[object]`: Ticketpreis des Platzes für ansässige Boote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 2 Untereigenschaften, wobei jedes Element eine Zeichenkette im Format `Schlüssel` : `Preis` in Euro € ist  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `annual`:       
- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `spotCategoryRange[array]`: Liste von der niedrigsten bis zur höchsten Kategorie: Eine Kombination von ihnen. Enum:'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'  - `type[string]`: NGSI-Entitätstyp. Es muss BoatPlacePricing sein  - `validFrom[date-time]`: Datum und Uhrzeit des Beginns der Preisregeln  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validThrough[date-time]`: Datum und Uhrzeit des Endes der Preisregeln  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `wintering[object]`: Ticketpreis des Platzes für überwinternde Boote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 3 Untereigenschaften, wobei jedes Element eine Zeichenkette im Format `Schlüssel` : `Preis` in Euro € ist  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `day`:       
	- `month`:       
<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`  - `validFrom`  - `validThrough`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Methode zur Gestaltung Ihres Repositorys für Bootspreise* Um die verschiedenen Preise nach Kategorie (A bis Z17) im Abschnitt *Informationen über Preise* zu beschreiben, ist die Verwendung einer Liste beim Schreiben des Datensatzes erforderlich. Abhängig von der Hafenkonfiguration wird ein Datensatz von 'spotCategoryRange' erstellt, um die Preise für einen Zeitraum als Repository zu bestimmen. Zwei Szenarien sind möglich - Szenario 1. Definition des Längenbereichs für eine einzelne Kategorie. spotCategoryRange' = [F], Boote akzeptiert= Länge 7,00 bis 7,49 und maximale Breite =< 2,70. [F] Länge 7,00 bis 7,49 / max Breite =< 2,70 - Szenario 2. Definition des Längenbereichs mit aufeinanderfolgenden Kategorien. 'spotCategoryRange' = [F, G], Boote akzeptiert= Länge 7,00 bis 7,99 und max Breite =< 2,80.'F' ergibt maxLänge von 7,00 bis 7,49 und maxBreite 2,70, 'G' ergibt maxLänge von 7,50 bis 7,99 und maxBreite 2,80    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
BoatPlacesPricing:      
  description: The purpose of the data model is to provide information on the pricing of mooring rings by category (length / Width). The information received relates only to pleasure boats and excludes commercial and passenger transport boats. The information on the Spot categories for boats is taken from the ISO 8666 standard.      
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
      description: A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
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
    fairing:      
      description: 'Ticket price of the place for fairing boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €'      
      properties:      
        day:      
          type: number      
        month:      
          type: number      
        week:      
          type: number      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
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
      description: 'Maximum draft allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
        units: metres      
    maxLength:      
      description: 'Maximum length allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '      
      type: number      
      x-ngsi:      
        model: https://schema.org/number      
        type: Property      
        units: metres      
    maxWidth:      
      description: 'Maximum width allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '      
      type: number      
      x-ngsi:      
        model: https://schema.org/width      
        type: Property      
        units: metres      
    minLength:      
      description: 'Minimum length allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '      
      type: number      
      x-ngsi:      
        model: https://schema.org/number      
        type: Property      
        units: metres      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
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
    passage:      
      description: 'Ticket price of the place for passing boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €'      
      properties:      
        day:      
          type: number      
        month:      
          type: number      
        week:      
          type: number      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
    period:      
      description: 'Type of period defined the date From and Through: A free text or a unique value of the different combination allowed ''season / offSeason'' - ''summer / winter'' - ''low / medium / high''. enum:''high, low, medium, offSeason, season, summer, winter'''      
      enum:      
        - high      
        - low      
        - medium      
        - offSeason      
        - season      
        - summer      
        - winter      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
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
        model: https://schema.org/URL      
        type: Relationship      
    refSeaPort:      
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
      description: 'Reference to the entity [Seaport](https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md) to use as main link'      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    resident:      
      description: 'Ticket price of the place for resident boats for this category / period. A structured value with 2 subproperties where each items is a string in the format `key` : `price` in Euro €'      
      properties:      
        annual:      
          type: number      
        month:      
          type: number      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
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
    spotCategoryRange:      
      description: 'List from the lowest to the highest categories: A combination of them. Enum:''A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'''      
      items:      
        enum:      
          - A      
          - B      
          - C      
          - D      
          - E      
          - F      
          - G      
          - H      
          - I      
          - J      
          - K      
          - L      
          - M      
          - N      
          - O      
          - P      
          - Q      
          - R      
          - S      
          - T1      
          - T2      
          - U      
          - V      
          - W      
          - X      
          - Y      
          - Z      
          - Z01      
          - Z02      
          - Z03      
          - Z04      
          - Z05      
          - Z06      
          - Z07      
          - Z08      
          - Z08      
          - Z09      
          - Z10      
          - Z11      
          - Z12      
          - Z13      
          - Z14      
          - Z15      
          - Z16      
          - Z17      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be BoatPlacePricing      
      enum:      
        - BoatPlacesPricing      
      type: string      
      x-ngsi:      
        type: Property      
    validFrom:      
      description: Start date and time of the pricing rules      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    validThrough:      
      description: End date and time of the pricing rules      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    wintering:      
      description: 'Ticket price of the place for wintering boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €'      
      properties:      
        day:      
          type: number      
        month:      
          type: number      
        week:      
          type: number      
      type: object      
      x-ngsi:      
        model: https://schema.org/StructuredValue      
        type: Property      
  required:      
    - id      
    - type      
    - location      
    - dateLastReported      
    - refSeaPort      
    - spotCategoryRange      
    - validFrom      
    - validThrough      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Ports/BoatPlacePricing/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
Zusätzliche Informationen zu diesem Datenmodell* Es kann mit dem folgenden Datenmodell verwendet werden. - **SeaPort** verwendet werden, um dem Hafen Informationen über zugelassene Boote im Hafen zu liefern.    
Dieses Datenmodell ist eine Ergänzung zum Datenmodell **BoatPlacesAvailable**.    
Datenspeicher (ISO 8666 Standard)** *Kategorie Länge Max Breite Max* A 4,99 2,00 B 5,49 2,15 C 5,99 2,30 D 6,49 2,45 E 6,99 2,60 F 7,49 2,80 G 7,99 2,80 H 8,49 2,95 I 8.99 3.10 J 9.49 3.25 K 9.99 3.40 L 10.49 3.55 M 10.99 3.70 N 11.49 3.85 O 11.99 4.00 P 12.99 4.30 Q 13.99 4.60 R 15.99 4.90 S 17.99 5.20 T1 20.99 5.60 T2 23.99 6.00 U 28,99 7,00 V 33,99 8,00 W 38,99 9,00 X 43,99 10,00 Y 48,99 11,00 Z 53,99 12,00 Z01 58,99 13,00 Z02 64,99 14,00 Z03 71,99 15,00 Z04 78,99 16,00 Z05 85,99 17,00 Z06 92,99 18.00 Z07 99,99 19,00 Z08 106,99 20,00 Z09 113,99 21,00 Z10 120,99 22,00 Z11 127,99 23,00 Z12 134,99 24,00 Z13 142,99 25,00 Z14 150,99 26,00 Z15 158,99 27,00 Z16 166,99 28,00 Z17 174,99 29,00    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### BoatPlacesPricing NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein BoatPlacesPricing im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
  "type": "BoatPlacesPricing",  
  "name": "Riviera-Port-NCE-SPAP-BPA-Range-FG",  
  "alternateName": "Riviera Port - Pricing of the Places by Categories",  
  "description": "Pricing of the Places by Categories",  
  "seeAlso": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019",  
  "areaServed": "Riviera Port",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "spotCategoryRange": [  
    "F",  
    "G"  
  ],  
  "minLength": 7,  
  "maxLength": 7.99,  
  "maxWidth": 2.8,  
  "maxDraft": 2.55,  
  "validFrom": "2021-01-01T17:21:20Z",  
  "validThrough": "2021-02-10T17:21:20Z",  
  "period": "season",  
  "passage": {  
    "day": 29.45,  
    "week": 200.15,  
    "month": 821.2  
  },  
  "resident": {  
    "month": 760.41,  
    "annual": 9125.0  
  },  
  "wintering": {  
    "day": 27.0,  
    "week": 185.0,  
    "month": 775.0  
  },  
  "fairing": {  
    "day": 17.3,  
    "week": 87.0,  
    "month": 260.9  
  },  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          100,  
          0  
        ],  
        [  
          101,  
          0  
        ],  
        [  
          101,  
          1  
        ],  
        [  
          100,  
          1  
        ],  
        [  
          100,  
          0  
        ]  
      ]  
    ]  
  }  
}  
```  
</details>    
#### BoatPlacesPricing NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein BoatPlacesPricing im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
  "type": "BoatPlacesPricing",  
  "name": {  
    "type": "Text",  
    "value": "Riviera-Port-NCE-SPAP-BPA-Range-FG"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Riviera Port - Pricing of the Places by Categories"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Pricing of the Places by Categories"  
  },  
  "seeAlso": {  
    "type": "Text",  
    "value": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Riviera Port"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "refSeaPort": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
  },  
  "spotCategoryRange": {  
    "type": "StructuredValue",  
    "value": [  
      "F",  
      "G"  
    ]  
  },  
  "minLength": {  
    "type": "Number",  
    "value": 7  
  },  
  "maxLength": {  
    "type": "Number",  
    "value": 7.99  
  },  
  "maxWidth": {  
    "type": "Number",  
    "value": 2.8  
  },  
  "maxDraft": {  
    "type": "Number",  
    "value": 2.55  
  },  
  "validFrom": {  
    "type": "DateTime",  
    "value": "2021-01-01T17:21:20Z"  
  },  
  "validThrough": {  
    "type": "DateTime",  
    "value": "2021-02-10T17:21:20Z"  
  },  
  "period": {  
    "type": "Text",  
    "value": "season"  
  },  
  "passage": {  
    "type": "StructuredValue",  
    "value": {  
      "day": 29.45,  
      "week": 200.15,  
      "month": 821.2  
    }  
  },  
  "resident": {  
    "type": "StructuredValue",  
    "value": {  
      "month": 760.41,  
      "annual": 9125.0  
    }  
  },  
  "wintering": {  
    "type": "StructuredValue",  
    "value": {  
      "day": 27.0,  
      "week": 185.0,  
      "month": 775.0  
    }  
  },  
  "fairing": {  
    "type": "StructuredValue",  
    "value": {  
      "day": 17.3,  
      "week": 87.0,  
      "month": 260.9  
    }  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        [  
          [  
            100,  
            0  
          ],  
          [  
            101,  
            0  
          ],  
          [  
            101,  
            1  
          ],  
          [  
            100,  
            1  
          ],  
          [  
            100,  
            0  
          ]  
        ]  
      ],  
      "type": "Polygon"  
    }  
  }  
}  
```  
</details>    
#### BoatPlacesPricing NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein BoatPlacesPricing im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-LD, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
  "type": "BoatPlacesPricing",  
  "alternateName": "Riviera Port - Pricing of the Places by Categories",  
  "areaServed": "Riviera Port",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "description": "Pricing of the Places by Categories",  
  "fairing": {  
    "day": 17.3,  
    "week": 87.0,  
    "month": 260.9  
  },  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          100,  
          0  
        ],  
        [  
          101,  
          0  
        ],  
        [  
          101,  
          1  
        ],  
        [  
          100,  
          1  
        ],  
        [  
          100,  
          0  
        ]  
      ]  
    ]  
  },  
  "maxDraft": 2.55,  
  "maxLength": 7.99,  
  "maxWidth": 2.8,  
  "minLength": 7,  
  "name": "Riviera-Port-NCE-SPAP-BPA-Range-FG",  
  "passage": {  
    "day": 29.45,  
    "week": 200.15,  
    "month": 821.2  
  },  
  "period": "season",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "resident": {  
    "month": 760.41,  
    "annual": 9125.0  
  },  
  "seeAlso": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019",  
  "spotCategoryRange": [  
    "F",  
    "G"  
  ],  
  "validFrom": "2021-01-01T17:21:20Z",  
  "validThrough": "2021-02-10T17:21:20Z",  
  "wintering": {  
    "day": 27.0,  
    "week": 185.0,  
    "month": 775.0  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### BoatPlacesPricing NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein BoatPlacesPricing im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
    "type": "BoatPlacePricing",  
    "alternateName": {  
        "type": "Property",  
        "value": "Riviera Port - Pricing of the Places by Categories"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Riviera Port"  
    },  
    "dateLastReported": {  
      "type": "Property",  
        "value": {  
          "@type": "DateTime",  
          "@value": "2020-03-17T08:45:00Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Pricing of the Places by Categories"  
    },  
    "fairing": {  
        "type": "Property",  
        "value": {  
            "day": 17.3,  
            "week": 87.0,  
            "month": 260.9  
        }  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Polygon",  
            "coordinates": [  
                [  
                    [  
                        100,  
                        0  
                    ],  
                    [  
                        101,  
                        0  
                    ],  
                    [  
                        101,  
                        1  
                    ],  
                    [  
                        100,  
                        1  
                    ],  
                    [  
                        100,  
                        0  
                    ]  
                ]  
            ]  
        }  
    },  
    "maxDraft": {  
        "type": "Property",  
        "value": 2.55  
    },  
    "maxLength": {  
        "type": "Property",  
        "value": 7.99  
    },  
    "maxWidth": {  
        "type": "Property",  
        "value": 2.8  
    },  
    "minLength": {  
        "type": "Property",  
        "value": 7  
    },  
    "name": {  
        "type": "Property",  
        "value": "Riviera-Port-NCE-SPAP-BPA-Range-FG"  
    },  
    "passage": {  
        "type": "Property",  
        "value": {  
            "day": 29.45,  
            "week": 200.15,  
            "month": 821.2  
        }  
    },  
    "period": {  
        "type": "Property",  
        "value": "season"  
    },  
    "refSeaPort": {  
        "type": "Relationship",  
        "value": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
    },  
    "resident": {  
        "type": "Property",  
        "value": {  
            "month": 760.41,  
            "annual": 9125.0  
        }  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019"  
    },  
    "spotCategoryRange": {  
        "type": "Property",  
        "value": [  
            "F",  
            "G"  
        ]  
    },  
    "validFrom": {  
        "type": "Property",  
        "value": {  
          "@type": "DateTime",  
          "@value": "2021-02-10T17:21:20Z"  
        }  
    },  
    "validThrough": {  
        "type": "Property",  
        "value": {  
          "@type": "DateTime",  
          "@value": "2021-02-10T17:21:20Z"  
        }  
    },  
    "wintering": {  
        "type": "Property",  
        "value": {  
            "day": 27.0,  
            "week": 185.0,  
            "month": 775.0  
        }  
    },  
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
