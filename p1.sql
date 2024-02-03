
--Creacion de las tablas
CREATE TABLE Status (
    id INT PRIMARY KEY,
    status_name VARCHAR(255) NOT NULL
);

CREATE TABLE Player (
    id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    status_id INT,
    FOREIGN KEY (status_id) REFERENCES Status(id)
);


INSERT INTO Status (id, status_name) VALUES (1, 'Activo');
INSERT INTO Status (id, status_name) VALUES (2, 'Lesionado');
INSERT INTO Status (id, status_name) VALUES (3, 'Suspendido');
INSERT INTO Status (id, status_name) VALUES (4, 'Retirado');

INSERT INTO Player (id, first_name, last_name, status_id) VALUES (1, 'Carlos', 'Urrutia', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (2, 'Ana', 'García', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (3, 'Luis', 'Pérez', 2);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (4, 'Miguel', 'Hernández', 3);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (5, 'Sofía', 'Martínez', 4);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (6, 'Lucía', 'Jiménez', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (7, 'Fernando', 'Ugalde', 2);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (8, 'Daniela', 'Vázquez', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (9, 'Juan', 'Morales', 3);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (10, 'Gabriela', 'Castro', 4);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (11, 'Javier', 'Urbina', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (12, 'Patricia', 'Ortega', 2);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (13, 'Manuel', 'Ruiz', 3);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (14, 'Laura', 'Moreno', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (15, 'Sergio', 'Ureña', 4);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (16, 'María', 'Navarro', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (17, 'Antonio', 'Díaz', 2);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (18, 'Jose', 'Urrutia', 3);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (19, 'Teresa', 'Romero', 1);
INSERT INTO Player (id, first_name, last_name, status_id) VALUES (20, 'David', 'González', 4);


-- Selecciona a todos los jugadores cuyo apellido comienza con 'U'
SELECT *
FROM Player
WHERE last_name LIKE 'U%';

-- Selecciona a todos los jugadores y muestra su nombre completo junto con el nombre del estado
-- Se une la tabla 'Player' con la tabla 'Status' a través de 'status_id'
SELECT CONCAT(first_name, ' ', last_name) AS nombre_completo, 
       s.status_name
FROM Player p
JOIN Status s ON p.status_id = s.id;

-- La misma selección que la anterior pero ordenada por el nombre completo del jugador
SELECT CONCAT(first_name, ' ', last_name) AS nombre_completo, 
       s.status_name
FROM Player p
JOIN Status s ON p.status_id = s.id
ORDER BY nombre_completo;

-- Combinación de las consultas para mostrar solo los jugadores cuyo apellido comienza con 'U'
-- Mostrando su nombre completo y estado, y ordenando por el nombre completo
SELECT CONCAT(first_name, ' ', last_name) AS nombre_completo, 
       s.status_name
FROM Player p
JOIN Status s ON p.status_id = s.id
WHERE last_name LIKE 'U%'
ORDER BY nombre_completo;