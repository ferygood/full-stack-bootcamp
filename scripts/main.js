let https = require("https");
let fs = require("fs");
let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json";


https.get(url, function(response){
    let data = "";
    //console.log("start");
    response.on("data", chunk => {
        //console.log("on data");
        data += chunk;
    });

    response.on("end", () => {
        data = JSON.parse(data);
        console.log(data);
        console.log(data["result"]["results"][0])
    });
});

