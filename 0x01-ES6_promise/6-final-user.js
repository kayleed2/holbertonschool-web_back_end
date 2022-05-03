import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignUp(firstName, lastName, fileName) {
  const user = signUpUser(firstName, lastName);
  const photo = uploadPhoto(fileName);
  async function f1() {
    const x = await Promise.allSettled([user, photo]).then((response) => response);
    return x;
  }
  f1();
}
