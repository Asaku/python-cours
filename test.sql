UPDATE 'utilisateur' SET 'nom'="Chevre", 'prenom'="Seguin", 'email'="seguin@chevre.com", WHERE id = 1


UPDATE 'utilisateur' SET 'nom'="Chevre", 'prenom'="Seguin", 'email'="seguin@chevre.com" WHERE id = 1
UPDATE `utilisateur` SET `nom`="Chevre", `prenom`="Seguin", `email`="seguin@chevre.com" WHERE id = 1


SELECT DISTINCT nom
FROM utilisateur;

INSERT INTO `utilisateur`(`nom`) VALUES ("mehdi")


SELECT MIN(code_postal) FROM utilisateur;

SELECT code_postal FROM utilisateur UNION SELECT nom FROM utilisateur;

CREATE TABLE groupe
(
   id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
   nom VARCHAR(100)
)
ALTER TABLE utilisateur ADD groupe_id INTEGER, ADD CONSTRAINT FOREIGN KEY(groupe_id) REFERENCES groupe(id)

SELECT * FROM table1
MINUS
SELECT * FROM table2

BEGIN
  DECLARE v_i INT DEFAULT 1;
  WHILE v_i <= 1000 DO
    INSERT INTO `utilisateur`(`nom`, `prenom`, `email`, `date_naissance`, `pays`, `ville`, `code_postal`) VALUES ("Queen", "Oliver", "arrow@teamarrow.com", "1980/05/28", "Na ilha", "This City", "12345");

    SET v_i = v_i + 1;
  END WHILE;
END

DELIMITER |
CREATE PROCEDURE nom_de_la_procedure(IN param INT)
BEGIN
    DECLARE i INT DEFAULT 1;

      -- Ma requete

        SET i = i + 1;
    END WHILE;
END |
DELIMITER ;

CALL nom_de_la_procedure(100);



