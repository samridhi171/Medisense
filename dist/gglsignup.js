import { initializeApp } from "https://www.gstatic.com/firebasejs/10.13.0/firebase-app.js";

import { getAuth, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.13/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyAefVT_gZdsg2W64Iq7qZz2fg7WNIFZ4p4",
  authDomain: "login-check-8dddf.firebaseapp.com",
  projectId: "login-check-8dddf",
  storageBucket: "login-check-8dddf.appspot.com",
  messagingSenderId: "357442081317",
  appId: "1:357442081317:web:70e9bb535fe12a192525cc"
};

// provider.addScope('https://www.googleapis.com/auth/contacts.readonly');

// import { getAuth } from "https://www.gstatic.com/firebasejs/10.13/firebase-auth.js";

const app=initializeApp(firebaseConfig);
const auth = getAuth(app);
auth.languageCode = 'en';
const provider = new GoogleAuthProvider();
// To apply the default browser preference instead of explicitly setting it.
// auth.useDeviceLanguage();

// provider.setCustomParameters({
//   'login_hint': 'user@example.com'
// });

const gglsignup = document.getElementById("gglsignup");

gglsignup.addEventListener("click", function(event)
{
  event.preventDefault()

  signInWithPopup(auth, provider)
  .then((result) => {
    const credential = GoogleAuthProvider.credentialFromResult(result);
    const token = credential.accessToken;
    const user = result.user;
    console.log(user);
    window.location.href="main.html";

    
  }).catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
  });
})


