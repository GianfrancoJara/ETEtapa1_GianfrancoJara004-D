$(document).ready(function()
{
    $("#infoClima").mouseover(function(){
        $.get("http://api.openweathermap.org/data/2.5/weather?q=santiago&appid=12af6ee760b0e5db6ed752a12c4c7fb4",
        function(data){
            $('#infoClima').html( 
                "La temperatura en Santiago actualmente es de "+(Math.round(data.main.temp - 273))+" grados Celsius, con una humedad del "+data.main.humidity+" porciento." );
        });
    });
})
