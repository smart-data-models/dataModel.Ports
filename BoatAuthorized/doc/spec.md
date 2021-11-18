Entity: BoatAuthorized  
======================  
[Open License](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatAuthorized/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **The data model is intended to provide information on the boats authorized to operate within the port according to the ISO 8666 standard for Boat Category. This repository is created by type of category of boat (pleasure craft, trade, passengers, ...). For each type of category, a list of optional subtypes of category can be associated.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `boatSubType`: Sub Type for a boatType. A combination of the elements. Enum:'aircraftCarrier, amphibiousAssaultShip, anchorHandlingVessel, artisanVessel, bac, barge, bargeCarrier, bulkCarrier, buoyTenderBoat, butaneCarrier, cableLayer, canoe, caravel, cargoCarrier, carrack, catamaran, chemicalCarrier, clipper, coastalFerry, cog, containerCarrier, corvette, craneBarge, crudeCarrier, cruise, cruiser, destroyer, dhow, divingVessel, djong, dredger, drifter, drillRig, factoryShip, ferry, fireBoat, fisheriesResearchVessel, flagshipBoat, floatingProductionStorageUnit, floatingStorageUnit, fluyt, frigate, gabare, galleon, galley, gondola, harbourFerry, helicopterCarrier, highSpeedVessel, houseBoat, hovercraft, iceBreakerShip, jetSki, junk, koch, lifeBoat, lightShip, liner, lineVessel, LiquefiedGasCarrier, littoralCombatShip, livestockCarrier, lngCarrier, longLiner, lpgCarrier, mineSweeping, monoHull, mooringBoat, multipurposeVessel, oceanographicBoat, other, paddleSteamer, pilotBoat, pinisi, pipeLayer, productCarrier, productionPlatform, referCarrier, researchVessel, roroCarrier, sailboat, sailingShip, salvageOperation, seiner, speedBoat, submarineAttack, submarineBallisticMissile, submarineCruiseMissile, supplyShip, tanker, timberCarrier, trawler, trimaran, tugBoat, viking, yacht, zodiac'  - `boatType`: A unique value of the list. Enum:'cargo, fishing, historic, passenger, specialist, Tanker, war, yachting'  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateLastReported`: Last time data were gathered  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `id`: Unique identifier of the entity  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxDraft`: Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter  - `maxLength`: Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter  - `maxTonnage`: Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric  - `maxWidth`: Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter  - `minLength`: Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter  - `name`: The name of this item.  - `openingHoursSpecification`: A structured value providing information about the opening hours of a place or a certain service inside a place  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `refPointOfInterest`: Point of Interest that the element has relation to  - `refSeaPort`: Port that belongs to  - `seeAlso`: list of uri pointing to additional resources about the item  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `type`: It has to be BoatAuthorized. NGSI Entity type    
Required properties  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `type`    
Method to design your repository of Boat Authorized* Create a record for each `boatType` authorized to circulate in the harbor with all corresponding `BoatSubType`. - record 1 - `id` i.e.  "BoatAuthorized:MNCA-NCE-BA-001-yatching" - "refSeapPortName` i.e. "MyPort" - `boatType` i.e. "yatching" - `boatSubType` i.e. [ "zodiac", "monoHull", "catamaran", "yacht", "sailboat", "jetSki" ] - record 2 - "id" i.e.  "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e.  "MyPort" - `boatType` i.e.  "passenger" - `boatSubType` i.e.  [ "cruise", "ferrie" ] - record 3 - "id" i.e.  "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e.  "MyPort" - `boatType` i.e.  "passenger" - `boatSubType` i.e.  [ "factoryShip", "seiner","artisanVessels","trawler" ]  
Rules about the date - section Information about the date and period of authorization* There are several scenarios possibles - **Case 1** Definition of a range starting on a specific date and ending without date binding. Allows to define a permanent authorization for example `dateObserved` i.e.  "2020-01-01T00:00:01Z" `dateObservedFrom` i.e. "2020-01-01T00:00:01Z" `dateObservedTo` "" - **Case 2** Definition of a range starting on a specific date and ending date. Allows to define a specific authorization for example for a boatshow or for a type of boat. `dateObserved` i.e.  "2020-10-10T00:00:01Z:2020-10-14T23:59:59Z" `dateObservedFrom` i.e. "2020-10-10T00:00:01Z" `dateObservedTo` i.e. "2020-10-14T23:59:59Z"  
Additional Information about this Data Model* It can be used with the following data Model. - **SeaPort** to provide information to the port about authorized Boat in the port.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateLastReported:    
      description: 'Last time data were gathered'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
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
      x-ngsi:    
        type: Geoproperty    
    maxDraft:    
      description: 'Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
        units: meters    
    maxLength:    
      description: 'Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: meters    
    maxTonnage:    
      description: 'Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric'    
      minimum: 0    
      type: number    
      x-ngsi:    
        type: Property    
        units: Tons    
    maxWidth:    
      description: 'Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
        units: meters    
    minLength:    
      description: 'Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: meters    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/openingHoursSpecification    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *boatauthorized_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refPointOfInterest:    
      description: 'Point of Interest that the element has relation to'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    refSeaPort:    
      description: 'Port that belongs to'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be BoatAuthorized. NGSI Entity type'    
      enum:    
        - BoatAuthorized    
      type: string    
      x-ngsi:    
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
## Example payloads    
#### BoatAuthorized NGSI-v2 key-values Example    
Here is an example of a BoatAuthorized in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BoatAuthorized NGSI-v2 normalized Example    
Here is an example of a BoatAuthorized in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### BoatAuthorized NGSI-LD key-values Example    
Here is an example of a BoatAuthorized in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BoatAuthorized NGSI-LD normalized Example    
Here is an example of a BoatAuthorized in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
