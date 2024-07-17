CREATE TABLE IF NOT EXISTS "NLWJourney2".trips (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER
);

CREATE TABLE IF NOT EXISTS "NLWJourney2".emails_to_invite (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    email TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES "NLWJourney2".trips(id)
);

CREATE TABLE IF NOT EXISTS "NLWJourney2".links (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    link TEXT NOT NULL,
    title TEXT NOT NULL,
    FOREIGN KEY (trip_id) REFERENCES "NLWJourney2".trips(id)
);

CREATE TABLE IF NOT EXISTS "NLWJourney2".participants (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    emails_to_invite_id TEXT,
    name TEXT NOT NULL,
    is_confirmed INTEGER,
    FOREIGN KEY (trip_id) REFERENCES "NLWJourney2".trips(id),
    FOREIGN KEY (emails_to_invite_id) REFERENCES "NLWJourney2".emails_to_invite(id)
);

CREATE TABLE IF NOT EXISTS "NLWJourney2".activities (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    title TEXT NOT NULL,
    occurs_at TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES "NLWJourney2".trips(id)
)