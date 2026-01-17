-- Script that creates the table with default id and must be unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT '1' UNIQUE,
    name VARCHAR(256)
);