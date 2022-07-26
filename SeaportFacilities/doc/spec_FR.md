[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SeaportFacilities  
==========================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le modèle de données est destiné à fournir des informations sur les ports pouvant accueillir des bateaux de plaisance, de commerce ou de transport de passagers. Il permet de représenter les paramètres de chaque port, sa localisation, ses capacités d'amarrage et les services gratuits ou payants qui lui sont associés, fournis directement par le port ou par des professionnels travaillant sur ou à proximité du port**.  
version : 0.0.1  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateLastReported`: Un horodatage qui indique la dernière fois qu'un flux a rapporté des données avec succès. La date et l'heure de ce référentiel en format ISO8601 UTC.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `openingHoursSpecification`: Une valeur structurée fournissant des informations sur les heures d'ouverture d'un lieu ou d'un certain service à l'intérieur d'un lieu.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refDevice`: Référence à l'entité principale [dispositif] (https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) si elle est utilisée comme deuxième lien.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Ce doit être SeaPortFacilities.    
Propriétés requises  
- `dateLastReported`  - `id`  - `location`  - `type`  - `typeOfPort`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
      description: 'A timestamp which denotes the last time when a flow successfully reported data. The date and time of this Repository in ISO8601 UTCformat'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
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
        anyOf: *seaportfacilities_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
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
      description: 'It has to be SeaPortFacilities'    
      enum:    
        - SeaPortFacilities    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - location    
    - dateLastReported    
    - typeOfPort    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Ports/blob/master/SeaportFacilities/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModels.Ports/SeaPort/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### SeaportFacilities NGSI-v2 key-values Exemple  
Voici un exemple d'une SeaportFacilities au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### SeaportFacilities NGSI-v2 normalisé Exemple  
Voici un exemple de SeaportFacilities au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### SeaportFacilities Valeurs-clés NGSI-LD Exemple  
Voici un exemple de SeaportFacilities au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
    "type": "SeaPort",  
    "alternateName": {  
        "type": "Property",  
        "value": "Riviera Port - Main harbor - Commerce & Passengers"  
    },  
    "areaServed": {  
        "type": "Property",  
        "value": "Nice Port"  
    },  
    "authorizedPropulsions": {  
        "type": "Property",  
        "value": [  
            "motor",  
            "electric",  
            "lng"  
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
    "contactPoint": {  
        "type": "Property",  
        "value": "Capitainerie"  
    },  
    "contractingAuthority": {  
        "type": "Property",  
        "value": "CCI"  
    },  
    "contractingCompagny": {  
        "type": "Property",  
        "value": "R\u00e9gie Autonome des ports"  
    },  
    "currencyAccepted": {  
        "type": "Property",  
        "value": [  
            "EUR",  
            "USD"  
        ]  
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
    "description": {  
        "type": "Property",  
        "value": "Harbor Description and services provided"  
    },  
    "electricTransport": {  
        "type": "Property",  
        "value": [  
            "electricBycicle",  
            "electricMotorBike"  
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
    "maxDraft": {  
        "type": "Property",  
        "value": 9.65  
    },  
    "maxLength": {  
        "type": "Property",  
        "value": 180  
    },  
    "maxTonnage": {  
        "type": "Property",  
        "value": 30000  
    },  
    "maxWidth": {  
        "type": "Property",  
        "value": 25  
    },  
    "minLength": {  
        "type": "Property",  
        "value": 6  
    },  
    "name": {  
        "type": "Property",  
        "value": "Riviera-Port-NCE-SP-001"  
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
    "numberOfPlace": {  
        "type": "Property",  
        "value": 120  
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
    "paymentAccepted": {  
        "type": "Property",  
        "value": [  
            "Cash",  
            "CreditCard"  
        ]  
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
    "rentalSaleServices": {  
        "type": "Property",  
        "value": [  
            "boatRental",  
            "boatSale",  
            "carRental"  
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
    "seeAlso": {  
        "type": "Property",  
        "value": "https://ccinicecotedazur/docs/port-nice_z-card_2015"  
    },  
    "transportServices": {  
        "type": "Property",  
        "value": [  
            "parking",  
            "shuttlesToAirport",  
            "taxis"  
        ]  
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
    "webSite": {  
        "type": "Property",  
        "value": "https://riviera-ports.com/ports/port-de-nice"  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Ports/master/context.jsonld"  
    ]  
}  
```  
#### SeaportFacilities NGSI-LD normalisé Exemple  
Voici un exemple de SeaportFacilities au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
    "id": "urn:ngsi-ld:SeaPort:SeaPort:MNCA-SP-001",  
    "type": "SeaPort",  
    "alternateName": "Riviera Port - Main harbor - Commerce & Passengers",  
    "areaServed": "Nice Port",  
    "authorizedPropulsion": [  
        "motor",  
        "electric",  
        "lng"  
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
    "contactPoint": "Capitainerie",  
    "contractingAuthority": "CCI",  
    "contractingCompany": "R\u00e9gie Autonome des ports",  
    "currencyAccepted": [  
        "EUR",  
        "USD"  
    ],  
    "dateLastReported": "2020-03-17T08:45:00Z",  
    "description": "Harbor Description and services provided",  
    "electricTransport": [  
        "electricBycicle",  
        "electricMotorBike"  
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
    "location": {  
        "type": "Point",  
        "coordinates": [  
            43.66481,  
            7.196545  
        ]  
    },  
    "maxDraft": 9.65,  
    "maxLength": 180,  
    "maxTonnage": 30000,  
    "maxWidth": 25,  
    "minLength": 6,  
    "name": "Riviera-Port-NCE-SP-001",  
    "nearbyServices": [  
        "groceryStores",  
        "presses",  
        "exchangeOffice",  
        "touristicExcursions"  
    ],  
    "numberOfPlace": 120,  
    "owner": [  
        "Departement_06",  
        "CCI06",  
        "MNCA",  
        "Ville_de_Nice"  
    ],  
    "paymentAccepted": [  
        "Cash",  
        "CreditCard"  
    ],  
    "portServicesProvided": [  
        "harborOffice",  
        "weather",  
        "customsServices",  
        "porters"  
    ],  
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
    "rentalSaleServices": [  
        "boatRental",  
        "boatSale",  
        "carRental"  
    ],  
    "routeType": [  
        "tram",  
        "metro",  
        "train",  
        "bus",  
        "ferry"  
    ],  
    "seeAlso": "https://ccinicecotedazur/docs/port-nice_z-card_2015",  
    "transportServices": [  
        "parking",  
        "shuttlesToAirport",  
        "taxis"  
    ],  
    "typeOfPort": [  
        "marina",  
        "merchandise",  
        "cruise",  
        "ferry",  
        "yatching"  
    ],  
    "webSite": "https://riviera-ports.com/ports/port-de-nice",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
