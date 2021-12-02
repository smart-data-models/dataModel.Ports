Entité : BoatAuthorized  
=======================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatAuthorized/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le modèle de données est destiné à fournir des informations sur les bateaux autorisés à circuler dans le port selon la norme ISO 8666 relative à la catégorie de bateau. Ce référentiel est créé par type de catégorie de bateau (plaisance, commerce, passagers, ...). Pour chaque type de catégorie, une liste de sous-types optionnels de catégorie peut être associée.**  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `boatSubType`: Sous-type pour un boatType. Une combinaison des éléments. Enum :'porte-avions, navire amphibie, navire de manutention d'ancres, navire artisanal, bac, barge, porte-charges, vraquier, bateau-bouée, transporteur de butane, câblier, canoë, caravelle, porte-cargo, carraque, catamaran, transporteur de produits chimiques, clipper, caboteur, cog, porte-conteneurs, corvette, grue, transporteur de brut, bateau de croisière, croiseur, destroyer, boutre, navire de plongée, djong, drague, navire de forage, navire-usine, ferry, bateau-feu, navire de recherche halieutique, navire amiral, unité flottante de stockage de la production, unité flottante de stockage, fluyt, frégate, gabare, galion, galère, gondole, harbourFerry, porte-hélicoptères, navire à grande vitesse, houseBoat, aéroglisseur, brise-glace, jetSki, jonque, koch, canot de sauvetage, navire léger, paquebot, navire de ligne, transporteur de gaz liquéfié, navire de combat côtier, transporteur de bétail, transporteur de gaz naturel liquéfié, transporteur de gaz de pétrole liquéfié, balayeur de mines, monocoque, bateau d'amarrage, navire polyvalent, bateau océanographique, autre, bateau à pagaies, bateau-pilote, pinisi, pipeLayer, productCarrier, productionPlatform, referCarrier, researchVessel, roroCarrier, sailboat, sailingShip, salvageOperation, seiner, speedBoat, submarineAttack, submarineBallisticMissile, submarineCruiseMissile, supplyShip, tanker, timberCarrier, trawler, trimaran, tugBoat, viking, yacht, zodiac'.  - `boatType`: Une valeur unique de la liste. Enum : 'cargo, pêche, historique, passagers, spécialiste, pétrolier, guerre, yachting'.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastReported`: Dernière fois que les données ont été recueillies  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `maxDraft`: Tirant d'eau maximal autorisé pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Par exemple, **MTR** représente Mètre  - `maxLength`: Longueur maximale autorisée pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MTR** représente Mètre  - `maxTonnage`: Tonnage maximal autorisé à accéder au port. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Par exemple, **TNE** représente une tonne métrique.  - `maxWidth`: Largeur maximale autorisée pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Par exemple, **MTR** représente Mètre  - `minLength`: Longueur minimale autorisée pour accéder au port. Le code de l'unité (texte) est donné en utilisant les [Codes communs du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Par exemple, **MTR** représente Mètre  - `name`: Le nom de cet élément.  - `openingHoursSpecification`: Une valeur structurée fournissant des informations sur les heures d'ouverture d'un lieu ou d'un certain service à l'intérieur d'un lieu.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refPointOfInterest`: Point d'intérêt auquel l'élément est lié  - `refSeaPort`: Port qui appartient à  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Il doit être BoatAuthorized. Type d'entité NGSI    
Propriétés requises  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `type`    
Méthode pour concevoir votre référentiel de Bateaux Autorisés* Créez un enregistrement pour chaque `Type de bateau` autorisé à circuler dans le port avec tous les `Sous-Type de bateau` correspondants. - record 1 - `id` c'est-à-dire "BoatAuthorized:MNCA-NCE-BA-001-yatching" - "refSeapPortName` c'est-à-dire "MyPort" - `boatType` c'est-à-dire "yatching" - `boatSubType` c'est-à-dire. [ "zodiac", "monoHull", "catamaran", "yacht", "voilier", "jetSki" ] - record 2 - "id" i.e. "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e. "MyPort" - `boatType` i.e. "passenger" - `boatSubType` i.e. [ "cruise", "ferrie" ] - record 3 - "id" i.e. "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e. "MyPort" - `boatType` i.e. "passenger" - `boatSubType` i.e. [ "factoryShip", "seiner", "artisanVessels", "trawler" ]  
Règles concernant la date - section Informations concernant la date et la période d'autorisation* Plusieurs scénarios sont possibles - **Cas 1** Définition d'une plage commençant à une date spécifique et se terminant sans contrainte de date. Permet de définir une autorisation permanente par exemple `dateObserved` c'est-à-dire "2020-01-01T00:00:01Z" `dateObservedFrom` c'est-à-dire "2020-01-01T00:00:01Z" `dateObservedTo` "" - **Case 2** Définition d'une plage commençant à une date spécifique et se terminant à une date précise. Permet de définir une autorisation spécifique par exemple pour un salon nautique ou pour un type de bateau. `dateObserved` i.e. "2020-10-10T00:00:01Z:2020-10-14T23:59:59Z" `dateObservedFrom` i.e. "2020-10-10T00:00:01Z" `dateObservedTo` i.e. "2020-10-14T23:59:59Z"  
Informations supplémentaires sur ce modèle de données* Il peut être utilisé avec le modèle de données suivant. - **SeaPort** pour fournir au port des informations sur les bateaux autorisés dans le port.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BoatAuthorized:    
  description: 'The data model is intended to provide information on the boats authorized to operate within the port according to the ISO 8666 standard for Boat Category. This repository is created by type of category of boat (pleasure craft, trade, passengers, ...). For each type of category, a list of optional subtypes of category can be associated.'    
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
    boatSubType:    
      description: 'Sub Type for a boatType. A combination of the elements. Enum:''aircraftCarrier, amphibiousAssaultShip, anchorHandlingVessel, artisanVessel, bac, barge, bargeCarrier, bulkCarrier, buoyTenderBoat, butaneCarrier, cableLayer, canoe, caravel, cargoCarrier, carrack, catamaran, chemicalCarrier, clipper, coastalFerry, cog, containerCarrier, corvette, craneBarge, crudeCarrier, cruise, cruiser, destroyer, dhow, divingVessel, djong, dredger, drifter, drillRig, factoryShip, ferry, fireBoat, fisheriesResearchVessel, flagshipBoat, floatingProductionStorageUnit, floatingStorageUnit, fluyt, frigate, gabare, galleon, galley, gondola, harbourFerry, helicopterCarrier, highSpeedVessel, houseBoat, hovercraft, iceBreakerShip, jetSki, junk, koch, lifeBoat, lightShip, liner, lineVessel, LiquefiedGasCarrier, littoralCombatShip, livestockCarrier, lngCarrier, longLiner, lpgCarrier, mineSweeping, monoHull, mooringBoat, multipurposeVessel, oceanographicBoat, other, paddleSteamer, pilotBoat, pinisi, pipeLayer, productCarrier, productionPlatform, referCarrier, researchVessel, roroCarrier, sailboat, sailingShip, salvageOperation, seiner, speedBoat, submarineAttack, submarineBallisticMissile, submarineCruiseMissile, supplyShip, tanker, timberCarrier, trawler, trimaran, tugBoat, viking, yacht, zodiac'''    
      items:    
        enum:    
          - aircraftCarrier    
          - amphibiousAssaultShip    
          - anchorHandlingVessel    
          - artisanVessel    
          - bac    
          - barge    
          - bargeCarrier    
          - bulkCarrier    
          - buoyTenderBoat    
          - butaneCarrier    
          - cableLayer    
          - canoe    
          - caravel    
          - cargoCarrier    
          - carrack    
          - catamaran    
          - chemicalCarrier    
          - clipper    
          - coastalFerry    
          - cog    
          - containerCarrier    
          - corvette    
          - craneBarge    
          - crudeCarrier    
          - cruise    
          - cruiser    
          - destroyer    
          - dhow    
          - divingVessel    
          - djong    
          - dredger    
          - drifter    
          - drillRig    
          - factoryShip    
          - ferry    
          - fireBoat    
          - fisheriesResearchVessel    
          - flagshipBoat    
          - floatingProductionStorageUnit    
          - floatingStorageUnit    
          - fluyt    
          - frigate    
          - gabare    
          - galleon    
          - galley    
          - gondola    
          - harbourFerry    
          - helicopterCarrier    
          - highSpeedVessel    
          - houseBoat    
          - hovercraft    
          - iceBreakerShip    
          - jetSki    
          - junk    
          - koch    
          - lifeBoat    
          - lightShip    
          - liner    
          - lineVessel    
          - LiquefiedGasCarrier    
          - littoralCombatShip    
          - livestockCarrier    
          - lngCarrier    
          - longLiner    
          - lpgCarrier    
          - mineSweeping    
          - monoHull    
          - mooringBoat    
          - multipurposeVessel    
          - oceanographicBoat    
          - other    
          - paddleSteamer    
          - pilotBoat    
          - pinisi    
          - pipeLayer    
          - productCarrier    
          - productionPlatform    
          - referCarrier    
          - researchVessel    
          - roroCarrier    
          - sailboat    
          - sailingShip    
          - salvageOperation    
          - seiner    
          - speedBoat    
          - submarineAttack    
          - submarineBallisticMissile    
          - submarineCruiseMissile    
          - supplyShip    
          - tanker    
          - timberCarrier    
          - trawler    
          - trimaran    
          - tugBoat    
          - viking    
          - yacht    
          - zodiac    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    boatType:    
      description: 'A unique value of the list. Enum:''cargo, fishing, historic, passenger, specialist, Tanker, war, yachting'''    
      items:    
        enum:    
          - cargo    
          - fishing    
          - historic    
          - passenger    
          - specialist    
          - Tanker    
          - war    
          - yachting    
        type: string    
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
      description: 'Last time data were gathered'    
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
    id:    
      anyOf: &boatauthorized_-_properties_-_owner_-_items_-_anyof    
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
      description: 'Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/depth    
        units: meters    
    maxLength:    
      description: 'Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: meters    
    maxTonnage:    
      description: 'Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        units: Tons    
    maxWidth:    
      description: 'Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/width    
        units: meters    
    minLength:    
      description: 'Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: https://schema.org/length    
        units: meters    
    name:    
      description: 'The name of this item.'    
      type: Property    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place'    
      items:    
        properties:    
          closes:    
            format: time    
            type: string    
          dayOfWeek:    
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
          opens:    
            format: time    
            type: string    
          validFrom:    
            format: date-time    
            type: string    
          validThrough:    
            format: date-time    
            type: string    
      minItems: 1    
      type: Property    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *boatauthorized_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refPointOfInterest:    
      description: 'Point of Interest that the element has relation to'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    refSeaPort:    
      description: 'Port that belongs to'    
      format: uri    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
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
    type:    
      description: 'It has to be BoatAuthorized. NGSI Entity type'    
      enum:    
        - BoatAuthorized    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - refSeaPort    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### Valeurs-clés NGSI-v2 autorisées par le bateau Exemple  
Voici un exemple de BoatAuthorized au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
  "type": "BoatAuthorized",  
  "name": "Riviera-Port-NCE-BA-001-yatching",  
  "alternateName": "Riviera Port - Autorized Boats in the port",  
  "description": "List of Type and SubType of boats authorized to move and moor in the harbor",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "areaServed": "Nice Port",  
  "dateObserved": "2020-01-01T00:00:01Z",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "refBoatType": "yatching",  
  "refBoatSubType": [  
    "monoHull",  
    "catamaran",  
    "yacht",  
    "sailboat",  
    "jetSki"  
  ],  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "19:30:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "maxTonnage": 3855,  
  "minLength": 3,  
  "maxLength": 35,  
  "maxWidth": 15,  
  "maxDraft": 6.00,  
  "dateLastReported": "2021-12-31T23:59:59",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      23,  
      45  
    ]  
  }  
}  
```  
#### BoatAuthorized NGSI-v2 normalisé Exemple  
Voici un exemple d'un BoatAuthorized au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
	"id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
	"type": "BoatAuthorized",  
	"name": {  
		"type": "Property",  
		"value": "Riviera-Port-NCE-BA-001-yatching"  
	},  
	"alternateName": {  
		"type": "Property",  
		"value": "Riviera Port - Autorized Boats in the port"  
	},  
	"description": {  
		"type": "Property",  
		"value": "List of Type and SubType of boats authorized to move and moor in the harbor"  
	},  
	"seeAlso": {  
		"type": "Property",  
		"value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Port"  
	},  
	"dateObserved": {  
		"type": "Property",  
		"value": "2020-01-01T00:00:01Z"  
	},  
	"refSeaPort": {  
		"type": "Relationship",  
		"object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
	},  
	"refBoatType": {  
		"type": "Property",  
		"value": "yatching"  
	},  
	"refBoatSubType": {  
		"type": "Property",  
		"value": ["monoHull", "catamaran", "yacht", "sailboat", "jetSki"]  
	},  
	"openingHoursSpecification": {  
		"type": "object",  
		"value": [{  
				"dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
				"opens": "07.00",  
				"closes": "20.00"  
			},  
			{  
				"dayOfWeek": "Saturday",  
				"opens": "08.30",  
				"closes": "21.00"  
			},  
			{  
				"dayOfWeek": "Sunday",  
				"opens": "8.30",  
				"closes": "20.00"  
			},  
			{  
				"dayOfWeek": "PublicHolidays",  
				"opens": "8.30",  
				"closes": "19.30"  
			}  
		],  
		"validFrom": "-01-01",  
		"validThrough": "-31-12"  
	},  
	"maxTonnage": {  
		"type": "Property",  
		"value": 3855  
	},  
	"minLength": {  
		"type": "Property",  
		"value": 3  
	},  
	"maxLength": {  
		"type": "Property",  
		"value": 35  
	},  
	"maxWidth": {  
		"type": "Property",  
		"value": 15  
	},  
	"maxDraft": {  
		"type": "Property",  
		"value": 6.00  
	}  
}  
```  
#### Valeurs-clés NGSI-LD autorisées par le bateau Exemple  
Voici un exemple de BoatAuthorized au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque vous utilisez `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
  "type": "BoatAuthorized",  
  "name": {  
    "type": "Property",  
    "value": "Riviera-Port-NCE-BA-001-yatching"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": "Riviera Port - Autorized Boats in the port"  
  },  
  "description": {  
    "type": "Property",  
    "value": "List of Type and SubType of boats authorized to move and moor in the harbor"  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Nice Port"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": "2020-01-01T00:00:01Z"  
  },  
  "refSeaPort": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
  },  
  "refBoatType": {  
    "type": "Property",  
    "value": "yatching"  
  },  
  "refBoatSubType": {  
    "type": "Property",  
    "value": [  
      "monoHull",  
      "catamaran",  
      "yacht",  
      "sailboat",  
      "jetSki"  
    ]  
  },  
  "openingHoursSpecification": {  
    "type": "object",  
    "value": [  
      {  
        "dayOfWeek": "Monday, Tuesday, Wednesday, Thursday, Friday",  
        "opens": "07.00",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "Saturday",  
        "opens": "08.30",  
        "closes": "21.00"  
      },  
      {  
        "dayOfWeek": "Sunday",  
        "opens": "8.30",  
        "closes": "20.00"  
      },  
      {  
        "dayOfWeek": "PublicHolidays",  
        "opens": "8.30",  
        "closes": "19.30"  
      }  
    ],  
    "validFrom": "-01-01",  
    "validThrough": "-31-12"  
  },  
  "maxTonnage": {  
    "type": "Property",  
    "value": 3855  
  },  
  "minLength": {  
    "type": "Property",  
    "value": 3  
  },  
  "maxLength": {  
    "type": "Property",  
    "value": 35  
  },  
  "maxWidth": {  
    "type": "Property",  
    "value": 15  
  },  
  "maxDraft": {  
    "type": "Property",  
    "value": 6.0  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### BoatAuthorized NGSI-LD normalisé Exemple  
Voici un exemple d'un BoatAuthorized au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
  "type": "BoatAuthorized",  
  "name": "Riviera-Port-NCE-BA-001-yatching",  
  "alternateName": "Riviera Port - Autorized Boats in the port",  
  "description": "List of Type and SubType of boats authorized to move and moor in the harbor",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "areaServed": "Nice Port",  
  "dateObserved": "2020-01-01T00:00:01Z",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "refBoatType": "yatching",  
  "refBoatSubType": [  
    "monoHull",  
    "catamaran",  
    "yacht",  
    "sailboat",  
    "jetSki"  
  ],  
  "openingHoursSpecification": [  
    {  
      "dayOfWeek": "Monday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Tuesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Wednesday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Thursday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Friday",  
      "opens": "07:00:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Saturday",  
      "opens": "08:30:00",  
      "closes": "21:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "Sunday",  
      "opens": "08:30:00",  
      "closes": "20:00:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    },  
    {  
      "dayOfWeek": "PublicHolidays",  
      "opens": "08:30:00",  
      "closes": "19:30:00",  
      "validFrom": "2021-01-01T00:00:00",  
      "validThrough": "2021-12-31T23:59:59"  
    }  
  ],  
  "maxTonnage": 3855,  
  "minLength": 3,  
  "maxLength": 35,  
  "maxWidth": 15,  
  "maxDraft": 6.0,  
  "dateLastReported": "2021-12-31T23:59:59",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      23,  
      45  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude