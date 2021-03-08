Entité : BoatPlacesPricing  
==========================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md)  
Description globale : **Le but du modèle de données est de fournir des informations sur la tarification des anneaux d'amarrage par catégorie (longueur / largeur). Les informations reçues concernent uniquement les bateaux de plaisance et excluent les bateaux commerciaux et de transport de passagers. Les informations sur les catégories Spot pour les bateaux sont tirées de la norme ISO 8666.**  

## Liste des biens  

- `address`: L'adresse postale  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateLastReported`: Un horodatage qui indique la dernière fois où l'appareil a transmis des données avec succès. La date et l'heure de cette observation au format UTC ISO8601  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `fairing`: Prix du billet de la place pour les bateaux de carénage pour cette catégorie / période. Une valeur structurée avec 3 sous-propriétés où chaque élément est une chaîne de caractères au format "clé" : "prix" en Euro €  - `id`: Identifiant unique de l'entité  - `location`:   - `maxDraft`: Tirant d'eau maximum autorisé pour accéder au spot. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  - `maxLength`: Longueur maximale autorisée pour accéder au spot. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  - `maxWidth`: Largeur maximale autorisée pour accéder au spot. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  - `minLength`: Longueur minimale autorisée pour accéder au spot. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `passage`: Prix du billet de la place pour les bateaux de passage pour cette catégorie / période. Une valeur structurée avec 3 sous-propriétés où chaque élément est une chaîne de caractères au format "clé" : "prix" en Euro €  - `period`: Le type de période définit la date du et jusqu'au : Un texte libre ou une valeur unique pour les différentes combinaisons autorisées "saison / hors saison" - "été / hiver" - "faible / moyen / élevé". énumérez : "élevé, faible, moyen, hors saison, saison, été, hiver".  - `refPointOfInterest`: Référence à un [PointOfInterest] (https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) lié au dépôt  - `refSeaPort`: Référence à l'entité [Seaport] (https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md) à utiliser comme lien principal  - `resident`: Prix du billet de la place pour les bateaux résidents pour cette catégorie / période. Une valeur structurée avec 2 sous-propriétés où chaque élément est une chaîne de caractères au format "clé" : "prix" en Euro €  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `spotCategoryRange`: Liste des catégories, de la plus basse à la plus haute : Une combinaison de ces catégories. Enumération : "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17".  - `type`: Type d'entité NGSI. Il doit s'agir de BoatPlacePricing  - `validFrom`: Date et heure de début des règles de tarification.  - `validThrough`: Date et heure de fin des règles de tarification.  - `wintering`: Prix du billet de la place pour les bateaux d'hivernage pour cette catégorie / période. Une valeur structurée avec 3 sous-propriétés où chaque élément est une chaîne de caractères au format "clé" : "prix" en Euro €    
Propriétés requises  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`  - `validFrom`  - `validThrough`    
Méthode de conception de votre référentiel de tarification des bateaux* Pour décrire les différentes tarifications par catégorie (A à Z17) dans la section *Informations sur la tarification*, l'utilisation d'une liste est nécessaire lors de la rédaction de la fiche. En fonction de la configuration du port, un enregistrement sera créé par "spotCategoryRange" pour déterminer la tarification pour une période donnée. Deux scénarios sont possibles - Scénario 1. Définition de la fourchette de longueur sur une seule catégorie . spotCategoryRange" = [F], Bateaux acceptés = longueur de 7,00 à 7,49 et largeur maximale =< 2,70. [F] longueur 7,00 à 7,49 / largeur maximale =< 2,70 - Scénario 2. Définition de la plage de longueur avec des catégories consécutives. spotCategoryRange" = [F, G], Bateaux acceptés= longueur 7.00 à 7.99 et largeur max =< 2.80. "F" donne maxLongueur de 7.00 à 7.49 et maxLargeur 2.70, "G" donne maxLongueur de 7.50 à 7.99 et maxLargeur 2.80  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/areaServed'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/https://schema.org/postalCode'''    
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
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
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
            - format: uri    
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
Informations complémentaires sur ce modèle de données* Il peut être utilisé avec le modèle de données suivant. - **Port maritime** pour fournir au port des informations sur les bateaux autorisés dans le port.  
Ce modèle de données est complémentaire au modèle de données **BoatPlacesAvailable**.  
Référentiel de données (norme ISO 8666)** *Catégorie Longueur Largeur maximale* A 4,99 2,00 B 5,49 2,15 C 5,99 2,30 D 6,49 2,45 E 6,99 2,60 F 7,49 2,80 G 7,99 2,80 H 8,49 2,95 I 8.99 3,10 J 9,49 3,25 K 9,99 3,40 L 10,49 3,55 M 10,99 3,70 N 11,49 3,85 O 11,99 4,00 P 12,99 4,30 Q 13,99 4,60 R 15,99 4,90 S 17,99 5,20 T1 20,99 5,60 T2 23,99 6.00 U 28,99 7,00 V 33,99 8,00 W 38,99 9,00 X 43,99 10,00 Y 48,99 11,00 Z 53,99 12,00 Z01 58,99 13,00 Z02 64,99 14,00 Z03 71,99 15,00 Z04 78,99 16,00 Z05 85,99 17,00 Z06 92,99 18.00 Z07 99,99 19,00 Z08 106,99 20,00 Z09 113,99 21,00 Z10 120,99 22,00 Z11 127,99 23,00 Z12 134,99 24,00 Z13 142,99 25,00 Z14 150,99 26,00 Z15 158,99 27,00 Z16 166,99 28,00 Z17 174,99 29,00  
## Exemples de charges utiles  
#### BoatPlacesPricing NGSI V2 key-values Exemple  
Voici un exemple d'un BoatPlacesPricing au format JSON comme valeurs clés. Ce format est compatible avec NGSI V2 lorsqu'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### BoatPlacesPricing NGSI V2 normalisé Exemple  
Voici un exemple d'un BoatPlacesPricing au format JSON tel que normalisé. Ce format est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### BoatPlacesPricing NGSI-LD key-values Example  
Voici un exemple d'un BoatPlacesPricing au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BoatPlacesPricing NGSI-LD normalisé Exemple  
Voici un exemple d'un BoatPlacesPricing au format JSON-LD tel que normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
