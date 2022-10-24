<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: BarcoAutorizado  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatAuthorized/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El modelo de datos está destinado a proporcionar información sobre las embarcaciones autorizadas a operar dentro del puerto según la norma ISO 8666 de Categoría de embarcaciones. Este repositorio se crea por tipo de categoría de embarcación (de recreo, de comercio, de pasajeros, ...). A cada tipo de categoría se le puede asociar una lista de subtipos opcionales de categoría.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatSubType[array]`: Subtipo para un barcoTipo. Una combinación de los elementos. Enum:'aircraftCarrier, amphibiousAssaultShip, anchorHandlingVessel, artisanVessel, bac, barge, bargeCarrier, bulkCarrier, buoyTenderBoat, butaneCarrier, cableLayer, canoe, caravel, cargoCarrier, carrack, catamaran, chemicalCarrier, clipper, coastalFerry, cog, containerCarrier, corvette, craneBarge, crudeCarrier, crucero, destructor, dhow, buque de buceo, djong, draga, trainera, drillRig, buque-fábrica, transbordador, buque de bomberos, buque de investigación pesquera, buque insignia, unidad de almacenamiento de producción flotante, unidad de almacenamiento flotante, fluyt, fragata, gabarra, galeón, galera, góndola, harbourFerry, helicóptero, buque de alta velocidad, buque vivienda, aerodeslizador, buque rompehielos, moto acuática, chatarra, koch, buque salvavidas, buque ligero, buque de línea, buque de gas licuado, buque de combate litoral, buque ganadero, buque de gas natural licuado, buque de línea, buque de transporte de gas licuado, monocasco, buque de amarre, buque polivalente, buque oceanográfico, otros, buque de remos, buque piloto, pinisi, pipeLayer, productCarrier, productionPlatform, referCarrier, researchVessel, roroCarrier, sailboat, sailingShip, salvageOperation, seiner, speedBoat, submarineAttack, submarineBallisticMissile, submarineCruiseMissile, supplyShip, tanker, timberCarrier, trawler, trimaran, tugBoat, viking, yacht, zodiac".  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatType[array]`: Un valor único de la lista. Enum:'carga, pesca, histórico, pasajeros, especialista, Petrolero, guerra, yate'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateLastReported[string]`: Última vez que se recogieron datos  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxDraft[number]`: Calado máximo permitido para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Meter  . Model: [https://schema.org/depth](https://schema.org/depth)- `maxLength[number]`: Longitud máxima permitida para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Meter  . Model: [https://schema.org/length](https://schema.org/length)- `maxTonnage[number]`: Tonelaje máximo autorizado para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **TNE** representa la tonelada métrica  - `maxWidth[number]`: Anchura máxima permitida para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Meter  . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: Longitud mínima permitida para acceder al puerto. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Meter  . Model: [https://schema.org/length](https://schema.org/length)- `name[string]`: El nombre de este artículo.  - `openingHoursSpecification[array]`: Un valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refPointOfInterest[string]`: Punto de interés con el que el elemento tiene relación  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[string]`: Puerto que pertenece a  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Tiene que ser BoatAuthorized. Tipo de entidad NGSI  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Método para diseñar su repositorio de Barcos Autorizados* Cree un registro para cada `tipo de barco` autorizado a circular por el puerto con todos los `subtipos de barco` correspondientes. - registro 1 - `id` es decir "BoatAuthorized:MNCA-NCE-BA-001-yatching" - "refSeapPortName` es decir "MyPort" - `boatType` es decir "yatching" - `boatSubType` es decir [ "zodiac", "monoHull", "catamarán", "yate", "velero", "jetSki" ] - record 2 - "id" i.e. "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e. "MyPort" - `boatType` i.e. "passenger" - `boatSubType` i.e. [ "cruise", "ferrie" ] - record 3 - "id" i.e. "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.e. "MyPort" - `boatType` i.e. "passenger" - `boatSubType` i.e. [ "factoryShip", "seiner", "artisanVessels", "trawler" ]  
Reglas sobre la fecha - sección Información sobre la fecha y el periodo de la autorización* Hay varios escenarios posibles - **Caso 1** Definición de un rango que comienza en una fecha específica y termina sin vinculación de fecha. Permite definir una autorización permanente para, por ejemplo, "2020-01-01T00:00:01Z" `dateObservedFrom` es decir, "2020-01-01T00:00:01Z" `dateObservedTo` "" - **Caso 2** Definición de un rango que comienza en una fecha específica y termina. Permite definir una autorización específica, por ejemplo, para un salón náutico o para un tipo de barco. `dateObserved` es decir, "2020-10-10T00:00:01Z:2020-10-14T23:59:59Z" `dateObservedFrom` es decir, "2020-10-10T00:00:01Z" `dateObservedTo` es decir, "2020-10-14T23:59Z"  
Información adicional sobre este modelo de datos* Se puede utilizar con el siguiente modelo de datos. - **Puerto marítimo** para proporcionar información al puerto sobre el barco autorizado en el puerto.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          dayOfWeek:    
            anyOf:    
              - description: 'Property. Array of days of the week.'    
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
              - description: 'Property. Array of days of the week.'    
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
            description: 'Property. Model:''http://schema.org/dayOfWeek''. The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays).'    
            type: string    
          opens:    
            format: time    
            pattern: ^(2[0-3]|[01][0-9]):?([0-5][0-9]):?([0-5][0-9])(\.[0-9]*)?(Z|[+-](?:2[0-3]|[01][0-9])(?::?(?:[0-5][0-9]))?)$    
            type: string    
          validFrom:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
          validThrough:    
            anyOf:    
              - description: 'Property. Model:''http://schema.org/Date.'    
                format: date    
                type: string    
              - description: 'Property. Model:''http://schema.org/DateTime.'    
                format: date-time    
                type: string    
            description: 'Property. The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format.'    
            type: string    
        type: object    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
#### BarcoAutorizado NGSI-v2 key-values Ejemplo  
Este es un ejemplo de BoatAuthorized en formato JSON-LD como valores clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
</details>  
#### BarcoAutorizado NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un BoatAuthorized en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
  "refSeaPort": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
  },  
  "refBoatType": {  
    "type": "Text",  
    "value": "yatching"  
  },  
  "refBoatSubType": {  
    "type": "array",  
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
    "value": 6.00  
  }  
}  
```  
</details>  
#### BoatAuthorized NGSI-LD key-values Ejemplo  
Este es un ejemplo de BoatAuthorized en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### BarcoAutorizado NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un BoatAuthorized en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
