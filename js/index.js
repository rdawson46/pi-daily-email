
/*
will locally host the html on a website
will be accessed to see the last email was sent out
*/

errorCode = parseInt(process.argv.slice(2)[0]);
ipAddr = process.argv.slice(2)[1];

const path = require('path');
const express = require('express');
const morgan = require('morgan');

const port = 8080;

const app = express();
app.use(express.json());
app.use(morgan('dev'));

app.get('/', (request, response)=>{
    if(errorCode){
        response
            .status(200)
            .sendFile(path.join(__dirname, './pages/error.html'))
    }else{
        response
            .status(200)
            .sendFile(path.join(__dirname, './pages/success.html'))
    }
});

app.post('/', (request, response)=>{
    const value = request.body.statusCode;
    console.log(value);
    if (value === undefined){
        response.status(400).send('Error')
    }else{
        errorCode = value;
    response.status(200).send('Data recieved');
    }
});

app.listen(port, ipAddr,()=>{
    console.log(`Server is running on port http://${ipAddr}:${port}`);
});
