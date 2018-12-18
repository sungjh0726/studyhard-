-- 1)
select * from Grade;
select * from Subject;
select * from Enroll;
select * from Dept;
select * from ClubMember;
select * from Subject;

create view v_grade_enroll_avr AS
	select e.*, stu.name, sbj.subject_cnt, ((g.midterm + g.finalterm) / 2 ) AS avr
		from Grade g inner join Enroll e on g.enroll = e.id,
					 inner join Student s on g.enroll = s.name,
					 inner join Subject sbj on g.enroll = sbj.cnt;
                     
-- 2)
-- 한 학생이 어떤과목을 듣는지 알아야함. 과목,점수,평균
Delimiter //
Create function f_student_avg(id int(100))
 RETURNS smallint
 Begin
	return select  e.*, g.avr_subject from Enroll
		where subject = (select id from Subject where id = _id);
 End //
Delimiter


-- 3)
delimiter //
create trigger tr_Club_ClubMember
	after insert on Club for Each Row
BEGIN

 update Club 
	set ClubMember= (
					select cm.id
					where ClubMember = (select cm.id from ClubMember cm order by rand())
        );

END //
Delimiter;


-- 4)
drop procedure if exists sp_top3_prof;
delimiter $$
create procedure sp_top3_prof(_prof_name varchar(31))
begin
    select s.name, 
        if (select count(*) from Grade (g.midterm + g.finalterm / 2) avg >=90) > (select count(*) from Grade (g.midterm + g.finalterm / 2) avg <=70)
         then add like_cnt += 10     
         
		else (select count(*) from Grade (g.midterm + g.finalterm / 2) avg >=90) < (select count(*) from Grade (g.midterm + g.finalterm / 2) avg <=70)
          then add like_cnt += 1
          
      from Grade g inner join Enroll e on  g.enroll = e.id
					inner join Enroll e on g.enroll = sbj.name
     )
     order by G.id desc;
end $$
delimiter ;



    
-- 5)
    
select e.lat_name, e.salary, d.department_name
  from Employees e left outer join Departments d on e.department_id = d.department_id
 where d.department_name = 'Marketing'
   and e.marketing < (select avg(marketing) from Employees where department_id = 80);
   
   
-- 6)

drop procedure if exists sp_subject_ranking;

delimiter //

create procedure sp_subject_ranking()
	begin
		declare _isdone boolean default false;
        declare _subject varchar(31); 
        declare _student varchar(45); 
        declare _avr varchar(45);
        declare local_i smallint default 1;
        
        declare _ttt int; -- QQQ
                
        declare cursor_1 cursor
			for select * from T_table0;
		
        declare continue handler 
			for not found set _isdone = True;

		drop table if exists T_table0;
        create temporary table T_table0(
			subject varchar(31),
			student varchar(45),
			avr varchar(45)
			);

		drop table if exists T_table1;
        create temporary table T_table1(
			subject varchar(31),
            student1 varchar(31),
            score1 varchar(31),
            student2 varchar(31),
            score2 varchar(31),
            student3 varchar(31),
            score3 varchar(31),
            isdone boolean default false
            );
            

		while (local_i <= 10) do
			insert into T_table0(subject, student, avr)
            select max(sub.subject), group_concat(sub.student) as student, group_concat(sub.avr) as avr
				from (select sbj.name as subject, stu.name as student, vge.avr as avr
								from v_grade_enroll as vge inner join Subject as sbj on sbj.id = vge.subject
																	        inner join Student as stu on stu.id = vge.student
                                where vge.subject = local_i order by avr desc limit 3) sub;
				
			set local_i = local_i + 1;
		end while;            
            
		select * from T_table0;
        
        open cursor_1;
            
			loop1 : loop
                
				fetch cursor_1 into _subject, _student, _avr;
                
                if _isdone then
					leave loop1;
				end if;
                
				insert into T_table1 value(_subject, substring_index(_student, ',', 1), substring_index(_avr, ',', 1),
															substring_index(substring_index(_student, ',', 2),',',-1),
                                                            substring_index(substring_index(_avr, ',', 2),',',-1),
                                                            substring_index(substring_index(_student, ',', 3),',',-1),
                                                            substring_index(substring_index(_avr, ',', 3),',',-1), _isdone);                
            
				
                
            end loop loop1;
            
        close cursor_1;
        
        select * from T_table1;
        
    end //

delimiter ;

/*
desc Subject;
desc Student;
desc Grade;
select subject, count(*) from Enroll group by subject;
select * from Subject;
select subject, student, avr
	from v_grade_enroll where subject = 1 order by avr desc limit 3;
select max(sub.subject) as subject, group_concat(sub.student) as student, group_concat(sub.avr) as avr
	from (select subject, student, avr
				from v_grade_enroll where subject = 1 order by avr desc limit 3) sub;
select max(sbj.id), group_concat(sub.student) as student, group_concat(sub.avr) as avr
	from (select vge.subject as subject, vge.student as student, vge.avr as avr
				from v_grade_enroll as vge where vge.subject = sbj.id order by avr desc limit 3) sub, Subject as sbj
;
select substring_index('a,b,c', ',', 1);
*/

 call sp_subject_ranking();
