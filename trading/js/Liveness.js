var request = require("request");
// set url
const url = "https://api.deversifi.dev/v1/trading/liveness";
// execute request and print result
request(url, function(error, response, body) {
    console.log(JSON.parse(body));
});