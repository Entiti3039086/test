let doctitle = document.title;
window.addEventListener("blur", () => {
    document.title = "get back here";
});
window.addEventListener("focus", () => {
    document.title = doctitle;
});