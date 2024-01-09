export default function getListStudentIds(studentList) {
  // check if argument is an array
  if (!Array.isArray(studentList)) {
    return [];
  }

  // Use map to extract ids from the array of objects
  return studentList.map((student) => student.id);
}
