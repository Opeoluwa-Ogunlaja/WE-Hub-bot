const express = require("express");
const { fetch_customer, create_customer, fetch_all_customers, delete_customer, update_customer } = require("../../controller/customer/customersCtrl");

const customerRoutes = express.Router();

// Create Customer
customerRoutes.post('/create', create_customer);
// Fetch Specific Customer Details Ctrl
customerRoutes.get("/:tel", fetch_customer)
// Fetch All Customers Ctrl
customerRoutes.get("/", fetch_all_customers);
// Update Customer Details
customerRoutes.put("/:tel", update_customer)
// Delete customer
customerRoutes.post('/delete', delete_customer)

module.exports = customerRoutes;