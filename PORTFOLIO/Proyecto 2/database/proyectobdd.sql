CREATE DATABASE sistema_ventas;
USE sistema_ventas;

CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    UNIQUE(nombre) 
);
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE, 
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(40) NOT NULL
);
CREATE TABLE Ordenes (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_producto INT NOT NULL,
    fecha DATE NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) ON DELETE RESTRICT ON UPDATE CASCADE
);


INSERT INTO Productos (nombre, categoria, precio, stock) VALUES
('Laptop', 'Electrónica', 1200.00, 50),
('Mouse', 'Electrónica', 25.00, 200),
('Teclado', 'Electrónica', 45.00, 150),
('Monitor', 'Electrónica', 300.00, 100),
('Silla Gamer', 'Muebles', 150.00, 20),
('Escritorio', 'Muebles', 200.00, 15),
('Auriculares', 'Electrónica', 80.00, 80),
('Cargador', 'Electrónica', 20.00, 100),
('Smartphone', 'Electrónica', 700.00, 30),
('Tablet', 'Electrónica', 400.00, 25);
INSERT INTO Clientes (nombre, email, telefono, direccion) VALUES
('Juan Pérez', 'juan@example.com', '123456789', 'Calle Falsa 123'),
('María López', 'maria@example.com', '987654321', 'Av. Siempre Viva 742'),
('Pedro Sánchez', 'pedro@example.com', '456789123', 'Calle Arcoiris 56'),
('Ana Gómez', 'ana@example.com', '789123456', 'Av. Del Sol 123'),
('Luis Torres', 'luis@example.com', '321654987', 'Calle Luna 45'),
('Laura Rivera', 'laura@example.com', '654987321', 'Calle Estrella 78'),
('Ricardo Díaz', 'ricardo@example.com', '963852741', 'Calle Cometa 90'),
('Sofía Vega', 'sofia@example.com', '852741963', 'Av. Galaxia 12'),
('Carlos Fernández', 'carlos@example.com', '147258369', 'Calle Planeta 34'),
('Gabriela Martínez', 'gabriela@example.com', '369258147', 'Calle Universo 56');
INSERT INTO Ordenes (id_cliente, id_producto, fecha, cantidad) VALUES
(1, 1, '2024-11-01', 2),
(1, 3, '2024-11-02', 1),
(1, 5, '2024-11-03', 1),
(1, 8, '2024-11-04', 3),
(2, 2, '2024-11-01', 5),
(2, 4, '2024-11-03', 2),
(2, 7, '2024-11-05', 1),
(3, 6, '2024-11-01', 1),
(3, 9, '2024-11-02', 2),
(3, 10, '2024-11-04', 1),
(3, 3, '2024-11-06', 4),
(4, 5, '2024-11-01', 1),
(4, 8, '2024-11-02', 3),
(4, 10, '2024-11-03', 1),
(5, 2, '2024-11-02', 6),
(5, 4, '2024-11-04', 2),
(5, 1, '2024-11-05', 1),
(6, 7, '2024-11-01', 2),
(6, 9, '2024-11-03', 3),
(6, 10, '2024-11-04', 2),
(7, 5, '2024-11-02', 1),
(7, 6, '2024-11-03', 4),
(7, 8, '2024-11-04', 2),
(8, 2, '2024-11-01', 3),
(8, 4, '2024-11-02', 2),
(8, 7, '2024-11-03', 1),
(9, 1, '2024-11-02', 2),
(9, 3, '2024-11-03', 1),
(9, 5, '2024-11-04', 4),
(10, 2, '2024-11-01', 5),
(10, 4, '2024-11-02', 2),
(10, 8, '2024-11-03', 3);


CREATE INDEX idx_producto_nombre ON Productos(nombre);
CREATE INDEX idx_cliente_email ON Clientes(email);
CREATE INDEX idx_orden_cliente_producto ON Ordenes(id_cliente, id_producto);


-- GESTION DE PRODUCTOS
DELIMITER // 
CREATE PROCEDURE AgregarProducto (
    IN nombre_prod VARCHAR(100),
    IN categoria_prod VARCHAR(50),
    IN precio_prod DECIMAL(10, 2),
    IN stock_prod INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;
    START TRANSACTION;
    INSERT INTO Productos (nombre, categoria, precio, stock)
    VALUES (nombre_prod, categoria_prod, precio_prod, stock_prod);
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarProducto (
    IN id_prod INT,
    IN nuevo_nombre VARCHAR(100),
    IN nueva_categoria VARCHAR(50),
    IN nuevo_precio DECIMAL(10, 2),
    IN nuevo_stock INT
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;
    START TRANSACTION;
    UPDATE Productos
    SET 
        nombre = nuevo_nombre,
        categoria = nueva_categoria,
        precio = nuevo_precio,
        stock = nuevo_stock
    WHERE id_producto = id_prod;
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE VerProductos()
BEGIN
    SELECT * FROM Productos;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE EliminarProducto (IN id_prod INT)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;
    START TRANSACTION;
    DELETE FROM Productos WHERE id_producto = id_prod;
    COMMIT;
END //
DELIMITER ;


-- GESTION DE CLIENTES
DELIMITER //
CREATE PROCEDURE RegistrarCliente (
    IN nombre_cli VARCHAR(100),
    IN email_cli VARCHAR(100),
    IN telefono_cli VARCHAR(15),
    IN direccion_cli VARCHAR(50)
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;
    START TRANSACTION;
    INSERT INTO Clientes (nombre, email, telefono, direccion)
    VALUES (nombre_cli, email_cli, telefono_cli, direccion_cli);
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarCliente (
    IN id_cli INT,
    IN nuevo_nombre VARCHAR(100),
    IN nuevo_email VARCHAR(100),
    IN nuevo_telefono VARCHAR(15),
    IN nuvea_direccion VARCHAR(50)
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;
    START TRANSACTION;
    UPDATE Clientes
    SET 
        nombre = nuevo_nombre,
        email = nuevo_email,
        telefono = nuevo_telefono,
        direccion = nuvea_direccion
    WHERE id_cliente = id_cli;
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE VerClientes()
BEGIN
    SELECT * FROM Clientes;
END //
DELIMITER ;


-- PROCESAMIENTO DE ORDENES
DELIMITER //
CREATE PROCEDURE MostrarOrdenesPorCliente(IN id_cliente INT)
BEGIN
    SELECT 
        o.id_orden,
        p.nombre AS producto,
        o.fecha,
        o.cantidad
    FROM 
        Ordenes o
    INNER JOIN 
        Productos p ON o.id_producto = p.id_producto
    WHERE 
        o.id_cliente = id_cliente;
END //
DELIMITER ;


-- CONSULTAS AVANZADAS
DELIMITER //
CREATE PROCEDURE ProductosMasVendidos()
BEGIN
    SELECT 
        p.nombre AS producto,
        SUM(o.cantidad) AS total_vendido
    FROM 
        Ordenes o
    INNER JOIN 
        Productos p ON o.id_producto = p.id_producto
    GROUP BY 
        p.id_producto
    ORDER BY 
        total_vendido DESC;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ConsultarStockProducto(IN id_producto INT)
BEGIN
    SELECT 
        p.nombre AS producto,
        p.stock AS stock_disponible
    FROM 
        Productos p
    WHERE 
        p.id_producto = id_producto;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ClientesConMasOrdenes()
BEGIN
    SELECT 
        c.nombre AS cliente,
        COUNT(o.id_orden) AS total_ordenes
    FROM 
        Clientes c
    LEFT JOIN 
        Ordenes o ON c.id_cliente = o.id_cliente
    GROUP BY 
        c.id_cliente
    HAVING 
        total_ordenes > 0
    ORDER BY 
        total_ordenes DESC;
END //
DELIMITER ;


-- REPORTE DE PRODUCTOS MAS VENDIDOS
DELIMITER //
CREATE PROCEDURE ReporteProductoMasVendido()
BEGIN
    SELECT 
        p.nombre AS producto,
        SUM(o.cantidad) AS total_vendido
    FROM 
        Ordenes o
    INNER JOIN 
        Productos p ON o.id_producto = p.id_producto
    GROUP BY 
        p.id_producto
    ORDER BY 
        total_vendido DESC
    LIMIT 1;  -- Solo el producto más vendido
END //
DELIMITER ;


-- MODIFICACION DE VALOR DE UN PRODUCTO
DELIMITER //
CREATE PROCEDURE ModificarOrdenesProducto(
    IN id_producto INT,      
    IN cantidad_maxima INT   
)
BEGIN
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;
    START TRANSACTION;
    UPDATE 
        Ordenes
    SET 
        cantidad = LEAST(cantidad, cantidad_maxima) 
    WHERE 
        id_producto = id_producto;  
    COMMIT;
END //
DELIMITER 