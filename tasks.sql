drop table if exists tasks;
create table tasks (
      id integer primary key autoincrement,
      username string not null,
      time string not null,
      filename string not null,
      prograss int8 not null
);



