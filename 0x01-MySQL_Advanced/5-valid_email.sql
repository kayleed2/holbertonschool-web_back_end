-- creates a trigger, resets the attribute valid_email when the email has been changed
CREATE TRIGGER email_update_trigger
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END$$
