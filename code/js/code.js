var button = document.getElementById("nice");
button.addEventListener("click", niceaction)
function niceaction(){
    var element = document.createElement("p");
    var text = document.createTextNode("いいね!");
    document.body.appendChild(element).appendChild(text);
}