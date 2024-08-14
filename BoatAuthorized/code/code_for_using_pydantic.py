from __future__ import annotations

from datetime import date, time
from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class BoatSubTypeEnum(Enum):
    aircraftCarrier = 'aircraftCarrier'
    amphibiousAssaultShip = 'amphibiousAssaultShip'
    anchorHandlingVessel = 'anchorHandlingVessel'
    artisanVessel = 'artisanVessel'
    bac = 'bac'
    barge = 'barge'
    bargeCarrier = 'bargeCarrier'
    bulkCarrier = 'bulkCarrier'
    buoyTenderBoat = 'buoyTenderBoat'
    butaneCarrier = 'butaneCarrier'
    cableLayer = 'cableLayer'
    canoe = 'canoe'
    caravel = 'caravel'
    cargoCarrier = 'cargoCarrier'
    carrack = 'carrack'
    catamaran = 'catamaran'
    chemicalCarrier = 'chemicalCarrier'
    clipper = 'clipper'
    coastalFerry = 'coastalFerry'
    cog = 'cog'
    containerCarrier = 'containerCarrier'
    corvette = 'corvette'
    craneBarge = 'craneBarge'
    crudeCarrier = 'crudeCarrier'
    cruise = 'cruise'
    cruiser = 'cruiser'
    destroyer = 'destroyer'
    dhow = 'dhow'
    divingVessel = 'divingVessel'
    djong = 'djong'
    dredger = 'dredger'
    drifter = 'drifter'
    drillRig = 'drillRig'
    factoryShip = 'factoryShip'
    ferry = 'ferry'
    fireBoat = 'fireBoat'
    fisheriesResearchVessel = 'fisheriesResearchVessel'
    flagshipBoat = 'flagshipBoat'
    floatingProductionStorageUnit = 'floatingProductionStorageUnit'
    floatingStorageUnit = 'floatingStorageUnit'
    fluyt = 'fluyt'
    frigate = 'frigate'
    gabare = 'gabare'
    galleon = 'galleon'
    galley = 'galley'
    gondola = 'gondola'
    harbourFerry = 'harbourFerry'
    helicopterCarrier = 'helicopterCarrier'
    highSpeedVessel = 'highSpeedVessel'
    houseBoat = 'houseBoat'
    hovercraft = 'hovercraft'
    iceBreakerShip = 'iceBreakerShip'
    jetSki = 'jetSki'
    junk = 'junk'
    koch = 'koch'
    lifeBoat = 'lifeBoat'
    lightShip = 'lightShip'
    liner = 'liner'
    lineVessel = 'lineVessel'
    LiquefiedGasCarrier = 'LiquefiedGasCarrier'
    littoralCombatShip = 'littoralCombatShip'
    livestockCarrier = 'livestockCarrier'
    lngCarrier = 'lngCarrier'
    longLiner = 'longLiner'
    lpgCarrier = 'lpgCarrier'
    mineSweeping = 'mineSweeping'
    monoHull = 'monoHull'
    mooringBoat = 'mooringBoat'
    multipurposeVessel = 'multipurposeVessel'
    oceanographicBoat = 'oceanographicBoat'
    other = 'other'
    paddleSteamer = 'paddleSteamer'
    pilotBoat = 'pilotBoat'
    pinisi = 'pinisi'
    pipeLayer = 'pipeLayer'
    productCarrier = 'productCarrier'
    productionPlatform = 'productionPlatform'
    referCarrier = 'referCarrier'
    researchVessel = 'researchVessel'
    roroCarrier = 'roroCarrier'
    sailboat = 'sailboat'
    sailingShip = 'sailingShip'
    salvageOperation = 'salvageOperation'
    seiner = 'seiner'
    speedBoat = 'speedBoat'
    submarineAttack = 'submarineAttack'
    submarineBallisticMissile = 'submarineBallisticMissile'
    submarineCruiseMissile = 'submarineCruiseMissile'
    supplyShip = 'supplyShip'
    tanker = 'tanker'
    timberCarrier = 'timberCarrier'
    trawler = 'trawler'
    trimaran = 'trimaran'
    tugBoat = 'tugBoat'
    viking = 'viking'
    yacht = 'yacht'
    zodiac = 'zodiac'


class BoatTypeEnum(Enum):
    cargo = 'cargo'
    fishing = 'fishing'
    historic = 'historic'
    passenger = 'passenger'
    specialist = 'specialist'
    Tanker = 'Tanker'
    war = 'war'
    yachting = 'yachting'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class DayOfWeek(Enum):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'
    PublicHolidays = 'PublicHolidays'


class DayOfWeek1(Enum):
    https___schema_org_Monday = 'https://schema.org/Monday'
    https___schema_org_Tuesday = 'https://schema.org/Tuesday'
    https___schema_org_Wednesday = 'https://schema.org/Wednesday'
    https___schema_org_Thursday = 'https://schema.org/Thursday'
    https___schema_org_Friday = 'https://schema.org/Friday'
    https___schema_org_Saturday = 'https://schema.org/Saturday'
    https___schema_org_Sunday = 'https://schema.org/Sunday'
    https___schema_org_PublicHolidays = 'https://schema.org/PublicHolidays'


class OpeningHoursSpecificationItem(BaseModel):
    closes: Optional[time] = Field(
        None,
        description=' \\tThe closing hour of the place or service on the given day(s) of the week',
    )
    dayOfWeek: Optional[Union[DayOfWeek, DayOfWeek1]] = Field(
        None,
        description='The day of the week for which these opening hours are valid. URLs from GoodRelations (http://purl.org/goodrelations/v1) are used (for Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday plus a special entry for PublicHolidays)',
    )
    opens: Optional[time] = Field(
        None,
        description='The opening hour of the place or service on the given day(s) of the week',
    )
    validFrom: Optional[Union[date, AwareDatetime]] = Field(
        None,
        description='The date when the item becomes valid. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format',
    )
    validThrough: Optional[Union[date, AwareDatetime]] = Field(
        None,
        description='The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours. A date value in the form CCYY-MM-DD or a combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] in ISO 8601 date format',
    )


class Type6(Enum):
    BoatAuthorized = 'BoatAuthorized'


class BoatAuthorized(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    boatSubType: Optional[List[BoatSubTypeEnum]] = Field(
        None,
        description="Sub Type for a boatType. A combination of the elements. Enum:'aircraftCarrier, amphibiousAssaultShip, anchorHandlingVessel, artisanVessel, bac, barge, bargeCarrier, bulkCarrier, buoyTenderBoat, butaneCarrier, cableLayer, canoe, caravel, cargoCarrier, carrack, catamaran, chemicalCarrier, clipper, coastalFerry, cog, containerCarrier, corvette, craneBarge, crudeCarrier, cruise, cruiser, destroyer, dhow, divingVessel, djong, dredger, drifter, drillRig, factoryShip, ferry, fireBoat, fisheriesResearchVessel, flagshipBoat, floatingProductionStorageUnit, floatingStorageUnit, fluyt, frigate, gabare, galleon, galley, gondola, harbourFerry, helicopterCarrier, highSpeedVessel, houseBoat, hovercraft, iceBreakerShip, jetSki, junk, koch, lifeBoat, lightShip, liner, lineVessel, LiquefiedGasCarrier, littoralCombatShip, livestockCarrier, lngCarrier, longLiner, lpgCarrier, mineSweeping, monoHull, mooringBoat, multipurposeVessel, oceanographicBoat, other, paddleSteamer, pilotBoat, pinisi, pipeLayer, productCarrier, productionPlatform, referCarrier, researchVessel, roroCarrier, sailboat, sailingShip, salvageOperation, seiner, speedBoat, submarineAttack, submarineBallisticMissile, submarineCruiseMissile, supplyShip, tanker, timberCarrier, trawler, trimaran, tugBoat, viking, yacht, zodiac'",
    )
    boatType: Optional[List[BoatTypeEnum]] = Field(
        None,
        description="A unique value of the list. Enum:'cargo, fishing, historic, passenger, specialist, Tanker, war, yachting'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastReported: Optional[AwareDatetime] = Field(
        None, description='Last time data were gathered'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    maxDraft: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter',
    )
    maxLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter',
    )
    maxTonnage: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric',
    )
    maxWidth: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter',
    )
    minLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    openingHoursSpecification: Optional[List[OpeningHoursSpecificationItem]] = Field(
        None,
        description='A structured value providing information about the opening hours of a place or a certain service inside a place',
        min_length=1,
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refPointOfInterest: Optional[AnyUrl] = Field(
        None, description='Point of Interest that the element has relation to'
    )
    refSeaPort: Optional[AnyUrl] = Field(None, description='Port that belongs to')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type6] = Field(
        None, description='It has to be BoatAuthorized. NGSI Entity type'
    )
