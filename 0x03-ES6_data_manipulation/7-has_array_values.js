export default function hasValuesFromArray(set, array) {
  let flag = true;
  for (const el of array) {
    flag = set.has(el);
  }
  return flag;
}
