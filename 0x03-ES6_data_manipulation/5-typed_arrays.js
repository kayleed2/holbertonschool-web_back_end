export default function createInt8TypedArray(length, position, value) {
  if (position > length || position < 0) {
    throw Error('Position outside of range');
  }
  const buff = new ArrayBuffer(length);
  const view = new DataView(buff, 0, length);
  view.setInt8(position, value);
  return view;
}
