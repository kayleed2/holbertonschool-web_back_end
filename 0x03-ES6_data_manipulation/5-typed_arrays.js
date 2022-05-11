export default function createInt8TypedArray(length, position, value) {
  try {
    const buff = new ArrayBuffer(length);
    const view = new DataView(buff, 0, length);
    view.setInt8(position, value);
    return view;
  } catch (error) {
    throw new Error('Position outside range');
  }
}
