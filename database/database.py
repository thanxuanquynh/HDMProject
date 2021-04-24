TABLES = {}


TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `username` VARCHAR(30) NOT NULL,"
    " `password` VARCHAR(30) NOT NULL,"
    " `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    " `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`), UNIQUE KEY `username` (`username`)"
    ") ENGINE=InnoDB")

TABLES['topics'] = (
    "CREATE TABLE `topics` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` TEXT NOT NULL,"
    "  `user_id` int(11) NOT NULL,"
    " `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    " `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

# TABLES['salaries'] = (
#     "CREATE TABLE `salaries` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `salary` int(11) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
# TABLES['dept_emp'] = (
#     "CREATE TABLE `dept_emp` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
# TABLES['dept_manager'] = (
#     "  CREATE TABLE `dept_manager` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `dept_no` char(4) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date NOT NULL,"
#     "  PRIMARY KEY (`emp_no`,`dept_no`),"
#     "  KEY `emp_no` (`emp_no`),"
#     "  KEY `dept_no` (`dept_no`),"
#     "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
#     "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
#     "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
#
# TABLES['titles'] = (
#     "CREATE TABLE `titles` ("
#     "  `emp_no` int(11) NOT NULL,"
#     "  `title` varchar(50) NOT NULL,"
#     "  `from_date` date NOT NULL,"
#     "  `to_date` date DEFAULT NULL,"
#     "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
#     "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
#     "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
#     ") ENGINE=InnoDB")
