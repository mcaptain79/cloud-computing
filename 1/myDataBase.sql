create table movie(
    movie_id int,
    movie_name varchar(100),
    movie_poster_link text,
    movie_director varchar(100),
    primary key (movie_id)
);
create table comment(
    comment_id int,
    movie_id int,
    comment_text text,
    primary key (comment_id),
    foreign key (movie_id) references movie(movie_id)
);
-- inserting movies
insert into movie values (1,'iron man 3','https://drive.google.com/file/d/1eXHUGKmlzqgBk3_tK88yJ-7UxxQocPyD/view?usp=sharing'
,'shane black');
insert into movie values (2,'fifty shades of grey','https://drive.google.com/file/d/1ngPBEYtNuIuDDJ7ZjIWUykdhGrpRkErh/view?usp=sharing'
,'james foley');
insert into movie values (3,'the avengers','https://drive.google.com/file/d/1Ezw6RjXE0bLy4Tt0O_DCN8c63YGCPYU5/view?usp=sharing'
,'Joss Whedon');
insert into movie values (4,'tenet','https://drive.google.com/file/d/1FmCNSFFdRiCT4Gu4zUkClCFMUiQgdhS5/view?usp=sharing'
,'Christopher Nolan');
insert into movie values (5,'joker','https://drive.google.com/file/d/1TBCQNlmhk3f6YcYzvhGsYz5q6CciE_M9/view?usp=sharing'
,'Todd Phillips');
-- inserting initial comments
insert into comment values (1,1,'very great movie,best movie i have ever seen');
insert into comment values (2,1,'greatest movie of all time');
insert into comment values (3,2,'wooooooooooooooooooooooooooooooow');
insert into comment values (4,2,'nice movie i recommend it');
insert into comment values (5,3,'best movie i have ever seen in my life');
insert into comment values(6,4,'nice movie but i did not understand a word :(');
insert into comment values(7,5,'great scenario and greater actor');
select * from comment;