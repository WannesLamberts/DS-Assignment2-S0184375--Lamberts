CREATE TABLE users(username varchar(255),password varchar(255),PRIMARY KEY (username));
CREATE TABLE friends(
    userfrom varchar(255) REFERENCES users(username),
    userto varchar(255) REFERENCES users(username),
    PRIMARY KEY (userfrom,userto)
                    );
CREATE TABLE groups(groupname varchar(255),creator varchar(255) NOT NULL REFERENCES users(username),PRIMARY KEY(groupname));
CREATE TABLE groupmembers(groupname varchar(255) REFERENCES groups(groupname),member varchar(255) NOT NULL REFERENCES users(username),PRIMARY KEY(groupname,member));


