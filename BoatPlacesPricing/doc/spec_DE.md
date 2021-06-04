Entität: BoatPlacesPricing  
==========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Der Zweck des Datenmodells ist es, Informationen über die Preisgestaltung von Festmachern nach Kategorie (Länge / Breite) zu liefern. Die erhaltenen Informationen beziehen sich nur auf Freizeitboote und schließen gewerbliche Boote und Boote zur Personenbeförderung aus. Die Informationen zu den Spot-Kategorien für Boote sind der Norm ISO 8666 entnommen.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateLastReported`: Ein Zeitstempel, der den letzten Zeitpunkt angibt, an dem das Gerät erfolgreich Daten gemeldet hat. Das Datum und die Uhrzeit dieser Beobachtung im ISO8601 UTC-Format  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `fairing`: Ticketpreis des Platzes für Verkleidungsboote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 3 Untereigenschaften, wobei jedes Element ein String im Format `Schlüssel` : `Preis` in Euro € ist  - `id`: Eindeutiger Bezeichner der Entität  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `maxDraft`: Maximal zulässiger Tiefgang für den Zugriff auf den Spot. Der Einheitencode (Text) wird unter Verwendung der [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben  - `maxLength`: Maximal zulässige Länge für den Zugriff auf den Spot. Der Gerätecode (Text) wird unter Verwendung der [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben  - `maxWidth`: Maximal zulässige Breite für den Zugriff auf den Spot. Der Gerätecode (Text) wird unter Verwendung der [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben  - `minLength`: Mindestlänge, die für den Zugriff auf den Spot erlaubt ist. Der Gerätecode (Text) wird unter Verwendung der [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `passage`: Ticketpreis des Platzes für durchfahrende Boote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 3 Untereigenschaften, wobei jedes Element ein String im Format `Schlüssel` : `Preis` in Euro € ist  - `period`: Typ des Zeitraums, der das Datum von und bis definiert: Ein freier Text oder ein eindeutiger Wert der verschiedenen erlaubten Kombinationen 'season / offSeason' - 'summer / winter' - 'low / medium / high'. enum:'high, low, medium, offSeason, season, summer, winter'  - `refPointOfInterest`: Verweis auf einen [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md), der mit dem Repository verknüpft ist  - `refSeaPort`: Verweis auf die Entität [Seaport](https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md), die als Hauptlink verwendet werden soll  - `resident`: Ticketpreis des Platzes für ansässige Boote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 2 Untereigenschaften, wobei jedes Element ein String im Format `Schlüssel` : `Preis` in Euro € ist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `spotCategoryRange`: Liste von den niedrigsten bis zu den höchsten Kategorien: Eine Kombination von ihnen. Enum:'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'  - `type`: NGSI-Entitätstyp. Es muss BoatPlacePricing sein  - `validFrom`: Startdatum und Uhrzeit der Preisregeln.  - `validThrough`: Enddatum und Uhrzeit der Preisregeln.  - `wintering`: Ticketpreis des Platzes für überwinternde Boote für diese Kategorie / diesen Zeitraum. Ein strukturierter Wert mit 3 Untereigenschaften, wobei jedes Element ein String im Format `Schlüssel` : `Preis` in Euro € ist    
Erforderliche Eigenschaften  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`  - `validFrom`  - `validThrough`    
Methode zur Gestaltung Ihres Repositorys für Bootspreise* Um die verschiedenen Preise nach Kategorie (A bis Z17) im Abschnitt *Informationen zur Preisgestaltung* zu beschreiben, ist die Verwendung einer Liste beim Schreiben des Datensatzes erforderlich. Abhängig von der Hafenkonfiguration wird ein Datensatz von 'spotCategoryRange' erstellt, um die Preisgestaltung für einen Zeitraum als Repository zu bestimmen. Es sind zwei Szenarien möglich - Szenario 1. Definition des Längenbereichs für eine einzelne Kategorie . 'spotCategoryRange' = [F], Boote akzeptiert= Länge 7,00 bis 7,49 und max Breite =< 2,70. [F] Länge 7,00 bis 7,49 / max Breite =< 2,70 - Szenario 2. Definition des Längenbereichs mit aufeinanderfolgenden Kategorien. 'spotCategoryRange' = [F, G], Boote akzeptiert= Länge 7,00 bis 7,99 und max Breite =< 2,80.'F' ergibt maxLänge von 7,00 bis 7,49 und maxBreite 2,70, 'G' ergibt maxLänge von 7,50 bis 7,99 und maxBreite 2,80  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BoatPlacesPricing:    
  description: 'The purpose of the data model is to provide information on the pricing of mooring rings by category (length / Width). The information received relates only to pleasure boats and excludes commercial and passenger transport boats. The information on the Spot categories for boats is taken from the ISO 8666 standard.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
    id:    
      anyOf: &boatplacespricing_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    maxDraft:    
      description: 'Maximum draft allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
        units: metres    
    maxLength:    
      description: 'Maximum length allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/number    
        units: metres    
    maxWidth:    
      description: 'Maximum width allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
        units: metres    
    minLength:    
      description: 'Minimum length allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) '    
      type: Property    
      x-ngsi:    
        model: https://schema.org/number    
        units: metres    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *boatplacespricing_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    refPointOfInterest:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    refSeaPort:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the entity [Seaport](https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md) to use as main link'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    resident:    
      description: 'Ticket price of the place for resident boats for this category / period. A structured value with 2 subproperties where each items is a string in the format `key` : `price` in Euro €'    
      properties:    
        annual:    
          type: number    
        month:    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be BoatPlacePricing'    
      enum:    
        - BoatPlacesPricing    
      type: Property    
    validFrom:    
      description: 'Start date and time of the pricing rules.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    validThrough:    
      description: 'End date and time of the pricing rules.'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    wintering:    
      description: 'Ticket price of the place for wintering boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €'    
      properties:    
        day:    
          type: number    
        month:    
          type: number    
        week:    
          type: number    
      type: Property    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
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
```  
</details>    
Zusätzliche Informationen zu diesem Datenmodell* Es kann mit dem folgenden Datenmodell verwendet werden. - **SeaPort** verwendet werden, um dem Hafen Informationen über autorisierte Boote im Hafen bereitzustellen.  
Dieses Datenmodell ist komplementär zum Datenmodell **BoatPlacesAvailable**.  
Datenspeicher (ISO 8666-Standard)** *Kategorie Länge Max Breite Max* A 4,99 2,00 B 5,49 2,15 C 5,99 2,30 D 6,49 2,45 E 6,99 2,60 F 7,49 2,80 G 7,99 2,80 H 8,49 2,95 I 8.99 3.10 J 9.49 3.25 K 9.99 3.40 L 10.49 3.55 M 10.99 3.70 N 11.49 3.85 O 11.99 4.00 P 12.99 4.30 Q 13.99 4.60 R 15.99 4.90 S 17.99 5.20 T1 20.99 5.60 T2 23.99 6.00 U 28,99 7,00 V 33,99 8,00 W 38,99 9,00 X 43,99 10,00 Y 48,99 11,00 Z 53,99 12,00 Z01 58,99 13,00 Z02 64,99 14,00 Z03 71,99 15,00 Z04 78,99 16,00 Z05 85,99 17,00 Z06 92,99 18.00 Z07 99.99 19.00 Z08 106.99 20.00 Z09 113.99 21.00 Z10 120.99 22.00 Z11 127.99 23.00 Z12 134.99 24.00 Z13 142.99 25.00 Z14 150.99 26.00 Z15 158.99 27.00 Z16 166.99 28.00 Z17 174.99 29.00  
## Beispiel-Nutzlasten  
#### BoatPlacesPricing NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine BoatPlacesPricing im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
  "maxWidth": 2.80,  
  "maxDraft": 2.55,  
  "validFrom": "2021-01-01T17:21:20Z",  
  "validThrough": "2021-02-10T17:21:20Z",  
  "period": "season",  
  "passage": {  
    "day": 29.45,  
    "week": 200.15,  
    "month": 821.20  
  },  
  "resident": {  
    "month": 760.41,  
    "annual": 9125.00  
  },  
  "wintering": {  
    "day": 27.00,  
    "week": 185.00,  
    "month": 775.00  
  },  
  "fairing": {  
    "day": 17.30,  
    "week": 87.00,  
    "month": 260.90  
  },  
  "location": {  
    "type": "Polygon",  
    "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]  
  }  
}  
```  
#### BoatPlacesPricing NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine BoatPlacesPricing im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
  "type": "BoatPlacePricing",  
  "name": {  
    "type": "Property",  
    "value": "Riviera-Port-NCE-SPAP-BPA-Range-FG"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Riviera Port - Pricing of the Places by Categories"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Pricing of the Places by Categories"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Riviera Port"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "refSeaPort": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
  },  
  "spotCategoryRange": {  
    "type": "property",  
    "value": [  
      "F",  
      "G"  
    ]  
  },  
  "minLength": {  
    "type": "Property",  
    "value": 7  
  },  
  "maxLength": {  
    "type": "Property",  
    "value": 7.99  
  },  
  "maxWidth": {  
    "type": "Property",  
    "value": 2.80  
  },  
  "maxDraft": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": "season"  
  },  
  "passage": {  
    "type": "Property",  
    "value": {  
      "day": 29.45,  
      "week": 200.15,  
      "month": 821.20  
    }  
  },  
  "resident": {  
    "type": "Property",  
    "value": {  
      "month": 760.41,  
      "annual": 9125.00  
    }  
  },  
  "wintering": {  
    "type": "Property",  
    "value": {  
      "day": 27.00,  
      "week": 185.00,  
      "month": 775.00  
    }  
  },  
  "fairing": {  
    "type": "Property",  
    "value": {  
      "day": 17.30,  
      "week": 87.00,  
      "month": 260.90  
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
    }  
  }  
}  
```  
#### BoatPlacesPricing NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für eine BoatPlacesPricing im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
  "type": "BoatPlacePricing",  
  "name": {  
    "type": "Property",  
    "value": "Riviera-Port-NCE-SPAP-BPA-Range-FG"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Riviera Port - Pricing of the Places by Categories"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Pricing of the Places by Categories"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Riviera Port"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "refSeaPort": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
  },  
  "spotCategoryRange": {  
    "type": "property",  
    "value": [  
      "F",  
      "G"  
    ]  
  },  
  "minLength": {  
    "type": "Property",  
    "value": 7  
  },  
  "maxLength": {  
    "type": "Property",  
    "value": 7.99  
  },  
  "maxWidth": {  
    "type": "Property",  
    "value": 2.8  
  },  
  "maxDraft": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": "season"  
  },  
  "passage": {  
    "type": "Property",  
    "value": {  
      "day": 29.45,  
      "week": 200.15,  
      "month": 821.2  
    }  
  },  
  "resident": {  
    "type": "Property",  
    "value": {  
      "month": 760.41,  
      "annual": 9125.0  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BootsplätzePreisgestaltung NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine BoatPlacesPricing im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
  "type": "BoatPlacePricing",  
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
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
