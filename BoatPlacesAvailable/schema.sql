/* (Beta) Export of data model BoatPlacesAvailable of the subject dataModel.Ports for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE BoatPlacesAvailable_type AS ENUM ('BoatPlacesAvailable');
CREATE TABLE BoatPlacesAvailable (address JSON, alternateName TEXT, areaServed TEXT, availableSpotNumber NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, dateObserved TIMESTAMP, description TEXT, id TEXT PRIMARY KEY, location JSON, maxDraft NUMERIC, maxLength NUMERIC, maxWidth NUMERIC, minLength NUMERIC, name TEXT, owner JSON, refPointOfInterest TEXT, refSeaPort TEXT, seeAlso JSON, source TEXT, spotCategoryRange JSON, totalCapacitySpotNumber NUMERIC, type BoatPlacesAvailable_type);