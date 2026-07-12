import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const dbPath = process.argv[2];

    readDatabase(dbPath)
      .then((studentsByField) => {
        const fields = Object.keys(studentsByField)
          .sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));

        const lines = ['This is the list of our students'];
        fields.forEach((field) => {
          const list = studentsByField[field];
          lines.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        });

        res.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const dbPath = process.argv[2];
    readDatabase(dbPath)
      .then((studentsByField) => {
        res.status(200).send(`List: ${studentsByField[major].join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
