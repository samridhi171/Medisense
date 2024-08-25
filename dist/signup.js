// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.13/firebase-auth.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAefVT_gZdsg2W64Iq7qZz2fg7WNIFZ4p4",
  authDomain: "login-check-8dddf.firebaseapp.com",
  projectId: "login-check-8dddf",
  storageBucket: "login-check-8dddf.appspot.com",
  messagingSenderId: "357442081317",
  appId: "1:357442081317:web:70e9bb535fe12a192525cc"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const submit = document.getElementById('submit');

submit.addEventListener("click", function(event)
{
  event.preventDefault()
  const email = document.getElementById("email").value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if(password!=confirmPassword)
  {
    alert("Passwords do not match.");

    document.getElementById("password").value = "";
    document.getElementById("confirmPassword").value= "";

    return false;
  }
  createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed up 
    const user = userCredential.user;
    // ...
    alert('New user created');
    window.location.href = "main.html";
    
    // document.getElementById('section2').style.display="grid";
    // document.getElementById('section3').style.display="grid";
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert("Please try again.");
    // ..
  });

})