function countdown() {
    const targetdate = document.querySelector('#targetdate').value;
    const td = new Date(targetdate).getTime();

    // To call defined fuction every second
    let x = setInterval(function () {

        // Getting current time in required format
        let now = new Date().getTime();

        // Calculating the difference
        let t = td - now;

        // Getting value of days, hours, minutes, seconds
        let days = Math.floor(t / (1000 * 60 * 60 * 24));
        let hours = Math.floor(
            (t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor(
            (t % (1000 * 60 * 60)) / (1000 * 60));
        let seconds = Math.floor(
            (t % (1000 * 60)) / 1000);

        // Output the remaining time
        document.getElementById("countdown").innerHTML =
            days + "days " + hours + "hours " +
            minutes + "minutes " + seconds + "seconds ";

        // Output all times
        document.getElementById("days").innerHTML = days;
        document.getElementById("hours").innerHTML = hours;
        document.getElementById("minutes").innerHTML = minutes;
        document.getElementById("seconds").innerHTML = seconds;

        // Output for over time
        if (t < 0) {
            clearInterval(x);
            document.getElementById("countdown")
                .innerHTML = "EXPIRED";
        }
    }, 1000);
}
if (window.addEventListener) {
    window.addEventListener('load', countdown, false); //W3C
} else {
    window.attachEvent('onload', countdown); //IE
}