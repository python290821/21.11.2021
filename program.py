'''
SELECT * from COMPANY;
Select * from COMPANY where id =1;
select id, name from COMPANY
  where id > 2;
select * from COMPANY where name='Paul';
select * from COMPANY where address like 'T%';
select * from COMPANY where address like '%T%' and SALARY > 80000
SELECT * from COMPANY where age=25 or age=30;
select count(*) from COMPANY;
select avg(salary) from COMPANY
update COMPANY set age=21 where id=5;
delete from COMPANY where address like 'Rich-Mond%';

 targil
 select all rows where the salary is above avg
 update all the rows -> set the salary to be 10% bigger
 *etgar: select all the rows sorted by the salary from high to low
 create a class in python for company use the init with the fields, __init__, __str__, __repr__
'''