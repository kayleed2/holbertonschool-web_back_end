export default function appendToEachArrayValue(array, appendString) {
  const tmp = [];
  for (const idx of array) {
    const value = array[idx];
    tmp[idx] = appendString + value;
  }

  return tmp;
}
