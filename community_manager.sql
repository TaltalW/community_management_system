SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `community`;
CREATE TABLE `community` (
  `Cno` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Cname` varchar(100) NOT NULL,
  `Ctype` varchar(100) DEFAULT NULL,
  `Csno` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `Csname` varchar(100) DEFAULT NULL,
  `Crank` varchar(100) DEFAULT NULL,
  `Cnum` int DEFAULT '0',
  `Crno` varchar(100) DEFAULT NULL,
  `Cdate` date DEFAULT NULL,
  PRIMARY KEY (`Cno`),
  KEY `community_FK` (`Csno`),
  KEY `community_FK_1` (`Crno`),
  CONSTRAINT `community_FK` FOREIGN KEY (`Csno`) REFERENCES `student` (`Sno`),
  CONSTRAINT `community_FK_1` FOREIGN KEY (`Crno`) REFERENCES `room` (`Rno`)
)ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;


INSERT INTO community_manager.community (Cno,Cname,Ctype,Csno,Csname,Crank,Cnum,Crno,Cdate) VALUES
	 ('0001','书画协会','艺术创意类','20210002','王明','A',10,'101','2020-12-01'),
	 ('0002','原创DV协会','艺术创意类',NULL,NULL,'B',0,'111','2020-11-12'),
	 ('0003','手工艺协会','艺术创意类',NULL,NULL,'B',0,'121','2019-12-11'),
	 ('0004','摄影协会','艺术创意类','20190011','王雪','B',2,'312','2018-10-05'),
	 ('0005','求真社','专业学习类','20200013','朱青','B',1,'120','2020-11-22'),
	 ('0006','天文爱好者协会','专业学习类',NULL,NULL,'B',0,'223','2021-11-01'),
	 ('0007','心理协会','爱心公益类','20200014','谢瑶','B',1,'630','2018-10-25'),
	 ('0008','圣兵爱心社','爱心公益类',NULL,NULL,'B',0,'227','2016-10-22'),
	 ('0009','机器人协会','科技创新类',NULL,NULL,'B',0,NULL,'2019-10-26'),
	 ('0010','篮球协会','体育竞技类',NULL,NULL,'B',0,NULL,'2019-12-03');
INSERT INTO community_manager.community (Cno,Cname,Ctype,Csno,Csname,Crank,Cnum,Crno,Cdate) VALUES
	 ('0011','科幻类','科技创新类',NULL,NULL,'B',0,NULL,'2018-10-25');
	

-- community_manager.member_login definition
DROP TABLE IF EXISTS `member_login`;
CREATE TABLE `member_login` (
  `Sno` varchar(100) NOT NULL,
  `Password` varchar(100) DEFAULT '123456',
  `login` varchar(100) DEFAULT '0',
  PRIMARY KEY (`Sno`),
  CONSTRAINT `member_login_FK` FOREIGN KEY (`Sno`) REFERENCES `student` (`Sno`)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- community_manager.room definition
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room` (
  `Rno` varchar(100) NOT NULL,
  `Rcno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Rno`)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

INSERT INTO community_manager.member_login (Sno,Password,login) VALUES
	 ('20190008','123456','0'),
	 ('20190011','123456','0'),
	 ('20190012','123456','0'),
	 ('20200001','123456','0'),
	 ('20200004','123456','0'),
	 ('20200010','123456','0'),
	 ('20200013','123456','0'),
	 ('20200014','123456','0'),
	 ('20210002','123456','0'),
	 ('20210003','123456','0');
INSERT INTO community_manager.member_login (Sno,Password,login) VALUES
	 ('20210007','123456','0'),
	 ('20210009','123456','0'),
	 ('20220005','123456','0'),
	 ('20220006','123456','0');
	
	
	
-- community_manager.student definition
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `Sno` varchar(100) NOT NULL,
  `Sname` varchar(100) NOT NULL,
  `Ssex` varchar(100) DEFAULT NULL,
  `Sdept` varchar(100) DEFAULT NULL,
  `Scno` varchar(100) DEFAULT NULL,
  `community` varchar(100) DEFAULT NULL,
  `Status` varchar(100) DEFAULT NULL,
  `Wechat` varchar(100) DEFAULT NULL,
  `Tel` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Sno`),
  KEY `student_FK` (`Scno`),
  CONSTRAINT `student_FK` FOREIGN KEY (`Scno`) REFERENCES `community` (`Cno`)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

INSERT INTO community_manager.student (Sno,Sname,Ssex,Sdept,Scno,community,Status,Wechat,Tel) VALUES
	 ('20190008','王美雪','女','法学院','0001','书画协会','member','cafamvoe','18700000078'),
	 ('20190011','王雪','女','法学院','0004','摄影协会','master','cdafawax','18600000191'),
	 ('20190012','李为','男','数学学院','0004','摄影协会','member','cafawcs','13800000021'),
	 ('20200001','张伟','男','计算机学院','0001','书画协会','member','aaaabbbb','18700000000'),
	 ('20200004','李鹏','男','法学院','0001','书画协会','member','wwwaaawd','18700000098'),
	 ('20200010','李大强','男','社会学院','0001','书画协会','member','vrdsrgs','18600000012'),
	 ('20200013','朱青','男','物理学院','0005','求真设','master','cafads','13900000012'),
	 ('20200014','谢瑶','女','外语学院','0007','心理协会','master','dsmohv','18700000029'),
	 ('20210002','王明','男','信息学院','0001','书画协会','master','ccccddd','18700000001'),
	 ('20210003','程丽','女','人工智能','0001','书画协会','member','aaaaqqq','18700000010');
INSERT INTO community_manager.student (Sno,Sname,Ssex,Sdept,Scno,community,Status,Wechat,Tel) VALUES
	 ('20210007','董莉莉','女','经济学院','0001','书画协会','member','cnahidre','18700000029'),
	 ('20210009','吴美琪','女','经济学院','0001','书画协会','member','csfscs','18700000983'),
	 ('20220005','王华庆','男','计算机学院','0001','书画协会','member','qojddec','18700000034'),
	 ('20220006','吴冰宁','女','计算机学院','0001','书画协会','member','sdcftwc','18700000264');





-- community_manager.room definition
DROP TABLE IF EXISTS `room`;
CREATE TABLE `room` (
  `Rno` varchar(100) NOT NULL,
  `Rcno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Rno`)
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;
INSERT INTO community_manager.room (Rno,Rcno) VALUES
	 ('101','0001'),
	 ('111','0002'),
	 ('120','0005'),
	 ('121','0003'),
	 ('223','0006'),
	 ('227','0008'),
	 ('312','0004'),
	 ('630','0007');