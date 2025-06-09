
// Firebase v8 configuration (no imports needed with CDN)
const firebaseConfig = {
  apiKey: "AIzaSyAfnE7PPsB3KfbvWe3bw-jF71p1Y_Br-E4",
  authDomain: "ctfd-9d97b.firebaseapp.com",
  projectId: "ctfd-9d97b",
  storageBucket: "ctfd-9d97b.firebasestorage.app",
  messagingSenderId: "95176890722",
  appId: "1:95176890722:web:5133e8f10a7d409980f43b",
  measurementId: "G-0EHZX2SXV0"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Initialize services
const db = firebase.firestore();
const auth = firebase.auth();
