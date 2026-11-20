-- Practice Data Migration: target tables for Supabase (PostgreSQL). AI-drafted from my business rules.
-- Run in the Supabase SQL Editor, then import clients before appointments.
-- Column names match the Final tabs' headers, except preferred_name and pronouns, which the export doesn't have (BR-36).

drop table if exists appointments;
drop table if exists clients;

create table clients (
    client_id          text primary key check (client_id ~ '^C[0-9]{4}$'),
    first_name         text not null check (btrim(first_name) <> ''),
    last_name          text not null check (btrim(last_name) <> ''),
    preferred_name     text,                                        -- left null; the practice asks the client (BR-36)
    pronouns           text,                                        -- left null; never guessed from a name (BR-36)
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
    intake_date        date,
    referral_source    text                                         -- optional; kept for marketing (BR-04)
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

-- Notes:
-- * The spreadsheet catches problems first; these checks are a safety net. A failed import is a pipeline bug.
-- * Flagged rows load: bad phones and emails as blanks, blank durations as 60, blank copays as 0 (BR-12, BR-13, BR-17, BR-20).
-- * No ">= 0" check on copay, because negative copays load as flagged rows (BR-20).
