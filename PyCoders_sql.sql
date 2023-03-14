CREATE TABLE "students"
(
    "student_id" INT NOT NULL,
    "name" TEXT NOT NULL,
    CONSTRAINT "PK_student" PRIMARY KEY  ("student_id")
);

CREATE TABLE "teachers"
(
    "teacher_id" INT NOT NULL,
    "name" TEXT NOT NULL,
    CONSTRAINT "PK_teacher" PRIMARY KEY  ("teacher_id")
);


INSERT INTO "students" ("student_id", "name") VALUES (1,'Adam');
INSERT INTO "students" ("student_id", "name") VALUES (2,'Lina');
INSERT INTO "students" ("student_id", "name") VALUES (3,'Zogri');


INSERT INTO "teachers" ("teacher_id", "name") VALUES (1,'Abood');
INSERT INTO "teachers" ("teacher_id", "name") VALUES (2,'Lolo');
INSERT INTO "teachers" ("teacher_id", "name") VALUES (3,'Rane');