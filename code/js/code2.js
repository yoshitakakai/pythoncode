var goal = 50;
var progress = 0;

while(goal > progress) {
    var result = Math.floor(Math.random() * 6) + 1;
    alert("サイコロの目は" + result + "です" + result + "マス進みます");
    progress += result;

    var rand = Math.floor(Math.random() * 4);
    if (rand === 0) {
        result = Math.floor(Math.random() * 6) + 1;
        progress += result;
        alert(result + "進むマスに止まった！さらに" + result + "マス進む！");
    }
    alert("現在"　+ progress + "マスまで進んでいます。あと" + (goal - progress) + "マスでゴールです！");
}
alert("ゴールしました！")

