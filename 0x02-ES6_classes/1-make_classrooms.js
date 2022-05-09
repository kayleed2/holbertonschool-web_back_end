import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const arr = [];
  const roomOne = new ClassRoom(19);
  const roomTwo = new ClassRoom(20);
  const roomThree = new ClassRoom(34);
  arr.push(roomOne);
  arr.push(roomTwo);
  arr.push(roomThree);
  return arr;
}
