CREATE EXTENSION IF NOT EXISTS  pgcrypto;

CREATE SCHEMA IF NOT EXISTS BASEAPP AUTHORIZATION docker;

CREATE TABLE IF NOT EXISTS BASEAPP.APPUSER (
     id SERIAL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    pw TEXT NOT NULL,
   fname TEXT NOT NULL,
   lname TEXT,
   active INT NOT NULL,
   created_on TIMESTAMPTZ NOT NULL DEFAULT NOW(),
   system_created TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO BASEAPP.APPUSER(email,fname,lname,pw,active)
VALUES ('mal@admin.com','mal','dadigama',crypt('malpw', gen_salt('bf')) , 1);

CREATE TABLE IF NOT EXISTS BASEAPP.CASE_PROFILE (
    cid SERIAL PRIMARY KEY,
    case_guid TEXT NOT NULL,
    system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by TEXT NOT NULL,
    offence TEXT NOT NULL UNIQUE,
    crime_no TEXT NOT NULL,
   log_no TEXT NOT NULL,
   _name TEXT NOT NULL,
   _rank TEXT NOT NULL,
   _no TEXT NOT NULL,
   _location TEXT NOT NULL,
   vrm TEXT NOT NULL,
   make TEXT NOT NULL,
   model TEXT NOT NULL,
   case_created TEXT NOT NULL ,
   case_started TEXT NOT NULL ,
   case_finished TEXT NOT NULL,
   module_openandi TEXT NOT NULL,
   _description TEXT NOT NULL,
   additional_information TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS BASEAPP.CASE_EVIDANCE (
    eid SERIAL PRIMARY KEY,
    cid INT NOT NULL,
    case_guid TEXT NOT NULL,
    system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by TEXT NOT NULL,
    eindex TEXT NOT NULL,
    edes TEXT NOT NULL,
    eseal_no TEXT NOT NULL

    );

CREATE TABLE IF NOT EXISTS baseapp.photo_path
(
    photo_id SERIAL PRIMARY KEY,
    system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    cid bigint,
    gid bigint,
    case_id text  NOT NULL,
    group_id text  NOT NULL,
    photo_des text ,
    file_path text NOT NULL,
    file_name text NOT NULL
);

CREATE TABLE IF NOT EXISTS baseapp._groups
(
    gid SERIAL PRIMARY KEY,
     system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    g_name text UNIQUE NOT NULL,
    g_des text ,
    active bigint default 1
);

CREATE TABLE IF NOT EXISTS baseapp.t_feedback
(
    fid SERIAL PRIMARY KEY,
    system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    cid bigint NOT NULL,
    gid bigint NOT NULL,
    student_id text  NOT NULL,
    grade text,
    feedback text
);

CREATE TABLE IF NOT EXISTS baseapp.t_grades
(
    id SERIAL PRIMARY KEY,
    system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    grade text NOT NULL,
    _value int,
    comment text
);

INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('High 2.2',0,'High 2.2');
INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('High 2.1',0,'High 2.1');
INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('Low 1st',0,'Low 1st');
INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('Low 2.2',0,'Low 2.2');
INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('Low 2.1',0,'Low 2.1');
INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('Mid 2.1',0,'Mid 2.1');
INSERT INTO baseapp.t_grades(grade, _value, comment)VALUES ('Mid 2.2',0,'Mid 2.2');
INSERT INTO baseapp.t_grades(grade, _value, comment) VALUES ('Mid 1st',0,'Mid 1st');

CREATE TABLE IF NOT EXISTS baseapp.t_student
(
    sid SERIAL PRIMARY KEY,
    system_created TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    student_fnm text NOT NULL,
    student_lnm text NOT NULL,
    student_email text UNIQUE NOT NULL,
    student_id bigint NOT NULL
);

INSERT INTO baseapp.t_student(student_fnm,student_lnm ,student_email, student_id)VALUES ('Andrew', 'Simon', 'as@ntu.com', 'NTU001');
INSERT INTO baseapp.t_student(student_fnm,student_lnm ,student_email, student_id)VALUES ('Bne', 'Stew', 'bs@ntu.com', 'NTU002');
INSERT INTO baseapp.t_student(student_fnm,student_lnm ,student_email, student_id)VALUES ('Kamal', 'Perea', 'kp@ntu.com', 'NTU003');