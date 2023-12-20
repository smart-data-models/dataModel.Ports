<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티 SeaportFacilities  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 데이터 모델은 유람선, 상업 또는 여객 운송을 수용할 수 있는 항구에 대한 정보를 제공하기 위한 것입니다. 각 항구의 매개변수, 위치, 계류 능력, 항구에서 직접 또는 항구 근처에서 일하는 전문가가 제공하는 관련 무료 또는 유료 서비스를 나타낼 수 있습니다.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예: 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `authorizedPropulsion[array]`: 항구에 입항할 수 있도록 허가된 추진 유형. 모터, 돛, 전기, 노, 원자력, LNG, LPG, 기타의 조합  . Model: [https://schema.org/Text](https://schema.org/Text)- `boatSupplyingServices[array]`: 항구에서 또는 항구 근처에서 일하는 전문가가 제공하는 보트에 대한 보완적인 공급 서비스에 대한 설명입니다. 경비, 연료주유소, 연료탱크트럭, 식수탱크트럭, 급수, 드라이페어, 물페어, 수리, 전문성, 통로, 리프팅크레인, 견인, 폐기물물펌프, 보트운반, 보트운송, 기타의 조합  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `contactPoint[object]`: https://schema.org/ContactPoint  - `contractingAuthority[string]`: 계약 기관의 이름  . Model: [https://schema.org/Text](https://schema.org/Text)- `contractingCompany[string]`: 항만 관리를 담당하는 계약 회사  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `currencyAccepted[array]`: 모델에 정의된 활성 코드 목록의 조합 [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [암호화 통화](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [거래소 거래 시스템](https://en.wikipedia.org/wiki/Local_exchange_trading_system)  . Model: [https://schema.org/currenciesAccepted, .Currency accepted for payment](https://schema.org/currenciesAccepted, .Currency accepted for payment)- `dataProvider[string]`: 조화 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateLastReported[date-time]`: 플로우가 데이터를 성공적으로 보고한 마지막 시간을 나타내는 타임스탬프입니다. 이 리포지토리의 날짜 및 시간(ISO8601 UTC 형식)  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `electricTransport[array]`:  시에서 제안한 다양한 유형의 전기 교통수단 목록입니다. 전기자동차, 전기자전거, 전기모터바이크, 전기스쿠터의 조합  . Model: [http://schema.org/Text](http://schema.org/Text)- `endDate[date-time]`: 항목의 종료 날짜 및 시간(ISO 8601 날짜 형식)입니다.  . Model: [https://schema.org/endDate](https://schema.org/endDate)- `facilities[array]`: 항구에서 제안된 시설에 대한 설명. 화장실, 샤워실, 세탁실, 전화, 쓰레기통, 쓰레기통, 컨테이너, 분리수거함, 전기단자, 수도단자, 실내예약, 와이파이, 기타의 조합  . Model: [http://schema.org/Text](http://schema.org/Text)- `id[*]`: 엔티티의 고유 식별자  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링, 멀티폴리곤일 수 있습니다.  - `maxDraft[number]`: 항구에 접근할 수 있는 최대 흘수입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `maxLength[number]`: 항구에 접근할 수 있는 최대 길이입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `maxTonnage[number]`: 항구 접근이 허가된 최대 톤수입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정됩니다. 예를 들어 **TNE**는 톤 미터법을 나타냅니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `maxWidth[number]`: 항구에 접근할 수 있는 최대 폭입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `minLength[number]`: 항구에 접근할 수 있는 최소 길이입니다. 단위 코드(텍스트)는 [UN/CEFACT 공통 코드](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes)를 사용하여 지정합니다. 예를 들어 **MTR**은 미터를 나타냅니다.  . Model: [http://schema.org/Number](http://schema.org/Number)- `name[string]`: 이 항목의 이름  - `nearbyServices[array]`: 항구 또는 항구 근처의 지리적 영역에 대한 추가 서비스에 대한 설명입니다. 여행사, 피팅점, 여행사, 환전소, 의료기관, 약국, 식료품점, 레스토랑, 언론사, 바, 상점, 바다여행, 시티투어, 관광여행, 기타의 조합  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `numberOfPlace[number]`: 항구의 총 장소 수  . Model: [http://schema.org/Number](http://schema.org/Number)- `openingHours[string]`: 비즈니스의 일반적인 영업 시간입니다. 영업 시간은 일 단위로 시작하여 주 단위 시간 범위로 지정한 다음 일 단위로 지정할 수 있습니다. 여러 날을 쉼표 ''로 구분하여 나열할 수 있으며, 각 날을 구분합니다. 요일 또는 시간 범위는 하이픈 '-'를 사용하여 지정합니다. 요일은 다음 두 글자 조합을 사용하여 지정합니다: 월, 화, 수, 목, 금, 토, 일요일. 시간은 24:00 형식을 사용하여 지정합니다. 예를 들어 오후 3시는 15:00, 오전 10시는 10:00으로 지정합니다. 다음은 예시입니다: <time itemprop='openingHours' datetime='Tu,Th 16:00-20:00'>화요일 및 목요일 오후 4-8시</time>. 주 7일 영업하는 비즈니스의 경우 <time itemprop='openingHours' datetime='월~수'>월요일~일요일, 하루 종일</time>으로 지정할 수 있습니다.  . Model: [https://schema.org/openingHours](https://schema.org/openingHours)- `openingHoursSpecification[array]`: 장소의 영업 시간 또는 장소 내 특정 서비스에 대한 정보를 제공하는 구조화된 값입니다.  . Model: [https://schema.org/openingHoursSpecification](https://schema.org/openingHoursSpecification)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `paymentAccepted[array]`: 수락된 결제입니다. 모델에 정의된 활성 코드 목록의 조합: 현금, 신용 카드, 암호화 통화, 기타  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `portServicesProvided[array]`: 항구에서 직접 제공하는 서비스에 대한 설명. 조합: 항구 사무실, 날씨, 세관 서비스, 포터, 보트 링 대여, 계류장 지원, 취급 지원, 공용 와이파이, 사설 와이파이, 기타  . Model: [http://schema.org/Text](http://schema.org/Text)- `refBoatAuthorized[array]`: 엔티티] 목록 참조(https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md)  - `refBoatPlaceAvailable[array]`: 엔티티] 목록 참조(https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)  . Model: [https://schema.org/URL](https://schema.org/URL)- `refBoatPlacePricing[array]`: 엔티티] 목록 참조(https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)  . Model: [https://schema.org/URL](https://schema.org/URL)- `refDevice[*]`: 두 번째 링크로 사용되는 경우 메인 엔티티 [디바이스] 참조(https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md)  - `refPointOfInterest[*]`: 리포지토리와 연결된 [관심 지점](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md)에 대한 참조  - `rentalSaleServices[array]`: 항구 또는 항구 근처의 지리적 영역에서 전문 판매 또는 렌탈 대행사가 제공하는 서비스에 대한 설명. 보트 대여, 보트 판매, 제트스키 대여, 제트스키 판매, 자동차 대여, 고급 자동차 대여, 밴 대여, 자전거 대여, 스쿠터 대여, 캐디, 팔레트 운송, 기타의 조합  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `routeType[array]`: 도시 교통 모드 GFTS 표준 [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt)의 다양한 도시 교통 모드 유형(지하철, 버스, 트램, ...)의 목록입니다. '설명' 속성으로만 구성된 값의 조합 트램(0), 지하철(1), 기차(2), 버스(3), 페리(4), 케이블트램(5), 케이블카(6), 푸니쿨라(7), 트롤리버스(11), 모노레일(12).  . Model: [http://schema.org/Text](http://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 일련의 문자입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `startDate[date-time]`: 항목의 시작 날짜 및 시간(ISO 8601 날짜 형식)입니다.  . Model: [https://schema.org/startDate](https://schema.org/startDate)- `transportServices[array]`: 전용 교통편 및 셔틀 서비스에 대해 제공되는 서비스에 대한 설명입니다. 조합: 주차, 공항행 셔틀, 철도행 셔틀, 내부 셔틀, 택시, 헬기장, 기타  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `type[string]`: SeaPortFacilities여야 합니다.  - `typeOfPort[array]`: 항구의 한 종류. 조합: 선착장, 상품, 크루즈, 페리, 승객, 요트, 낚시, 군사, 강, 기타  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `webSite[string]`: 자세한 정보는 항구 공식 웹사이트로 이동하세요.  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `dateLastReported`  - `id`  - `location`  - `type`  - `typeOfPort`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SeaportFacilities:    
  description: 'The Data Model is intended to provide information about ports that can accommodate pleasure craft, commerce or passenger  transport. It permit to represent the parameters of each port, its location, its mooring capacities and the free or paid services associated with it provided directly by the port or by professionals working on or near the port.'    
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
    authorizedPropulsion:    
      description: 'A Type of propulsion authorized to enter in the harbor. A combination of motor, sail, electric, oar, nuclear, lng, lpg, other'    
      items:    
        enum:    
          - motor    
          - sail    
          - electric    
          - oar    
          - nuclear    
          - lng    
          - lpg    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    boatSupplyingServices:    
      description: 'Description of the complementary supplying services for the boat offered by professionals working on or near the harbor. A combination of guarding, fuelStation, fuelTankerTruck , drinkingWaterTankerTruck, provisioning, dryFairing, waterFairing, repair, expertise, gangways, liftingCranes, towing, wasteWaterPumping, boatConveying, boatTransfer, other'    
      items:    
        enum:    
          - boatConveying    
          - boatTransfer    
          - drinkingWaterTankerTruck    
          - dryFairing    
          - expertise    
          - fuelStation    
          - fuelTankerTruck    
          - gangways    
          - guarding    
          - liftingCranes    
          - provisioning    
          - repair    
          - towing    
          - waterFairing    
          - wasteWaterPumping    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    contactPoint:    
      description: https://schema.org/ContactPoint    
      type: object    
      x-ngsi:    
        type: Property    
    contractingAuthority:    
      description: Name of the contracting authority    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contractingCompany:    
      description: The Contracting Company responsible of the management of the port    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    currencyAccepted:    
      description: 'A combination of a list of active codes defined in the model [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system'    
      items:    
        enum:    
          - AUD    
          - GBP    
          - EUR    
          - JPY    
          - CHF    
          - USD    
          - AFN    
          - ALL    
          - DZD    
          - AOA    
          - ARS    
          - AMD    
          - AWG    
          - AUD    
          - ATS (EURO)    
          - BEF (EURO)    
          - AZN    
          - BSD    
          - BHD    
          - BDT    
          - BBD    
          - BYR    
          - BZD    
          - BMD    
          - BTN    
          - BOB    
          - BAM    
          - BWP    
          - BRL    
          - GBP    
          - BND    
          - BGN    
          - BIF    
          - XOF    
          - XAF    
          - XPF    
          - KHR    
          - CAD    
          - CVE    
          - KYD    
          - CLP    
          - CNY    
          - COP    
          - KMF    
          - CDF    
          - CRC    
          - HRK    
          - CUC    
          - CUP    
          - CYP (EURO)    
          - CZK    
          - DKK    
          - DJF    
          - DOP    
          - XCD    
          - EGP    
          - SVC    
          - EEK (EURO)    
          - ETB    
          - EUR    
          - FKP    
          - FIM (EURO)    
          - FJD    
          - GMD    
          - GEL    
          - DMK (EURO)    
          - GHS    
          - GIP    
          - GRD (EURO)    
          - GTQ    
          - GNF    
          - GYD    
          - HTG    
          - HNL    
          - HKD    
          - HUF    
          - ISK    
          - INR    
          - IDR    
          - IRR    
          - IQD    
          - IED (EURO)    
          - ILS    
          - ITL (EURO)    
          - JMD    
          - JPY    
          - JOD    
          - KZT    
          - KES    
          - KWD    
          - KGS    
          - LAK    
          - LVL (EURO)    
          - LBP    
          - LSL    
          - LRD    
          - LYD    
          - LTL (EURO)    
          - LUF (EURO)    
          - MOP    
          - MKD    
          - MGA    
          - MWK    
          - MYR    
          - MVR    
          - MTL (EURO)    
          - MRO    
          - MUR    
          - MXN    
          - MDL    
          - MNT    
          - MAD    
          - MZN    
          - MMK    
          - ANG    
          - NAD    
          - NPR    
          - NLG (EURO)    
          - NZD    
          - NIO    
          - NGN    
          - KPW    
          - NOK    
          - OMR    
          - PKR    
          - PAB    
          - PGK    
          - PYG    
          - PEN    
          - PHP    
          - PLN    
          - PTE (EURO)    
          - QAR    
          - RON    
          - RUB    
          - RWF    
          - WST    
          - STD    
          - SAR    
          - RSD    
          - SCR    
          - SLL    
          - SGD    
          - SKK (EURO)    
          - SIT (EURO)    
          - SBD    
          - SOS    
          - ZAR    
          - KRW    
          - ESP (EURO)    
          - LKR    
          - SHP    
          - SDG    
          - SRD    
          - SZL    
          - SEK    
          - CHF    
          - SYP    
          - TWD    
          - TZS    
          - THB    
          - TOP    
          - TTD    
          - TND    
          - TRY    
          - TMM    
          - USD    
          - UGX    
          - UAH    
          - UYU    
          - AED    
          - VUV    
          - VEB    
          - VND    
          - YER    
          - ZMK    
          - ZWD    
        type: string    
      type: array    
      x-ngsi:    
        model: 'https://schema.org/currenciesAccepted, .Currency accepted for payment'    
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
      description: A timestamp which denotes the last time when a flow successfully reported data. The date and time of this Repository in ISO8601 UTCformat    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
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
    electricTransport:    
      description: ' List of the different types of electric transport proposed by the city. A combination of electricCar, electricBycicle, electricMotorBike, electricScooter '    
      items:    
        enum:    
          - electricBycicle    
          - electricCar    
          - electricMotorBike    
          - electricScooter    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    endDate:    
      description: The end date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/endDate    
        type: Property    
    facilities:    
      description: 'Description of the proposed facilities on the harbor. A combination of : toilets, showers, laundry, telephone, dustbins, dumpsters, container, selectiveSortingWaste, electricTerminal, waterTerminal, indoorRoomReservation, wifi, other'    
      items:    
        enum:    
          - container    
          - dustbins    
          - dumpsters    
          - electricTerminal    
          - 'indoorRoomReservation '    
          - laundry    
          - selectiveSortingWaste    
          - showers    
          - telephone    
          - toilets    
          - waterTerminal    
          - wifi    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
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
      description: 'A Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    maxLength:    
      description: 'A Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    maxTonnage:    
      description: 'Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: TNE    
    maxWidth:    
      description: 'A Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    minLength:    
      description: 'A Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
        units: MTR    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    nearbyServices:    
      description: 'Description of the additional services on the geographical area on or near the harbor. A combination of :touristOffice, fittingsStores, travelAgency, exchangeOffice, medicalOffice, pharmacy, groceryStores, restaurants, presses, bar, shops, seaExcursions, cityTour, touristicExcursions, others'    
      items:    
        enum:    
          - bar    
          - cityTour    
          - fittingsStores    
          - groceryStores    
          - exchangeOffice    
          - medicalOffice    
          - pharmacy    
          - presses    
          - restaurants    
          - seaExcursions    
          - shops    
          - touristicExcursions    
          - touristOffice    
          - travelAgency    
          - others    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    numberOfPlace:    
      description: Total number of place in the harbor    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    openingHours:    
      description: 'The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas '','' separating each day. Day or time ranges are specified using a hyphen ''-''. Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su. Times are specified using 24:00 format. For example, 3pm is specified as 15:00, 10am as 10:00. Here is an example: <time itemprop=''openingHours'' datetime=''Tu,Th 16:00-20:00''>Tuesdays and Thursdays 4-8pm</time>. If a business is open 7 days a week, then it can be specified as <time itemprop=''openingHours'' datetime=''Mo-Su''>Monday through Sunday, all day</time>'    
      type: string    
      x-ngsi:    
        model: https://schema.org/openingHours    
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
    paymentAccepted:    
      description: 'Accepted payment. A combination of a list of active codes defined in the model : Cash, CreditCard, CryptoCurrency, other'    
      items:    
        enum:    
          - Cash    
          - CreditCard    
          - CryptoCurrency    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    portServicesProvided:    
      description: 'Description of the services provided directly by the harbor. A combination of : harborOffice, weather, customsServices, porters, boatRingRental, mooringAssistance, handlingAssistance, publicWifi, privateWifi, other'    
      items:    
        enum:    
          - harborOffice    
          - weather    
          - customsServices    
          - porters    
          - boatRingRental    
          - mooringAssistance    
          - handlingAssistance    
          - publicWifi    
          - privateWifi    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
        type: Property    
    refBoatAuthorized:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md)'    
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
        type: Relationship    
    refBoatPlaceAvailable:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)'    
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
        model: https://schema.org/URL    
        type: Property    
    refBoatPlacePricing:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)'    
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
        model: https://schema.org/URL    
        type: Relationship    
    refDevice:    
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
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
      x-ngsi:    
        type: Relationship    
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
        type: Relationship    
    rentalSaleServices:    
      description: 'ADescription of services provided by professional sales or rental agencies on the geographical area on or near the harbor. A combination of : boatRental, boatSale, jetSkiRental, jetSkiSale, carRental, luxuryCarRental, vanRental, bikeRental, scooterRental, Caddie, palletTransport, other'    
      items:    
        enum:    
          - bikeRental    
          - boatRental    
          - boatSale    
          - Caddie    
          - carRental    
          - jetSkiRental    
          - jetSkiSale    
          - luxuryCarRental    
          - palletTransport    
          - scooterRental    
          - vanRental    
          - Others    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    routeType:    
      description: "List of the different types of urban transport Mode (Metro, Bus, Tram, ...) from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values composed only of the attribute 'description' tram(0), metro(1), train(2), bus(3), ferry(4), cableTram(5), cableCar(6), funicular(7), trolleybus(11), monorail(12)"    
      items:    
        enum:    
          - bus    
          - cableCar    
          - cableTram    
          - ferry    
          - funicular    
          - metro    
          - monorail    
          - train    
          - tram    
          - trolleybus    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/Text    
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
    startDate:    
      description: The start date and time of the item (in ISO 8601 date format).    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/startDate    
        type: Property    
    transportServices:    
      description: 'Description of the services provided for dedicated transport and shuttle services. A combination of : parking, shuttlesToAirport, shuttlesToRailway, internalShuttles, taxis, heliport, other'    
      items:    
        enum:    
          - heliport    
          - internalShuttle    
          - parking    
          - shuttlesToAirport    
          - shuttlesToRailway    
          - taxis    
          - Others    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    type:    
      description: It has to be SeaPortFacilities    
      enum:    
        - SeaPortFacilities    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfPort:    
      description: 'A Type of harbor. A combination of : marina, merchandise, cruise, ferry, passengers, yachting, fishing, military, river, other'    
      items:    
        enum:    
          - cruise    
          - ferry    
          - fishing    
          - marina    
          - merchandise    
          - military    
          - passengers    
          - river    
          - yachting    
          - other    
        type: string    
      type: array    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    webSite:    
      description: Link to the official website of the harbor for more information    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - typeOfPort    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.Ports/SeaPortFacilities/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### SeaportFacilities NGSI-v2 키-값 예제  
다음은 JSON-LD 형식의 SeaportFacilities를 키 값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
  "type": "SeaPortFacilities",  
  "name": "Riviera-Port-NCE-SP-001",  
  "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
  "description": "Harbor Description and services provided",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Port",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "refBoatAuthorized": [  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
  ],  
  "refBoatPlaceAvailable": [  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
  ],  
  "refBoatPlacePricing": [  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
  ],  
  "owner": [  
    "Departement_06",  
    "CCI06",  
    "MNCA",  
    "Ville_de_Nice"  
  ],  
  "contractingAuthority": "CCI",  
  "contractingCompany": "R\u00e9gie Autonome des ports",  
  "contactPoint": {  
    "name": "Capitainerie"  
  },  
  "webSite": "https://riviera-ports.com/ports/port-de-nice",  
  "typeOfPort": [  
    "marina",  
    "merchandise",  
    "cruise",  
    "ferry",  
    "yachting"  
  ],  
  "authorizedPropulsion": [  
    "motor",  
    "electric",  
    "lng"  
  ],  
  "maxTonnage": 30000,  
  "numberOfPlace": 120,  
  "minLength": 6,  
  "maxLength": 180,  
  "maxWidth": 25,  
  "maxDraft": 9.65,  
  "portServicesProvided": [  
    "harborOffice",  
    "weather",  
    "customsServices",  
    "porters"  
  ],  
  "boatSupplyingServices": [  
    "fuelStation",  
    "fuelTankerTruck",  
    "drinkingWaterTankerTruck",  
    "dryFairing",  
    "repair",  
    "expertise",  
    "gangways",  
    "liftingCranes",  
    "towing",  
    "wasteWaterPumping",  
    "boatConveying"  
  ],  
  "facilities": [  
    "wifi",  
    "telephone",  
    "toilets",  
    "selectiveSortingWaste",  
    "electricTerminal",  
    "waterTerminal",  
    "dustbins",  
    "dumpsters",  
    "container"  
  ],  
  "nearbyServices": [  
    "groceryStores",  
    "presses",  
    "exchangeOffice",  
    "touristicExcursions"  
  ],  
  "rentalSaleServices": [  
    "boatRental",  
    "boatSale",  
    "carRental"  
  ],  
  "transportServices": [  
    "parking",  
    "shuttlesToAirport",  
    "taxis"  
  ],  
  "routeType": [  
    "tram",  
    "metro",  
    "train",  
    "bus",  
    "ferry"  
  ],  
  "electricTransport": [  
    "electricBycicle",  
    "electricMotorBike"  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR",  
    "USD"  
  ]  
}  
```  
</details>  
#### SeaportFacilities NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 SeaportFacilities의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
  "type": "SeaPortFacilities",  
  "name": {  
    "type": "Text",  
    "value": "Riviera-Port-NCE-SP-001"  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": "Riviera Port - Main harbor - Commerce & Passengers"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Harbor Description and services provided"  
  },  
  "seeAlso": {  
    "type": "Text",  
    "value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
    }  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "Nice Port"  
  },  
  "dateLastReported": {  
    "type": "DateTime",  
    "value": "2020-03-17T08:45:00Z"  
  },  
  "refBoatAuthorized": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
      "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
    ]  
  },  
  "refBoatPlaceAvailable": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
      "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
    ]  
  },  
  "refBoatPlacePricing": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
      "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
    ]  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "Departement_06",  
      "CCI06",  
      "MNCA",  
      "Ville_de_Nice"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Text",  
    "value": "CCI"  
  },  
  "contractingCompagny": {  
    "type": "Text",  
    "value": "R\u00e9gie Autonome des ports"  
  },  
  "contactPoint": {  
    "type": "StructuredValue",  
    "value": {  
      "name": "Capitainerie"  
    }  
  },  
  "webSite": {  
    "type": "Text",  
    "value": "https://riviera-ports.com/ports/port-de-nice"  
  },  
  "typeOfPort": {  
    "type": "StructuredValue",  
    "value": [  
      "marina",  
      "merchandise",  
      "cruise",  
      "ferry",  
      "yachting"  
    ]  
  },  
  "authorizedPropulsions": {  
    "type": "StructuredValue",  
    "value": [  
      "motor",  
      "electric",  
      "lng"  
    ]  
  },  
  "maxTonnage": {  
    "type": "Number",  
    "value": 30000  
  },  
  "numberOfPlace": {  
    "type": "Number",  
    "value": 120  
  },  
  "minLength": {  
    "type": "Number",  
    "value": 6  
  },  
  "maxLength": {  
    "type": "Number",  
    "value": 180  
  },  
  "maxWidth": {  
    "type": "Number",  
    "value": 25  
  },  
  "maxDraft": {  
    "type": "Number",  
    "value": 9.65  
  },  
  "portServicesProvided": {  
    "type": "StructuredValue",  
    "value": [  
      "harborOffice",  
      "weather",  
      "customsServices",  
      "porters"  
    ]  
  },  
  "boatSupplyingServices": {  
    "type": "StructuredValue",  
    "value": [  
      "fuelStation",  
      "fuelTankerTruck",  
      "drinkingWaterTankerTruck",  
      "dryFairing",  
      "repair",  
      "expertise",  
      "gangways",  
      "liftingCranes",  
      "towing",  
      "wasteWaterPumping",  
      "boatConveying"  
    ]  
  },  
  "facilities": {  
    "type": "StructuredValue",  
    "value": [  
      "wifi",  
      "telephone",  
      "toilets",  
      "selectiveSortingWaste",  
      "electricTerminal",  
      "waterTerminal",  
      "dustbins",  
      "dumpsters",  
      "container"  
    ]  
  },  
  "nearbyServices": {  
    "type": "StructuredValue",  
    "value": [  
      "groceryStores",  
      "presses",  
      "exchangeOffice",  
      "touristicExcursions"  
    ]  
  },  
  "rentalSaleServices": {  
    "type": "StructuredValue",  
    "value": [  
      "boatRental",  
      "boatSale",  
      "carRental"  
    ]  
  },  
  "transportServices": {  
    "type": "StructuredValue",  
    "value": [  
      "parking",  
      "shuttlesToAirport",  
      "taxis"  
    ]  
  },  
  "routeType": {  
    "type": "StructuredValue",  
    "value": [  
      "tram",  
      "metro",  
      "train",  
      "bus",  
      "ferry"  
    ]  
  },  
  "electricTransport": {  
    "type": "StructuredValue",  
    "value": [  
      "electricBycicle",  
      "electricMotorBike"  
    ]  
  },  
  "paymentAccepted": {  
    "type": "StructuredValue",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "StructuredValue",  
    "value": [  
      "EUR",  
      "USD"  
    ]  
  }  
}  
```  
</details>  
#### SeaportFacilities NGSI-LD 키 값 예제  
다음은 JSON-LD 형식의 SeaportFacilities를 키 값으로 사용하는 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
  "type": "SeaPortFacilities",  
  "name": "Riviera-Port-NCE-SP-001",  
  "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
  "description": "Harbor Description and services provided",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.66481,  
      7.196545  
    ]  
  },  
  "areaServed": "Nice Port",  
  "dateLastReported": "2020-03-17T08:45:00Z",  
  "refBoatAuthorized": [  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
    "urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
  ],  
  "refBoatPlaceAvailable": [  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
    "urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
  ],  
  "refBoatPlacePricing": [  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
    "urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
  ],  
  "owner": [  
    "Departement_06",  
    "CCI06",  
    "MNCA",  
    "Ville_de_Nice"  
  ],  
  "contractingAuthority": "CCI",  
  "contractingCompany": "R\u00e9gie Autonome des ports",  
  "contactPoint": {  
    "name": "Capitainerie"  
  },  
  "webSite": "https://riviera-ports.com/ports/port-de-nice",  
  "typeOfPort": [  
    "marina",  
    "merchandise",  
    "cruise",  
    "ferry",  
    "yachting"  
  ],  
  "authorizedPropulsion": [  
    "motor",  
    "electric",  
    "lng"  
  ],  
  "maxTonnage": 30000,  
  "numberOfPlace": 120,  
  "minLength": 6,  
  "maxLength": 180,  
  "maxWidth": 25,  
  "maxDraft": 9.65,  
  "portServicesProvided": [  
    "harborOffice",  
    "weather",  
    "customsServices",  
    "porters"  
  ],  
  "boatSupplyingServices": [  
    "fuelStation",  
    "fuelTankerTruck",  
    "drinkingWaterTankerTruck",  
    "dryFairing",  
    "repair",  
    "expertise",  
    "gangways",  
    "liftingCranes",  
    "towing",  
    "wasteWaterPumping",  
    "boatConveying"  
  ],  
  "facilities": [  
    "wifi",  
    "telephone",  
    "toilets",  
    "selectiveSortingWaste",  
    "electricTerminal",  
    "waterTerminal",  
    "dustbins",  
    "dumpsters",  
    "container"  
  ],  
  "nearbyServices": [  
    "groceryStores",  
    "presses",  
    "exchangeOffice",  
    "touristicExcursions"  
  ],  
  "rentalSaleServices": [  
    "boatRental",  
    "boatSale",  
    "carRental"  
  ],  
  "transportServices": [  
    "parking",  
    "shuttlesToAirport",  
    "taxis"  
  ],  
  "routeType": [  
    "tram",  
    "metro",  
    "train",  
    "bus",  
    "ferry"  
  ],  
  "electricTransport": [  
    "electricBycicle",  
    "electricMotorBike"  
  ],  
  "paymentAccepted": [  
    "Cash",  
    "CreditCard"  
  ],  
  "currencyAccepted": [  
    "EUR",  
    "USD"  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### SeaportFacilities NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 SeaportFacilities의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
	"id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
	"type": "SeaPort",  
	"name": {  
		"type": "Property",  
		"value": "Riviera-Port-NCE-SP-001"  
	},  
	"alternateName": {  
		"type": "Property",  
		"value": "Riviera Port - Main harbor - Commerce & Passengers"  
	},  
	"description": {  
		"type": "Property",  
		"value": "Harbor Description and services provided"  
	},  
	"seeAlso": {  
		"type": "Property",  
		"value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
	},  
	"location": {  
		"type": "GeoProperty",  
		"value": {  
			"type": "Point",  
				"coordinates": [43.664810, 7.196545]  
			}  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Port"  
	},  
	"dateLastReported": {  
		"type": "Property",  
		"value": "2020-03-17T08:45:00Z",  
		"metadata": {  
			"TimeInstant": {  
				"type": "Text",  
				"value": "2020-03-17TT08:45:00Z"  
			}  
		}  
	},  
	"refBoatAuthorized": {  
		"type": "Relationship",  
		"value": ["urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-passenger",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-fishing",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-cargo",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-tankers",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-specialist",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-war",  
					"urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-historic"  
		]  
	},  
	"refBoatPlaceAvailable": {  
		"type": "Relationship",  
		"value": ["urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-BC",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-DE",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-FG",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-HI",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-JK",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-LO",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-PQ",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-RT2",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-U",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-VW",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-XZ",  
					"urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-Z02"  
		]  
	},  
	"refBoatPlacePricing": {  
		"type": "Relationship",  
		"value": ["urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-BC",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-DE",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-FG",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-HI",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-JK",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-LO",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-PQ",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-RT2",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-U",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-VW",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-XZ",  
					"urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-Z02"  
		]  
	},  
	"owner" : {  
		"type": "Property",  
		"value": ["Departement_06", "CCI06", "MNCA", "Ville_de_Nice"]  
	},  
	"contractingAuthority": {  
		"type": "Property",  
		"value": "CCI"  
	},  
	"contractingCompagny": {  
		"type": "Property",  
		"value": "RÃ©gie Autonome des ports"  
	},  
	"contactPoint": {  
		"type": "Property",  
		"value": {  
            "name": "Capitainerie"  
        }  
	},  
	"webSite": {  
		"type": "Property",  
		"value": "https://riviera-ports.com/ports/port-de-nice"  
	},  
	"typeOfPort": {  
		"type": "Property",  
		"value": ["marina", "merchandise", "cruise", "ferry", "yatching"]  
	},  
	"authorizedPropulsions": {  
		"type": "Property",  
		"value": ["motor", "electric","lng"]  
	},  
	"maxTonnage": {  
		"type": "Property",  
		"value": 30000  
	},  
	"numberOfPlace": {  
		"type": "Property",  
		"value": 120  
	},  
	"minLength": {  
		"type": "Property",  
		"value": 6  
	},  
	"maxLength": {  
		"type": "Property",  
		"value": 180  
	},  
	"maxWidth": {  
		"type": "Property",  
		"value": 25  
	},  
	"maxDraft": {  
		"type": "Property",  
		"value": 9.65  
	},  
	"portServicesProvided": {  
		"type": "Property",  
		"value": ["harborOffice", "weather", "customsServices", "porters"]  
	},  
	"boatSupplyingServices": {  
		"type": "Property",  
		"value": ["fuelStation", "fuelTankerTruck", "drinkingWaterTankerTruck", "dryFairing", "repair", "expertise", "gangways", "liftingCranes", "towing", "wasteWaterPumping", "boatConveying"]  
	},  
	"facilities": {  
		"type": "Property",  
		"value": ["wifi", "telephone", "toilets", "selectiveSortingWaste", "electricTerminal", "waterTerminal", "dustbins", "dumpsters", "container"]  
	},  
	"nearbyServices": {  
		"type": "Property",  
		"value": ["groceryStores", "presses", "exchangeOffice", "touristicExcursions"]  
	},  
	"rentalSaleServices": {  
		"type": "Property",  
		"value": ["boatRental", "boatSale", "carRental"]  
	},  
	"transportServices": {  
		"type": "Property",  
		"value": ["parking", "shuttlesToAirport", "taxis"]  
	},  
	"routeType": {  
		"type": "Property",  
		"value": ["tram", "metro", "train", "bus", "ferry"]  
	},  
	"electricTransport": {  
		"type": "Property",  
		"value": ["electricBycicle", "electricMotorBike"]  
	},  
	"paymentAccepted": {  
		"type": "Property",  
		"value": ["Cash", "CreditCard"]  
	},  
	"currencyAccepted": {  
		"type": "Property",  
		"value": ["EUR", "USD"]  
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
크기 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
