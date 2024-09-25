const firebaseConfig = {
    apiKey: "AIzaSyDNXtkG73gmch35SWy2ktdrtdZF2H3fAYQ",
    authDomain: "pureskin-aromri.firebaseapp.com",
    databaseURL: "https://pureskin-aromri-default-rtdb.firebaseio.com",
    projectId: "pureskin-aromri",
    storageBucket: "pureskin-aromri.appspot.com",
    messagingSenderId: "576299778428",
    appId: "1:576299778428:web:96b10e21921889cc4ba4f9",
    measurementId: "G-GNXR63NF0R"
  };
//initialize firebase
  firebase.initializeApp(firebaseConfig);

//refernece your database
const contactFormDB = firebase.database().ref('contactform')