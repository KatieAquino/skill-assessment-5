"use strict"

//Add an event listener to the form
// In the event handler (the callback function), retrieve the ID number that the user selected
// Use that ID number to send a GET request to /api/human/<human_id>
// Use data from the server to update the contents of #fname, #lname, and #email with their appropriate values

//
$('#get-human').on('submit', (evt) => {
    evt.preventDefault();
    
    const formData = {human_id: $('#human-id').val(),};

    console.log(formData); //debugging purposes
    console.log(`/api/human/${formData['human_id']}`)
    
    $.get(`/api/human/${formData['human_id']}`, formData, (res) => {
        $('#fname').html(res.fname);
        $('#lname').html(res.lname);
        $('#email').html(res.email);
    });
});

// (╯°□°)╯︵ ┻━┻ see below for the many things i tried,
// I really struggled with getting this one for some reason, got too
// fixated on having the syntax be <int:human_id> like it was in
// server.py and in the notes. But stoked to finally have it!

// function displayHuman(evt) {
//     // evt.preventDefault();
    
//     let formInput = {
//         human_id: $('#human-id').val(),
//     };
//     // let url = `/api/human/${formInput['human_id']}`;
//     let url = '/api/human/<int:human_id>';
    
    
//     $.get(url, formInput, (res) => {
//         $('#fname').html(res.fname);
//         $('#lname').text(res.lname);
//         $('#email').text(res.email);
//     });
// }

// $('#get-human').on('submit', (evt) => {
//     evt.preventDefault();
    
//     const formData = {human_id: $('#human-id').val(),};
//     console.log(formData);
    
//     $.get('/api/human/<int:human_id>', formData, (res) => {
//         $('#fname').html(res.fname);
//         $('#lname').html(res.lname);
//         $('#email').text(res.email);
//     });
// });