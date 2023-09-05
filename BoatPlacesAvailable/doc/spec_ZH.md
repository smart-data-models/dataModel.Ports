<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：可用船位  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatPlacesAvailable/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**该数据模型的目的是按类别提供港口内船只可用系泊环的信息。所收到的信息仅涉及游艇，不包括商业和客运船只。有关船只 Spot 类别的信息来自 ISO 8666 标准。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableSpotNumber[number]`: 港口为该类别提供的职位数  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `dateObserved[date-time]`: 以 ISO8601 UTC 格式表示的观测日期和时间。可以用一个特定的时间瞬间或一个 ISO8601 时间间隔来表示  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `maxDraft[number]`: 允许进入港口的最大吃水。单位代码（文本）使用 [UN/CEFACT 通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)。例如，**MTR** 代表米  . Model: [https://schema.org/depth](https://schema.org/depth)- `maxLength[number]`: 允许进入港口的最大长度。单位代码（文本）使用 [UN/CEFACT 通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)。例如，**MTR** 表示米（Meter）。  . Model: [https://schema.org/length](https://schema.org/length)- `maxWidth[number]`: 允许进入港口的最大宽度。单位代码（文本）使用 [UN/CEFACT 通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)。例如，**MTR** 代表米  . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: 允许进入港口的最小长度。单位代码（文本）使用 [UN/CEFACT 通用代码](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)。例如，**MTR** 表示米（Meter）。  . Model: [https://schema.org/length](https://schema.org/length)- `name[string]`: 该项目的名称  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `refPointOfInterest[string]`: 元素与之相关的兴趣点  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[string]`: 属于  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `spotCategoryRange[array]`: 从低到高排列：所列项目的组合。枚举:'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T1, T2, U, V, W, X, Y, Z, Z01, Z02, Z03, Z04, Z05, Z06, Z07, Z08, Z08, Z09, Z10, Z11, Z12, Z13, Z14, Z15, Z16, Z17'  . Model: [https://schema.org/Text](https://schema.org/Text)- `totalCapacitySpotNumber[number]`: 此范围内端口的点位总容量  . Model: [https://schema.org/Number](https://schema.org/Number)- `type[string]`: NGSI 实体类型。必须是 BoatPlacesAvailable  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `availableSpotNumber`  - `dateObserved`  - `id`  - `location`  - `refSeaPort`  - `spotCategoryRange`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
设计您的艇库的方法 授权 为了在可用位置信息部分按类别（A 至 Z17）描述不同的可用位置，在编写记录时必须使用列表。根据端口配置，`spotCategoryRange` 将创建一条记录，以确定在给定时间内剩余的位置数。可能会出现两种情况 情况 1.定义单个类别的长度范围。`spotCategoryRange` = ["F"], 接受船只。长度为 7.00 至 7.49，最大宽度 =< 2.70。"F" 长度 7.00 至 7.49 / 最大宽度 =< 2.70 情景 2.定义具有连续类别的长度范围。`spotCategoryRange` = ["F", "G"], 接受船只。长度为 7.00 至 7.99，最大宽度 =< 2.80。F "表示最大长度为 7.00 到 7.49，最大宽度为 2.70。"G "表示最大长度为 7.50 到 7.99，最大宽度为 2.80。  
关于此数据模型的其他信息 可与以下数据模型一起使用。- SeaPort 向港口提供有关港口内授权船只的信息。  
该数据模型是数据模型 BoatPlacesPricing 的补充。  
数据存储库（ISO 8666 标准） 分类 长度 最大 宽度 最大 A 4.99 2.00 B 5.49 2.15 C 5.99 2.30 D 6.49 2.45 E 6.99 2.60 F 7.49 2.80 G 7.99 2.80 H 8.49 2.95 I 8.99 3.10 J 9.49 3.25 K 9.99 3.40 L 10.49 3.55 M 10.99 3.70 N 11.49 3.85 O 11.99 4.00 P 12.99 4.30 Q 13.99 4.60 R 15.99 4.90 S 17.99 5.20 T1 20.99 5.60 T2 23.99 6.00 u 28.99 7.00 v 33.99 8.00 w 38.99 9.00 x 43.99 10.00 y 48.99 11.00 z 53.99 12.00 z01 58.99 13.00 z02 64.99 14.00 z03 71.99 15.00 z04 78.99 16.00 z05 85.99 17.00 z06 92.99 18.00 Z07 99.99 19.00 Z08 106.99 20.00 Z09 113.99 21.00 Z10 120.99 22.00 Z11 127.99 23.00 Z12 134.99 24.00 Z13 142.99 25.00 Z14 150.99 26.00 Z15 158.99 27.00 Z16 166.99 28.00 Z17 174.99 29.00  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BoatPlacesAvailable:    
  description: The purpose of the data model is to provide information on the availability of mooring rings for boats in the port by category. The information received relates only to pleasure boats and excludes commercial and passenger transport boats. The information on the Spot categories for boats is taken from the ISO 8666 standard.    
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
    availableSpotNumber:    
      description: Number of places available in the port for this category    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: The date and time of this observation in ISO8601 UTC format. It can be represented by a specific time instant or by an ISO8601 interval    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
        units: meters    
    maxLength:    
      description: 'Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/length    
        type: Property    
        units: meters    
    maxWidth:    
      description: 'Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      type: number    
      x-ngsi:    
        model: https://schema.org/width    
        type: Property    
        units: meters    
    minLength:    
      description: 'Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
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
      description: Point of Interest that the element has relation to    
      type: string    
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
      description: Port that belongs to    
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
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    totalCapacitySpotNumber:    
      description: Total Capacity of Spot in the port for this range    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be BoatPlacesAvailable    
      enum:    
        - BoatPlacesAvailable    
      type: string    
      x-ngsi:    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/BoatPlacesAvailable/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Ports/BoatPlaceAvailable/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### BoatPlacesAvailable NGSI-v2 键值示例  
下面是一个以 JSON-LD 格式作为键值的 BoatPlacesAvailable 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### BoatPlacesAvailable NGSI-v2 标准化示例  
下面是一个以 JSON-LD 格式规范化的 BoatPlacesAvailable 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### BoatPlacesAvailable NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 BoatPlacesAvailable 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BoatPlaceAvailable:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
    "type": "BoatPlaceAvailable",  
    "alternateName": {  
        "type": "Property",  
        "value": "Riviera Port - Available places"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Riviera Port"  
    },  
    "availableSpotNumber": {  
        "type": "Property",  
        "value": 3  
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
    "description": {  
        "type": "Property",  
        "value": "Availability places"  
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
    "refSeaPort": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001"  
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
    "totalCapacitySpotNumber": {  
        "type": "Property",  
        "value": 10  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### BoatPlacesAvailable NGSI-LD 归一化示例  
下面是一个以 JSON-LD 格式规范化的 BoatPlacesAvailable 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:BoatPlaceAvailable:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
    "type": "BoatPlaceAvailable",  
    "alternateName": "Riviera Port - Available places",  
    "areaServed": "Riviera Port",  
    "dateObserved": "2020-03-17T08:45:00Z",  
    "description": "Availability places",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            123,  
            45  
        ]  
    },  
    "maxDraft": 2.55,  
    "maxLength": 7.99,  
    "maxWidth": 2.8,  
    "minLength": 7,  
    "name": "Riviera-Port-NCE-SPAP-BPA-Range-FG",  
    "refSeaPort": "urn:ngsi-ld:SeaPort:Riviera-Port-NCE-SP-001",  
    "seeAlso": "https://ccinicecotedazur/docs/tarifs-plaisance-yachting-ports-passage-2019",  
    "spotCategoryRange": [  
        "F",  
        "G"  
    ],  
    "totalCapacitySpotNumber": 10,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
