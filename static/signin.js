function signIn(){
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;
//  console.log('test');
  console.log(email);
  console.log(password);
  firebase.auth().signInWithEmailAndPassword(email, password)
  .then((user) => {
    if(user['user']['emailVerified'] == false){
      console.log("test1");
      document.getElementById('error').innerHTML = "Email not authenticated";
    }
    else if(user['user']['emailVerified'] == true){
      console.log("test2");
      location.href = '/templates';
    }
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
    console.log(errorMessage);
    document.getElementById('error').innerHTML = errorMessage;
  });

}
