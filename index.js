document.getElementById("submitButton").onclick = function ()
{

    fish_name = document.getElementsByName("textBox");
    n = 20;
    for (let i = 0; i < n; i++) {
        const currentFish = window["fish" + i]; 
        if (!currentFish) break;
        
        if (currentFish === fish_name) {
            found = true;
            break;
        }
    }
}