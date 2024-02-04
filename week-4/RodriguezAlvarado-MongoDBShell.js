/**
 * Title: RodriguezAlvarado-MongoDBShell.js
 * Author: Zadkiel Rodriguez Alvarado
 * Data: 02/03/2024
 * Description: MongoDB Shell
 * Sources:
 *       https://www.mongodb.com/docs/mongodb-shell/write-scripts/  
 */
// Load user.js module
load("user.js");

// Display all of the documents in the user's collection
db.users.find();

// Display user with email address jbach@me.com
db.users.find({ email: "jbach@me.com" });

// Display user with last name Mozart
db.users.find({ lastName: "Mozart" });

// Display user with first name Richard
db.users.find({ firstName: "Richard" });

// Display user with employeeId 1010
db.users.find({ employeeId: "1010" });
