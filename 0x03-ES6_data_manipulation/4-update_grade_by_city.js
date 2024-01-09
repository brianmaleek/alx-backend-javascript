export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // Check if input is an array and city is a string
  if (!Array.isArray(studentList) || typeof city !== 'string') {
    return [];
  }

  // Use filter to get students located in the specified city
  const studentsInCity = studentList.filter((student) => student.location === city);

  // Use map to update grades of students in the specified city
  const updatedStudents = studentsInCity.map((student) => {
    const newGrade = newGrades.filter((grade) => grade.studentId === student.id)[0];
    return {
      ...student,
      grade: newGrade ? newGrade.grade : 'N/A',
    };
  });

  return updatedStudents;
}
