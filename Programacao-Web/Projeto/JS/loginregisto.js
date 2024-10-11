function openOverlay(){
    showLogin();
    document.getElementById('overlay').style.display='flex';

    const savedUsername = localStorage.getItem('rememberUsername');
    const rememberMeChecked = localStorage.getItem('rememberMeChecked');

    if(savedUsername){
        document.getElementById('usernameL').value = savedUsername;
    }   

    if(rememberMeChecked){
        document.getElementById("rememberme").checked=true;
    }
}

function showRegister(){
    document.getElementById('loginForm').style.display='none';
    document.getElementById('registerForm').style.display='flex';
    document.getElementById('popupTitle').innerText = 'Register';
}

function showLogin(){
    document.getElementById('loginForm').style.display='flex';
    document.getElementById('registerForm').style.display='none';
    document.getElementById('popupTitle').innerText = 'Login';
}

function login(){
    var username = document.getElementById("usernameL").value;
    var password = document.getElementById("passwordL").value;
    var rememberMeCheckBox = document.getElementById("rememberme");

    // Estas credenciais estão hardcoded propositadamente por natureza de demonstração.
    if(username === 'ipss_l' && password === '1234'){
        document.getElementById('error-messageL').innerText = ''; // Limpar qualquer erro prévio
        // Sava o nome de utilizador se o login for bem sucedido e se a checkbox estiver verificada
        if(rememberMeCheckBox.checked){
            localStorage.setItem('rememberUsername', username);
            localStorage.setItem('rememberMeChecked', 'true');
        } else {
            localStorage.removeItem('rememberUsername'); // Limpa o nome de utilizador da memória se a checkbox não estiver verificada
            localStorage.removeItem('rememberMeChecked');
        }

        localStorage.setItem('isLoggedIn', 'true');
        document.getElementById('ButtonUser').style.display='flex';
        document.getElementById('ButtonLogin').style.display='none';
        // Redirecionar para página de utilizador(neste caso, de administração)
        window.location.href='/Programação Web/Projeto/HTML/Utilizador.html';
    } else {
        document.getElementById('error-messageL').innerText = "Credenciais inválidas";
    }
}

function register(){
    var ownname = document.getElementById('ownnameR').value;
    var username = document.getElementById('usernameR').value;
    var email = document.getElementById('emailR').value;
    var password1 = document.getElementById('password1R').value;
    var password2 = document.getElementById('password2R').value;
    
    document.getElementById('error-messageR').innerText = ''; // Limpar qualquer erro prévio


    if (!ownname.includes(' ')) {
        document.getElementById('ownnameR').style.borderColor='#ff0000';
        document.getElementById('error-messageR').innerText = 'Por favor introduza o seu primeiro e último nome!';
        return;
    } else {
        document.getElementById('ownnameR').style.borderColor='aliceblue';
    }


    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        document.getElementById('emailR').style.borderColor='#ff0000';
        document.getElementById('error-messageR').innerText = 'Endereço de Email inválido!';
        return;
    } else {
        document.getElementById('emailR').style.borderColor='aliceblue';
    }

    if(password2 !== password1){
        document.getElementById('password1R').style.borderColor='#ff0000';
        document.getElementById('password2R').style.borderColor='#ff0000';
        document.getElementById('error-messageR').innerText = "As palavras-passe não são idênticas!";
        return;
    } else {
        document.getElementById('password1R').style.borderColor='aliceblue';
        document.getElementById('password2R').style.borderColor='aliceblue';
    }

    if (!ownname || !username || !email || !password1 || !password2) {
        document.getElementById('error-messageR').innerText = 'Por favor preencha todos os campos';
        if (!ownname) document.getElementById('ownnameR').style.borderColor='#ff0000';
        if (!username) document.getElementById('usernameR').style.borderColor='#ff0000';
        if (!email) document.getElementById('emailR').style.borderColor='#ff0000';
        if (!password1) document.getElementById('password1R').style.borderColor='#ff0000';
        if (!password2) document.getElementById('password2R').style.borderColor='#ff0000';
        return; // Stop execution if any field is blank
    } else {
        document.getElementById('ownnameR').style.borderColor='#ff0000';
        document.getElementById('usernameR').style.borderColor='#ff0000';
        document.getElementById('emailR').style.borderColor='#ff0000';
        document.getElementById('password1R').style.borderColor='#ff0000';
        document.getElementById('password2R').style.borderColor='#ff0000';
    }

    closeOverlay();

    document.getElementById('ownnameR').value = '';
    document.getElementById('usernameR').value = '';
    document.getElementById('emailR').value = '';
    document.getElementById('password1R').value = '';
    document.getElementById('password2R').value = '';

    
}

function closeOverlay(){
    document.getElementById('overlay').style.display='none';
}

function logoff(){
    localStorage.removeItem('isLoggedIn');
    document.getElementById('userIcon').style.display = 'none';
    document.getElementById('ButtonLogin').style.display='block';
}

window.onload = function () {
  const isLoggedIn = localStorage.getItem('isLoggedIn');
  
  if(isLoggedIn){
    document.getElementById('ButtonUser').style.display='flex';
    document.getElementById('ButtonLogin').style.display='none';
  } else {
    document.getElementById('ButtonUser').style.display='none';
    document.getElementById('ButtonLogin').style.display='flex';
  }
};