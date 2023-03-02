/* (Beta) Export of data model BoatAuthorized of the subject dataModel.Ports for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE BoatAuthorized_type AS ENUM ('BoatAuthorized');
CREATE TABLE BoatAuthorized (address json, alternateName text, areaServed text, boatSubType json, boatType json, dataProvider text, dateCreated timestamp, dateLastReported timestamp, dateModified timestamp, description text, id text, location json, maxDraft text, maxLength text, maxTonnage text, maxWidth text, minLength text, name text, openingHoursSpecification json, owner json, refPointOfInterest text, refSeaPort text, seeAlso json, source text, type BoatAuthorized_type);