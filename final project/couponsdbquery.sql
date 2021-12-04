-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema couponsdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `couponsdb` ;

-- -----------------------------------------------------
-- Schema couponsdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `couponsdb` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `couponsdb` ;

-- -----------------------------------------------------
-- Table `couponsdb`.`store`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `couponsdb`.`store` ;

CREATE TABLE IF NOT EXISTS `couponsdb`.`store` (
  `store_id` INT NOT NULL,
  `store_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`store_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `couponsdb`.`coupon`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `couponsdb`.`coupon` ;

CREATE TABLE IF NOT EXISTS `couponsdb`.`coupon` (
  `coupon_id` INT NOT NULL,
  `coupon_code` VARCHAR(45) NULL DEFAULT NULL,
  `start_date` DATE NULL DEFAULT NULL,
  `expiration_date` DATE NULL DEFAULT NULL,
  `store_id` INT NOT NULL,
  PRIMARY KEY (`coupon_id`),
  INDEX `fk_coupon_store_idx` (`store_id` ASC) VISIBLE,
  CONSTRAINT `fk_coupon_store`
    FOREIGN KEY (`store_id`)
    REFERENCES `couponsdb`.`store` (`store_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
