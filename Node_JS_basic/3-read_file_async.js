const fs = require('fs');

function countStudents(path) {
  return fs.promises.readFile(path, 'utf8')
    .then((data) => {
      const rows = data.split('\n').filter((line) => line.trim() !== '');
      const students = rows.slice(1);
      const byField = {};

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');
        if (!byField[field]) {
          byField[field] = [];
        }
        byField[field].push(firstname);
      });

      console.log(`Number of students: ${students.length}`);
      Object.keys(byField).forEach((field) => {
        console.log(`Number of students in ${field}: ${byField[field].length}. List: ${byField[field].join(', ')}`);
      });
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
