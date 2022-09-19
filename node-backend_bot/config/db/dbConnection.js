const mongoose = require("mongoose");

const dbConnection = async () => {
    try {
        await mongoose.connect(process.env.MONGO_URL, {
            useNewUrlParser: true
        });
        console.log("DB Connected Successfully");
    } catch (error) {
        console.log(error.message);
    }
}

module.exports = dbConnection;