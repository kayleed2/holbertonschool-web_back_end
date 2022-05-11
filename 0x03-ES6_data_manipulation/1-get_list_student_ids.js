export default function getListStudentIds(listofObjs) {
  if (Array.isArray(listofObjs) === false) {
    return [];
  }
  const ids = listofObjs.map((x) => x.id);
  return ids;
}
