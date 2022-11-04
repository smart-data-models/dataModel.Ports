<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: BoatPlacesPricing  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **El objetivo del modelo de datos es proporcionar información sobre el precio de las anillas de amarre por categoría (eslora / Anchura). La información recibida se refiere únicamente a las embarcaciones de recreo y excluye las embarcaciones comerciales y de transporte de pasajeros. La información sobre las categorías de puntos de amarre para embarcaciones se ha tomado de la norma ISO 8666.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateLastReported[string]`: Una marca de tiempo que denota la última vez que el dispositivo comunicó datos con éxito. La fecha y la hora de esta observación en formato ISO8601 UTC  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `fairing[object]`: Precio de la plaza para barcos carenados para esta categoría / período. Un valor estructurado con 3 subpropiedades donde cada elemento es una cadena con el formato `clave` : `precio` en euros  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `maxDraft[number]`: Calado máximo permitido para acceder al punto. El código de la unidad (texto) se indica utilizando los [Códigos comunes del UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLength[number]`: Longitud máxima permitida para acceder al punto. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/number](https://schema.org/number)- `maxWidth[number]`: Anchura máxima permitida para acceder al punto. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: Longitud mínima permitida para acceder al punto. El código de la unidad (texto) se da utilizando los [Códigos comunes UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)  . Model: [https://schema.org/number](https://schema.org/number)- `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `passage[object]`: Precio de la plaza para los barcos de paso para esta categoría / período. Un valor estructurado con 3 subpropiedades donde cada elemento es una cadena con el formato `clave` : `precio` en euros  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `period[string]`: Tipo de periodo que define la fecha Desde y Hasta: Un texto libre o un valor único de las diferentes combinaciones permitidas 'temporada / fuera de temporada' - 'verano / invierno' - 'baja / media / alta'. enum:'alta, baja, media, fuera de temporada, temporada, verano, invierno'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `refPointOfInterest[*]`: Referencia a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) vinculado con el Repositorio  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[*]`: Referencia a la entidad [Seaport](https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md) para utilizarla como enlace principal  . Model: [https://schema.org/URL](https://schema.org/URL)- `resident[object]`: Precio de la plaza para embarcaciones residentes para esta categoría / período. Un valor estructurado con 2 subpropiedades donde cada elemento es una cadena con el formato `clave` : `precio` en euros  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `spotCategoryRange[array]`: Enumerar de la categoría más baja a la más alta: Una combinación de ellas. Enum:'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'  - `type[string]`: Tipo de entidad NGSI. Tiene que ser BoatPlacePricing  - `validFrom[string]`: Fecha y hora de inicio de las normas de tarificación.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validThrough[string]`: Fecha y hora de finalización de las normas de precios.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `wintering[object]`: Precio de la plaza para barcos de invernada para esta categoría / período. Un valor estructurado con 3 subpropiedades donde cada elemento es una cadena con el formato `clave` : `precio` en euros  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`  - `validFrom`  - `validThrough`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Método para diseñar su repositorio de Precios de Barcos* Para describir los diferentes precios por categoría (de la A a la Z17) en la sección *Información sobre precios*, es necesario el uso de una lista al escribir el registro. Dependiendo de la configuración del puerto, se creará un registro por 'spotCategoryRange' para determinar los precios para un periodo como repositorio. Son posibles dos escenarios - Escenario 1. Definición del rango de duración en una sola categoría . 'spotCategoryRange' = [F], Barcos aceptados= longitud 7.00 a 7.49 y anchura máxima =< 2.70. [F] longitud 7,00 a 7,49 / anchura máxima =< 2,70 - Escenario 2. Definición del rango de longitudes con categorías consecutivas. 'spotCategoryRange' = [F, G], Barcos aceptados= longitud 7.00 a 7.99 y anchura máxima =< 2.80.'F' da una longitud máxima de 7.00 a 7.49 y una anchura máxima de 2.70, 'G' da una longitud máxima de 7.50 a 7.99 y una anchura máxima de 2.80  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
      description: 'A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat'    
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
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *boatplacespricing_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository'    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
      description: 'NGSI Entity type. It has to be BoatPlacePricing'    
      enum:    
        - BoatPlacesPricing    
      type: string    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Start date and time of the pricing rules.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    validThrough:    
      description: 'End date and time of the pricing rules.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Ports/BoatPlacePricing/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
Información adicional sobre este modelo de datos* Se puede utilizar con el siguiente modelo de datos. - **PuertoMarino** para proporcionar información al puerto sobre las embarcaciones autorizadas en el mismo.  
Este Modelo de Datos es complementario al Modelo de Datos **Lugares de BarcosDisponibles**.  
Repositorio de datos (norma ISO 8666)** *Categoría Longitud Anchura Máxima* A 4,99 2,00 B 5,49 2,15 C 5,99 2,30 D 6,49 2,45 E 6,99 2,60 F 7,49 2,80 G 7,99 2,80 H 8,49 2,95 I 8.99 3,10 J 9,49 3,25 K 9,99 3,40 L 10,49 3,55 M 10,99 3,70 N 11,49 3,85 O 11,99 4,00 P 12,99 4,30 Q 13,99 4,60 R 15,99 4,90 S 17,99 5,20 T1 20,99 5,60 T2 23,99 6.00 U 28.99 7.00 V 33.99 8.00 W 38.99 9.00 X 43.99 10.00 Y 48.99 11.00 Z 53.99 12.00 Z01 58.99 13.00 Z02 64.99 14.00 Z03 71.99 15.00 Z04 78.99 16.00 Z05 85.99 17.00 Z06 92.99 18.00 Z07 99.99 19.00 Z08 106.99 20.00 Z09 113.99 21.00 Z10 120.99 22.00 Z11 127.99 23.00 Z12 134.99 24.00 Z13 142.99 25.00 Z14 150.99 26.00 Z15 158.99 27.00 Z16 166.99 28.00 Z17 174.99 29.00  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### BoatPlacesPricing NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de BoatPlacesPricing en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
</details>  
#### BoatPlacesPricing NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de BoatPlacesPricing en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### BoatPlacesPricing NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de BoatPlacesPricing en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
        "type": "DateTime",  
        "value": "2020-03-17T08:45:00Z"  
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
        "type": "property",  
        "value": [  
            "F",  
            "G"  
        ]  
    },  
    "validFrom": {  
        "type": "DateTime",  
        "value": "2021-01-01T17:21:20Z"  
    },  
    "validThrough": {  
        "type": "DateTime",  
        "value": "2021-02-10T17:21:20Z"  
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
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### Precios de los lugares de embarque Ejemplo normalizado de NGSI-LD  
Este es un ejemplo de BoatPlacesPricing en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BoatPlacePricing:BoatPlacePricing:MNCA-BPP-Range-FG",  
    "type": "BoatPlacePricing",  
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
