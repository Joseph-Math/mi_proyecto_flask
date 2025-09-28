CREATE DATABASE IF NOT EXISTS desarrollo_web CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE desarrollo_web;

CREATE TABLE IF NOT EXISTS productos (
  id_producto INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(255) NOT NULL,
  precio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  stock INT NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(150) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

-- Usuario administrador demo (usuario: admin, contraseña: admin123)
INSERT INTO usuarios (username, password) VALUES ('admin', 'scrypt:32768:8:1$jcFPAFSD2UnvCr48$12df8b663a3351f5b580e44d22c62c2c611a6aa58cec6dbee52d3fb7aef6263eb76dfae08f750500479d646e0290bb6e9c59dc4d6e5f10f335e39c8ea6c42cae');
