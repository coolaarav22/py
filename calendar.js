document.addEventListener('DOMContentLoaded', () => {
    const daysGrid = document.getElementById('daysGrid');
    const monthYearDisplay = document.getElementById('monthYear');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    let currentDate = new Date(); // Start with the current date

    // Function to render the calendar
    function renderCalendar() {
        daysGrid.innerHTML = ''; // Clear previous days

        const year = currentDate.getFullYear();
        const month = currentDate.getMonth();

        // Get the first day of the month (0 = Sunday, 1 = Monday, etc.)
        const firstDay = new Date(year, month, 1).getDay();
        // Get the number of days in the current month
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        // Update the header display
        monthYearDisplay.textContent = new Date(year, month).toLocaleString('default', { month: 'long', year: 'numeric' });

        // Add day headers (Sun, Mon, Tue...)
        const daysOfWeek = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        daysOfWeek.forEach(dayName => {
            const dayHeader = document.createElement('div');
            dayHeader.textContent = dayName;
            daysGrid.appendChild(dayHeader);
        });

        // Add blank days for padding the start of the month
        for (let i = 0; i < firstDay; i++) {
            const blankDay = document.createElement('div');
            blankDay.classList.add('day', 'other-month');
            daysGrid.appendChild(blankDay);
        }

        // Add the days of the month
        for (let i = 1; i <= daysInMonth; i++) {
            const dayEl = document.createElement('div');
            dayEl.textContent = i;
            dayEl.classList.add('day');

            // Highlight today's date if it matches the actual current date
            const today = new Date();
            if (i === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
                dayEl.classList.add('today');
            }

            daysGrid.appendChild(dayEl);
        }
    }

    // Event listeners for navigation buttons
    prevBtn.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() - 1);
        renderCalendar();
    });

    nextBtn.addEventListener('click', () => {
        currentDate.setMonth(currentDate.getMonth() + 1);
        renderCalendar();
    });

    // Initial render
    renderCalendar();
});