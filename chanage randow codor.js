const changeColorBtn = document.getElementById('changeColorBtn');

function generateRandomColor() {
    // Generate random values for red, green, and blue components (0-255)
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);

    // Construct the RGB color string
    return `rgb(${r}, ${g}, ${b})`;
}

// Event listener for the button click
changeColorBtn.addEventListener('click', () => {
    document.body.style.backgroundColor = generateRandomColor();
});

// Optionally, set an initial random background color when the page loads
document.body.style.backgroundColor = generateRandomColor();