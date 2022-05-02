export default function appendToEachArrayValue(array, appendString) {
  const tmp = array;
  for (const idx of array) {
    const value = tmp[idx];
    tmp[idx] = appendString + value;
  }

  return tmp;
}
