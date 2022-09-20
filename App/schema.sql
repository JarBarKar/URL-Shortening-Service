--
-- Database: `tiny_url_clone`
--
CREATE DATABASE IF NOT EXISTS `tiny-url-clone` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `tiny-url-clone`;

-- --------------------------------------------------------

--
-- Table structure for table `url_shortener`
--

DROP TABLE IF EXISTS `url_shortener`;
CREATE TABLE IF NOT EXISTS `url_shortener` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `original_url` varchar(128) NOT NULL,
  `short_url` varchar(64) NOT NULL,
  `visits` int(6) NOT NULL,
  `date_created` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

