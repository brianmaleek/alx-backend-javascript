// Create a const instance of Weakmap
export const weakMap = new WeakMap();

// Create a function named queryAPI
export function queryAPI(endpoint) {
  // Check if endpoint is an object
  if (typeof endpoint !== 'object' || endpoint === null || !endpoint.protocol || !endpoint.name) {
    throw Error('Endpoint is not an object');
  }

  // Initialize the count of endpoint in weakMap
  if (!weakMap.has(endpoint)) {
    weakMap.set(endpoint, 0);
  }

  // Increment the count of endpoint in weakMap
  const count = weakMap.get(endpoint);
  weakMap.set(endpoint, count + 1);

  // If the count of endpoint is greater than or equal to 5
  if (count >= 5) {
    throw new Error('Endpoint load is high');
  }
}
