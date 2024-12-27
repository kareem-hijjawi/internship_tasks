

document.addEventListener('DOMContentLoaded', () => {
    const habitList = document.querySelectorAll('#habit-list li');

    function showNotification(task) {
        alert(`Reminder: Time to complete "${task}"!`);
    }

    function checkReminders() {
        const now = new Date();
        const currentTime = now.toTimeString().slice(0, 5);

        habitList.forEach(item => {
            const task = item.textContent.split(' - ')[0];
            const time = item.dataset.time;

            if (time === currentTime) {
                showNotification(task);
            }
        });
    }

    setInterval(checkReminders, 60000); // Check every minute
});
