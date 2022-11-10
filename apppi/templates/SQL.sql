create table if not exists mainmenu (
id integer primary key autoincrement,
title text not null,
url text not null
);

create table if not exists obuv (
id integer primary key autoincrement,
title text not null,
obuv text not null,
url text not null
);