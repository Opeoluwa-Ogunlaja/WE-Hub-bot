const expressAsyncHandler = require("express-async-handler");
const Customer = require("../../models/customer/Customer");

const createUserCtrl = expressAsyncHandler(async (req, res) => {
    const { tel, firstName, lastName } = req.body;
    console.log(req.body)

    const customerFound = await Customer.findOne({tel});
    if (customerFound) throw new Error("Customer Already Exists")

    try {
        const customer = await Customer.create({
            tel, firstName, lastName
        })
        customer.save()

        res.json(customer);
    } catch (error) {
        res.json(error);
    }
});

const fetchUserCtrl = expressAsyncHandler(async (req, res) => {
    const { tel } = req.params;

    const customerFound = await Customer.findOne({tel})
    if (!customerFound) throw new Error("You havent't started registering. Input your first name  to start") 

    res.json(customerFound);
});

const fetchAllCustomersCtrl = expressAsyncHandler(async (req, res) => {
    try {
        const customers = await Customer.find();
        res.json(customers);
    } catch (error) {
        res.json(error)
    }
});

const deleteCustomerCtrl = expressAsyncHandler(async (req, res) => {
    const { tel } = req?.body;

    let customerFound = await Customer.findOne({tel})
    if (!customerFound) throw new Error("Customer doesn\'t exist")

    try {
        customerFound = await Customer.findOneAndDelete({tel});
        res.json(customerFound);
    } catch (error) {
        res.json("error");
    }
})

const updateCustomerCtrl = expressAsyncHandler(async (req, res) => {
    const { tel } = req.params
    console.log(tel);

    let customerFound = await Customer.findOne({tel})
    if (!customerFound) throw new Error("Customer does not exist")
    
    try {
        const customer = await Customer.findOneAndUpdate({tel}, {
            ...req?.body
        }, {
            new: true
        })
        
        res.json(customer)
    } catch (error) {
        console.log(error)
        res.json(error)
    }
});

module.exports = {
    create_customer: createUserCtrl,
    fetch_customer: fetchUserCtrl,
    fetch_all_customers: fetchAllCustomersCtrl,
    delete_customer: deleteCustomerCtrl,
    update_customer: updateCustomerCtrl
}