Entidad: SeaportFacilities  
==========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **El modelo de datos está destinado a proporcionar información sobre los puertos que pueden acoger embarcaciones de recreo, comercio o transporte de pasajeros. Permite representar los parámetros de cada puerto, su ubicación, sus capacidades de amarre y los servicios gratuitos o de pago asociados a él prestados directamente por el puerto o por los profesionales que trabajan en él o en sus proximidades.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateLastReported`: Una marca de tiempo que denota la última vez que un flujo comunicó datos con éxito. La fecha y la hora de este repositorio en formato ISO8601 UTC  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `openingHoursSpecification`: Un valor estructurado que proporciona información sobre el horario de apertura de un lugar o de un determinado servicio dentro de un lugar  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice`: Referencia a la Entidad Principal [Dispositivo](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) si se utiliza como segundo enlace  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tiene que ser SeaPort    
Propiedades requeridas  
- `dateLastReported`  - `id`  - `location`  - `type`  - `typeOfPort`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SeaportFacilities:    
  description: 'The Data Model is intended to provide information about ports that can accommodate pleasure craft, commerce or passenger  transport. It permit to represent the parameters of each port, its location, its mooring capacities and the free or paid services associated with it provided directly by the port or by professionals working on or near the port.'    
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
        anyOf: *seaportfacilities_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'It has to be SeaPort'    
      enum:    
        - SeaPort    
      type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - typeOfPort    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### SeaportFacilities NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de SeaportFacilities en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### SeaportFacilities NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de SeaportFacilities en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### SeaportFacilities NGSI-LD key-values Ejemplo  
Este es un ejemplo de SeaportFacilities en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
      "coordinates": [  
        43.66481,  
        7.196545  
      ]  
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
    "Object": [  
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
    "type": "Relationship",  
    "Object": [  
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
    "type": "Relationship",  
    "Object": [  
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
    "type": "Property",  
    "value": [  
      "Departement_06",  
      "CCI06",  
      "MNCA",  
      "Ville_de_Nice"  
    ]  
  },  
  "contractingAuthority": {  
    "type": "Property",  
    "value": "CCI"  
  },  
  "contractingCompagny": {  
    "type": "Property",  
    "value": "R\u00e9gie Autonome des ports"  
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
    "value": [  
      "marina",  
      "merchandise",  
      "cruise",  
      "ferry",  
      "yatching"  
    ]  
  },  
  "authorizedPropulsions": {  
    "type": "Property",  
    "value": [  
      "motor",  
      "electric",  
      "lng"  
    ]  
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
    "value": [  
      "harborOffice",  
      "weather",  
      "customsServices",  
      "porters"  
    ]  
  },  
  "boatSupplyingServices": {  
    "type": "Property",  
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
    "type": "Property",  
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
    "type": "Property",  
    "value": [  
      "groceryStores",  
      "presses",  
      "exchangeOffice",  
      "touristicExcursions"  
    ]  
  },  
  "rentalSaleServices": {  
    "type": "Property",  
    "value": [  
      "boatRental",  
      "boatSale",  
      "carRental"  
    ]  
  },  
  "transportServices": {  
    "type": "Property",  
    "value": [  
      "parking",  
      "shuttlesToAirport",  
      "taxis"  
    ]  
  },  
  "routeType": {  
    "type": "Property",  
    "value": [  
      "tram",  
      "metro",  
      "train",  
      "bus",  
      "ferry"  
    ]  
  },  
  "electricTransport": {  
    "type": "Property",  
    "value": [  
      "electricBycicle",  
      "electricMotorBike"  
    ]  
  },  
  "paymentAccepted": {  
    "type": "Property",  
    "value": [  
      "Cash",  
      "CreditCard"  
    ]  
  },  
  "currencyAccepted": {  
    "type": "Property",  
    "value": [  
      "EUR",  
      "USD"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### SeaportFacilities NGSI-LD normalizado Ejemplo  
Este es un ejemplo de SeaportFacilities en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud