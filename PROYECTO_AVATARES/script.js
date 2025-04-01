const canvas = document.getElementById("avatarCanvas");
const ctx = canvas.getContext("2d");


function drawAvatar(skinColor, hairColor) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
 
    ctx.fillStyle = skinColor;
    ctx.beginPath();
    ctx.arc(150, 100, 50, 0, Math.PI * 2);
    ctx.fill();
    
   
    ctx.fillStyle = hairColor;
    ctx.fillRect(110, 50, 80, 20);
}


document.getElementById("colorPiel").addEventListener("input", (e) => {
    drawAvatar(e.target.value, document.getElementById("colorCabello").value);
});

document.getElementById("colorCabello").addEventListener("input", (e) => {
    drawAvatar(document.getElementById("colorPiel").value, e.target.value);
});


document.getElementById("downloadAvatar").addEventListener("click", () => {
    let link = document.createElement("a");
    link.download = "avatar.png";
    link.href = canvas.toDataURL();
    link.click();
});


drawAvatar("#f1c27d", "#000000");
