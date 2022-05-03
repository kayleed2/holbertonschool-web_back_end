export default function getResponseFromAPI() {
  const bool = true;
  return Promise.resolve(bool);
}
//   const prom = new Promise((resolve, reject) => {
//     if (bool === true) {
//       resolve();
//     } else {
//       reject();
//     }
//   });

//   prom.then(() => Promise.resolve(bool));
//   prom.catch(() => Promise.reject(bool));
// }
