-- creates a view need_meeting that lists all students w score < 80
CREATE VIEW need_meeting AS
SELECT students.name
FROM students
WHERE
	students.score < 80 AND
	last_meeting IS NULL OR
	DATEDIFF(NOW(), last_meeting) > 30;
