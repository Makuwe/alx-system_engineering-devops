avaScript Object Notation (JSON) is a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa). You'll come across it quite often, so in this article, we give you all you need to work with JSON using JavaScript, including parsing JSON so you can access data within it, and creating JSON.

Prerequisites:	A basic understanding of HTML and CSS, familiarity with JavaScript basics (see First steps and Building blocks) and OOJS basics (see Introduction to objects).
Objective:	To understand how to work with data stored in JSON, and create your own JSON strings.
No, really, what is JSON?
JSON is a text-based data format following JavaScript object syntax, which was popularized by Douglas Crockford. Even though it closely resembles JavaScript object literal syntax, it can be used independently from JavaScript, and many programming environments feature the ability to read (parse) and generate JSON.

JSON exists as a string — useful when you want to transmit data across a network. It needs to be converted to a native JavaScript object when you want to access the data. This is not a big issue — JavaScript provides a global JSON object that has methods available for converting between the two.

Note: Converting a string to a native object is called deserialization, while converting a native object to a string so it can be transmitted across the network is called serialization.

A JSON string can be stored in its own file, which is basically just a text file with an extension of .json, and a MIME type of application/json.

JSON structure
As described above, JSON is a string whose format very much resembles JavaScript object literal format. You can include the same basic data types inside JSON as you can in a standard JavaScript object — strings, numbers, arrays, booleans, and other object literals. This allows you to construct a data hierarchy, like so:

json
Copy to Clipboard
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
If we loaded this string into a JavaScript program and parsed it into a variable called superHeroes for example, we could then access the data inside it using the same dot/bracket notation we looked at in the JavaScript object basics article. For example:

js
Copy to Clipboard
superHeroes.homeTown;
superHeroes["active"];
To access data further down the hierarchy, you have to chain the required property names and array indexes together. For example, to access the third superpower of the second hero listed in the members list, you'd do this:

js
Copy to Clipboard
superHeroes["members"][1]["powers"][2];
First, we have the variable name — superHeroes.
Inside that, we want to access the members property, so we use ["members"].
members contains an array populated by objects. We want to access the second object inside the array, so we use [1].
Inside this object, we want to access the powers property, so we use ["powers"].
Inside the powers property is an array containing the selected hero's superpowers. We want the third one, so we use 
