export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const cityStudents = studentList.filter((obj) => obj.location === city);
  return cityStudents.map((st) => {
    let grade = newGrades.filter((grade) => grade.studentId === st.id);
    if (grade.length === 0) {
      grade = 'N/A';
    } else {
      grade = grade[0].grade;
    }
    return { ...st, grade };
  });
}
