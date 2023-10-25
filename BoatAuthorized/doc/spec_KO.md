<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: BoatAuthorized  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Ports/blob/master/BoatAuthorized/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 데이터 모델은 선박 범주에 대한 ISO 8666 표준에 따라 항만 내에서 운항이 허가된 선박에 대한 정보를 제공하기 위한 것입니다. 이 저장소는 보트 범주 유형(유람선, 무역, 여객선 등)별로 생성됩니다. 각 범주 유형에 대해 선택적 범주 하위 유형 목록을 연결할 수 있습니다.**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatSubType[array]`: 보트 유형에 대한 하위 유형입니다. 요소의 조합입니다. Enum:'항공기항모, 수륙양용돌격함, 닻취급선, 장인선, 바크, 바지선, 바지선, 벌크선, 부이텐더선, 부탄선, 케이블선, 카누, 카페리, 화물선, 카라반, 쌍동선, 케미칼선, 클리퍼, 해안 페리, 톱니바퀴, 컨테이너선, 코르벳, 크레인바지선, 원유운반선, 크루즈, 순양함, 구축함, 다우, 다이빙선박, 종, 준설선, 표류선, 드릴리그, 공장선박, 페리, 소방선, 어업연구선, 기함선, 부유식생산저장장치, 부유식저장장치, 플루이트, 프리깃, 가바레, 갤리온, 갤리선, 곤돌라, 항구페리선, 헬리콥터선박, 고속선, 하우스보트, 호버크래프트, 쇄빙선, 제트스키, 정크, 코흐, 라이프보트, 라이트선, 라이너, 라인선, 액화가스선, 연안전투선, 가축선, LNG선, 롱라이너, LPG선, 광산청소, 모노선체, 계류선, 다목적선, 해양선, 기타, 패들스티머, 조종선, 피니시선, 파이프, 제품캐리어, 생산플랫폼, 참조캐리어, 연구선박, 로로캐리어, 범선, 항해선박, 인양작업, 선망선, 속도선박, 잠수함공격, 잠수함탄도미사일, 잠수함순항미사일, 공급선박, 유조선, 목재캐리어, 트롤선, 트라이마란, 예인선, 바이킹, 요트, 조디악'  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatType[array]`: 목록의 고유 값입니다. Enum:'화물, 낚시, 역사, 여객, 전문가, 유조선, 전쟁, 요트'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateLastReported[date-time]`: 마지막으로 데이터를 수집한 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `maxDraft[number]`: 항구에 접근하는 데 허용되는 최대 흘수입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [https://schema.org/depth](https://schema.org/depth)- `maxLength[number]`: 항구에 접근할 수 있는 최대 길이입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [https://schema.org/length](https://schema.org/length)- `maxTonnage[number]`: 항구에 접근할 수 있는 최대 톤수입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **TNE**는 톤 미터법을 나타냅니다.  - `maxWidth[number]`: 항구에 접근할 수 있는 최대 폭입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [https://schema.org/width](https://schema.org/width)- `minLength[number]`: 항구에 접근할 수 있는 최소 길이입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [https://schema.org/length](https://schema.org/length)- `name[string]`: 이 항목의 이름  - `openingHoursSpecification[array]`: 장소의 영업 시간 또는 장소 내 특정 서비스에 대한 정보를 제공하는 구조화된 값입니다.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refPointOfInterest[uri]`: 요소와 관련된 관심 지점  . Model: [https://schema.org/URL](https://schema.org/URL)- `refSeaPort[uri]`: 속한 포트  . Model: [https://schema.org/URL](https://schema.org/URL)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: BoatAuthorized여야 합니다. NGSI 엔티티 유형  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `dateLastReported`  - `id`  - `location`  - `refSeaPort`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
승인된 보트 저장소를 설계하는 방법* 항만에서 순환하도록 승인된 각 `boatType`에 해당하는 모든 `BoatSubType`에 대한 레코드를 생성합니다. - 레코드 1 - `id`, 예: "BoatAuthorized:MNCA-NCE-BA-001-yatching" - "refSeapPortName`, 예: "MyPort" - `boatType`, 예: "yatching" - `boatSubType`, 예:. [ "조디악", "모노헐", "쌍동선", "요트", "범선", "제트스키" ] - 레코드 2 - "id" 즉, "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.예. "MyPort" - `boatType` 즉, "승객" - `boatSubType` 즉, [ "크루즈", "페리" ] - 레코드 3 - "id" 즉, "BoatAuthorized:MNCA-NCE-BA-001-passenger" - `refSeapPortName` i.예. "MyPort" - `boatType` 예. "passenger" - `boatSubType` 예. [ "factoryShip", "seiner","artisanVessels","트롤어선" ]와 같이.  
날짜에 대한 규칙 - 섹션 승인 날짜 및 기간에 대한 정보* 가능한 몇 가지 시나리오가 있습니다 - **사례 1** 특정 날짜에 시작하여 날짜 구속 없이 끝나는 범위 정의. 영구 권한 부여를 정의할 수 있습니다(예: "2020-01-01T00:00:01Z" "2020-01-01T00:00:01Z" "") - **사례 2** 특정 날짜에서 시작하여 특정 날짜로 끝나는 범위를 정의할 수 있습니다. 예를 들어 보트쇼 또는 보트 유형에 대한 특정 승인을 정의할 수 있습니다. 날짜 관찰` 예: "2020-10-10T00:00:01Z:2020-10-14T23:59:59Z" `날짜 관찰` 예: "2020-10-10T00:00:01Z" `날짜 관찰` 예: "2020-10-14T23:59:59Z"  
이 데이터 모델에 대한 추가 정보* 다음 데이터 모델과 함께 사용할 수 있습니다. - 항구에서 승인된 보트에 대한 정보를 항구에 제공하기 위해 **SeaPort**.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### BoatAuthorized NGSI-v2 키 값 예시  
다음은 키 값으로 JSON-LD 형식의 BoatAuthorized의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### BoatAuthorized NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 BoatAuthorized의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### BoatAuthorized NGSI-LD 키-값 예시  
다음은 키 값으로 JSON-LD 형식의 BoatAuthorized의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### BoatAuthorized NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 BoatAuthorized의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
