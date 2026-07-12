const fs = require('fs');

function countStudents(path) {
  let data;

  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

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
}

module.exports = countStudents;
