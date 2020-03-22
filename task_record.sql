DROP TABLE IF EXISTS task_record;
CREATE TABLE task_record(
   user_id         INTEGER  NOT NULL
  ,task            VARCHAR(28) NOT NULL
  ,term            VARCHAR(26) NOT NULL
  ,definition      VARCHAR(30)
  ,completion_time NUMERIC(4,1) NOT NULL
);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (99,'length of cell phone','left upper corner of phone','corner of phone',12.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (105,'length of cell phone','left upper corner of phone','upper left corner',8.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (106,'length of leaf s210','left side','left side',4.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (106,'length of leaf height s210','top of leaf','top',3.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (107,'length of cell phone by S211','upper left screen corner','top',4.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (107,'length of whole leaf','tip of leaf','top',3.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (44,'length of cell phone S208','top','the top the highest point',20.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (44,'length of eyes S208','side','the width',14.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (108,'length of cellphone (S212)','Top corner of screen','Top corner of the phone screen',15.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (108,'length of cellphone (S212)','Top corner of screen','Top corner of the phone screen',8.0);
INSERT INTO task_record(user_id,task,term,definition,completion_time) VALUES (108,'length of cellphone (S212)','Top',NULL,2.0);
