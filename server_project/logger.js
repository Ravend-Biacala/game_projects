
var url = 'http://mylogger.io/log';

function log(message) {
    // send an HTTP request
    console.log(message); //log is scope to this module, their private not visable to the outside

}

/*
creating a module

module.exports.log = log;
//module.export.endPoint = url; 

*/

/*
module.exports.log = log;
//in this module we don't need an object like "log" because its only one object, this would be nesasarry if it were many methods and properties

*/

/*
#we make module into calling a function

*/

module.exports = log;