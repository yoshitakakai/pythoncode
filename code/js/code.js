var height = prompt("身長はいくつ？");
var ticket = prompt("持っているチケットは？");
if (height >= 100) {
    if (ticket === "premium") {
        alert("プレミアムシートに乗車可能");
    } else {
        alert("普通シートに乗車可能");
    }

}else if (height >= 90){
    alert("付き添いありで乗車可能");
} else {
    alert("乗車不可");
}