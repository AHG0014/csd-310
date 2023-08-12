-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('5700 Bogart St NW, Albuquerque, NM 87120');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Hunger Games', 'Suzanne Collins', 'The beginning of The Hunger Games Series');

INSERT INTO book(book_name, author, details)
    VALUES('Catching Fire', 'Suzanne Collins', 'The Secound part of The Hunger Games Series');

INSERT INTO book(book_name, author, details)
    VALUES('MockingJay', 'Suzanne Collins', "Third Part of The Hunger Games Series");

INSERT INTO book(book_name, author)
    VALUES('The Ballad of Songbirds and Snakes', 'Suzanne Collins');

INSERT INTO book(book_name, author)
    VALUES('Twilight', 'Stephanie Mayer');

INSERT INTO book(book_name, author)
    VALUES("Midnight Sun", 'Stephanie Mayer');

INSERT INTO book(book_name, author)
    VALUES('It Ends With Us', 'Colleen Hoover');

INSERT INTO book(book_name, author)
    VALUES('Misery', 'Stephan King');

INSERT INTO book(book_name, author)
    VALUES('Fairy Tale', 'Stephan King');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Fred', 'Fernandez');

INSERT INTO user(first_name, last_name)
    VALUES('Brian', 'Andrews');

INSERT INTO user(first_name, last_name)
    VALUES('Sam', 'Smith');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Fred'), 
        (SELECT book_id FROM book WHERE book_name = 'The Ballad of Songbirds and Snakes')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Brian'),
        (SELECT book_id FROM book WHERE book_name = 'Catching Fire')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sam'),
        (SELECT book_id FROM book WHERE book_name = 'Mockingjay')
    );