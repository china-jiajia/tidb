#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import prettytable as pt

tb = pt.PrettyTable()

sql = '''select * from test.t1;'''
sql = '''/*--user=admin;--password=han123;--host=127.0.0.1;\
--execute=1;--remote-backup=1;--port=3306;*/
inception_magic_start;
use `test`;
insert into test.t1(id) select c1,c2 from t1;
insert into test.t1(id,c1) select * from t1;
insert into test.t1(id,c1) select c1,c2 from t1;
inception_magic_commit;
'''

sql = '''/*--user=admin;--password=han123;--host=127.0.0.1;\
--execute=1;--remote-backup=1;--port=3306;*/
inception_magic_start;
use `test`;
 delete from t1 where id =1;
# delete t1 from t1,t2,t3 where t1.iid = t2.id and t2.id = t3.id and t3.id = 1;
inception_magic_commit;
'''

sql = '''/*--user=admin;--password=han123;--host=127.0.0.1;\
--execute=1;--remote-backup=1;--port=3306;*/
inception_magic_start;
use `test`;
update t1 set c1  = 1000 where id  =10001;
inception_magic_commit;
'''


sql = '''/*--user=admin;--password=han123;--host=127.0.0.1;\
--execute=1;--backup=1;--port=3306;--enable-ignore-warnings;*/
inception_magic_start;
use `test`;

create table t1(id int);
alter table t1 add column db varchar(20);

# alter table tt1 modify column c1 int after c2;
# insert into tt1(id,c1,c2,c3) values(2,20,"200","2000");
# delete from tt1;
#
# alter table tt1 modify column c2 int after id;
# insert into tt1(id,c1,c2,c3) values(2,20,"200","2000");
# delete from tt1;
#
# alter table tt1 modify column id int not null after c2;
#
# insert into tt1(id,c1,c2,c3) values(2,20,"200","2000");
# delete from tt1;
#
# alter table tt1 modify column c3 varchar(10) first;
# insert into tt1(id,c1,c2,c3) values(2,20,"200","2000");
# update tt1 set c2 = "21",c3="aaa" where id = 2;
# delete from tt1;


# alter table tt1 modify column c2 int after id;
# insert into tt1(id,c1,c2,c3) values(3,30,"300","3000");

# alter table tt1 modify column id int not null after c2;

# insert into tt1(id,c1,c2,c3) values(4,40,"400","4000");

# alter table tt1 modify column c3 varchar(10) first;
# insert into tt1(id,c1,c2,c3) values(5,50,"500","5000");


# create table tt2 like tt1;

# alter table tt2 add column c1 int first;
# insert into tt2(id,c1) values(1,10);
# delete from tt2;
# alter table tt2 drop column c1;

# alter table tt2 add column c2 int after id;
# insert into tt2(id,c2,c3) values(1,100,"test");
# update tt2 set c2 = 20,c3="aaa" where id = 1;
# delete from tt2;

# alter table tt2 drop column c2;


# alter table tt1 add index ix1(c2);

# show variables like 'log%';

# drop table if exists t2 ;

# create table t2(id int auto_increment primary key,t1 timestamp  NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,t2 timestamp);

#create table ttt1(id int primary key,c1 int auto_increment );

#delete from t1 where id > 0;

#insert into ttt1(id,c1) values(1,null);
#insert into ttt1(id,c1) values(1,'null');
# insert into ttt1(id,c1) values(2,'test'),(3,'test');
#insert into ttt1(id,c1) select id+3,c1 from ttt1 order by rand();

#insert into ttt1(id,c1) select id+3,c1 from ttt1 where id = 1 order by 1;

# insert into ttt1(id,c1,c1) select 8,'123';

#drop table if exists ttt2;

#create table ttt2(id int primary key,c1 int );

#insert into ttt2(id,c1,c1) select 1,1,1;
# insert into ttt2 select 2,2;

# update ttt1 set c11 = c1 ;

# delete from ttt1;

# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select * from information_schema.tables;

# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;
# insert into t1(TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT) select TABLE_CATALOG,TABLE_SCHEMA,TABLE_NAME,TABLE_TYPE,ENGINE,VERSION,ROW_FORMAT,TABLE_ROWS,AVG_ROW_LENGTH,DATA_LENGTH,MAX_DATA_LENGTH,INDEX_LENGTH,DATA_FREE,AUTO_INCREMENT,CREATE_TIME,UPDATE_TIME,CHECK_TIME,TABLE_COLLATION,CHECKSUM,CREATE_OPTIONS,TABLE_COMMENT from t1;

# delete from t1 where id > 0;

#create table tt33(id varchar(10) primary key,c1 int,index idx_1 (c1));
# create table tt34(id varchar(10) ,c1 int,primary key(id));

# create table `table`(id varchar(10) ,`column` int);

inception_magic_commit;
'''

# create table t1(id int primary key,c1 int);
# create table t2(id int primary key,c1 int,c2 int);
sql = '''/*--user=admin;--password=han123;--host=127.0.0.1;--check=1;--backup=1;--port=3306;--enable-ignore-warnings;*/
inception_magic_start;
use test_inc;
create table t1(id int primary key,c1 int);
create table t2(id int primary key,c1 int,c2 int);
delete from t1 where c1 = 1;
delete from t1 where id1 =1;
DELETE FROM t1 USING t1,t2 WHERE t1.id=t2.id ;
delete t1 from t1 left join t2 on t1.id=t2.id where t1.id >1 and t2.c1<>1;
delete t1 from t1 where id =1;
delete t1 from t1 inner join t2 on t1.id=t2.id where c2=1;
delete t2 from t1 inner join t2 on t1.id=t2.id2 where c21=1;
inception_magic_commit;'''

# alter table t1 add column c2 int;
# alter table t1 add column c3 int after c7,add column c4 int;

conn = pymysql.connect(host='127.0.0.1', user='root',
                       passwd='', db='', port=4000, charset="utf8mb4")
# cur = conn.cursor(pymysql.cursors.SSCursor)
cur = conn.cursor()
ret = cur.execute(sql)
result = cur.fetchall()
num_fields = len(cur.description)
field_names = [i[0] for i in cur.description]


tb.field_names = field_names
for row in result:
    tb.add_row(row)

print(tb)

# print(result)
# print(len(result))
# print(field_names)
# for row in result:
#     print(row)
cur.close()
conn.close()
