-- Base de datos corregida para phpMyAdmin
CREATE DATABASE IF NOT EXISTS `liceo_policial` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `liceo_policial`;
-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: liceo_policial
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.22.04.1

-- Este archivo contiene la exportación de la base de datos 'liceo_policial'
-- La base de datos fue exportada usando phpMyAdmin 4.9.0.1

--
-- Estructura de la tabla `asistencia`
--

CREATE TABLE `asistencia` (
  `id_asistencia` int(11) NOT NULL,
  `fecha_asistencia` date NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL,
  `estado_asistencia` tinyint(1) NOT NULL COMMENT '1: Presente, 0: Ausente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla para el registro de asistencia de los alumnos.';

--
-- Volcado de datos para la tabla `asistencia`
--

INSERT INTO `asistencia` (`id_asistencia`, `fecha_asistencia`, `id_alumno`, `id_curso`, `estado_asistencia`) VALUES
(1, '2023-08-01', 1, 1, 1),
(2, '2023-08-01', 2, 2, 1),
(3, '2023-08-01', 3, 3, 1),
(4, '2023-08-02', 1, 1, 1),
(5, '2023-08-02', 2, 2, 0);

-- --------------------------------------------------------

--
-- Estructura de la tabla `calificaciones`
--

CREATE TABLE `calificaciones` (
  `id_calificacion` int(11) NOT NULL,
  `nota` decimal(4,2) NOT NULL,
  `fecha_calificacion` date NOT NULL,
  `id_alumno` int(11) NOT NULL,
  `id_curso` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla que almacena las notas de los alumnos.';

--
-- Volcado de datos para la tabla `calificaciones`
--

INSERT INTO `calificaciones` (`id_calificacion`, `nota`, `fecha_calificacion`, `id_alumno`, `id_curso`) VALUES
(1, '8.50', '2023-07-25', 1, 1),
(2, '7.80', '2023-07-25', 2, 2),
(3, '9.00', '2023-07-25', 3, 3),
(4, '6.50', '2023-08-02', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de la tabla `cursos`
--

CREATE TABLE `cursos` (
  `id_curso` int(11) NOT NULL,
  `nombre_curso` varchar(100) NOT NULL,
  `id_profesor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tabla de los cursos que se imparten en el liceo.';

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`id_curso`, `nombre_curso`, `id_profesor`) VALUES
(1, 'Matemáticas', 1),
(2, 'Física', 2),
(3, 'Química', 3);

-- --------------------------------------------------------

--
-- Estructura de la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_estudiante` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `grado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Información de los alumnos matriculados.';

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id_estudiante`, `nombre`, `apellido`, `fecha_nacimiento`, `grado`) VALUES
(1, 'Juan', 'Pérez', '2005-03-15', '10º'),
(2, 'Ana', 'Gómez', '2006-01-20', '11º'),
(3, 'Carlos', 'López', '2005-09-10', '10º');

-- --------------------------------------------------------

--
-- Estructura de la tabla `profesores`
--

CREATE TABLE `profesores` (
  `id_profesor` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `especialidad` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Información del personal docente.';

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`id_profesor`, `nombre`, `apellido`, `especialidad`) VALUES
(1, 'Maria', 'Garcia', 'Matemáticas'),
(2, 'Pedro', 'Sanchez', 'Física'),
(3, 'Laura', 'Diaz', 'Química');

-- --------------------------------------------------------

--
-- Índices de las tablas volcadas
--

--
-- Indices de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id_asistencia`);

--
-- Indices de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD PRIMARY KEY (`id_calificacion`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id_curso`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_estudiante`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`id_profesor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `id_asistencia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  MODIFY `id_calificacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id_curso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id_estudiante` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `id_profesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD CONSTRAINT `fk_asistencia_estudiante` FOREIGN KEY (`id_alumno`) REFERENCES `estudiantes` (`id_estudiante`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_asistencia_cursos` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `calificaciones`
--
ALTER TABLE `calificaciones`
  ADD CONSTRAINT `fk_calificaciones_estudiante` FOREIGN KEY (`id_alumno`) REFERENCES `estudiantes` (`id_estudiante`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_calificaciones_cursos` FOREIGN KEY (`id_curso`) REFERENCES `cursos` (`id_curso`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD CONSTRAINT `fk_cursos_profesor` FOREIGN KEY (`id_profesor`) REFERENCES `profesores` (`id_profesor`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;
=======
-- Base de datos liceo_policial
CREATE DATABASE IF NOT EXISTS liceo_policial;
USE liceo_policial;

-- Tabla usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    mail VARCHAR(100) NOT NULL
);

-- Tabla roles
CREATE TABLE IF NOT EXISTS roles (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL
);

-- Tabla estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    curso_id INT
);
>>>>>>> db1b010 (Agregar script de base de datos liceo_policial)
