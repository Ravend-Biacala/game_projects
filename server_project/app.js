
/*function sayHello(name) {
    console.log('Hello ' + name);
}

//sayHello('Mosh');
*/
//console.log(window); #this is a global object

/*
setTimeout()
clearTimeout();
setinterval()
clearInterval()

*/



 /*

var message = '';
console.log(global.message);

 */


/*
console.log(module); 'appear to global but is isnt
const log = require('./logger'); //to load a module we use the require function
console.log(logger);

*/

/*
//constants
constant logger = require('./logger'); //better to store the logger into a constant
logger.log.('message');
*/

/*

*/

const log = require('./logger');
log('message') // so we just call the funciton and change the function to log cuz its simpler
