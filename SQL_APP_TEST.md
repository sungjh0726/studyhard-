# Title 1. 학생, 과목, 교수, 수강내역 ,테이블 관게를 고려하여 생성하는 DDL을 작성하시오.
CREATE TABLE `Student` (

  `id` int(11) NOT NULL AUTO_INCREMENT,
  
  `name` varchar(32) NOT NULL,
  
  `addr` varchar(30) NOT NULL,
  
  `birth` date NOT NULL,
  
  `tel` varchar(15) NOT NULL,
  
  `email` varchar(31) NOT NULL,
  
  `regdt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  
  PRIMARY KEY (`id`)
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



select * from Student;

desc student;


create table Prof(

	id smallint unsigned not null auto_increment primary key,
	
    name varchar(31) not null,
    
    likecnt int default 0 
    
    
);

select ceil(rand() * 100) from dual;


insert into Prof(name, likecnt) select name,ceil(rand() * 100)  from Student order by rand() limit 100;


select * from Prof;


create table subject(

	id int unsigned not null auto_increment primary key,
	
    name varchar(31) not null,
    
    prof smallint unsigned not null,
    
    constraint foreign key fk_prof(prof) references Prof(id)
    
    on delete set null,

);

select * from subject;

insert into subject(name,prof)

 select '국어', id from Prof order by rand() limit 10;
 
 update subject set name ='기술' where name = '국어' and id <> 10 limit 1;
 
 select * from subject;
 

desc subject;


select * from Enroll;

create table Enroll(

	id int unsigned auto_increment primary key,
	
    subject int unsigned not null,
    
    student int unsigned not null,
    
	constraint foreign key fk_subject(subject) references subject(id), 
	
    constraint foreign key fk_student(student) references Student(id)
    
	
);

select * from Enroll;

desc prof


# Title 2. 학생테이블과 과목테이블을 활용하여, 수강내역테이블에 테스트용 데이터를 구성하는 DML을 절차적으로 작성하시오.

Start transaction;

insert into subject(name,prof) select '국어', id from Prof order by rand() limit 6

update subject set name ='기술' where name = '국어' and id <> 10 limit 1;

update subject set name ='가정' where name = '국어' and id <> 10 limit 1;

update subject set name ='수학' where name = '국어' and id <> 10 limit 1;

update subject set name ='영어' where name = '국어' and id <> 10 limit 1;

update subject set name ='생물' where name = '국어' and id <> 10 limit 1;

update subject set name ='화학' where name = '국어' and id <> 10 limit 1;



select * from subject;

desc subject;


insert into Enroll(name, subject) select name from Student order by rand() limit 1000;


insert into Enroll(name, Student) select name from subject;

insert into Enroll(student, subject)

 select id, (select id from subject order by rand() limit 1) sid from Student order by id;
 

insert into Enroll(student, subject)

 select id, (select id from subject order by rand() limit 1) sid from Student order by rand() limit 500
 
 on duplicate key update student = student;
 
 
insert into Enroll(student, subject)

 select id, (select id from subject order by rand() limit 1) sid from Student order by rand() limit 500
 
 on duplicate key update student = student;
 

select * from Enroll;


desc * Enroll;

commit;




# Title 3. 동아리(Club)별 회원테이블(Clubmember)을 다음과 같이 만들고, 동아리별 50명 내외로 가입시키시오.
          
          # (단, Club 테이블의 leader 컬럼은 삭제하고, 리더를 회원테이블의 레벨(level) 2로 등록하시오)
          
	  
start transaction;

create table Club(

	id smallint unsigned not null auto_increment primary key,
	
	name varchar(31) not null,
	
    createdate timestamp not null default current_timestamp,
    
	leader int unsigned,
	
   
);

select * from Club;


alter table Club drop column leader;


create table Clubmember(

	id int unsigned not null auto_increment primary key,
	
	club smallint unsigned not null,
	
    student int unsigned not null,
    
    level smallint unsigned not null,
    
    constraint foreign key fk_club(club) references Club(id),
    
    constraint foreign key fk_student(student) references Student(id) 
    
 
 );
 
 select * from subject;
 
 select * from Club;
 
 
 insert into Club(name) values('요술부');
 
insert into Club(name) values('테니스부');

insert into Club(name) values('요트부');

insert into Club(name) values('댄스부');


 select * from Club;
 
 insert into Clubmemeber (Club, student) select 4, id from Student order by rand() limit 50;
 
update Clubmember set level = rand() where id >0;

update Clubmember set level = 2 where student = 100;


commit;





# Title 4. 학고 테이블(Dept)을 만들고 5개 학과 이상 샘플 데이터를 등록하고, 학생 테이블에 학과 컬럼(dept)을 추가한 후 모든 학생에 대해 랜덤하게 과 배정을 시키시오.


create table Dept(

	id smallint(5) unsigned not null auto_increment primary key,
	
    name varchar(31) comment '학과명',
    
    prof smallint(5) unsigned comment '교수명',
    
    student int(11) unsigned comment '과대표',
    
    constraint foreign key fk_prof(prof) references Prof(id),
    
    constraint foreign key fk_student(student) references Student(id)
    

);

select * from Dept;

desc Dept;

insert into Dept(name) values('경영학과');

insert into Dept(name) values('경제학과');

insert into Dept(name) values('신문방송학과');

insert into Dept(name) values('디자인학과');

insert into Dept(name) values('통계학과');


-- alter table Student add column dept;

ALTER TABLE `dooodb`.`Student` 

ADD COLUMN `dept` VARCHAR(45) NOT NULL AFTER `gender`;


select * from Student;

insert into Dept (Dept, student) select 4, id from Student order by rand() limit 4;

update Dept set prof = rand() where id >0;


select * from Student;


# Title 5. 강의실 테이블(Classroom)을 만들고, 샘플강의실 10개를 등록하고, 고목별 강의실 배치를 위해 과목(Subject) 테이블에 강의실컬럼(classroom)을 추가한후 배정하시오.


start taransaction;


create table Classroom(

	id int unsigned not null auto_increment primary key,
	
    name smallint unsigned not null,
    
    subject int unsigned not null,
    
    constraint foreign key fk_subject(subject) references subject(id)
    
    
);

select * from Classroom;


insert into Classroom(name) values('201호');

insert into Classroom(name) values('202호');


insert into Classroom(name) values('203호');

insert into Classroom(name) values('204호');

insert into Classroom(name) values('205호');

insert into Classroom(name) values('206호');

insert into Classroom(name) values('207호');

insert into Classroom(name) values('208호');

insert into Classroom(name) values('209호');

insert into Classroom(name) values('210호');

ALTER TABLE `dooodb`.`subject` 

ADD COLUMN `classroom` VARCHAR(45) NOT NULL AFTER `prof`;


select * from subject;



ALTER TABLE `dooodb`.`subject` 

ADD CONSTRAINT `classroom`

  FOREIGN KEY (`classroom`)
  
  REFERENCES `dooodb`.`Classroom` (`name`)
  
  ON DELETE NO ACTION
  
  ON UPDATE NO ACTION;
  
  
 update subject set calssroom = rand() where id > 0;
 
  
# Title 6. 1) 수강하는 과목별 중간고사, 기말고사 성적을 저장하는 테이블(Grade)를 생성하고,

start transaction;


create table Grade(

	id smallint unsigned auto_increment primary key,
	
    enroll int unsigned not null,
    
    midterm smallint unsigned not null default 0,
    
    finalterm smallint unsigned not null default 0,
    
	constraint foreign key fk_enroll(enroll) references Enroll(id)
	

);

select * from Grade;


2) 수강테이블을 기준으로 샘플 데이터를 중간(midterm), 기말(finalterm) 성적 (100점만점)으로 구성하고,


insert into Grade(enroll) select id from Enroll;


update Grade set midterm = ceil((0.5 + rand() / 2) * 100) where id > 0;


update Grade set finalterm = ceil((0.5 + rand() / 2) * 100) where id > 0;



3) 과목별 수강생을 과목/성적 순으로 아래와 같은 형식으로 출력하는 SQL을 작성하시오

.
  과목명   학생명   중간    기말    총점   평균   학점
  
  start transaction;
  
  select report1.sbj_name, report1.stu_name, 
  
          report1.midterm, report1.finalterm, report1.total_score, report1.avg_score, report1.rating
	  
from

(

 select report.*, (case when report.avg_score = 100 then 'A+'
 
			          when report.avg_score >= 90 then 'A'
				  
                                  when report.avg_score >= 80 then 'B'
				  
                                  
				  when report.avg_score >= 70 then 'C'
				  
                                  when report.avg_score >= 60 then 'D'
				  
                                  else 'F' end) rating
				  
   from
   
(                                   


select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 

						((g.midterm + g.finalterm) / 2) avg_score
						
			 from Grade g inner join Subject sbj on g.subject = sbj.id
			 
								   inner join Student stu on g.student = stu.id
								   
) report

) report1

order by report1.sbj_name asc, report1.avg_score desc;


commit;

  
4) 과목별 통계 리포트를 과목순으로 하여 아래와 같이 출력하는 SQL을 작성하시오


  과목명   학생명   중간    기말    총점    평균    학점
  
  
  start transaction;



select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 

						((g.midterm + g.finalterm) / 2) avg_score
						
			 from Grade g inner join Subject sbj on g.subject = sbj.id
			 
								   inner join Student stu on g.student = stu.id;


select report.sbj_name, avg(report.avg_score), (if(report.avg_score = max(report.avg_score), count(*)

from

(

select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 

						((g.midterm + g.finalterm) / 2) avg_score
						
			 from Grade g inner join Subject sbj on g.subject = sbj.id
			 
								   inner join Student stu on g.student = stu.id
								   
)report

group by report.subject asc

order by report.sbj_name limit 10






select report.sbj_name, report.stu_name, report.*

from

(

select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 

						((g.midterm + g.finalterm) / 2) avg_score
						
			 from Grade g inner join Subject sbj on g.subject = sbj.id
			 
								   inner join Student stu on g.student = stu.id
								   
)report

where report.subject = report.subject

order by report.sbj_name asc, report.avg_score desc;








commit;






5) 학생별 통계리포트를 성적순으로 하여 아래와 같이 출력하는 SQL을 작성하시오.


    학새명   과목수   총점    평균    평점
    
    
start transaction;


select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 

						((g.midterm + g.finalterm) / 2) avg_score
						
			 from Grade g inner join Subject sbj on g.subject = sbj.id
								   inner join Student stu on g.student = stu.id;






 select report1.*, (case when report1.avg_point = 100 then 'A+'
 
                                 when report1.avg_point >= 90 then 'A'
				 
                                when report1.avg_point >= 80 then 'B'
				
                                when report1.avg_point >= 70 then 'C'
				
                                when report1.avg_point >= 60 then 'D'
				
                                else 'F' end) rating
   from
   
(  

select  report.stu_name, count(*), sum(report.total_score) total_point, avg(report.avg_score) avg_point

from 

(

select g.*, sbj.name as sbj_name, stu.name as stu_name, (g.midterm + g.finalterm) total_score, 

						((g.midterm + g.finalterm) / 2) avg_score
						
			 from Grade g inner join Subject sbj on g.subject = sbj.id
			 
								   inner join Student stu on g.student = stu.id
								   
) report

group by report.student

order by report.stu_name asc

)report1;


commit;

