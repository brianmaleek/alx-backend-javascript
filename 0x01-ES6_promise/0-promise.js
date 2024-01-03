/* eslint-disable no-constant-condition */
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    if (true) {
      resolve();
    } else {
      reject(new Error('Promise rejected'));
    }
  });
}
