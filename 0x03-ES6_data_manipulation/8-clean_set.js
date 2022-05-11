export default function cleanSet(set, startString) {
  const strings = [];
  let app;
  if (startString === '') return '';
  for (const el of set) {
    if (el.startsWith(startString)) {
      app = el.replace(startString, '');
      strings.push(app);
    }
  }
  return strings.join('-');
}
