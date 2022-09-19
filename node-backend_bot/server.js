const express = require("express");
const dotenv = require("dotenv");
const dbConnection = require('./config/db/dbConnection');
const { errorHandler, notFound } = require('./middleware/error/errorHandler');
const customerRoutes = require("./routes/customer/customerRoutes");
dotenv.config();

const app = express();

dbConnection();

// JSON MiddleWare
app.use(express.json());

// User Info related routes
app.use("/customers", customerRoutes);

app.get('/', (req, res) => {
  res.json("online")
})

// ----------------------------------
// Error Handlers
// ----------------------------------
app.use(notFound);
app.use(errorHandler)

// ----------------------------------
// Starting the server
// ----------------------------------
const PORT = process.env.PORT ?? 5000; 


app.listen(PORT, () => {
    console.log(`server started successfully on port ${PORT}`);
});