-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema aaa
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `aaa` ;

-- -----------------------------------------------------
-- Schema aaa
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aaa` DEFAULT CHARACTER SET utf8 ;
USE `aaa` ;

-- -----------------------------------------------------
-- Table `aaa`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaa`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `correo` VARCHAR(255) NULL,
  `contrasenha` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaa`.`auto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaa`.`auto` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `modelo` VARCHAR(2555) NULL,
  `marca` VARCHAR(255) NULL,
  `ingredientes` VARCHAR(255) NULL,
  `descripcion` TEXT NULL,
  `precio` DECIMAL(10,2) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_auto_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_auto_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `aaa`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaa`.`compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaa`.`compra` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha_compra` DATE NULL,
  `user_id` INT NOT NULL,
  `auto_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_compra_user1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_compra_auto1_idx` (`auto_id` ASC) VISIBLE,
  CONSTRAINT `fk_compra_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `aaa`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_compra_auto1`
    FOREIGN KEY (`auto_id`)
    REFERENCES `aaa`.`auto` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
