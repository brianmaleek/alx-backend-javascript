export default function createIteratorObject(report) {
  const newArray = [];
  for (const item of Object.values(report.allEmployees)) {
    newArray.push(...item);
  }
  return newArray;
}
