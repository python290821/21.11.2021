'''
SELECT * from COMPANY;
-- drop table COMPANY -- danger!
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
 update all the rows -> set the salary to be 10% bigger
   solution:
   update COMPANY set salary = SALARY * 1.1;
 delete workers at the age of 25
   solution:
   DELETE from COMPANY where age=25;
 *etgar: select all rows where the salary is above avg
   solution:
   select * from COMPANY where SALARY > (select avg(salary) from COMPANY)
 *etgar: select all the rows sorted by the salary from high to low
   solution:
   select * from COMPANY order by salary desc
'''