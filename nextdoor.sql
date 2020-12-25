-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Дек 25 2020 г., 11:15
-- Версия сервера: 10.4.17-MariaDB
-- Версия PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `db_test`
--

-- --------------------------------------------------------

--
-- Структура таблицы `nextdoor`
--

CREATE TABLE `nextdoor` (
  `id_` varchar(24) NOT NULL,
  `name_` varchar(45) DEFAULT NULL,
  `address` varchar(90) DEFAULT NULL,
  `phone` varchar(16) DEFAULT NULL,
  `website` varchar(45) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `nextdoor`
--

INSERT INTO `nextdoor` (`id_`, `name_`, `address`, `phone`, `website`, `category`) VALUES
('business_15371698', 'Five Guys', '4480 W 121st Ave\nBroomfield, CO 80020', NULL, NULL, 'Burger restaurant'),
('business_17786506', 'Famous Dave\'s Bar-B-Que', '3250 W Frye Rd\nChandler, AZ 85226', NULL, NULL, 'Barbecue restaurant'),
('business_26505533', 'Cheddar\'s Scratch Kitchen', '10250 Grant St\nThornton, CO 80229', '303-280-2307', 'http://www.cheddars.com/', 'Restaurant | Kid-friendly restaurant');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `nextdoor`
--
ALTER TABLE `nextdoor`
  ADD UNIQUE KEY `id_` (`id_`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
