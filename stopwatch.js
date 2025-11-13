let startTime;
let elapsedTime = 0;
let timerInterval;
let isRunning = false;

const display = document.getElementById('display');
const startBtn = document.getElementById('startBtn');
const pauseBtn = document.getElementById('pauseBtn');
const resetBtn = document.getElementById('resetBtn');

function formatTime(ms) {
    const hours = Math.floor(ms / 3600000);
    ms %= 3600000;
    const minutes = Math.floor(ms / 60000);
    ms %= 60000;
    const seconds = Math.floor(ms / 1000);
    const milliseconds = ms % 1000;

    return (
        String(hours).padStart(2, '0') + ':' +
        String(minutes).padStart(2, '0') + ':' +
        String(seconds).padStart(2, '0') + '.' +
        String(milliseconds).padStart(3, '0')
    );
}

function startStopwatch() {
    if (!isRunning) {
        startTime = Date.now() - elapsedTime;
        timerInterval = setInterval(() => {
            elapsedTime = Date.now() - startTime;
            display.textContent = formatTime(elapsedTime);
        }, 10); // Update every 10 milliseconds for smoother display
        isRunning = true;
    }
}

function pauseStopwatch() {
    if (isRunning) {
        clearInterval(timerInterval);
        isRunning = false;
    }
}

function resetStopwatch() {
    clearInterval(timerInterval);
    isRunning = false;
    elapsedTime = 0;
    display.textContent = formatTime(elapsedTime);
}

startBtn.addEventListener('click', startStopwatch);
pauseBtn.addEventListener('click', pauseStopwatch);
resetBtn.addEventListener('click', resetStopwatch);