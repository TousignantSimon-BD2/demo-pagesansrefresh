-- Drop the database if it exists to ensure a clean slate
DROP DATABASE IF EXISTS voiture_db;

-- Create the database
CREATE DATABASE voiture_db;

-- Use the newly created database
USE voiture_db;

-- Create the voiture table without the 'numero' column
CREATE TABLE voiture (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marque VARCHAR(255) NOT NULL,
    modele VARCHAR(255) NOT NULL,
    UNIQUE (marque, modele)
);

-- Insert sample data
INSERT INTO voiture (marque, modele) VALUES
('Renault', 'Clio'),
('Peugeot', '208'),
('Citroën', 'C3');