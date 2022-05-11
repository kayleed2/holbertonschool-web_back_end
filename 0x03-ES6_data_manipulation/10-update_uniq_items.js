export default function updateUniqueItems(aMap) {
  if (aMap instanceof Map) {
    for (const [key, value] of aMap.entries()) {
      if (value === 1) aMap.set(key, 100);
    }
    return aMap;
  }
  throw Error('Cannot process');
}
