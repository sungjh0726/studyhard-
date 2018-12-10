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


# Title 3. 동아리(Club)별 회원테이블(Clubmember)을 다음과 같이 만들고, 동아리별 50명 내외로 가입시키시오.
          
          (단, Club 테이블의 leader 컬럼은 삭제하고, 리더를 회원테이블의 레벨(level) 2로 등록하시오)
          
# Title 4. 학고 테이블(Dept)을 만들고 5개 학과 이상 샘플 데이터를 등록하고, 학생 테이블에 학과 컬럼(dept)을 추가한 후 모든 학생에 대해 랜덤하게 과 배정을 시키시오.


# Title 5. 강의실 테이블(Classroom)을 만들고, 샘플강의실 10개를 등록하고, 고목별 강의실 배치를 위해 과목(Subject) 테이블에 강의실컬럼(classroom)을 추가한후 배정하시오.


# Title 6. 1) 수강하는 과목별 중간고사, 기말고사 성적을 저장하는 테이블(Grade)를 생성하고,


2) 수강테이블을 기준으로 샘플 데이터를 중간(midterm), 기말(finalterm) 성적 (100점만점)으로 구성하고,

3) 과목별 수강생을 과목/성적 순으로 아래와 같은 형식으로 출력하는 SQL을 작성하시오.
  과목명   학생명   중간    기말    총점   평균   학점
  
  
4) 과목별 통계 리포트를 과목순으로 하여 아래와 같이 출력하는 SQL을 작성하시오
  과목명   학생명   중간    기말    총점    평균    학점
  
  
5) 학생별 통계리포트를 성적순으로 하여 아래와 같이 출력하는 SQL을 작성하시오.
    학새명   과목수   총점    평균    평점
