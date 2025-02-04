-- when creating tables in terminal, start(maybe) and always send with ;  
DROP TABLE donors;
DROP TABLE donations;
DROP TABLE campaigns;


CREATE TABLE IF NOT EXISTS donors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    state TEXT
);

CREATE TABLE IF NOT EXISTS campaigns(
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS donations(
    id INTEGER PRIMARY KEY,
    amount INTEGER,
    donor_id INTEGER,
    campaign_id INTEGER,
    FOREIGN KEY (donor_id) REFERENCES donors(id),
    FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
    
);


INSERT INTO donors(name, state)
VALUES("Mary Beth", "CA");
INSERT INTO donors(name, state)
VALUES("Polly Ann", "FL");


INSERT INTO campaigns(name)
VALUES("Frog");
INSERT INTO campaigns(name)
VALUES("Leopard");

INSERT INTO donations(amount, donor_id, campaign_id)
VALUES(200, 1, 1);
INSERT INTO donations(amount, donor_id, campaign_id)
VALUES(500, 2, 2);
INSERT INTO donations(amount, donor_id, campaign_id)
VALUES(600, 1, 1);
-- -- here is where we'll create the classes on sql backend

-- DROP TABLE students;
-- DROP TABLE teachers;
-- DROP TABLE schedules;

-- CREATE TABLE IF NOT EXISTS students(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     emergency_phone INTEGER
-- );

-- CREATE TABLE IF NOT EXISTS teachers(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     email INTEGER,
--     specialty TEXT
-- );
-- --this for donation, foreign keys will be campaign_id and donor_id
-- CREATE TABLE IF NOT EXISTS schedules(
--     id INTEGER PRIMARY KEY,
--     classname TEXT,
--     period INTEGER,
--     grade FLOAT,
--     student_id INTEGER,
--     teacher_id INTEGER,
--     FOREIGN KEY (student_id) REFERENCES students(id),
--     FOREIGN KEY (teacher_id) REFERENCES teachers(id)
-- );