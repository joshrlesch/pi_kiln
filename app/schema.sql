DROP TABLE IF EXISTS environment;


CREATE TABLE environment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  humidity TEXT NOT NULL,
  temp TEXT NOT NULL,
  sensor TEXT NOT NULL,
  date TEXT NOT NULL
);
