export default function updateStudentGradeByCity(studentList, city, newGrades) {
  const cityStudent = studentList.filter((obj) => obj.location === city);
  return cityStudent.map((st) => {
    let num = newGrades.filter((gr) => gr.studentId === st.id);
    if (num.length === 0) {
      num = 'N/A';
    } else {
      num = num[0].grade;
    }
    return { ...st, num };
  });
}
