DROP DATABASE inventory_data;

CREATE DATABASE inventory_data;

USE inventory_data;

CREATE TABLE Inventory (
  id INT(3) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  size VARCHAR(20),
  category VARCHAR(20),
  quantity_available FLOAT UNSIGNED,
  retail_price FLOAT UNSIGNED,
  case_retail_price FLOAT UNSIGNED,
  case_pack INT UNSIGNED;
)
