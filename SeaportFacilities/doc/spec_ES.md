Entidad: SeaportFacilities  
==========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md)  
Descripción global: **El modelo de datos tiene por objeto proporcionar información sobre los puertos que pueden acoger embarcaciones de recreo, comercio o transporte de pasajeros. Permite representar los parámetros de cada puerto, su ubicación, su capacidad de atraque y los servicios gratuitos o de pago asociados a él, prestados directamente por el puerto o por los profesionales que trabajan en él o cerca de él**.  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `authorizedPropulsion`: Un tipo de propulsiones autorizadas para entrar en el puerto. Una combinación de motor, vela, eléctrica, remo, nuclear, lng, lpg, otras  - `boatSupplyingServices`: escripción de los servicios complementarios de suministro para el barco ofrecidos por los profesionales que trabajan en el puerto o cerca de él. Una combinación de vigilancia, estación de combustible, camión cisterna de combustible, camión cisterna de agua potable, aprovisionamiento, limpieza en seco, limpieza de agua, reparación, peritaje, pasarelas, elevación de grúas, remolque, bombeo de aguas residuales, transporte de embarcaciones, traslado de embarcaciones, otros.  - `contactPoint`: https://schema.org/ContactPoint  - `contractingAuthority`: Nombre de la autoridad contratante  - `contractingCompany`: La Compañía Contratante responsable de la gestión del puerto.  - `currencyAccepted`: Una combinación de una lista de códigos activos definidos en el modelo [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateLastReported`: Una marca de tiempo que denota la última vez en que un flujo informó con éxito de los datos. La fecha y la hora de este Repositorio en formato UTC ISO8601  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `electricTransport`:  Lista de los diferentes tipos de transporte eléctrico propuestos por la ciudad. Una combinación de coche eléctrico, bicicleta eléctrica, moto eléctrica, scooter eléctrico...  - `facilities`: Descripción de las instalaciones propuestas en el puerto. Una combinación de: baños, duchas, lavandería, teléfono, basureros, contenedores, clasificación selectiva de residuos, terminal eléctrica, terminal de agua, reserva de habitaciones interiores, wifi, otros...  - `id`: Identificador único de la entidad  - `location`:   - `maxDraft`: Un calado máximo permitido para acceder al puerto. El código de unidad (texto) se da usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Meter  - `maxLength`: Una longitud máxima permitida para acceder al puerto. El código de unidad (texto) se da usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Meter  - `maxTonnage`: Tonelaje máximo autorizado para acceder al puerto. El código de unidad (texto) se da usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **TNE** representa Tonelada Métrica.  - `maxWidth`: Un ancho máximo permitido para acceder al puerto. El código de unidad (texto) se da usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . Por ejemplo, **MTR** representa Meter  - `minLength`: Una longitud mínima permitida para acceder al puerto. El código de la unidad (texto) se da usando los [Códigos Comunes de UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). Por ejemplo, **MTR** representa Meter  - `name`: El nombre de este artículo.  - `nearbyServices`: Descripción de los servicios adicionales en la zona geográfica en el puerto o cerca del mismo. Una combinación de: oficina de turismo, tiendas, agencia de viajes, oficina de intercambio, oficina médica, farmacia, tiendas de comestibles, restaurantes, prensas, bares, tiendas, excursiones marítimas, city tour, excursiones turísticas, otros.  - `numberOfPlace`: Número total de lugares en el puerto.  - `openingHoursSpecification`: Un valor estructurado que proporciona información sobre los horarios de apertura de un lugar o un determinado servicio dentro de un lugar.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `paymentAccepted`: Aceptado el pago. Una combinación de una lista de códigos activos definidos en el modelo: Efectivo, Tarjeta de Crédito, CriptoCartera, otros  - `portServicesProvided`: Descripción de los servicios prestados directamente por el puerto. Una combinación de: oficina portuaria, meteorología, aduanas, servicios, porteadores, barco, alquiler de anillos, asistencia en el amarre, asistencia en la manipulación, WiFi público, WiFi privado, otros.  - `refBoatAuthorized`: Referencia a una lista de [Entidad](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md).  - `refBoatPlaceAvailable`: Referencia a una lista de [Entidad](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)  - `refBoatPlacePricing`: Referencia a una lista de [Entidad](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)  - `refDevice`: Referencia a la Entidad Principal [Dispositivo](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) si se utiliza como segundo enlace  - `refPointOfInterest`: Referencia a un [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) vinculado con el Repositorio  - `rentalSaleServices`: Descripción de los servicios prestados por agencias profesionales de venta o alquiler en la zona geográfica del puerto o en sus proximidades. Una combinación de : barcoAlquiler, barcoVenta, jetSkiAlquiler, jetSkiVenta, cocheAlquiler, coche de lujoAlquiler, furgonetaAlquiler, bicicletaAlquiler, scooterAlquiler, Caddie, paletTransporte, otros  - `routeType`: Lista de los diferentes tipos de modo de transporte urbano (Metro, Bus, Tranvía, ...) de la norma GFTS de modo de transporte urbano [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). Una combinación de valores compuesta sólo por el atributo 'descripción' tranvía(0), metro(1), tren(2), autobús(3), transbordador(4), cableTram(5), cableCar(6), funicular(7), trolebús(11), monorraíl(12)  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `transportServices`: Descripción de los servicios prestados para el transporte dedicado y los servicios de lanzadera. Una combinación de: transporte, lanzaderas al aeropuerto, lanzaderas al ferrocarril, lanzaderas internas, taxis, helipuerto, otros...  - `type`: Tiene que ser SeaPort  - `typeOfPort`: Un tipo de puerto. Una combinación de: marina, mercancía, crucero, ferry, pasajeros, yachting, pesca, militar, fluvial, otros  - `webSite`: Enlace al sitio web oficial del puerto para más información.    
Propiedades requeridas  
- `dateLastReported`  - `id`  - `location`  - `type`  - `typeOfPort`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SeaportFacilities:    
  description: 'The Data Model is intended to provide information about ports that can accommodate pleasure craft, commerce or passenger  transport. It permit to represent the parameters of each port, its location, its mooring capacities and the free or paid services associated with it provided directly by the port or by professionals working on or near the port.'    
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
    authorizedPropulsion:    
      description: 'A Type of propulsions authorized to enter in the harbor. A combination of motor, sail, electric, oar, nuclear, lng, lpg, other'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    boatSupplyingServices:    
      description: 'escription of the complementary supplying services for the boat offered by professionals working on or near the harbor. A combination of guarding, fuelStation, fuelTankerTruck , drinkingWaterTankerTruck, provisioning, dryFairing, waterFairing, repair, expertise, gangways, liftingCranes, towing, wasteWaterPumping, boatConveying, boatTransfer, other'    
      items:    
        enum:    
          - guarding    
          - fuelStation    
          - fuelTankerTruck    
          - drinkingWaterTankerTruck    
          - provisioning    
          - dryFairing    
          - waterFairing    
          - repair    
          - expertise    
          - gangways    
          - liftingCranes    
          - towing    
          - wasteWaterPumping    
          - boatConveying    
          - boatTransfer    
          - other    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    contactPoint:    
      description: https://schema.org/ContactPoint    
      type: Property    
    contractingAuthority:    
      description: 'Name of the contracting authority'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    contractingCompany:    
      description: 'The Contracting Company responsible of the management of the port.'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
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
          - 'ATS (EURO)'    
          - 'BEF (EURO)'    
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
          - 'CYP (EURO)'    
          - CZK    
          - DKK    
          - DJF    
          - DOP    
          - XCD    
          - EGP    
          - SVC    
          - 'EEK (EURO)'    
          - ETB    
          - EUR    
          - FKP    
          - 'FIM (EURO)'    
          - FJD    
          - GMD    
          - GEL    
          - 'DMK (EURO)'    
          - GHS    
          - GIP    
          - 'GRD (EURO)'    
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
          - 'IED (EURO)'    
          - ILS    
          - 'ITL (EURO)'    
          - JMD    
          - JPY    
          - JOD    
          - KZT    
          - KES    
          - KWD    
          - KGS    
          - LAK    
          - 'LVL (EURO)'    
          - LBP    
          - LSL    
          - LRD    
          - LYD    
          - 'LTL (EURO)'    
          - 'LUF (EURO)'    
          - MOP    
          - MKD    
          - MGA    
          - MWK    
          - MYR    
          - MVR    
          - 'MTL (EURO)'    
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
          - 'NLG (EURO)'    
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
          - 'PTE (EURO)'    
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
          - 'SKK (EURO)'    
          - 'SIT (EURO)'    
          - SBD    
          - SOS    
          - ZAR    
          - KRW    
          - 'ESP (EURO)'    
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
      type: Property    
      x-ngsi:    
        model: 'https://schema.org/currenciesAccepted, .Currency accepted for payment'    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateLastReported:    
      description: 'A timestamp which denotes the last time when a flow successfully reported data. The date and time of this Repository in ISO8601 UTCformat'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    electricTransport:    
      description: ' List of the different types of electric transport proposed by the city. A combination of electricCar, electricBycicle, electricMotorBike, electricScooter '    
      items:    
        enum:    
          - electricCar    
          - electricBycicle    
          - electricMotorBike    
          - electricScooter    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    facilities:    
      description: 'Description of the proposed facilities on the harbor. A combination of : toilets, showers, laundry, telephone, dustbins, dumpsters, container, selectiveSortingWaste, electricTerminal, waterTerminal, indoorRoomReservation, wifi, other'    
      items:    
        enum:    
          - toilets    
          - showers    
          - laundry    
          - telephone    
          - dustbins    
          - dumpsters    
          - container    
          - selectiveSortingWaste    
          - electricTerminal    
          - waterTerminal    
          - 'indoorRoomReservation '    
          - wifi    
          - other    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    id:    
      anyOf: &seaportfacilities_-_properties_-_owner_-_items_-_anyof    
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
      description: 'A Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: MTR    
    maxLength:    
      description: 'A Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: MTR    
    maxTonnage:    
      description: 'Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: TNE    
    maxWidth:    
      description: 'A Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: MTR    
    minLength:    
      description: 'A Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
        units: MTR    
    name:    
      description: 'The name of this item.'    
      type: Property    
    nearbyServices:    
      description: 'Description of the additional services on the geographical area on or near the harbor. A combination of :touristOffice, fittingsStores, travelAgency, exchangeOffice, medicalOffice, pharmacy, groceryStores, restaurants, presses, bar, shops, seaExcursions, cityTour, touristicExcursions, others'    
      items:    
        enum:    
          - touristOffice    
          - fittingsStores    
          - travelAgency    
          - exchangeOffice    
          - medicalOffice    
          - pharmacy    
          - groceryStores    
          - restaurants    
          - presses    
          - bar    
          - shops    
          - seaExcursions    
          - cityTour    
          - touristicExcursions    
          - others    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    numberOfPlace:    
      description: 'Total number of place in the harbor.'    
      minimum: 0    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Number    
    openingHoursSpecification:    
      description: 'A structured value providing information about the opening hours of a place or a certain service inside a place.'    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *seaportfacilities_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
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
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
    refBoatAuthorized:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md).'    
      items:    
        anyOf: *seaportfacilities_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
    refBoatPlaceAvailable:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)'    
      items:    
        anyOf: *seaportfacilities_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    refBoatPlacePricing:    
      description: 'Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)'    
      items:    
        anyOf: *seaportfacilities_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    refDevice:    
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
      type:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
    refPointOfInterest:    
      description: 'Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository'    
      type:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
    rentalSaleServices:    
      description: 'ADescription of services provided by professional sales or rental agencies on the geographical area on or near the harbor. A combination of : boatRental, boatSale, jetSkiRental, jetSkiSale, carRental, luxuryCarRental, vanRental, bikeRental, scooterRental, Caddie, palletTransport, other'    
      items:    
        enum:    
          - boatRental    
          - boatSale    
          - jetSkiRental    
          - jetSkiSale    
          - carRental    
          - luxuryCarRental    
          - vanRental    
          - bikeRental    
          - scooterRental    
          - Caddie    
          - palletTransport    
          - Others    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    routeType:    
      description: "List of the different types of urban transport Mode (Metro, Bus, Tram, ...) from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values composed only of the attribute 'description' tram(0), metro(1), train(2), bus(3), ferry(4), cableTram(5), cableCar(6), funicular(7), trolleybus(11), monorail(12)"    
      items:    
        enum:    
          - tram    
          - metro    
          - train    
          - bus    
          - ferry    
          - cableTram    
          - cableCar    
          - funicular    
          - trolleybus    
          - monorail    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/Text    
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
    transportServices:    
      description: 'Description of the services provided for dedicated transport and shuttle services. A combination of : arking, shuttlesToAirport, shuttlesToRailway, internalShuttles, taxis, heliport, other'    
      items:    
        enum:    
          - parking    
          - shuttlesToAirport    
          - shuttlesToRailway    
          - internalShuttle    
          - taxis    
          - heliport    
          - Others    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    type:    
      description: 'It has to be SeaPort'    
      enum:    
        - SeaPort    
      type: Property    
    typeOfPort:    
      description: 'A Type of harbor. A combination of : marina, merchandise, cruise, ferry, passengers, yachting, fishing, military, river, other'    
      items:    
        enum:    
          - marina    
          - merchandise    
          - cruise    
          - ferry    
          - passengers    
          - yachting    
          - fishing    
          - military    
          - river    
          - other    
        type: string    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    webSite:    
      description: 'Link to the official website of the harbor for more information.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - typeOfPort    
  type: object    
```  
</details>    
## Ejemplo de cargas útiles  
#### SeaportFacilities NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un SeaportFacilities en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
  "type": "SeaPort",  
  "name": "Riviera-Port-NCE-SP-001",  
  "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
  "description": "Harbor Description and services provided",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
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
    "Departement_06", "CCI06", "MNCA", "Ville_de_Nice"  
  ],  
  "contractingAuthority": "CCI",  
  "contractingCompany": "Régie Autonome des ports",  
  "contactPoint": "Capitainerie",  
  "webSite": "https://riviera-ports.com/ports/port-de-nice",  
  "typeOfPort": [  
    "marina",  
    "merchandise",  
    "cruise",  
    "ferry",  
    "yatching"  
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
#### SeaportFacilities NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un SeaportFacilities en formato JSON normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
			"type": "point",  
				"coordinates": [43.664810, 7.196545]  
			}  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Port"  
	},  
	"dateLastReported": {  
		"type": "DateTime",  
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
		"Object": ["urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
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
		"Object": ["urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
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
		"Object": ["urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
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
		"value": "Régie Autonome des ports"  
	},  
	"contactPoint": {  
		"type": "Property",  
		"value": "Capitainerie"  
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
	}  
}  
```  
#### SeaportFacilities NGSI-LD key-values Example  
Aquí hay un ejemplo de un SeaportFacilities en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
  "type": "SeaPort",  
  "name": "Riviera-Port-NCE-SP-001",  
  "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
  "description": "Harbor Description and services provided",  
  "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      43.664810,  
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
    "Departement_06", "CCI06", "MNCA", "Ville_de_Nice"  
  ],  
  "contractingAuthority": "CCI",  
  "contractingCompany": "RÃ©gie Autonome des ports",  
  "contactPoint": "Capitainerie",  
  "webSite": "https://riviera-ports.com/ports/port-de-nice",  
  "typeOfPort": [  
    "marina",  
    "merchandise",  
    "cruise",  
    "ferry",  
    "yatching"  
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
    "https://schema.lab.fiware.org/ld/context",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### SeaportFacilities NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un SeaportFacilities en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
			"type": "point",  
				"coordinates": [43.664810, 7.196545]  
			}  
	},  
	"areaServed": {  
		"type": "Property",  
		"value": "Nice Port"  
	},  
	"dateLastReported": {  
		"type": "DateTime",  
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
		"Object": ["urn:ngsi-ld:BoatAuthorized:MNCA-NCE-BA-001-yatching",  
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
		"Object": ["urn:ngsi-ld:BoatPlaceAvailable:MNCA-BPA-Range-A",  
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
		"Object": ["urn:ngsi-ld:BoatPlacePricing:MNCA-BPP-Range-A",  
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
		"value": "Capitainerie"  
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
		"https://schema.lab.fiware.org/ld/context",  
		"https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
	]  
}  
```  
