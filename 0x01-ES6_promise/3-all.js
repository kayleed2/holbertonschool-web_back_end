import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const upload = uploadPhoto();
  const user = createUser();
  Promise.all([upload, user]).then((response) => {
    console.log(response[0].body, response[1].firstName, response[1].lastName);
  });
}
