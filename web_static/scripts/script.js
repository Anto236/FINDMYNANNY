// $(document).ready(function () {
//     $('.signup-button').popover({
//         html: true,
//         content: function () {
//             return '<a href="nanny.html" class="popover-link">I am... Nanny</a><br><a href="family.html" class="popover-link">I am... Family</a>';
//         },
//         placement: 'bottom',
//         trigger: 'click'
//     });

//     $('body').on('click', function (e) {
//         if ($('.signup-button').has(e.target).length === 0 && !$('.signup-button').is(e.target)) {
//             $('.signup-button').popover('hide');
//         }
//     });
// });


// Get the login button element
const loginButton = document.querySelector('.signup-button');

// Get the login dropdown element
const loginDropdown = document.querySelector('.login-dropdown');

// Add a click event listener to the login button
loginButton.addEventListener('click', () => {
    // Toggle the visibility of the login dropdown
    loginDropdown.classList.toggle('visible');
});