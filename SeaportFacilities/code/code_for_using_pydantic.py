from __future__ import annotations

from datetime import date, time
from enum import Enum
from typing import Any, Dict, List, Optional, Union

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


class AuthorizedPropulsionEnum(Enum):
    motor = 'motor'
    sail = 'sail'
    electric = 'electric'
    oar = 'oar'
    nuclear = 'nuclear'
    lng = 'lng'
    lpg = 'lpg'
    other = 'other'


class BoatSupplyingService(Enum):
    boatConveying = 'boatConveying'
    boatTransfer = 'boatTransfer'
    drinkingWaterTankerTruck = 'drinkingWaterTankerTruck'
    dryFairing = 'dryFairing'
    expertise = 'expertise'
    fuelStation = 'fuelStation'
    fuelTankerTruck = 'fuelTankerTruck'
    gangways = 'gangways'
    guarding = 'guarding'
    liftingCranes = 'liftingCranes'
    provisioning = 'provisioning'
    repair = 'repair'
    towing = 'towing'
    waterFairing = 'waterFairing'
    wasteWaterPumping = 'wasteWaterPumping'
    other = 'other'


class CurrencyAcceptedEnum(Enum):
    AUD = 'AUD'
    GBP = 'GBP'
    EUR = 'EUR'
    JPY = 'JPY'
    CHF = 'CHF'
    USD = 'USD'
    AFN = 'AFN'
    ALL = 'ALL'
    DZD = 'DZD'
    AOA = 'AOA'
    ARS = 'ARS'
    AMD = 'AMD'
    AWG = 'AWG'
    AUD_1 = 'AUD'
    ATS__EURO_ = 'ATS (EURO)'
    BEF__EURO_ = 'BEF (EURO)'
    AZN = 'AZN'
    BSD = 'BSD'
    BHD = 'BHD'
    BDT = 'BDT'
    BBD = 'BBD'
    BYR = 'BYR'
    BZD = 'BZD'
    BMD = 'BMD'
    BTN = 'BTN'
    BOB = 'BOB'
    BAM = 'BAM'
    BWP = 'BWP'
    BRL = 'BRL'
    GBP_1 = 'GBP'
    BND = 'BND'
    BGN = 'BGN'
    BIF = 'BIF'
    XOF = 'XOF'
    XAF = 'XAF'
    XPF = 'XPF'
    KHR = 'KHR'
    CAD = 'CAD'
    CVE = 'CVE'
    KYD = 'KYD'
    CLP = 'CLP'
    CNY = 'CNY'
    COP = 'COP'
    KMF = 'KMF'
    CDF = 'CDF'
    CRC = 'CRC'
    HRK = 'HRK'
    CUC = 'CUC'
    CUP = 'CUP'
    CYP__EURO_ = 'CYP (EURO)'
    CZK = 'CZK'
    DKK = 'DKK'
    DJF = 'DJF'
    DOP = 'DOP'
    XCD = 'XCD'
    EGP = 'EGP'
    SVC = 'SVC'
    EEK__EURO_ = 'EEK (EURO)'
    ETB = 'ETB'
    EUR_1 = 'EUR'
    FKP = 'FKP'
    FIM__EURO_ = 'FIM (EURO)'
    FJD = 'FJD'
    GMD = 'GMD'
    GEL = 'GEL'
    DMK__EURO_ = 'DMK (EURO)'
    GHS = 'GHS'
    GIP = 'GIP'
    GRD__EURO_ = 'GRD (EURO)'
    GTQ = 'GTQ'
    GNF = 'GNF'
    GYD = 'GYD'
    HTG = 'HTG'
    HNL = 'HNL'
    HKD = 'HKD'
    HUF = 'HUF'
    ISK = 'ISK'
    INR = 'INR'
    IDR = 'IDR'
    IRR = 'IRR'
    IQD = 'IQD'
    IED__EURO_ = 'IED (EURO)'
    ILS = 'ILS'
    ITL__EURO_ = 'ITL (EURO)'
    JMD = 'JMD'
    JPY_1 = 'JPY'
    JOD = 'JOD'
    KZT = 'KZT'
    KES = 'KES'
    KWD = 'KWD'
    KGS = 'KGS'
    LAK = 'LAK'
    LVL__EURO_ = 'LVL (EURO)'
    LBP = 'LBP'
    LSL = 'LSL'
    LRD = 'LRD'
    LYD = 'LYD'
    LTL__EURO_ = 'LTL (EURO)'
    LUF__EURO_ = 'LUF (EURO)'
    MOP = 'MOP'
    MKD = 'MKD'
    MGA = 'MGA'
    MWK = 'MWK'
    MYR = 'MYR'
    MVR = 'MVR'
    MTL__EURO_ = 'MTL (EURO)'
    MRO = 'MRO'
    MUR = 'MUR'
    MXN = 'MXN'
    MDL = 'MDL'
    MNT = 'MNT'
    MAD = 'MAD'
    MZN = 'MZN'
    MMK = 'MMK'
    ANG = 'ANG'
    NAD = 'NAD'
    NPR = 'NPR'
    NLG__EURO_ = 'NLG (EURO)'
    NZD = 'NZD'
    NIO = 'NIO'
    NGN = 'NGN'
    KPW = 'KPW'
    NOK = 'NOK'
    OMR = 'OMR'
    PKR = 'PKR'
    PAB = 'PAB'
    PGK = 'PGK'
    PYG = 'PYG'
    PEN = 'PEN'
    PHP = 'PHP'
    PLN = 'PLN'
    PTE__EURO_ = 'PTE (EURO)'
    QAR = 'QAR'
    RON = 'RON'
    RUB = 'RUB'
    RWF = 'RWF'
    WST = 'WST'
    STD = 'STD'
    SAR = 'SAR'
    RSD = 'RSD'
    SCR = 'SCR'
    SLL = 'SLL'
    SGD = 'SGD'
    SKK__EURO_ = 'SKK (EURO)'
    SIT__EURO_ = 'SIT (EURO)'
    SBD = 'SBD'
    SOS = 'SOS'
    ZAR = 'ZAR'
    KRW = 'KRW'
    ESP__EURO_ = 'ESP (EURO)'
    LKR = 'LKR'
    SHP = 'SHP'
    SDG = 'SDG'
    SRD = 'SRD'
    SZL = 'SZL'
    SEK = 'SEK'
    CHF_1 = 'CHF'
    SYP = 'SYP'
    TWD = 'TWD'
    TZS = 'TZS'
    THB = 'THB'
    TOP = 'TOP'
    TTD = 'TTD'
    TND = 'TND'
    TRY = 'TRY'
    TMM = 'TMM'
    USD_1 = 'USD'
    UGX = 'UGX'
    UAH = 'UAH'
    UYU = 'UYU'
    AED = 'AED'
    VUV = 'VUV'
    VEB = 'VEB'
    VND = 'VND'
    YER = 'YER'
    ZMK = 'ZMK'
    ZWD = 'ZWD'


class ElectricTransportEnum(Enum):
    electricBycicle = 'electricBycicle'
    electricCar = 'electricCar'
    electricMotorBike = 'electricMotorBike'
    electricScooter = 'electricScooter'


class Facility(Enum):
    container = 'container'
    dustbins = 'dustbins'
    dumpsters = 'dumpsters'
    electricTerminal = 'electricTerminal'
    indoorRoomReservation_ = 'indoorRoomReservation '
    laundry = 'laundry'
    selectiveSortingWaste = 'selectiveSortingWaste'
    showers = 'showers'
    telephone = 'telephone'
    toilets = 'toilets'
    waterTerminal = 'waterTerminal'
    wifi = 'wifi'
    other = 'other'


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


class NearbyService(Enum):
    bar = 'bar'
    cityTour = 'cityTour'
    fittingsStores = 'fittingsStores'
    groceryStores = 'groceryStores'
    exchangeOffice = 'exchangeOffice'
    medicalOffice = 'medicalOffice'
    pharmacy = 'pharmacy'
    presses = 'presses'
    restaurants = 'restaurants'
    seaExcursions = 'seaExcursions'
    shops = 'shops'
    touristicExcursions = 'touristicExcursions'
    touristOffice = 'touristOffice'
    travelAgency = 'travelAgency'
    others = 'others'


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


class PaymentAcceptedEnum(Enum):
    Cash = 'Cash'
    CreditCard = 'CreditCard'
    CryptoCurrency = 'CryptoCurrency'
    other = 'other'


class PortServicesProvidedEnum(Enum):
    harborOffice = 'harborOffice'
    weather = 'weather'
    customsServices = 'customsServices'
    porters = 'porters'
    boatRingRental = 'boatRingRental'
    mooringAssistance = 'mooringAssistance'
    handlingAssistance = 'handlingAssistance'
    publicWifi = 'publicWifi'
    privateWifi = 'privateWifi'
    other = 'other'


class RentalSaleService(Enum):
    bikeRental = 'bikeRental'
    boatRental = 'boatRental'
    boatSale = 'boatSale'
    Caddie = 'Caddie'
    carRental = 'carRental'
    jetSkiRental = 'jetSkiRental'
    jetSkiSale = 'jetSkiSale'
    luxuryCarRental = 'luxuryCarRental'
    palletTransport = 'palletTransport'
    scooterRental = 'scooterRental'
    vanRental = 'vanRental'
    Others = 'Others'


class RouteTypeEnum(Enum):
    bus = 'bus'
    cableCar = 'cableCar'
    cableTram = 'cableTram'
    ferry = 'ferry'
    funicular = 'funicular'
    metro = 'metro'
    monorail = 'monorail'
    train = 'train'
    tram = 'tram'
    trolleybus = 'trolleybus'


class TransportService(Enum):
    heliport = 'heliport'
    internalShuttle = 'internalShuttle'
    parking = 'parking'
    shuttlesToAirport = 'shuttlesToAirport'
    shuttlesToRailway = 'shuttlesToRailway'
    taxis = 'taxis'
    Others = 'Others'


class Type6(Enum):
    SeaPortFacilities = 'SeaPortFacilities'


class TypeOfPortEnum(Enum):
    cruise = 'cruise'
    ferry = 'ferry'
    fishing = 'fishing'
    marina = 'marina'
    merchandise = 'merchandise'
    military = 'military'
    passengers = 'passengers'
    river = 'river'
    yachting = 'yachting'
    other = 'other'


class SeaportFacilities(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    authorizedPropulsion: Optional[List[AuthorizedPropulsionEnum]] = Field(
        None,
        description='A Type of propulsion authorized to enter in the harbor. A combination of motor, sail, electric, oar, nuclear, lng, lpg, other',
    )
    boatSupplyingServices: Optional[List[BoatSupplyingService]] = Field(
        None,
        description='Description of the complementary supplying services for the boat offered by professionals working on or near the harbor. A combination of guarding, fuelStation, fuelTankerTruck , drinkingWaterTankerTruck, provisioning, dryFairing, waterFairing, repair, expertise, gangways, liftingCranes, towing, wasteWaterPumping, boatConveying, boatTransfer, other',
    )
    contactPoint: Optional[Dict[str, Any]] = Field(
        None, description='https://schema.org/ContactPoint'
    )
    contractingAuthority: Optional[str] = Field(
        None, description='Name of the contracting authority'
    )
    contractingCompany: Optional[str] = Field(
        None,
        description='The Contracting Company responsible of the management of the port',
    )
    currencyAccepted: Optional[List[CurrencyAcceptedEnum]] = Field(
        None,
        description='A combination of a list of active codes defined in the model [Norme ISO 4217](http://en.wikipedia.org/wiki/ISO_4217), [Crypto Currencies](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) , [Exchange Trading System](https://en.wikipedia.org/wiki/Local_exchange_trading_system',
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
        None,
        description='A timestamp which denotes the last time when a flow successfully reported data. The date and time of this Repository in ISO8601 UTCformat',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    electricTransport: Optional[List[ElectricTransportEnum]] = Field(
        None,
        description=' List of the different types of electric transport proposed by the city. A combination of electricCar, electricBycicle, electricMotorBike, electricScooter ',
    )
    endDate: Optional[AwareDatetime] = Field(
        None, description='The end date and time of the item (in ISO 8601 date format).'
    )
    facilities: Optional[List[Facility]] = Field(
        None,
        description='Description of the proposed facilities on the harbor. A combination of : toilets, showers, laundry, telephone, dustbins, dumpsters, container, selectiveSortingWaste, electricTerminal, waterTerminal, indoorRoomReservation, wifi, other',
    )
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
        description='A Maximum draft allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter',
    )
    maxLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description='A Maximum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter',
    )
    maxTonnage: Optional[confloat(ge=0.0)] = Field(
        None,
        description='Maximum tonnage authorized to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **TNE** represents Tonne Metric',
    )
    maxWidth: Optional[confloat(ge=0.0)] = Field(
        None,
        description='A Maximum width allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) . For instance, **MTR** represents Meter',
    )
    minLength: Optional[confloat(ge=0.0)] = Field(
        None,
        description='A Minimum length allowed to access the harbor. The unit code (text) is given using the [UN/CEFACT Common Codes](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). For instance, **MTR** represents Meter',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nearbyServices: Optional[List[NearbyService]] = Field(
        None,
        description='Description of the additional services on the geographical area on or near the harbor. A combination of :touristOffice, fittingsStores, travelAgency, exchangeOffice, medicalOffice, pharmacy, groceryStores, restaurants, presses, bar, shops, seaExcursions, cityTour, touristicExcursions, others',
    )
    numberOfPlace: Optional[confloat(ge=0.0)] = Field(
        None, description='Total number of place in the harbor'
    )
    openingHours: Optional[str] = Field(
        None,
        description="The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'. Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su. Times are specified using 24:00 format. For example, 3pm is specified as 15:00, 10am as 10:00. Here is an example: <time itemprop='openingHours' datetime='Tu,Th 16:00-20:00'>Tuesdays and Thursdays 4-8pm</time>. If a business is open 7 days a week, then it can be specified as <time itemprop='openingHours' datetime='Mo-Su'>Monday through Sunday, all day</time>",
    )
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
    paymentAccepted: Optional[List[PaymentAcceptedEnum]] = Field(
        None,
        description='Accepted payment. A combination of a list of active codes defined in the model : Cash, CreditCard, CryptoCurrency, other',
    )
    portServicesProvided: Optional[List[PortServicesProvidedEnum]] = Field(
        None,
        description='Description of the services provided directly by the harbor. A combination of : harborOffice, weather, customsServices, porters, boatRingRental, mooringAssistance, handlingAssistance, publicWifi, privateWifi, other',
    )
    refBoatAuthorized: Optional[
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
        description='Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatAuthorized/doc/spec.md)',
    )
    refBoatPlaceAvailable: Optional[
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
        description='Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlaceAvailable/doc/spec.md)',
    )
    refBoatPlacePricing: Optional[
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
        description='Reference to a list of [Entity](https://github.com/smart-data-models/dataModel.Port/blob/master/BoatPlacePricing/doc/spec.md)',
    )
    refDevice: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to the Main Entity [Device](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/doc/spec.md) if used as second link',
    )
    refPointOfInterest: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='Reference to a [PointOfInterest](https://github.com/smart-data-models/dataModel.PointOfInterest/blob/master/PointOfInterest/doc/spec.md) linked with the Repository',
    )
    rentalSaleServices: Optional[List[RentalSaleService]] = Field(
        None,
        description='ADescription of services provided by professional sales or rental agencies on the geographical area on or near the harbor. A combination of : boatRental, boatSale, jetSkiRental, jetSkiSale, carRental, luxuryCarRental, vanRental, bikeRental, scooterRental, Caddie, palletTransport, other',
    )
    routeType: Optional[List[RouteTypeEnum]] = Field(
        None,
        description="List of the different types of urban transport Mode (Metro, Bus, Tram, ...) from the urban transport Mode GFTS standard [STOP](https://developers.google.com/transit/gtfs/reference/#stopstxt). A combination of values composed only of the attribute 'description' tram(0), metro(1), train(2), bus(3), ferry(4), cableTram(5), cableCar(6), funicular(7), trolleybus(11), monorail(12)",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startDate: Optional[AwareDatetime] = Field(
        None,
        description='The start date and time of the item (in ISO 8601 date format).',
    )
    transportServices: Optional[List[TransportService]] = Field(
        None,
        description='Description of the services provided for dedicated transport and shuttle services. A combination of : parking, shuttlesToAirport, shuttlesToRailway, internalShuttles, taxis, heliport, other',
    )
    type: Optional[Type6] = Field(None, description='It has to be SeaPortFacilities')
    typeOfPort: Optional[List[TypeOfPortEnum]] = Field(
        None,
        description='A Type of harbor. A combination of : marina, merchandise, cruise, ferry, passengers, yachting, fishing, military, river, other',
    )
    webSite: Optional[str] = Field(
        None,
        description='Link to the official website of the harbor for more information',
    )
