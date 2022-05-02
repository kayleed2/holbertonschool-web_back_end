export default function appendToEachArrayValue(array, appendString) {
  const tmp = [];
  for (const idx of array) {
    tmp.push(appendString + idx);
  }

  return tmp;
}
