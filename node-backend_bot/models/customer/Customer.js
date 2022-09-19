const mongoose = require("mongoose");

const customerSchema = new mongoose.Schema({
    tel: {
        type: String,
        required: [true, "Phone number is required"]
    },
    firstName: {
        type: String,
        default: ""
    },
    lastName: {
        type: String,
        default: ""
    },
    occupation: {
        type: String,
        default: ""
    },
    registered: {
        type: Boolean,
        default: false
    },
    startedRegistration:{
        type: Boolean,
        default: false
    }
})

const Customer = mongoose.model("Customer", customerSchema);

module.exports = Customer;