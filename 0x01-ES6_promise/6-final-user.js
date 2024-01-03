/* eslint-disable import/extensions */
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  try {
    const [userResult, photoResult] = await Promise.allSettled([userPromise, photoPromise]);

    return [
      {
        status: userResult.status,
        value: userResult.status === 'fulfilled' ? userResult.value : userResult.reason,
      },
      {
        status: photoResult.status,
        value: photoResult.status === 'fulfilled' ? photoResult.value : photoResult.reason,
      },
    ];
  } catch (error) {
    console.error('Error during signup:', error);
    return [];
  }
}
