export default function (studentList, city) {
  // Check if input is an array and city is a string
  if (!Array.isArray(studentList) || typeof city !== 'string') {
    return [];
  }

  // Use filter to get students located in the specified city
  return studentList.filter((student) => student.location === city);
}
