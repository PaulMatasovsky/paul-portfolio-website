-- Practice Data Migration: target tables for Supabase (PostgreSQL)
-- Run in the Supabase SQL Editor before importing the cleaned CSVs.
-- Import order matters: clients first, then appointments (appointments must point to an existing client).
-- Column names match the headers your Final tabs should export.
-- AI-drafted scaffolding; review before running.

drop table if exists appointments;
drop table if exists clients;

create table clients (
    client_id          text primary key check (client_id ~ '^C[0-9]{4}$'),
    first_name         text not null check (btrim(first_name) <> ''),
    last_name          text not null check (btrim(last_name) <> ''),
    date_of_birth      date not null check (date_of_birth > '1900-01-01' and date_of_birth <= current_date),
    phone              text check (phone ~ '^[0-9]{10}$'),          -- digits only; null if unknown or invalid
    email              text check (email ~ '^[^@[:space:]]+@[^@[:space:]]+\.[a-z]{2,}$'),
    street_address     text,
    city               text,
    state              char(2) check (state ~ '^[A-Z]{2}$'),
    zip                text check (zip ~ '^[0-9]{5}$'),
    insurance_provider text,
    member_id          text,
    primary_clinician  text not null,
    status             text not null check (status in ('Active', 'Inactive', 'Discharged')),
    intake_date        date
);

create table appointments (
    appointment_id   text primary key check (appointment_id ~ '^A[0-9]{5}$'),
    client_id        text not null references clients (client_id),
    appointment_date date not null,
    start_time       time not null,
    duration_minutes integer check (duration_minutes between 15 and 180),
    service_code     text not null check (service_code in ('90791', '90832', '90834', '90837', '90847')),
    clinician        text not null,
    location         text check (location in ('Office', 'Telehealth')),
    status           text not null check (status in ('Scheduled', 'Completed', 'No Show', 'Cancelled', 'Late Cancel')),
    copay            numeric(7, 2)
);

-- Notes for your decisions:
-- * A copay has no ">= 0" check on purpose: negative copays are FLAG rows in the answer key, not rejects.
--   Add the check if your business rules reject them instead.
-- * FLAG rows with a bad phone or email still load, but with that field left blank;
--   the checks above would reject the bad value itself.
-- * duration_minutes allows null for the same reason (missing durations are FLAG rows).
-- * The constraints are a second safety net. The Sheets pipeline should catch problems first;
--   if an import fails here, that's a bug in the pipeline worth writing up.
