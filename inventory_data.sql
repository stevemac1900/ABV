DROP DATABASE inventory_data;

CREATE DATABASE inventory_data;

USE inventory_data;

CREATE TABLE inventory(
  beerID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(500),
  containers_per_pack INT,
  container_size VARCHAR(200),
  container_type VARCHAR(100),
  category VARCHAR(200),
  packs_per_case INT;
)

CREATE TABLE purchasing_details(
  dt DATETIME DEFAULT CURRENT_TIMESTAMP,
  quantity_available FLOAT,
  retail_price FLOAT,
  case_retail_price FLOAT,
  id INT NOT NULL FOREIGN KEY REFERENCES Inventory(beerID);
)

-- Rename fields
CREATE INDEX AUTHOR_INDEX
ON Inventory_availability(dt);
