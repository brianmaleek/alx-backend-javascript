export default function getStudentIdsSum(studentList) {
  // check if argument is an array
  if (!Array.isArray(studentList)) {
    return [];
  }

  // Use reduce to calculate sum of student ids
  return studentList.reduce((sum, student) => sum + student.id, 0);
}
