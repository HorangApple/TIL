//https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/profile-lookup
//Setup
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
        "lastName": "Potter",
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["JavaScript", "Gaming", "Foxes"]
    }
];


function lookUpProfile(name, prop){
// Only change code below this line
  if (contacts[name]) {
    if (contacts[name][prop]){
      return contacts[name][prop];
    } else {
      return 'No such property';
    }
  } else {
    return 'No such contact';
  }
// Only change code above this line
}

// Change these values to test your function
console.log(lookUpProfile("Akira", "likes"));