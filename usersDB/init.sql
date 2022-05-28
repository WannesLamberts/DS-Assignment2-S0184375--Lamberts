CREATE TABLE users(username varchar(255),password varchar(255),PRIMARY KEY (username));
CREATE TABLE friends(
    userfrom varchar(255) REFERENCES users(username),
    userto varchar(255) REFERENCES users(username),
    PRIMARY KEY (userfrom,userto)
                    );
INSERT INTO friends(userfrom,userto) VALUES ('test','test');


