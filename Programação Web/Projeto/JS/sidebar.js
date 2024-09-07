let headerLinks = document.querySelector(".HeaderLinks");
let menuOpenBtn = document.querySelector(".HeaderContainer .HamburgerIcon");
let menuCloseBtn = document.querySelector(".SidebarTop .SidebarX");

menuOpenBtn.onclick = function() {
headerLinks.style.right = "0%";
}
menuCloseBtn.onclick = function() {
headerLinks.style.right = "-100%";
}