
/*function signUp() {
  const teamName = document.getElementById("teamName").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  // Validate inputs
  if (!teamName || !email || !password) {
    document.getElementById("message").textContent = "❌ Please fill in all fields";
    return;
  }

  firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      const uid = userCredential.user.uid;
      return db.collection("users").doc(uid).set({
        "team name": teamName,
        points: 0
      });
    })
    .then(() => {
      document.getElementById("message").textContent = "✅ Signup successful!";
    })
    .catch((error) => {
      console.error("Signup error:", error);
      document.getElementById("message").textContent = "❌ " + error.message;
    });
}*/
// Firebase logic (must be type="module")
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

// Replace these with your actual Firebase config
const firebaseConfig = {
  apiKey: "AIzaSyAfnE7PPsB3KfbvWe3bw-jF71p1Y_Br-E4",
  authDomain: "ctfd-9d97b.firebaseapp.com",
  projectId: "ctfd-9d97b",
  storageBucket: "ctfd-9d97b.appspot.com",
  messagingSenderId: "95176890722",
  appId: "1:95176890722:web:5133e8f10a7d409980f43b"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

async function loadQuestionData() {
  const docRef = doc(db, "questions", "question3"); // Example: "question3"
  const docSnap = await getDoc(docRef);

  if (docSnap.exists()) {
    document.getElementById("qno").textContent = docSnap.data().qno;
    document.getElementById("points").textContent = docSnap.data().points;
  } else {
    document.getElementById("qno").textContent = "N/A";
    document.getElementById("points").textContent = "N/A";
  }
}

loadQuestionData();
