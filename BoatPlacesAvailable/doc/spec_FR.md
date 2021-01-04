Entité : BoatPlacesAvailable  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesAvailable/LICENSE.md)  
Description globale : **Le but du modèle de données est de fournir des informations sur la disponibilité des anneaux d'amarrage pour les bateaux dans le port par catégorie. Les informations reçues ne concernent que les bateaux de plaisance et excluent les bateaux commerciaux et de transport de passagers. Les informations sur les catégories Spot pour les bateaux sont tirées de la norme ISO 8666.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `availableSpotNumber`: Nombre de places disponibles dans le port pour cette catégorie  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateObserved`: La date et l'heure de cette observation au format ISO8601 UTC. Elle peut être représentée par un instant précis ou par un intervalle ISO8601  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`:   - `maxDraft`: Tirant d'eau maximum autorisé pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Par exemple, **MTR** représente Meter  - `maxLength`: Longueur maximale autorisée pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MTR** représente Meter  - `maxWidth`: Largeur maximale autorisée pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Par exemple, **MTR** représente Meter  - `minLength`: Longueur minimale autorisée pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MTR** représente Meter  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `refPointOfInterest`: Point d'intérêt auquel l'élément a un rapport avec  - `refSeaPort`: Port qui appartient à  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `spotCategoryRange`:  Liste des catégories, de la plus basse à la plus haute : Une combinaison des éléments énumérés. Enumération : "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17".  - `totalCapacitySpotNumber`: Capacité totale du spot dans le port pour cette gamme  - `type`: Type d'entité NGSI. Il doit s'agir de BoatPlaceAvailable    
Propriétés requises  
- `availableSpotNumber`  - `dateObserved`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`    
Méthode de conception de votre répertoire des bateaux autorisés Pour décrire les différentes places disponibles par catégorie (A à Z17) dans la section Informations sur les places disponibles, l'utilisation d'une liste est nécessaire lors de la rédaction de la fiche. En fonction de la configuration du port, un enregistrement sera créé par "spotCategoryRange" pour déterminer le nombre de places restantes à un moment donné. Deux scénarios sont possibles Scénario 1. Définition de la plage de longueur sur une seule catégorie . `spotCategoryRange` = ["F"], Bateaux acceptés. longueur 7,00 à 7,49 et largeur maxi =< 2,70. "F" longueur 7,00 à 7,49 / largeur maxi =< 2,70 Scénario 2. Définition de la plage de longueur avec des catégories consécutives. SpotCategoryRange = ["F", "G"], Bateaux acceptés. longueur 7.00 à 7.99 et largeur max =< 2.80. "F" donne une longueur maximale de 7,00 à 7,49 et une largeur maximale de 2,70 G" donne une longueur maximale de 7,50 à 7,99 et une largeur maximale de 2,80  
Informations complémentaires sur ce modèle de données Il peut être utilisé avec le modèle de données suivant. - SeaPort pour fournir des informations au port sur les bateaux autorisés dans le port.  
Ce modèle de données est complémentaire au modèle de données BoatPlacesPricing.  
Référentiel de données (norme ISO 8666) Catégorie Longueur Largeur maximale A 4,99 2,00 B 5,49 2,15 C 5,99 2,30 D 6,49 2,45 E 6,99 2,60 F 7,49 2,80 G 7,99 2,80 H 8,49 2,95 I 8,99 3.10 J 9,49 3,25 K 9,99 3,40 L 10,49 3,55 M 10,99 3,70 N 11,49 3,85 O 11,99 4,00 P 12,99 4,30 Q 13,99 4,60 R 15,99 4,90 S 17,99 5,20 T1 20,99 5,60 T2 23.99 6,00 U 28,99 7,00 V 33,99 8,00 W 38,99 9,00 X 43,99 10,00 Y 48,99 11,00 Z 53,99 12,00 Z01 58,99 13,00 Z02 64,99 14,00 Z03 71,99 15,00 Z04 78,99 16,00 Z05 85,99 17,00 Z06 92.99 18,00 Z07 99,99 19,00 Z08 106,99 20,00 Z09 113,99 21,00 Z10 120,99 22,00 Z11 127,99 23,00 Z12 134,99 24,00 Z13 142,99 25,00 Z14 150,99 26,00 Z15 158,99 27,00 Z16 166,99 28,00 Z17 174,99 29,00  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BoatPlacesAvailable:    
  description: 'The purpose of the data model is to provide information on the availability of mooring rings for boats in the port by category. The information received relates only to pleasure boats and excludes commercial and passenger transport boats. The information on the Spot categories for boats is taken from the ISO 8666 standard.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    availableSpotNumber:    
      description: 'Number of places available in the port for this category'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format. It can be represented by a specific time instant or by an ISO8601 interval'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &boatplacesavailable_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth    
        units: meters    
    maxLength:    
      description: 'Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: meters    
    maxWidth:    
      description: 'Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
        units: meters    
    minLength:    
      description: 'Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: meters    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *boatplacesavailable_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
      description: 'Point of Interest that the element has relation to'    
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
      description: 'Port that belongs to'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
      description: ' List from the lowest to the highest categories: A combination of the items listed. Enum:''A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'''    
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
      x-ngsi:    
        model: https://schema.org/Text    
    totalCapacitySpotNumber:    
      description: 'Total Capacity of Spot in the port for this range'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Number    
    type:    
      description: 'NGSI Entity type. It has to be BoatPlaceAvailable'    
      enum:    
        - BoatPlaceAvailable    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateObserved    
    - refSeaPort    
    - spotCategoryRange    
    - availableSpotNumber    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### BoatPlacesAvailable NGSI V2 key-values Example  
Voici un exemple de place de bateau disponible au format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlaceAvailable:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
  "type": "BoatPlaceAvailable",  
  "name": "Riviera-Port-NCE-SPAP-BPA-Range-FG",  
  "alternateName": "Riviera Port - Available places",  
  "description": "Availability places",  
  "seeAlso": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019",  
  "areaServed": "Riviera Port",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "spotCategoryRange": [  
    "F",  
    "G"  
  ],  
  "minLength": 7,  
  "maxLength": 7.99,  
  "maxWidth": 2.80,  
  "maxDraft": 2.55,  
  "totalCapacitySpotNumber": 10,  
  "availableSpotNumber": 3,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      123,  
      45  
    ]  
  }  
}  
```  
#### BoatPlacesAvailable NGSI V2 normalized Example  
Voici un exemple d'une place de bateau disponible au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlaceAvailable:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
  "type": "BoatPlaceAvailable",  
  "name": {  
    "type": "Property",  
    "value": "Riviera-Port-NCE-SPAP-BPA-Range-FG"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Riviera Port - Available places"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Availability places"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Riviera Port"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-03-17T08:45:00Z"  
      }  
    }  
  },  
  "refSeaPort": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
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
  "totalCapacitySpotNumber": {  
    "type": "Property",  
    "value": 10  
  },  
  "availableSpotNumber": {  
    "type": "Property",  
    "value": 3  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        123,  
        45  
      ]  
    }  
  }  
}  
```  
#### BoatPlacesAvailable NGSI-LD key-values Example  
Voici un exemple de place de bateau disponible au format JSON-LD en tant que valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlaceAvailable:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
  "type": "BoatPlaceAvailable",  
  "name": "Riviera-Port-NCE-SPAP-BPA-Range-FG",  
  "alternateName": "Riviera Port - Available places",  
  "description": "Availability places",  
  "seeAlso": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019",  
  "areaServed": "Riviera Port",  
  "dateObserved": "2020-03-17T08:45:00Z",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "spotCategoryRange": [  
    "F",  
    "G"  
  ],  
  "minLength": 7,  
  "maxLength": 7.99,  
  "maxWidth": 2.80,  
  "maxDraft": 2.55,  
  "totalCapacitySpotNumber": 10,  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      123,  
      45  
    ]  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BoatPlacesAvailable NGSI-LD normalized Example  
Voici un exemple d'une place de bateau disponible en format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatPlaceAvailable:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
  "type": "BoatPlaceAvailable",  
  "name": {  
    "type": "Property",  
    "value": "Riviera-Port-NCE-SPAP-BPA-Range-FG"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Riviera Port - Available places"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Availability places"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Riviera Port"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z",  
    "metadata": {  
      "TimeInstant": {  
        "type": "Text",  
        "value": "2020-03-17T08:45:00Z"  
      }  
    }  
  },  
  "refSeaPort": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
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
  "totalCapacitySpotNumber": {  
    "type": "Property",  
    "value": 10  
  },  
  "availableSpotNumber": {  
    "type": "Property",  
    "value": 3  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        123,  
        45  
      ]  
    }  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
