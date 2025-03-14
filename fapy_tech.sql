-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-03-2025 a las 04:08:36
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fapy_tech`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `iphone`
--

CREATE TABLE `iphone` (
  `IMEI` char(15) NOT NULL,
  `modelo` varchar(10) NOT NULL,
  `color` varchar(10) NOT NULL,
  `gb` smallint(4) NOT NULL,
  `bateria` tinyint(2) NOT NULL,
  `precio` smallint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `iphone`
--

INSERT INTO `iphone` (`IMEI`, `modelo`, `color`, `gb`, `bateria`, `precio`) VALUES
('416335163166161', '12', 'green', 128, 80, 310),
('423432423423424', '11 pro', 'green', 128, 76, 260),
('454564651351564', '13', 'pink', 128, 79, 400),
('753232131212347', '13 pro', 'white', 256, 80, 520);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `iphone`
--
ALTER TABLE `iphone`
  ADD PRIMARY KEY (`IMEI`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
