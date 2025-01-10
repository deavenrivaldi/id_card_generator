function restrictNonLetters(event) {
    // remove any non-letter characters (incl numbers, punctuations, etc.)
    event.target.value = event.target.value.replace(/[^A-Za-z\s]/g, '');

    // remove leading space if it exists 
    if(event.target.value.startsWith(' ')) {
        event.target.value = event.target.value.substring(1);
    }
}

function inputNIK(event) {
    // remove any non-numeric characters
    event.target.value = event.target.value.replace(/[^0-9]/g, '');

    // remove lieading zero if it exists
    if(event.target.value.startsWith('0')) {
        event.target.value = event.target.value.substring(1);
    }
}

function inputRTRW(event) {
    // replace any character that is not a number or '/'
    event.target.value = event.target.value.replace(/[^0-9]/g, '');

    // Ensure both parts are 3 digits (pad with 0 if necessary)
    event.target.value = event.target.value.padStart(3, '0'); //pad RT part to 3 digits
    // Limit input to 3 digits
    if (event.target.value.length > 3) {
        event.target.value = event.target.value.substring(0, 3);
    }
}