const canvas = document.getElementById('pixelCanvas');
const context = canvas.getContext('2d');

const pixelSize = 5; // ピクセルのサイズ
const imageData = context.createImageData(pixelSize, pixelSize);
// ピクセルアートのデータ（仮のデータ）

//黒
const p0 = [0, 0, 0]
//暗グレー
const p85 = [85, 85, 85]
//明グレー
const p170 = [170, 170, 170]
//白
const p255 = [255, 255, 255]

const pixelArt = [
  [p255, p255, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, 1, 1, 1, 1, [255, 255, 255], 1, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, 1, [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [170, 170, 170], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], 1, p170, [255, 255, 255], [255, 255, 255], [255, 255, 255], p170, [255, 255, 255], [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], [170, 170, 170], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [1, [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [1, [255, 255, 255], [255, 255, 255], [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [1, [255, 255, 255], [255, 255, 255], [170, 170, 170], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], 1, 1, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [1, p85, p85, [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [1, p85, p85, [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [1, p85, p85, p85, p85, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [170, 170, 170], 1, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], 1, p85, [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [170, 170, 170], [170, 170, 170], [170, 170, 170], 1, 1, [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], 1, 1, 1, 1, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], 1, 1, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], 1, 1, 1, 1, 1, 1, [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
  [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
];

// ピクセルアートを描画する
for (let y = 0; y < pixelArt.length; y++) {
  for (let x = 0; x < pixelArt[y].length; x++) {
    const colorCode = pixelArt[y][x];

    for (let i = 0; i < imageData.data.length; i += 4) {
      imageData.data[i] = colorCode[0]; // R
      imageData.data[i + 1] = colorCode[1]; // G
      imageData.data[i + 2] = colorCode[2]; // B
      imageData.data[i + 3] = 255; // アルファ値（不透明）
    }

    context.putImageData(imageData, x * pixelSize, y * pixelSize);
  }
}