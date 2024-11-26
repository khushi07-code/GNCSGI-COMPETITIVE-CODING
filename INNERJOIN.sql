Select Person.firstName,Person.lastName,Address.city, Address.state from Person 
INNER JOIN Address On Person.personId=Address.PersonId;
