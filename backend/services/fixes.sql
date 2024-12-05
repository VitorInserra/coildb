-- For Faculty table:
-- 1. Drop the existing primary key constraint
--ALTER TABLE faculty DROP CONSTRAINT IF EXISTS faculty_pkey;

-- 2. Add the `id` column with auto-increment and set it as the primary key
--ALTER TABLE faculty ADD COLUMN id SERIAL PRIMARY KEY;
--ALTER TABLE faculty ADD CONSTRAINT faculty_pkey PRIMARY KEY (id);

-- For GradStudent table:
--ALTER TABLE grad_student DROP CONSTRAINT IF EXISTS grad_student_pkey;
--ALTER TABLE grad_student ADD COLUMN id SERIAL PRIMARY KEY;
--ALTER TABLE grad_student ADD CONSTRAINT grad_student_pkey PRIMARY KEY (id);

-- For School table:
--ALTER TABLE schools DROP CONSTRAINT IF EXISTS schools_pkey;
--ALTER TABLE schools ADD COLUMN id SERIAL PRIMARY KEY;
--ALTER TABLE schools ADD CONSTRAINT schools_pkey PRIMARY KEY (id);

-- For Department table:
--ALTER TABLE departments DROP CONSTRAINT IF EXISTS departments_pkey;
--ALTER TABLE departments ADD COLUMN id SERIAL PRIMARY KEY;
--ALTER TABLE departments ADD CONSTRAINT departments_pkey PRIMARY KEY (id);

--ALTER TABLE schools
--ADD COLUMN repeat_faculty INTEGER DEFAULT 0,
--ADD COLUMN unique_faculty INTEGER DEFAULT 0;

-- oc cp backend/services/fixes.sql postgresql-1-w9knm:/tmp/fixes.sql
-- oc rsh postgresql-1-w9knm psql -U dev_user -d dev_db -f /tmp/fixes.sql