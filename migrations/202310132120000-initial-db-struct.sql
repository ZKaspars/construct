CREATE TABLE IF NOT EXISTS liked_jokes (
      id int NOT NULL AUTO_INCREMENT,
      text varchar(255) NOT NULL,
      type varchar(10) NOT NULL,
      flags varchar(255) NOT NULL,
      PRIMARY KEY(id)
    )