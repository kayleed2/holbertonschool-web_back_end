export default function handleResponseFromAPI(promise) {
  promise.then(
    () => {
      const dic = { status: 200, body: 'Success' };
      console.log('Got a response from the API');
      return Promise.resolve(dic);
    },
    () => new Error('Got a response from the API'),
  );
}
