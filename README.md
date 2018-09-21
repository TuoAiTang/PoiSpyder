# PoiSpyder
爬取去哪儿网数据，简单建立一个北京市景点数据库
爬取地址：http://travel.qunar.com/p-cs299914-beijing-jingdian-3-1
建立数据库：poi_info
CREATE TABLE `poi_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `parent` varchar(45) DEFAULT NULL,
  `parent_rank` int(11) DEFAULT NULL,
  `mentioned_times` int(11) DEFAULT NULL,
  `overview` tinytext,
  `tickets` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `open_time` varchar(225) DEFAULT NULL,
  `tips` varchar(255) DEFAULT NULL,
  `best_time` varchar(225) DEFAULT NULL,
  `comment_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
分别对应网页上的各个字段：
  景点名称
  父景点
  在父景点中排名
  在游记中被提到的次数
  概述
  门票情况
  详细地址
  开放时间
  小贴士
  最佳游览时间
  评论数量
