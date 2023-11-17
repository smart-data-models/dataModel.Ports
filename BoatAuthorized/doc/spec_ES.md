<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: BarcoAutorizado    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatAuthorized/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **El modelo de datos está destinado a proporcionar información sobre las embarcaciones autorizadas a operar dentro del puerto según la norma ISO 8666 de Categoría de Embarcación. Este repositorio se crea por tipo de categoría de embarcación (embarcación de recreo, comercio, pasajeros, ...). Para cada tipo de categoría, se puede asociar una lista de subtipos de categoría opcionales.**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatSubType[array]`: Subtipo para un boatType. Una combinación de los elementos. Enum:aircraftCarrier, amphibiousAssaultShip, anchorHandlingVessel, artisanVessel, bac, barge, bargeCarrier, bulkCarrier, buoyTenderBoat, butaneCarrier, cableLayer, canoe, caravel, cargoCarrier, carrack, catamaran, chemicalCarrier, clipper, coastalFerry, cog, containerCarrier, corvette, craneBarge, crudeCarrier, crucero, crucero, destructor, dhow, buque de inmersión, djong, draga, trainera, drillRig, buque factoría, transbordador, fireBoat, buque de investigación pesquera, buque insignia, floatingProductionStorageUnit, floatingStorageUnit, fluyt, fragata, gabare, galeón, galera, góndola, harbourFerry, helicopterCarrier, highSpeedVessel, casaBarco, aerodeslizador, buque rompehielos, jetSki, chatarra, koch, lifeBoat, lightShip, liner, lineVessel, LiquefiedGasCarrier, littoralCombatShip, livestockCarrier, lngCarrier, longLiner, lpgCarrier, mineSweeping, monoHull, mooringBoat, multipurposeVessel, oceanographicBoat, other, paddleSteamer, pilotBoat, pinisi, pipeLayer, productCarrier, productionPlatform, referCarrier, researchVessel, roroCarrier, sailboat, sailingShip, salvageOperation, seiner, speedBoat, submarineAttack, submarineBallisticMissile, submarineCruiseMissile, supplyShip, tanker, timberCarrier, trawler, trimaran, tugBoat, viking, yacht, zodiac'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatType[array]`: Valor único de la lista. Enum:'cargo, fishing, historic, passenger, specialist, Tanker, war, yachting'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateLastReported[date-time]`: Última vez que se recogieron datos  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `maxDraft[number]`: Calado máximo permitido para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Metro  . Model: [https://schema.org/depth](https://schema.org/depth)- `maxLength[number]`: Longitud máxima permitida para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Metro  . Model: [https://schema.org/length](https://schema.org/length)- `maxTonnage[number]`: Tonelaje máximo autorizado para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **TNE** representa Tonelada Métrica  - `maxWidth[number]`: Anchura máxima permitida para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Metro  . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: Longitud mínima permitida para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Metro  . Model: [https://schema.org/length](https://schema.org/length)- `name[string]`: El nombre de este artículo  - `openingHoursSpecification[array]`: Valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `refPointOfInterest[uri]`: Punto de interés con el que el elemento tiene relación  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[uri]`: Puerto que pertenece a  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tiene que ser BoatAuthorized. Tipo de entidad NGSI  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Método para diseñar su repositorio de Barcos Autorizados* Cree un registro para cada `Tipo de Barco` autorizado a circular por el puerto con todos los `SubTipos de Barco` correspondientes. - record 1 - `id` i.e. "BoatAuthorized:MNCA-NCE-BA-001-yatching" - "refSeapPortName` i.e. "MyPort" - `boatType` i.e. "yatching" - `boatSubType` i.e. [ "zodiac", "monoHull", "catamaran", "yacht", "sailboat", "jetSki" ] - record 2 - "id" i.e. "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e. "MyPort" - `boatType` i.e. "passenger" - `boatSubType` i.e. [ "cruise", "ferrie" ] - record 3 - "id" i.e. "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e. "MyPort" - `boatType` i.e. "passenger" - `boatSubType` i.e. [ "factoryShip", "seiner", "artisanVessels", "trawler" ]    
Reglas sobre la fecha - sección Información sobre la fecha y el periodo de autorización* Existen varios escenarios posibles - **Caso 1** Definición de un rango que comienza en una fecha específica y termina sin fecha vinculante. Permite definir una autorización permanente, por ejemplo `dateObserved` es decir, "2020-01-01T00:00:01Z" `dateObservedFrom` es decir, "2020-01-01T00:00:01Z" `dateObservedTo` "" - **Caso 2** Definición de un intervalo que comienza en una fecha específica y termina en otra. Permite definir una autorización específica por ejemplo para un salón náutico o para un tipo de barco. `dateObserved` es decir, "2020-10-10T00:00:01Z:2020-10-14T23:59:59Z" `dateObservedFrom` es decir, "2020-10-10T00:00:01Z" `dateObservedTo` es decir, "2020-10-14T23:59:59Z".    
Información adicional sobre este modelo de datos* Puede utilizarse con el siguiente modelo de datos. - **SeaPort** para proporcionar información al puerto sobre Barco autorizado en el puerto.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
BoatAuthorized:      
  description: 'The data model is intended to provide information on the boats authorized to operate within the port according to the ISO 8666 standard for Boat Category. This repository is created by type of category of boat (pleasure craft, trade, passengers, ...). For each type of category, a list of optional subtypes of category can be associated.'      
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
      description: Last time data were gathered      
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
      description: The name of this item      
      type: string      
      x-ngsi:      
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
    refPointOfInterest:      
      description: Point of Interest that the element has relation to      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
    refSeaPort:      
      description: Port that belongs to      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Relationship      
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
    type:      
      description: It has to be BoatAuthorized. NGSI Entity type      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/BoatAuthorized/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Ports/BoatAuthorized/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### BoatAuthorized NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de BoatAuthorized en formato JSON-LD como valores clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
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
  }  
}  
```  
</details>    
#### BoatAuthorized NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de BoatAuthorized en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
  "type": "BoatAuthorized",  
  "name": {  
    "type": "Text",  
    "value": "Riviera-Port-NCE-BA-001-yatching"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Riviera Port - Autorized Boats in the port"  
  },  
  "description": {  
    "type": "Text",  
    "value": "List of Type and SubType of boats authorized to move and moor in the harbor"  
  },  
  "seeAlso": {  
    "type": "Text",  
    "value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Port"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
    "value": "2020-01-01T00:00:01Z"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2021-12-31T23:59:59"  
  },  
  "refSeaPort": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
  },  
  "refBoatType": {  
    "type": "Text",  
    "value": "yatching"  
  },  
  "refBoatSubType": {  
    "type": "StructuredValue",  
    "value": [  
      "monoHull",  
      "catamaran",  
      "yacht",  
      "sailboat",  
      "jetSki"  
    ]  
  },  
  "openingHoursSpecification": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "closes": "20:00:00",  
        "dayOfWeek": "Monday",  
        "opens": "07:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "20:00:00",  
        "dayOfWeek": "Tuesday",  
        "opens": "07:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "20:00:00",  
        "dayOfWeek": "Wednesday",  
        "opens": "07:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "20:00:00",  
        "dayOfWeek": "Thursday",  
        "opens": "07:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "20:00:00",  
        "dayOfWeek": "Friday",  
        "opens": "07:00:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "21:00:00",  
        "dayOfWeek": "Saturday",  
        "opens": "08:30:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "20:00:00",  
        "dayOfWeek": "Sunday",  
        "opens": "08:30:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      },  
      {  
        "closes": "19:30:00",  
        "dayOfWeek": "PublicHolidays",  
        "opens": "08:30:00",  
        "validFrom": "2021-01-01T00:00:00",  
        "validThrough": "2021-12-31T23:59:59"  
      }  
    ]  
  },  
  "maxTonnage": {  
    "type": "Number",  
    "value": 3855  
  },  
  "minLength": {  
    "type": "Number",  
    "value": 3  
  },  
  "maxLength": {  
    "type": "Number",  
    "value": 35  
  },  
  "maxWidth": {  
    "type": "Number",  
    "value": 15  
  },  
  "maxDraft": {  
    "type": "Number",  
    "value": 6.0  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        23,  
        45  
      ],  
      "type": "Point"  
    }  
  }  
}  
```  
</details>    
#### BoatAuthorized NGSI-LD key-values Ejemplo    
He aquí un ejemplo de BoatAuthorized en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
  "type": "BoatAuthorized",  
  "alternateName": "Riviera Port - Autorized Boats in the port",  
  "areaServed": "Nice Port",  
  "dateLastReported": "2021-12-31T23:59:59",  
  "dateObserved": "2020-01-01T00:00:01Z",  
  "description": "List of Type and SubType of boats authorized to move and moor in the harbor",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      23,  
      45  
    ]  
  },  
  "maxDraft": 6.0,  
  "maxLength": 35,  
  "maxTonnage": 3855,  
  "maxWidth": 15,  
  "minLength": 3,  
  "name": "Riviera-Port-NCE-BA-001-yatching",  
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
  "refBoatSubType": [  
    "monoHull",  
    "catamaran",  
    "yacht",  
    "sailboat",  
    "jetSki"  
  ],  
  "refBoatType": "yatching",  
  "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### BarcoAutorizado NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de BoatAuthorized en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:BoatAuthorized:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
    "type": "BoatAuthorized",  
    "alternateName": {  
        "type": "Property",  
        "value": "Riviera Port - Autorized Boats in the port"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Port"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": "2020-01-01T00:00:01Z"  
    },  
    "description": {  
        "type": "Property",  
        "value": "List of Type and SubType of boats authorized to move and moor in the harbor"  
    },  
    "maxDraft": {  
        "type": "Property",  
        "value": 6.0  
    },  
    "maxLength": {  
        "type": "Property",  
        "value": 35  
    },  
    "maxTonnage": {  
        "type": "Property",  
        "value": 3855  
    },  
    "maxWidth": {  
        "type": "Property",  
        "value": 15  
    },  
    "minLength": {  
        "type": "Property",  
        "value": 3  
    },  
    "name": {  
        "type": "Property",  
        "value": "Riviera-Port-NCE-BA-001-yatching"  
    },  
    "openingHoursSpecification": {  
        "type": "object",  
        "value": [  
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
        ]  
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
    "refBoatType": {  
        "type": "Property",  
        "value": "yatching"  
    },  
    "refSeaPort": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
