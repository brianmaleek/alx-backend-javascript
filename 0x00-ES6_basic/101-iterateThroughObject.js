export default function iterateThroughObject(reportWithIterator) {
  const returnString = [];
  for (const item of reportWithIterator) {
    returnString.push(item);
  }
  return returnString.join(' | ');
}
