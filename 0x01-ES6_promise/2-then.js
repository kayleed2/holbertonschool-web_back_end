export default function handleResponseFromAPI(promise) {
  promise.then(
    () => {
      const dic = { status: 200, body: 'success' };
      console.log('Got a response from the API');
      return Promise.resolve(dic);
    },
    () => new Error(),
  );
}
