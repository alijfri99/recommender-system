use ir_assignment;
create index idxISBN on books(ISBN);
create index idxISBN on ratings(ISBN);
-- create index idxID on users(`User-ID`);
-- create index idxID on ratings(`User-ID`);