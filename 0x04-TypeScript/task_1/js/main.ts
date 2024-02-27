// 
interface Teacher {
    // readonly properties cannot be changed after initialization
    readonly firstName: string;
    readonly lastName: string;
    fullTimeEmployee: boolean;
    yearsOfExperience?: number;
    location: string;
    [key: string]: any; // any other properties
}

// initializeTeacher() returns a Teacher object
const initializeTeacher = (firstName: string, lastName: string): Teacher => {
    return {
        firstName,
        lastName,
        fullTimeEmployee: false,
        location: 'Default location'
    };
};

// teacher1 is a Teacher object
const teacher1: Teacher = initializeTeacher('Leah', 'Rowan');
teacher1.yearsOfExperience = 5;
teacher1.contract = true;

// printTeacher() prints the Teacher object
console.log(teacher1);
