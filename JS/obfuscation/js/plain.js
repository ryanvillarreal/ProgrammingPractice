window.addEventListener('load', function() {
    console.log('All assets are loaded');
})
const secret_squirrel = "Secret Passphrase";
function submission(){
    // get values by document Element ID - trim for extra whitespace (might break some passwords)
    var passwd = document.getElementById('floatingPassword').value.trim();
    var email = document.getElementById('floatingInput').value.trim();

    //validate values are not NULL
    if (email == "" || passwd == ""){
        alert('fill this form in');
        return false;
    }
    deEncrypt(email, passwd);
}
function deEncrypt(email, passwd){
    var username = CryptoJS.AES.encrypt(email, secret_squirrel);
    var pass = CryptoJS.AES.encrypt(passwd, secret_squirrel);
    if(CryptoJS.MD5(passwd).toString() == CryptoJS.MD5(secret_squirrel).toString())
    {
        alert("Got it! You Win!");
    }
    else{
        console.log(username.toString());
        console.log(pass.toString())
        alert("Not quite right!");
    }
}