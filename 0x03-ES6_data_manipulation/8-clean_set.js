export default function cleanSet(_set, startString) {
  if (typeof _set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  const stringSet = [..._set].filter((x) => x && x.startsWith(startString)).map((x) => x.replace(startString, ''));
  return stringSet.join('-');
}
