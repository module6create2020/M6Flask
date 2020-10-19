(function() {
    dateObj = new Date(Date.now());

    h = dateObj.getUTCHours();
    m = dateObj.getUTCMinutes();
    s = dateObj.getUTCSeconds();

    formattedTime = h.toString().padStart(2, '0') + ':';
    formattedTime += m.toString().padStart(2, '0') + ':';
    formattedTime += s.toString().padStart(2, '0');

    document.querySelector('.output').textContent = formattedTime;
})();