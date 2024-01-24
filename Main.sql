show databases;
create database bg;
use bg;

show tables;

CREATE TABLE Leaderboard 
(
    UID VARCHAR(255) primary key,
    Name VARCHAR(255),
    Score INT,
    Country CHAR(2),
    TimeStamp TIMESTAMP
);

Select * from Leaderboard;





