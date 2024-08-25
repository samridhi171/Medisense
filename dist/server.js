const express = require('express');
const { exec } = require('child_process');

const app = express();
const PORT = 3000;

app.get('/run-commands', (req, res) => {
    const commands = `
        git clone https://github.com/cesarealmendarez/DeepASL.git &&
        cd DeepASL &&
        pip3 install opencv-python mediapipe numpy &&
        python3 app.py
    `;

    exec(commands, (error, stdout, stderr) => {
        if (error) {
            console.error(Error executing commands: ${error});
            return res.status(500).send('Error executing commands');
        }
        if (stderr) {
            console.error(stderr: ${stderr});
            return res.status(500).send(Error output: ${stderr});
        }
        res.send(Command Output:\n${stdout});
    });
});

app.listen(PORT, () => {
    console.log(Server running on port ${PORT});
});