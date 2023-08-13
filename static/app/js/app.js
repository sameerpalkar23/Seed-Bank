var input = document.querySelector('.input_text');
var button = document.querySelector('.submit')

var main = document.querySelector('#name');
var temp = document.querySelector('.temp');
var hum = document.querySelector('.hum');
var rain = document.querySelector('.rain');
var desc = document.querySelector('.desc');
var clouds = document.querySelector('.clouds');


button.addEventListener('click',function(name){
    fetch('https://api.openweathermap.org/data/2.5/weather?q='+input.value+'&appid=f1d56e2b9cd49a2562e616ad600878f5')
    .then(response => response.json())
    .then(data => {
        var nameValue = data['name'];
        var tempValue = data['main']['temp'];
        var humValue = data['main']['humidity'];
        var rainValue = data['main']['pressure'];

        
        

        main.innerHTML =nameValue;
        temp.innerHTML ="Temperature - "+tempValue;
        hum.innerHTML ="Humidity - "+humValue;
        rain.innerHTML ="Pressure - "+rainValue;
        input.value = "";

        
    })
    


})