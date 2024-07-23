-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-07-2024 a las 06:38:08
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
-- Base de datos: `bd2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prueba`
--

CREATE TABLE `prueba` (
  `id` int(50) NOT NULL,
  `pelicula` mediumtext NOT NULL,
  `imagen` mediumtext NOT NULL,
  `Horario1` varchar(250) NOT NULL,
  `Horario2` varchar(250) NOT NULL,
  `Horario3` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prueba`
--

INSERT INTO `prueba` (`id`, `pelicula`, `imagen`, `Horario1`, `Horario2`, `Horario3`) VALUES
(1, 'Spiderman No Way Home', '1.jpg\r\n', 'Funcion 14:00', 'Funcion 15:00', 'Funcion 17:00'),
(2, 'Deadpool and Wolverine', '2.jpg', 'Funcion 11:00', 'Funcion 15:00', 'Funcion 17:00'),
(3, 'Venom: The Last Dance', '3.jpg', 'Funcion 12:00', 'Funcion 16:00', 'Funcion 19:00'),
(4, 'Dragon ball', 'db.jpeg', 'Funcion 11:00', 'Funcion 13:00', 'Funcion 18:00'),
(5, 'El libro de la vida', 'uwu.jpeg', 'Funcion 12:00', 'Funcion 17:00', 'Funcion 19:00');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `prueba`
--
ALTER TABLE `prueba`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
