// interface definition for student object
interface Student {
    firstName: string;
    lastName: string;
    age: number;
    location: string;
}

// student1 is a Student object
const student1: Student = {
    firstName: 'Bian',
    lastName: 'Maleek',
    age: 25,
    location: 'San Francisco'
};

// student2 is a Student object
const student2: Student = {
    firstName: 'Maleek',
    lastName: 'Brian',
    age: 24,
    location: 'New York'
};

// studentList is an array of Student objects
const studentList: Array<Student> = [student1, student2];

// Create the table
function createTable(): void {
    const body: HTMLBodyElement = document.getElementsByTagName('body')[0];
    const tbl: HTMLTableElement = document.createElement('table');
    const tblBody: HTMLTableSectionElement = document.createElement('tbody');

    for (const student of studentList) {
        const tableRow: HTMLTableRowElement = document.createElement('tr');

        for (let columnIndex = 0; columnIndex < 4; columnIndex++) {
            const tableCell: HTMLTableCellElement = document.createElement('td');
            let cellText: Text;

            switch (columnIndex) {
                case 0:
                    cellText = document.createTextNode(student.firstName);
                    break;
                case 1:
                    cellText = document.createTextNode(student.lastName);
                    break;
                case 2:
                    cellText = document.createTextNode(student.age.toString());
                    break;
                case 3:
                    cellText = document.createTextNode(student.location);
                    break;
            }

            tableCell.appendChild(cellText);
            tableRow.appendChild(tableCell);
        }

        tblBody.appendChild(tableRow);
    }

    tbl.appendChild(tblBody);
    body.appendChild(tbl);
    tbl.setAttribute('border', '2');
}

// Call the function to create the table
createTable();
