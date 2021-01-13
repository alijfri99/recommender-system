use ir_assignment;
create index idxISBN on books(ISBN);
create index idxISBN on ratings(ISBN);

alter table books add column `id` int unsigned primary KEY AUTO_INCREMENT;

-- SHOW KEYS FROM users WHERE Key_name = 'PRIMARY';


alter table users add primary key (`User-ID`);


create table `temp_ratings` AS SELECT `ratings`.`User-ID` , `books`.id  ,  `ratings`.`Book-Rating` FROM `ratings` INNER JOIN `books` on `ratings`.ISBN =  `books`.ISBN;


  
drop table `ratings`;

ALTER TABLE `temp_ratings`
  RENAME TO `ratings`;
  
alter table `ratings` add primary key (id , `User-ID`);

ALTER TABLE `ratings`
  ADD CONSTRAINT fk_book_id  FOREIGN KEY (id) REFERENCES `books`(id) ON DELETE CASCADE;

ALTER TABLE `ratings`
  ADD CONSTRAINT fk_user_id  FOREIGN KEY (`User-ID`) REFERENCES `users`(`User-ID`) ON DELETE CASCADE;