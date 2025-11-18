function rollDice() {
    // Generate random numbers from 1 to 6
    let random1 = Math.floor(Math.random() * 6) + 1;
    let random2 = Math.floor(Math.random() * 6) + 1;

    // Update dice images (assuming dice1.png ... dice6.png exist)
    document.getElementById("dice1").src = "images/dice" + random1 + ".png";
    document.getElementById("dice2").src = "images/dice" + random2 + ".png";

    // Determine result
    let resultText = "";

    if (random1 > random2) {
        resultText = "Player 1 Wins! 🎉";
    } else if (random2 > random1) {
        resultText = "Player 2 Wins! 🎉";
    } else {
        resultText = "It's a Draw! 🤝";
    }

    // Display result
    document.getElementById("result").textContent = resultText;
}