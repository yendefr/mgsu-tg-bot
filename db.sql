-- Table Definition
CREATE TABLE "public"."files" (
    "id" text NOT NULL,
    "name" text,
    "category" text,
    "subject" text,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS students_id_seq;

-- Table Definition
CREATE TABLE "public"."students" (
    "id" int4 NOT NULL DEFAULT nextval('students_id_seq'::regclass),
    "name" text,
    "surname" text,
    "group_number" int4,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Sequence and defined type
CREATE SEQUENCE IF NOT EXISTS tasks_id_seq;

-- Table Definition
CREATE TABLE "public"."tasks" (
    "id" int4 NOT NULL DEFAULT nextval('tasks_id_seq'::regclass),
    "subject" text,
    "description" text,
    "expire_date" date,
    "is_semester" bool DEFAULT false,
    PRIMARY KEY ("id")
);

-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."tasks_files" (
    "task_id" text NOT NULL,
    "file_id" text NOT NULL
);

