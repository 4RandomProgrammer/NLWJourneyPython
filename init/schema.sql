CREATE TABLE IF NOT EXISTS "NLWJourney".trips (
    id TEXT PRIMARY KEY,
    destination TEXT NOT NULL,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    owner_name TEXT NOT NULL,
    owner_email TEXT NOT NULL,
    status INTEGER
);

CREATE TABLE IF NOT EXISTS "NLWJourney".emails_to_invite (
    id TEXT PRIMARY KEY,
    trip_id TEXT REFERENCES trips(id),
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "NLWJourney".links (
    id TEXT PRIMARY KEY,
    trip_id TEXT REFERENCES trips(id),
    link TEXT NOT NULL,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS "NLWJourney".participants (
    id TEXT PRIMARY KEY,
    trip_id TEXT NOT NULL,
    emails_to_invite_id TEXT NOT NULL,
    name TEXT NOT NULL,
    is_confirmed INTEGER,
    FOREIGN KEY (trip_id) REFERENCES "NLWJourney".trips(id),
    FOREIGN KEY (emails_to_invite_id) REFERENCES "NLWJourney".emails_to_invite(id)
);

CREATE TABLE IF NOT EXISTS "NLWJourney".activities (
    id TEXT PRIMARY KEY,
    trip_id TEXT,
    title TEXT NOT NULL,
    occurs_at TIMESTAMP,
    FOREIGN KEY (trip_id) REFERENCES "NLWJourney".trips(id)
);