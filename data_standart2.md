drop table if exists Job;
drop table if exists Department;
drop table if exists Employee;
drop table if exists JobHistory;

create table Job (
   id varchar(45) not null,
   title varchar(45) not null,
   min_salary int default 0,
   max_salary int default 0,
   primary key(id)
);

create table Department (
   id int default 0 not null,
   name varchar(45) not null,
   manager_id int default 0,
   primary key(id)
);
alter table Department add constraint f_manager_id_employee_id foreign key (manager_id) references Employee(id);


create table Employee (
   id int default 0 not null,
   first_name varchar(45),
   last_name varchar(45) not null,
   email varchar(45) not null,
   tel varchar(45),
   hire_date datetime not null default current_timestamp,
   job varchar(45) not null default ' ',
   salary int default 0,
   commission_pct int default 0,
   manager_id int default 0,
   department int default 0,
   primary key(id),
   constraint uq_email unique (email),
   constraint f_id_manager_id foreign key (manager_id) references Employee(id),
   constraint f_job_id foreign key (job) references Job(id),
   constraint f_department_id foreign key (department) references Department(id)
);

create table JobHistory (
   employee int not null,
   start_date datetime not null,
   end_date datetime not null,
   job varchar(45) not null,
   department int default 0,
   primary key(employee, start_date)
);
alter table JobHistory add constraint f_employee_id foreign key (employee) references Employee(id);
alter table JobHistory add constraint f_jobhistory_job_id foreign key (job) references Job(id);
alter table JobHistory add constraint f_jobhistory_department_id foreign key (department) references Department(id);

