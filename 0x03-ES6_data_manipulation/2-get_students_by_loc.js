export default function getStudentsByLocation(studentList, city) {
  const students = studentList.filter((obj) => obj.location === city);
  return students;
}
