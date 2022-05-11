export default function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  const view = new DataView(buff, 0, length);
  try {
    view.setInt8(position, value);
  } catch (error) {
    console.log('Position outside of range');
  }
  return view;
}
