<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: BoatPlacesPricing  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesPricing/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **The purpose of the data model is to provide information on the pricing of mooring rings by category (length / Width). The information received relates only to pleasure boats and excludes commercial and passenger transport boats. The information on the Spot categories for boats is taken from the ISO 8666 standard.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateLastReported[date-time]`: A timestamp which denotes the last time when the device successfully reported data. The date and time of this observation in ISO8601 UTCformat  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `fairing[object]`: Ticket price of the place for fairing boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `day`:     
	- `month`:     
- `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maxDraft[number]`: Maximum draft allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)   . Model: [https://schema.org/Number](https://schema.org/Number)- `maxLength[number]`: Maximum length allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)   . Model: [https://schema.org/number](https://schema.org/number)- `maxWidth[number]`: Maximum width allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)   . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: Minimum length allowed to access the spot. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)   . Model: [https://schema.org/number](https://schema.org/number)- `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `passage[object]`: Ticket price of the place for passing boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `day`:     
	- `month`:     
- `period[string]`: Type of period defined the date From and Through: A free text or a unique value of the different combination allowed 'season / offSeason' - 'summer / winter' - 'low / medium / high'. enum:'high, low, medium, offSeason, season, summer, winter'  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `refPointOfInterest[*]`: Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[*]`: Reference to the entity [Seaport](https://github.com/smart-data-models/dataModel.Port/blob/master/Seaport/doc/spec.md) to use as main link  . Model: [https://schema.org/URL](https://schema.org/URL)- `resident[object]`: Ticket price of the place for resident boats for this category / period. A structured value with 2 subproperties where each items is a string in the format `key` : `price` in Euro €  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `annual`:     
- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `spotCategoryRange[array]`: List from the lowest to the highest categories: A combination of them. Enum:'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'  - `type[string]`: NGSI Entity type. It has to be BoatPlacePricing  - `validFrom[date-time]`: Start date and time of the pricing rules  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `validThrough[date-time]`: End date and time of the pricing rules  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `wintering[object]`: Ticket price of the place for wintering boats for this category / period. A structured value with 3 subproperties where each items is a string in the format `key` : `price` in Euro €  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)	- `day`:     
	- `month`:     
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`  - `validFrom`  - `validThrough`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Method to design your repository of Boat Pricing* To describe the different pricing by category (A to Z17) in the section *Information about pricing*, the use of a list is necessary when writing the record. Depending on the port configuration, a record will be created by 'spotCategoryRange' to determine the pricing for a period as repository. Two scenarios are possible - Scenario 1. Definition of the length range on a single category . 'spotCategoryRange' = [F], Boats accepted= length 7.00 to 7.49 and max width =< 2.70. [F]  length 7.00 to 7.49 / max width =< 2.70 - Scenario 2. Definition of the length range with consecutive categories. 'spotCategoryRange' = [F, G], Boats accepted= length 7.00 to 7.99 and max width =< 2.80.'F' gives maxLength from 7.00 to 7.49 and maxWidth 2.70,  'G' gives maxLength from 7.50 to 7.99 and maxWidth 2.80  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
Additional Information about this Data Model* It can be used with the following data Model. - **SeaPort** to provide information to the port about authorized Boat in the port.  
This Data Model is complementary to the Data Model **BoatPlacesAvailable**.  
Data repository (ISO 8666 standard)** *Categorie Length Max  Width Max* A    4.99   2.00 B    5.49   2.15 C    5.99   2.30 D    6.49   2.45 E    6.99   2.60 F    7.49   2.80 G    7.99   2.80 H    8.49   2.95 I    8.99   3.10 J    9.49   3.25 K    9.99   3.40 L   10.49   3.55 M   10.99   3.70 N   11.49   3.85 O   11.99   4.00 P   12.99   4.30 Q   13.99   4.60 R   15.99   4.90 S   17.99   5.20 T1   20.99   5.60 T2   23.99   6.00 U   28.99   7.00 V   33.99   8.00 W   38.99   9.00 X   43.99  10.00 Y   48.99  11.00 Z   53.99  12.00 Z01   58.99  13.00 Z02   64.99  14.00 Z03   71.99  15.00 Z04   78.99  16.00 Z05   85.99  17.00 Z06   92.99  18.00 Z07   99.99  19.00 Z08  106.99  20.00 Z09  113.99  21.00 Z10  120.99  22.00 Z11  127.99  23.00 Z12  134.99  24.00 Z13  142.99  25.00 Z14  150.99  26.00 Z15  158.99  27.00 Z16  166.99  28.00 Z17  174.99  29.00  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### BoatPlacesPricing NGSI-v2 key-values Example    
Here is an example of a BoatPlacesPricing in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### BoatPlacesPricing NGSI-v2 normalized Example    
Here is an example of a BoatPlacesPricing in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### BoatPlacesPricing NGSI-LD key-values Example    
Here is an example of a BoatPlacesPricing in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### BoatPlacesPricing NGSI-LD normalized Example    
Here is an example of a BoatPlacesPricing in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
