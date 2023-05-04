function displayTrainType() {
    var station = inputStation();
    var type = getTrainType(station);
    if (station >= 1 && station <= 3) {
        alert("その駅には" + type + "の電車が停まります");
    } else {
        displayTrainType();
    }
}
function inputStation() {
    var station = prompt("行き先を選んで\n1.A 2.B 3.C");
    station = Number(station);
    return station;
}

function getTrainType(station) {
    var type;
    switch (station) {
        case 1:
            type = "快速";
            break;
        case 2:
            type = "快速と急行";
            break;
        case 3:
            type = "急行";
            break;
        default:
            alert("入力が正しくありません")
    }
    return type;
}

displayTrainType();