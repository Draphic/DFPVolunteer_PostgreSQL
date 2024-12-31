-- Create the 'volunteering' database
CREATE DATABASE volunteering;

-- Connect to the 'volunteering' database
\c volunteering

-- Create the 'volunteering' schema
CREATE SCHEMA volunteering;

-- Create the 'volunteers' table
CREATE TABLE volunteering.volunteers (
    volunteer_id BIGSERIAL PRIMARY KEY,
    sign_up_time TIMESTAMP WITHOUT TIME ZONE,
    first_name CHARACTER VARYING(50),
    last_name CHARACTER VARYING(50),
    email CHARACTER VARYING(256) CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    phone_number NUMERIC(10) CHECK (phone_number::text ~* '^\d{10}$'),
    organization CHARACTER VARYING(256)
);

-- Create the 'sign_in_responses' table
CREATE TABLE volunteering.sign_in_responses (
    session_id BIGSERIAL PRIMARY KEY,
    sign_in_date DATE,
    volunteer_id BIGINT,
    sign_in TIMESTAMP WITHOUT TIME ZONE,
    sign_out TIMESTAMP WITHOUT TIME ZONE
);

-- Add the foreign key constraint with ON UPDATE CASCADE
ALTER TABLE volunteering.sign_in_responses
ADD CONSTRAINT fk_volunteer
FOREIGN KEY (volunteer_id)
REFERENCES volunteering.volunteers (volunteer_id)
ON UPDATE CASCADE;
