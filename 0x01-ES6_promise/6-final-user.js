import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignUp(firstName, lastName, fileName) {
  return [
    await signUpUser(firstName, lastName)
      .then((response) => response),
    await uploadPhoto(fileName)
      .catch((response) => response),
  ];
}
