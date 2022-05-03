export default function getFullResponseFromAPI(success) {
  if (success === true) {
    const dic = { status: 200, body: 'Sucess' };
    return Promise.resolve(dic);
  }
  return Promise.reject(new Error('The fake API is not working currently'));
}
