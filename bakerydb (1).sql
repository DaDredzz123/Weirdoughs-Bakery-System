-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 19, 2025 at 02:21 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bakerydb`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `customer_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`customer_id`, `name`, `email`, `phone`, `address`, `created_at`) VALUES
(1, 'l', 'l', '0909', '', '2025-12-05 11:41:36'),
(2, 'l', 'l', 'l09090', '', '2025-12-05 11:45:34'),
(3, 'l', 'l', '9090', '', '2025-12-05 11:48:15'),
(4, 'l', 'l', '09009', '', '2025-12-05 11:53:27'),
(5, 'l', 'l', '0909', '', '2025-12-05 11:54:11'),
(6, 'l', 'l', '0909', '', '2025-12-05 11:54:27'),
(7, 'l', 'l', '0908', '', '2025-12-05 11:58:27'),
(8, 'l', 'l', '0909', '', '2025-12-05 11:59:12'),
(9, 'l', 'l', '0909', '', '2025-12-05 12:03:44'),
(10, 'l', 'l', '0909', '', '2025-12-05 12:04:38'),
(11, 'l', 'l', '0909', '', '2025-12-05 12:09:40'),
(12, 'l', 'l', '0909', '', '2025-12-05 12:11:55'),
(13, 'l', 'l', '09009', '', '2025-12-05 12:13:50'),
(14, 'l', 'l', '0909', '', '2025-12-05 12:14:29'),
(15, 'l', 'l', '0909', '', '2025-12-05 12:15:18'),
(16, 'l', 'l', '0909', '', '2025-12-05 12:16:09'),
(17, 'l', 'l', '0909', '', '2025-12-05 12:17:24'),
(18, 'l', 'l', '0909', '', '2025-12-05 12:21:18'),
(19, 'l', 'l', '0909', '', '2025-12-05 12:23:15'),
(20, 'l', 'l', '0909', '', '2025-12-05 12:25:30'),
(21, 'l', 'l', '0909', '', '2025-12-05 12:26:27'),
(22, 'q', 'q', '123', '', '2025-12-05 12:31:08'),
(23, 'q', 'q', '12', '', '2025-12-05 12:32:22'),
(24, 'q', 'q', '123', '', '2025-12-05 12:33:07'),
(25, 'q', 'q', '12', '', '2025-12-05 12:33:40'),
(26, 'q', 'q', '12', '', '2025-12-05 12:34:37'),
(27, 'q', 'q', '1', '', '2025-12-05 12:35:28'),
(28, 'q', 'q', '12', '', '2025-12-05 12:35:55'),
(29, 'q', 'q', '12', '', '2025-12-05 12:36:13'),
(30, 'q', 'q', '12', '', '2025-12-05 12:36:30'),
(31, 'q', 'q1', '12', '', '2025-12-05 12:36:56'),
(32, 'q', 'q', '12', '', '2025-12-05 12:37:41'),
(33, 'q', 'q', '12', '', '2025-12-05 12:38:06'),
(34, 'Q', 'Q', '12', '', '2025-12-05 12:39:30'),
(35, 'q', 'q', '12', '', '2025-12-05 12:39:54'),
(36, 'q', 'q', '12', '', '2025-12-05 12:40:38'),
(37, 'q', 'q', '12', '', '2025-12-05 12:41:40'),
(38, 'q', 'q', '12', '', '2025-12-05 12:42:13'),
(39, 'q', 'q', '12', '', '2025-12-05 12:42:34'),
(40, 'q', 'q', '12', '', '2025-12-05 12:43:01'),
(41, 'q', 'q', 'q12', '', '2025-12-05 12:43:55'),
(42, 'q', 'q', 'q12', '', '2025-12-05 12:44:35'),
(43, 'q', 'q', '12', '', '2025-12-05 12:45:29'),
(44, 'q', 'q', '12', '', '2025-12-05 12:45:58'),
(45, 'w', 'qq', '12', '', '2025-12-05 12:46:38'),
(46, 'q', 'q', '12', '', '2025-12-05 12:47:25'),
(47, 'q', 'q', '12', '', '2025-12-05 12:47:45'),
(48, 'q', 'q', '12', '', '2025-12-05 12:48:04'),
(49, 'q', 'q', '12', '', '2025-12-05 12:48:45'),
(50, 'q', 'q', '12', '', '2025-12-05 12:49:27'),
(51, 'q', 'q', '12', '', '2025-12-05 12:49:42'),
(52, 'q', 'q', '12', '', '2025-12-05 12:50:08'),
(53, 'q', 'q', '12', '', '2025-12-05 12:50:28'),
(54, 'q', 'q', '12', '', '2025-12-05 12:51:11'),
(55, 'q', 'q', '12', '', '2025-12-05 12:51:44'),
(56, 'q', 'q', '12', '', '2025-12-05 12:52:04'),
(57, 'q', 'q', '12', '', '2025-12-05 12:52:29'),
(58, 'q', 'q', '12', '', '2025-12-05 12:53:01'),
(59, 'q', 'q', '12', '', '2025-12-05 12:53:19'),
(60, 'q', 'q12', '12', '', '2025-12-05 12:53:43'),
(61, '12', '12', '12', '', '2025-12-05 12:54:13'),
(62, 'q', 'q', '12', '', '2025-12-05 12:54:34'),
(63, 'q', 'q', '12', '', '2025-12-05 12:55:07'),
(64, 'q', 'q', '12', '', '2025-12-05 12:56:03'),
(65, 'q', 'q', '12', '', '2025-12-05 12:56:27'),
(66, 'q', 'q', '12', '', '2025-12-05 12:57:00'),
(67, 'q', 'q', '12', '', '2025-12-05 12:57:29'),
(68, 'q', 'q', '12', '', '2025-12-05 12:58:05'),
(69, 'q', 'q', '12', '', '2025-12-05 12:58:34'),
(70, 'q', 'q', '12', '', '2025-12-05 12:59:28'),
(71, 'q', 'q', '12', '', '2025-12-05 12:59:46'),
(72, 'q', 'q', '12', '', '2025-12-05 13:00:21'),
(73, 'q', 'q', '12', '', '2025-12-05 13:00:38'),
(74, 'q', 'q', '12', '', '2025-12-05 13:00:57'),
(75, 'q', 'q', '12', '', '2025-12-05 13:01:22'),
(76, 'q', 'q', '12', '', '2025-12-05 13:01:42'),
(77, 'q', 'q', '12', '', '2025-12-05 13:02:06'),
(78, 'q', 'q', '12', '', '2025-12-05 13:02:24'),
(79, 'q', 'q', '12', '', '2025-12-05 13:02:52'),
(80, 'q', 'q', '12', '', '2025-12-05 13:03:15'),
(81, 'q', 'q', 'q12', '', '2025-12-05 13:04:06'),
(82, 'q', 'q', '12', '', '2025-12-05 13:04:38'),
(83, 'q', 'q', '12', '', '2025-12-05 13:05:10'),
(84, 'q', 'q', 'q', '', '2025-12-05 13:05:38'),
(85, 'q', 'q', '12', '', '2025-12-05 13:06:06'),
(86, 'q', 'q', '12', '', '2025-12-05 13:06:44'),
(87, 'q', 'q', '12', '', '2025-12-05 13:07:39'),
(88, 'q', 'q', '12', '', '2025-12-05 13:08:05'),
(89, 'q', 'q', '12', '', '2025-12-05 13:08:29'),
(90, 'q', 'q', '12', '', '2025-12-05 13:08:49'),
(91, 'q', 'q', '12', '', '2025-12-05 13:09:06'),
(92, 'jeje', 'qwqwe', '1231', '', '2025-12-05 13:11:26'),
(93, 'jeje', 'awdad', '2131', '', '2025-12-05 13:11:54'),
(94, 'wew', 'weww', '2342', '', '2025-12-05 13:12:14'),
(95, 'qwq', 'qwqw', '121', '', '2025-12-05 13:12:35'),
(96, 'q', 'q', '12', '', '2025-12-05 13:13:40'),
(97, 'w', 'w', '21', '', '2025-12-05 13:14:15'),
(98, 'q', 'q', '12', '', '2025-12-05 13:15:00'),
(99, 'q', 'q', '12', '', '2025-12-05 13:15:22'),
(100, 'q', 'q', '12', '', '2025-12-05 13:15:45'),
(101, 'q', 'q', '12', '', '2025-12-05 13:16:20'),
(102, 'q', 'q', 'q', '', '2025-12-05 13:16:56'),
(103, 'q', 'q', '12', '', '2025-12-05 13:17:12'),
(104, 'q', 'q', '12', '', '2025-12-05 13:17:31'),
(105, 'q', 'q', '12', '', '2025-12-05 13:17:59'),
(106, 'q', 'q', '12', '', '2025-12-05 13:18:33'),
(107, 'q', 'q', '12', '', '2025-12-05 13:18:53'),
(108, 'q', 'q', '12', '', '2025-12-05 13:19:26'),
(109, 'q', 'q', '12', '', '2025-12-05 13:19:46'),
(110, 'qq', 'q', 'q1', '', '2025-12-05 13:20:27'),
(111, 'q', 'q', '12', '', '2025-12-05 13:20:46'),
(112, 'a', 'a', 'a21', '', '2025-12-05 13:21:02'),
(113, 'a', 'a', 'q2', '', '2025-12-05 13:21:34'),
(114, 'q', 'q', '12', '', '2025-12-05 13:22:10'),
(115, 'q', 'q', '12', '', '2025-12-05 13:22:31'),
(116, 'q', 'q', '12', '', '2025-12-05 13:22:54'),
(117, 'q', 'q', '12', '', '2025-12-05 13:23:19'),
(118, 'q', 'q', '12', '', '2025-12-05 13:23:57'),
(119, 'a', 'a', '2', '', '2025-12-05 13:24:15'),
(120, 'q', 'q', '12', '', '2025-12-05 13:24:38'),
(121, 'q', 'q', '12', '', '2025-12-05 13:24:55'),
(122, 'q', 'q', '12', '', '2025-12-05 13:25:24'),
(123, 'q', 'q', '21', '', '2025-12-05 13:26:17'),
(124, 'q', 'q', '12', '', '2025-12-05 13:26:40'),
(125, 'qw', 'qw', 'qw12', '', '2025-12-05 13:26:59'),
(126, 'q', 'q', 'wq1', '', '2025-12-05 13:27:19'),
(127, 'qQ', 'q', 'q12', '', '2025-12-05 13:27:37'),
(128, 'qq', 'q', 'q', '', '2025-12-05 13:27:51'),
(129, 'qq', 'q', 'q', '', '2025-12-05 13:28:20'),
(130, 'q', 'a', 'a', '', '2025-12-05 13:28:38'),
(131, 'q', 'q', '12', '', '2025-12-05 13:29:04'),
(132, 'q', 'q', '1', '', '2025-12-05 13:29:49'),
(133, 'qq', 'q', 'q', '', '2025-12-05 13:30:14'),
(134, 'a', 'q', 'qqqq', '', '2025-12-05 13:30:39'),
(135, 'q', 'q', 'q', '', '2025-12-05 13:30:56'),
(136, 'q', 'q', 'q12', '', '2025-12-05 13:31:32'),
(137, 'q', 'q', '12', '', '2025-12-05 13:32:11'),
(138, 'q', 'q', '12', '', '2025-12-05 13:32:32'),
(139, 'a', 'a', 'a', '', '2025-12-05 13:33:00'),
(140, 'Ljc', 'basta', '123456', '', '2025-12-05 13:37:57'),
(141, 'hhkjg', 'jyguygy', '123456', '', '2025-12-05 13:40:31'),
(142, 'k,knyu,', 'ju', '123', '', '2025-12-05 13:41:39'),
(143, 'sjdfkshdf', 'sdfsdf', '23132', '', '2025-12-05 13:54:49'),
(144, 'gsgs', 'sdg', '1212', '', '2025-12-05 13:57:07'),
(145, 'sfasfa', 'asfasf', '111', '', '2025-12-05 14:04:31'),
(146, 'dasdas', 'asdasd', '123', '', '2025-12-05 14:08:22'),
(147, 'dsdg', 'sdgsdg', '123', '', '2025-12-05 14:09:43'),
(148, 'hsdfgh', 'dfgdfh', '5445', '', '2025-12-05 14:10:17'),
(149, 'fasfas', 'asfasf', '12', '', '2025-12-05 14:10:51'),
(150, 'fsdfsd', 'sdfsdf', '12', '', '2025-12-05 14:15:43'),
(151, 'FASFA', 'AFSFAS', '23', '', '2025-12-05 14:16:48'),
(152, 'aasfa', 'asfasf', 'a321', '', '2025-12-05 14:17:23'),
(153, 'asfasf', 'asfasf', '12', '', '2025-12-05 14:23:03'),
(154, 'fasfasa', 'fasfasf', 'asf1231', '', '2025-12-05 14:23:36'),
(155, 'ssf', 'asfas', '312321', '', '2025-12-05 14:26:03'),
(156, 'sadasd', 'asas', '31', '', '2025-12-05 14:27:36'),
(157, 'scasc', 'ascasc', '1231', '', '2025-12-05 14:30:22'),
(158, 'fasfas', 'asfasf', '32', '', '2025-12-05 14:31:47'),
(159, 'safasf', 'asfasf', '3153', '', '2025-12-05 14:32:05'),
(160, 'kljkl', 'dfgsg', '213', '', '2025-12-05 14:33:05'),
(161, 'ASFASF', 'ASFASF', '1321', '', '2025-12-05 14:33:46'),
(162, 'jhgjv', 'dvsdv', '3213', '', '2025-12-05 14:34:41'),
(163, 'sdsd', 'sdsd', '131', '', '2025-12-05 14:35:05'),
(164, 'dvsdfsd', 'sdfsdf', '32', '', '2025-12-05 14:35:46'),
(165, 'dsgsdg', 'sdgsdg', '2313', '', '2025-12-05 14:36:13'),
(166, 'sfsfe', 'fsefe', '132', '', '2025-12-05 14:37:48'),
(167, 'fafas', 'sdvsdv', '2313', '', '2025-12-05 14:39:09'),
(168, 'fafa', 'sedfe', 's3213', '', '2025-12-05 14:39:48'),
(169, 'cczxc', 'dsvsd', '231', '', '2025-12-05 14:40:27'),
(170, 'sacasc', 'ascvasvc', '132', '', '2025-12-05 14:40:53'),
(171, 'vsdv', 'sdvsdv', '123', '', '2025-12-05 14:41:42'),
(172, 'adfasf', 'asfasf', '123', '', '2025-12-05 14:42:00'),
(173, 'scascv', 'ascasc', '231', '', '2025-12-05 14:42:27'),
(174, 'jvbkj', 'bnbn', '1231', '', '2025-12-05 14:42:50'),
(175, 'ACASC', 'ASVCASDV', '1231', '', '2025-12-05 14:43:51'),
(176, 'CSASCAS', 'CASCA', '23', '', '2025-12-05 14:44:17'),
(177, 'ZX XZ', 'CSC', '123', '', '2025-12-05 14:44:50'),
(178, 'BDBDF', 'DBFB', '123', '', '2025-12-05 14:45:17'),
(179, 'SVASV', 'AVASV', '123', '', '2025-12-05 14:45:36'),
(180, 'SCAS', 'VASDVA', '231', '', '2025-12-05 14:45:57'),
(181, 'CASCA', 'ASCAS', '132', '', '2025-12-05 14:46:15'),
(182, 'ASVASV', 'ASVASV', '1321', '', '2025-12-05 14:46:31'),
(183, 'SVASVA', 'AVSV', '434', '', '2025-12-05 14:47:02'),
(184, 'SVCASV', 'ASVAS', '3213', '', '2025-12-05 14:47:19'),
(185, 'CASCAS', 'SCASC', 'SAC', '', '2025-12-05 14:47:51'),
(186, 'ASCAS', 'CASCAS', '213', '', '2025-12-05 14:48:19'),
(187, 'SACAS', 'CASCAS', '3543', '', '2025-12-05 14:48:40'),
(188, 'FAFA', 'CASV', '145654', '', '2025-12-05 14:49:09'),
(189, 'ASCASC', 'ASCAS', '3213', '', '2025-12-05 14:49:31'),
(190, 'ASAS', 'SAC', '12', '', '2025-12-05 14:49:48'),
(191, 'ASFAS', 'ASFASF', '21121', '', '2025-12-05 14:50:11'),
(192, 'sfasf', 'afas', '2112', '', '2025-12-05 14:51:23'),
(193, 'sdasd', 'asfsaf', '123', '', '2025-12-05 14:51:51'),
(194, 'ASDASD', 'ASDAS', '32121', '', '2025-12-05 14:52:39'),
(195, 'JHGJG', 'KJB', '1234', '', '2025-12-05 14:53:15'),
(196, 'JKHKJH', 'FSDF', '23', '', '2025-12-05 14:54:06'),
(197, 'GHF', 'HGF', '213', '', '2025-12-05 14:54:55'),
(198, 'HFHF', 'GHJ', '2123', '', '2025-12-05 14:55:46'),
(199, 'ASFASF', 'SFASF', '1233', '', '2025-12-05 14:56:07'),
(200, 'ASFAS', 'SFASF', '45', '', '2025-12-05 14:57:03'),
(201, 'SDVSDV', 'SVSDV', '1231', '', '2025-12-05 14:57:25'),
(202, 'DASF', 'SDFSDF', '12313', '', '2025-12-05 14:57:45'),
(203, 'asasc', 'sdcasdvc', '1231', '', '2025-12-05 14:58:45'),
(204, 'ascas', 'ascasc', '3132', '', '2025-12-05 14:59:48'),
(205, 'FASFASF', 'FASF', '123', '', '2025-12-05 15:01:29'),
(206, 'SDASF', 'ASFASF', '1231', '', '2025-12-05 15:13:09'),
(207, 'dasd', 'asddas', '1321', '', '2025-12-05 15:15:25'),
(208, 'l', 'l', '0909', '', '2025-12-05 18:06:45'),
(209, 'l', 'l', '0909', '', '2025-12-05 18:31:50'),
(210, 'l', 'l', '0909', '', '2025-12-06 21:33:46'),
(211, 'l', 'l;', '0909', '', '2025-12-06 21:38:09'),
(212, 'l', 'l', '0909', '', '2025-12-06 21:40:31'),
(213, 'l', 'l', '09090', 'LOL', '2025-12-06 21:43:08'),
(214, 'l', 'l', '0909', '', '2025-12-06 21:46:43'),
(215, 'l', 'l', '0909', '', '2025-12-06 21:47:31'),
(216, 'lol', 'lol', '0909', '', '2025-12-06 21:48:08'),
(217, 'l', 'l', '0909', '', '2025-12-06 21:50:43'),
(218, 'l', 'l', '0909', '', '2025-12-06 21:53:52'),
(219, 'l', 'l', '0909', '', '2025-12-06 21:55:35'),
(220, 'l', 'l', '0909', '', '2025-12-06 21:56:30'),
(221, 'l', 'l', '0909', '', '2025-12-06 21:59:44'),
(222, 'l', 'l', '0909', '', '2025-12-06 22:03:59'),
(223, 'l', 'l', '0909', '', '2025-12-06 22:05:14'),
(224, 'l', 'l', '09090', '', '2025-12-06 22:07:52'),
(225, 'l', 'l', '0909', '', '2025-12-06 22:11:18'),
(226, 'l', 'l', '0909', '', '2025-12-06 22:13:51'),
(227, 'l', 'l', '0909', '', '2025-12-06 22:16:49'),
(228, 'l', 'l', '0909', '', '2025-12-06 22:19:26'),
(229, 'l', 'l', '0909', '', '2025-12-06 22:23:04'),
(230, 'l', 'l', '0909', '', '2025-12-06 22:25:18'),
(231, 'l', 'l', '0909', '', '2025-12-06 22:26:42'),
(232, 'l', 'l', '0909', 'lol', '2025-12-06 22:30:39'),
(233, 'LOL', 'LOL', '0909', 'lol', '2025-12-06 22:34:22'),
(234, 'l', 'l', '0909', 'lol', '2025-12-06 22:37:21'),
(235, 'l', 'l', '0909', 'lol', '2025-12-06 22:40:40'),
(236, 'l', 'l', '0909', '', '2025-12-06 22:43:23'),
(237, 'l', 'l', '0909', 'lol', '2025-12-10 09:37:01'),
(238, 'l', 'l', '0909', '', '2025-12-10 10:22:05'),
(239, 'l', 'l', '0909', '', '2025-12-10 10:22:36'),
(240, 'l', 'l', '0909', '', '2025-12-10 10:23:09'),
(241, 'l', 'l', '0909', '', '2025-12-10 10:23:33'),
(242, 'l', 'l', '0909', '', '2025-12-10 10:24:08'),
(243, 'l', 'l', '0909', '', '2025-12-12 08:59:05'),
(244, 'l', 'l', '0909', 'lol', '2025-12-15 12:19:29'),
(245, 'RED C. BUENAFE', 'RED@LOL.COM', '0909009090', 'UNIVERSITY OF  MINDANAO', '2025-12-16 19:49:15'),
(246, 'RED', 'LOL@LOL.com', '090909', '', '2025-12-17 09:35:18'),
(247, 'Red', 'DADNAL', '09090', 'LOLLLO', '2025-12-17 09:45:39'),
(248, 'RED BUENAFE', 'Redbuenafe@lol.com', '09090090', 'brgy 76-A D.C', '2025-12-17 11:01:39'),
(249, 'Red', 'asdwaa@gmail.com', '098184231112', '', '2025-12-17 11:06:34'),
(250, 'Red', 'lol@lol.com', '090909', 'lol address lol', '2025-12-17 12:48:21'),
(251, 'RED', 'L', '9090', 'lol', '2025-12-17 13:21:46'),
(252, 'red', 'lol@lol', '0990', 'lol', '2025-12-17 13:38:17'),
(253, 'l', 'l', '0909', 'lol', '2025-12-18 13:26:42');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `hire_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `inventory_id` int(11) NOT NULL,
  `item_name` varchar(100) DEFAULT NULL,
  `quantity` decimal(10,2) DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `last_updated` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`inventory_id`, `item_name`, `quantity`, `unit`, `supplier_id`, `last_updated`) VALUES
(1, 'Bread Flour', 150.00, 'kg', 1, '2025-12-05 11:39:35'),
(2, 'Whole Wheat Flour', 100.00, 'kg', 2, '2025-12-05 11:39:35'),
(3, 'Multigrain Mix', 80.00, 'kg', 3, '2025-12-05 11:39:35'),
(4, 'Yeast', 20.00, 'kg', 4, '2025-12-05 11:39:35'),
(5, 'Salt', 25.00, 'kg', 5, '2025-12-05 11:39:35'),
(6, 'Olive Oil', 30.00, 'liters', 6, '2025-12-05 11:39:35'),
(7, 'Butter', 100.00, 'kg', 7, '2025-12-05 11:39:35'),
(8, 'Eggs', 2000.00, 'pcs', 8, '2025-12-05 11:39:35'),
(9, 'Bananas', 50.00, 'kg', 9, '2025-12-05 11:39:35'),
(10, 'Pumpkin Puree', 40.00, 'kg', 10, '2025-12-05 11:39:35'),
(11, 'Zucchini', 30.00, 'kg', 11, '2025-12-05 11:39:35'),
(12, 'All-purpose Flour', 200.00, 'kg', 1, '2025-12-05 11:39:35'),
(13, 'Granulated Sugar', 120.00, 'kg', 2, '2025-12-05 11:39:35'),
(14, 'Brown Sugar', 80.00, 'kg', 2, '2025-12-05 11:39:35'),
(15, 'Cocoa Powder', 30.00, 'kg', 3, '2025-12-05 11:39:35'),
(16, 'Vanilla Extract', 5.00, 'liters', 4, '2025-12-05 11:39:35'),
(17, 'Cream Cheese', 40.00, 'kg', 5, '2025-12-05 11:39:35'),
(18, 'Whipping Cream', 60.00, 'liters', 6, '2025-12-05 11:39:35'),
(19, 'Carrots', 25.00, 'kg', 7, '2025-12-05 11:39:35'),
(20, 'Strawberries', 35.00, 'kg', 8, '2025-12-05 11:39:35'),
(21, 'Lemon Juice', 20.00, 'liters', 9, '2025-12-05 11:39:35'),
(22, 'Cherries', 15.00, 'kg', 10, '2025-12-05 11:39:35'),
(23, 'Cinnamon', 10.00, 'kg', 11, '2025-12-05 11:39:35');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `order_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `order_date` datetime DEFAULT current_timestamp(),
  `total_amount` decimal(10,2) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`order_id`, `customer_id`, `order_date`, `total_amount`, `status`) VALUES
(1, 213, '2025-12-06 21:43:30', 105.00, 'Completed'),
(2, 232, '2025-12-06 22:31:26', 105.00, 'Completed'),
(3, 233, '2025-12-06 22:34:37', 45.00, 'Completed'),
(4, 234, '2025-12-06 22:37:41', 26.75, 'Completed'),
(5, 235, '2025-12-06 22:40:55', 53.50, 'Completed'),
(6, 237, '2025-12-10 09:37:39', 105.00, 'Completed'),
(7, 244, '2025-12-15 12:19:47', 114.00, 'Completed'),
(8, 245, '2025-12-16 19:50:02', 105.00, 'Completed'),
(9, 247, '2025-12-17 09:47:43', 45.00, 'Completed'),
(10, 248, '2025-12-17 11:04:36', 535.00, 'Completed'),
(11, 250, '2025-12-17 12:48:40', 45.00, 'Completed'),
(12, 251, '2025-12-17 13:23:04', 5.00, 'Completed'),
(13, 252, '2025-12-17 13:41:56', 5.00, 'Completed'),
(14, 253, '2025-12-18 13:26:59', 105.00, 'Completed');

-- --------------------------------------------------------

--
-- Table structure for table `order_items`
--

CREATE TABLE `order_items` (
  `order_item_id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_items`
--

INSERT INTO `order_items` (`order_item_id`, `order_id`, `product_id`, `quantity`, `price`) VALUES
(1, 1, 2, 1, 45.00),
(2, 1, 8, 1, 60.00),
(3, 2, 2, 1, 45.00),
(4, 2, 8, 1, 60.00),
(5, 3, 2, 1, 45.00),
(6, 4, 5, 1, 26.75),
(7, 5, 7, 1, 53.50),
(8, 6, 2, 1, 45.00),
(9, 6, 8, 1, 60.00),
(10, 7, 12, 1, 114.00),
(11, 8, 2, 1, 45.00),
(12, 8, 8, 1, 60.00),
(13, 9, 2, 1, 45.00),
(14, 10, 16, 1, 318.00),
(15, 10, 15, 1, 217.00),
(16, 11, 2, 1, 45.00),
(17, 12, 21, 1, 5.00),
(18, 13, 21, 1, 5.00),
(19, 14, 2, 1, 45.00),
(20, 14, 8, 1, 60.00);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `stock_quantity` int(11) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `description`, `price`, `category`, `stock_quantity`, `image_url`) VALUES
(1, 'Sourdough Bread', 'Crusty artisan sourdough loaf', 25.50, 'Bread', 30, NULL),
(2, 'Baguette', 'Classic French baguette', 45.00, 'Bread', 17, NULL),
(3, 'Whole Wheat Bread', 'Healthy whole grain loaf', 37.00, 'Bread', 20, NULL),
(4, 'Multigrain Bread', 'Bread with seeds and grains', 40.25, 'Bread', 15, NULL),
(5, 'Ciabatta', 'Italian white bread with airy texture', 26.75, 'Bread', 17, NULL),
(6, 'Focaccia', 'Flat oven-baked Italian bread', 32.00, 'Bread', 12, NULL),
(7, 'Brioche', 'Soft and buttery French bread', 53.50, 'Bread', 9, NULL),
(8, 'Banana Bread', 'Moist bread with ripe bananas', 60.00, 'Bread', 15, NULL),
(9, 'Pumpkin Bread', 'Seasonal spiced pumpkin loaf', 70.25, 'Bread', 10, NULL),
(10, 'Zucchini Bread', 'Sweet bread with shredded zucchini', 61.75, 'Bread', 8, NULL),
(11, 'Chocolate Cake', 'Rich chocolate sponge cake', 125.00, 'Cake', 10, NULL),
(12, 'Vanilla Cake', 'Classic vanilla layered cake', 114.00, 'Cake', 9, NULL),
(13, 'Red Velvet Cake', 'Velvety red cake with cream cheese frosting', 216.00, 'Cake', 8, NULL),
(14, 'Carrot Cake', 'Spiced cake with carrots and nuts', 215.50, 'Cake', 6, NULL),
(15, 'Cheesecake', 'Creamy New York-style cheesecake', 217.00, 'Cake', 4, NULL),
(16, 'Black Forest Cake', 'Chocolate cake with cherries and cream', 318.00, 'Cake', 3, NULL),
(17, 'Lemon Drizzle Cake', 'Zesty lemon cake with glaze', 114.50, 'Cake', 7, NULL),
(18, 'Strawberry Shortcake', 'Layered cake with strawberries and cream', 416.50, 'Cake', 6, NULL),
(19, 'Coffee Cake', 'Cinnamon crumb cake with coffee flavor', 513.00, 'Cake', 9, NULL),
(20, 'Marble Cake', 'Swirled chocolate and vanilla cake', 514.75, 'Cake', 10, NULL),
(21, 'Pandesal', 'Baratohon nga pan', 5.00, 'Bread', 18, 'Pandesal.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `supplier_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `contact_info` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`supplier_id`, `name`, `contact_info`) VALUES
(1, 'Golden Grains Corp.', 'goldengrains@gmail.com, 09170000001'),
(2, 'Baker\'s Best Supply', 'bakersbest@gmail.com, 09170000002'),
(3, 'Sweet Source Inc.', 'sweetsource@gmail.com, 09170000003'),
(4, 'Flour & More', 'flourmore@gmail.com, 09170000004'),
(5, 'Dairy Direct', 'dairydirect@gmail.com, 09170000005'),
(6, 'Eggcellent Farms', 'eggcellent@gmail.com, 09170000006'),
(7, 'Sugar Rush Traders', 'sugarrush@gmail.com, 09170000007'),
(8, 'Yeast & Co.', 'yeastco@gmail.com, 09170000008'),
(9, 'ChocoDelights', 'chocodelights@gmail.com, 09170000009'),
(10, 'Butter Bliss', 'butterbliss@gmail.com, 09170000010'),
(11, 'Creamy Goods', 'creamygoods@gmail.com, 09170000011'),
(12, 'BakeMate Supplies', 'bakemate@gmail.com, 09170000012');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`customer_id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`inventory_id`),
  ADD KEY `supplier_id` (`supplier_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `order_items`
--
ALTER TABLE `order_items`
  ADD PRIMARY KEY (`order_item_id`),
  ADD KEY `order_id` (`order_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`supplier_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=254;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `inventory_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `order_items`
--
ALTER TABLE `order_items`
  MODIFY `order_item_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `supplier_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `inventory`
--
ALTER TABLE `inventory`
  ADD CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order_items`
--
ALTER TABLE `order_items`
  ADD CONSTRAINT `order_items_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
