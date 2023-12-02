-- Connect to the database
CREATE DATABASE IF NOT EXISTS mus_league;
USE mus_league;

-- Create the season_0 table
CREATE TABLE IF NOT EXISTS season_0 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    score FLOAT,
    wins INT,
    losses INT,
    total INT
);

-- Create the games_history_0 table
CREATE TABLE IF NOT EXISTS games_history_0 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    winner1 VARCHAR(255),
    winner1_percentage FLOAT,
    winner1_old_elo FLOAT,
    winner1_new_elo FLOAT,
    winner2 VARCHAR(255),
    winner2_percentage FLOAT,
    winner2_old_elo FLOAT,
    winner2_new_elo FLOAT,
    loser1 VARCHAR(255),
    loser1_percentage FLOAT,
    loser1_old_elo FLOAT,
    loser1_new_elo FLOAT,
    loser2 VARCHAR(255),
    loser2_percentage FLOAT,
    loser2_old_elo FLOAT,
    loser2_new_elo FLOAT
);

-- Insert data into the season_0 table
-- You can use a script or manually insert data into this table

-- Commit and close the connection
COMMIT;