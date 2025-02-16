-- Création de la base de données sentiment_db si elle n'existe pas
CREATE DATABASE IF NOT EXISTS sentiment_db;

-- Sélection de la base de données sentiment_db
USE sentiment_db;

-- Création de la table tweet si elle n'existe pas
CREATE TABLE IF NOT EXISTS tweet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT NOT NULL,
    positive TINYINT(1) NOT NULL DEFAULT 0,
    negative TINYINT(1) NOT NULL DEFAULT 0
);

-- Insertion des données dans la table tweet
INSERT INTO tweet (id, text, positive, negative) VALUES
(2, 'J\'adore ce film', 1, 0),
(3, 'C\'est horrible', 0, 1),
(4, 'C\'est génial', 1, 0),
(5, 'Je déteste ça', 0, 1),
(6, 'Ce film est incroyable', 1, 0),
(7, 'Je n\'aime pas ce film', 0, 1),
(8, 'Tellement bien réalisé', 1, 0),
(9, 'C\'est une vraie catastrophe', 0, 1),
(10, 'Un chef-d\'œuvre', 1, 0),
(11, 'Un échec total', 0, 1),
(12, 'Je suis très heureux aujourd\'hui', 1, 0),
(13, 'C\'est une journée horrible', 0, 1),
(14, 'J\'adore ce film', 1, 0),
(15, 'C\'est vraiment ennuyeux', 0, 1),
(16, 'Je me sens super bien', 1, 0),
(17, 'Je déteste cet endroit', 0, 1),
(18, 'C\'est incroyable', 1, 0),
(19, 'Je suis dégoûté', 0, 1),
(20, 'Super expérience', 1, 0),
(21, 'J\'ai horreur de cela', 0, 1),
(22, 'Quel beau coucher de soleil', 1, 0),
(23, 'Je ne veux plus y aller', 0, 1),
(24, 'C\'est tellement génial', 1, 0),
(25, 'Je n\'aime pas ce genre de musique', 0, 1),
(26, 'J\'ai adoré cette aventure', 1, 0),
(27, 'C\'est vraiment une mauvaise idée', 0, 1),
(28, 'Quelle belle surprise', 1, 0),
(29, 'J\'ai passé une très mauvaise journée', 0, 1),
(30, 'C\'est un excellent film', 1, 0),
(31, 'Ce film est nul', 0, 1),
(32, 'Je suis au paradis', 1, 0),
(33, 'Je déteste être ici', 0, 1),
(34, 'Tout va bien', 1, 0),
(35, 'Je suis déprimé', 0, 1),
(36, 'Je me sens génial', 1, 0),
(37, 'Ce n\'est pas du tout ce que j\'attendais', 0, 1),
(38, 'Une expérience merveilleuse', 1, 0),
(39, 'Cela me rend triste', 0, 1),
(40, 'C\'est une chance incroyable', 1, 0),
(41, 'Je me sens tellement mal', 0, 1),
(42, 'C\'est vraiment super', 1, 0),
(43, 'Je suis tellement contrarié', 0, 1),
(44, 'Quel moment incroyable', 1, 0),
(45, 'Ce n\'est pas du tout à la hauteur de mes attentes', 0, 1),
(46, 'Un moment inoubliable', 1, 0),
(47, 'Je me sens vide à l\'intérieur', 0, 1),
(48, 'C\'est une expérience unique', 1, 0),
(49, 'Je n\'en peux plus', 0, 1),
(50, 'J\'ai adoré ce moment', 1, 0),
(51, 'C\'est terriblement mauvais', 0, 1),
(52, 'C\'est incroyable, j\'en redemande', 1, 0),
(53, 'C\'est insupportable', 0, 1),
(54, 'Un film époustouflant', 1, 0),
(55, 'J\'ai détesté chaque minute', 0, 1),
(56, 'C\'est tout simplement parfait', 1, 0),
(57, 'Je veux tout oublier', 0, 1),
(58, 'C\'est un vrai chef-d\'œuvre', 1, 0),
(59, 'Je suis au plus bas', 0, 1),
(60, 'Je suis tellement content', 1, 0),
(61, 'Rien ne va aujourd\'hui', 0, 1),
(62, 'C\'est une expérience magnifique', 1, 0),
(63, 'Je suis vraiment frustré', 0, 1),
(64, 'Tout va bien se passer', 1, 0),
(65, 'C\'est vraiment décevant', 0, 1),
(66, 'J\'adore ce plat', 1, 0),
(67, 'C\'est tellement ennuyeux', 0, 1),
(68, 'Je me sens tellement heureux', 1, 0),
(69, 'Je suis terriblement du', 0, 1),
(70, 'C\'est un vrai délice', 1, 0),
(71, 'J\'ai tout gâché', 0, 1),
(72, 'Je ne veux pas partir', 1, 0),
(73, 'Ce n\'est pas ce que j\'espérais', 0, 1),
(74, 'Un moment magique', 1, 0),
(75, 'Je suis complètement démoralisé', 0, 1),
(76, 'Une journée fantastique', 1, 0),
(77, 'C\'est vraiment pénible', 0, 1),
(78, 'Un souvenir inoubliable', 1, 0),
(79, 'Je ne peux plus continuer', 0, 1),
(80, 'Je suis tellement fier', 1, 0),
(81, 'C\'est une vraie perte de temps', 0, 1),
(82, 'C\'est un rêve devenu réalité', 1, 0),
(83, 'Je me sens complètement vide', 0, 1),
(84, 'C\'est une aventure incroyable', 1, 0),
(85, 'Je suis totalement épuisé', 0, 1),
(86, 'Quelle expérience fantastique', 1, 0),
(87, 'Je suis terriblement fatigué', 0, 1),
(88, 'Un moment à ne pas oublier', 1, 0),
(89, 'Je suis complètement anéanti', 0, 1),
(90, 'C\'est un bonheur sans fin', 1, 0),
(91, 'Je ne peux plus supporter cela', 0, 1),
(92, 'C\'est exactement ce que je voulais', 1, 0),
(93, 'C\'est vraiment frustrant', 0, 1),
(94, 'C\'est incroyable, j\'en ai les larmes aux yeux', 1, 0),
(95, 'C\'est déprimant', 0, 1),
(96, 'Je suis si content', 1, 0),
(97, 'J\'ai honte de moi-même', 0, 1),
(98, 'C\'est un pur bonheur', 1, 0),
(99, 'Je suis trop stressé', 0, 1),
(100, 'C\'est vraiment merveilleux', 1, 0),
(101, 'C\'est une perte de temps totale', 0, 1),
(102, 'C\'est un véritable régal', 1, 0),
(103, 'Je ne vois aucune issue', 0, 1),
(104, 'Je suis tellement heureux que ça me donne des frissons', 1, 0),
(105, 'Je n\'en peux plus de cette situation', 0, 1),
(106, 'C\'est une aventure incroyable', 1, 0),
(107, 'Je suis à bout', 0, 1),
(108, 'C\'est un moment unique', 1, 0),
(109, 'Je suis au fond du gouffre', 0, 1),
(110, 'C\'est la meilleure expérience de ma vie', 1, 0),
(111, 'Je ne peux plus rien faire', 0, 1),
(112, 'C\'est juste parfait', 1, 0),
(113, 'C\'est trop difficile', 0, 1),
(114, 'Je suis dans un état de bonheur total', 1, 0),
(115, 'C\'est un véritable cauchemar', 0, 1),
(116, 'Je suis tellement épanoui', 1, 0),
(117, 'Je me sens dans un trou noir', 0, 1),
(118, 'J\'adore cette chanson, elle est super !', 1, 0),
(119, 'C\'est une galère', 0, 1),
(120, 'C\'est génial, je suis heureux !', 1, 0),
(121, 'Je suis désespéré', 0, 1),
(122, 'Quel beau paysage', 1, 0),
(123, 'Je suis dans un profond malheur', 0, 1),
(124, 'C\'est tellement magnifique', 1, 0),
(125, 'Je suis dans un puits sans fond', 0, 1),
(126, 'C\'est un véritable exploit', 1, 0),
(127, 'Je suis désolé, mais c\'est insupportable', 0, 1),
(128, 'C\'est magique', 1, 0),
(129, 'Je suis à bout de forces', 0, 1),
(130, 'Je me sens invincible', 1, 0),
(131, 'Ce film est une catastrophe', 0, 1),
(132, 'Une soirée incroyable', 1, 0),
(133, 'Je suis épuisé, c\'est trop', 0, 1),
(134, 'C\'est un moment magique', 1, 0),
(135, 'Je suis dans un état de stress permanent', 0, 1),
(136, 'Quel voyage fantastique', 1, 0),
(137, 'Je n\'arrive plus à supporter cette situation', 0, 1),
(138, 'Un instant inoubliable', 1, 0),
(139, 'Je suis complètement perdu', 0, 1),
(140, 'C\'est tout simplement spectaculaire', 1, 0),
(141, 'Je suis en colère', 0, 1),
(142, 'Une expérience sans pareille', 1, 0),
(143, 'Je ne peux plus gérer cette pression', 0, 1),
(144, 'Un paysage à couper le souffle', 1, 0),
(145, 'C\'est trop difficile à supporter', 0, 1),
(146, 'C\'est un véritable chef-d\'œuvre', 1, 0),
(147, 'Je suis profondément déprimé', 0, 1),
(148, 'Une aventure exaltante', 1, 0),
(149, 'C\'est un cauchemar', 0, 1),
(150, 'Je suis tellement fier de ce projet', 1, 0),
(151, 'C\'est insupportable', 0, 1),
(152, 'Un moment d\'exception', 1, 0),
(153, 'Je suis dans un état de tristesse profonde', 0, 1),
(154, 'C\'est un moment magique', 1, 0),
(155, 'C\'est vraiment épuisant', 0, 1),
(156, 'Quel sentiment de fierté', 1, 0),
(157, 'Je suis complètement démoralisé', 0, 1),
(158, 'C\'est un vrai bonheur', 1, 0),
(159, 'Je suis vraiment découragé', 0, 1),
(160, 'C\'est un moment merveilleux', 1, 0),
(161, 'Je suis dévasté', 0, 1),
(162, 'C\'est un vrai délice', 1, 0),
(163, 'Je me sens vraiment mal', 0, 1),
(164, 'C\'est un bonheur pur', 1, 0),
(165, 'Je suis si fatigué', 0, 1),
(166, 'Une journée fantastique', 1, 0),
(167, 'Je suis complètement déprimé', 0, 1),
(168, 'C\'est une aventure exceptionnelle', 1, 0),
(169, 'C\'est une journée horrible', 0, 1),
(170, 'Un moment d\'émerveillement', 1, 0),
(171, 'Je suis tellement contrarié', 0, 1),
(172, 'C\'est juste parfait', 1, 0),
(173, 'Je suis dans un état de désespoir', 0, 1),
(174, 'C\'est une expérience inoubliable', 1, 0),
(175, 'Je suis au plus bas', 0, 1),
(176, 'Quel plaisir d\'être ici', 1, 0),
(177, 'Je suis vraiment frustré', 0, 1),
(178, 'C\'est une joie immense', 1, 0),
(179, 'Je suis à bout de forces', 0, 1),
(180, 'C\'est un vrai miracle', 1, 0);

