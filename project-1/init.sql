CREATE TABLE IF NOT EXISTS page_counter (
    id INT PRIMARY KEY AUTO_INCREMENT,
    count INT NOT NULL DEFAULT 0
);

INSERT INTO page_counter (id, count) VALUES (1, 0);
