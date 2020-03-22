DROP TABLE IF EXISTS task_duration;
CREATE TABLE task_duration(
   user_id         INTEGER  NOT NULL
  ,task            VARCHAR(30) NOT NULL
  ,completion_time NUMERIC(5,1) NOT NULL
);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (107,'length of cell phone by S211',484.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (107,'width of leaf by s211',43.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (107,'length of eyes',42.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (107,'length of whole leaf',61.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (108,'Length of cellphone (S212)',39.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (108,'Width of leaf blade by (S212)',49.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (108,'Length of boys eyes by (S212)',21.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (108,'Length of leaf blade by (S212)',16.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (106,'length of cell phone s210',30.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (106,'length of leaf s210',38.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (106,'length of boys eyes',16.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (106,'length of leaf height s210',33.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (99,'length of leaf',43.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (99,'length of eyes',61.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (99,'length of leaf blade',70.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (99,'length of cell phone',109.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (44,'length of cell phone S208',98.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (44,'length of leaf blade s208',51.0);
INSERT INTO task_duration(user_id,task,completion_time) VALUES (44,'length of eyes S208',76.0);
