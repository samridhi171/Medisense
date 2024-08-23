document.addEventListener('DOMContentLoaded', function(e)
{
    document.getElementById('button1').classList.add('animate-slideInSideBySide');
    document.getElementById('section1').scrollIntoView({
        behavior:'auto',
        block:'start', 
    });
    document.getElementById('section1').style.marginTop = "80px";
})
// for mobile_menu

let vector = document.getElementById('vector');
let vector_tab = document.getElementById('vector_tab');
let mascot = document.getElementById('mascot');

vector.addEventListener('click',function()
{
    vector_tab.classList.toggle('hidden');
    mascot.classList.toggle('hidden');
    
});

// document.addEventListener('DOMContentLoaded', function() {

//     // Check if there's a hash in the URL
//     if (window.location.hash) {
//         // If there's a hash, replace it with the home section hash
//         window.location.hash = '#section1';
//     } else {
//         // If there's no hash, ensure the page scrolls to the home section
//         const homeSection = document.getElementById('section1');
//         if (homeSection) {
//             homeSection.scrollIntoView({
//                 behavior: 'auto',
//                 block: 'start'
//             });
//         }
//     }
// });



// function toggleMenu() {
//     if (vector_tab.style.transform === "translateX(250px)") {
//         vector_tab.style.transform = "translateX(-250px)"; // Slide out
//     } else {
//         vector_tab.style.transform = "translateX(250px)"; // Slide in
//     }
//   }