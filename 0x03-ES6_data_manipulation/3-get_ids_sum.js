export default function getStudentIdsSum(studentList) {
  const ids = studentList.map((x) => x.id);
  const sum = ids.reduce((previousVal, currentVal) => previousVal + currentVal);
  return sum;
}
