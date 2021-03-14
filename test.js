//const { report } = require("process");
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();
xhr.open("get", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json");
xhr.onload=function(){
    console.log(this.responseText);
};
xhr.send();
console.log("hello wolrd")
console.log(xhr["result"]["results"]);
