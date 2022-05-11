export default function cleanSet(set, startString) {
  const strings = [];
  let app;
  if (startString === '' || typeof startString !== 'string') return '';
  for (const el of set) {
    if (el.startsWith(startString) && typeof el === 'string') {
      app = el.replace(startString, '');
      strings.push(app);
    }
  }
  return strings.join('-');
}
