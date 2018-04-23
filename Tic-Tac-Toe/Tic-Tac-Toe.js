/*Applications have state, stored in object tree.

All JS objects are part of an inheritance tree with a parent object (not including the root)

JS is an interpreted programming language
Content -> Presentation -> Behavior


Objects have properties, events, and methods
  -Characteristics (name, value)
  -Events, what happens in response to something
  -Methods (Get and post functions essentially)

Events trigger methods, which alter characteristics


1.) HTML code received as .html file
2.) Model of page created using object tree (with document object as root)
3.) Nodes extended below
4.) Rendering completes using CSS link

We use the <script> element to tell the browser we are using a JS script
<script src = "myScript.js">  </script>
  Best practice is to place your scripts before the closing body tag

We can also do <script> document.write('<h3>This is my text!</h3>'); </script> to directly
in-line the script, rather than importing it from another page

Scripts are loaded where the script element is placed. For the example previously, of dynamically
printing different messages depending on time of day, where the text will be located depends on
where the script is placed. BUT, this has performance implications (page 356)


Variables can only contain $, _, or alpha-numeric characters


Function Expressions are declared as:
var area = function (a, b){};
These type of functions are not seen by interpreter before run-time, so cannot be call it before declaring

IIFE (immediately invoked function Expressions)
var area = (
  function(){
    var width = 3;
    var height = 2;
    return width * height;
  }()         //Paranthesis ont his line tell interpreter to immediately call function
);            //Outer paranthesis ensure intepreter treats everything inside as expression (closing group operator)

              //Can playe the final paranthesis after the closing group operator, best practice is before
The above runs the function and stores the return into var area


USE CASES:
Argument when a function is called
Assign value to an object's property
Event handlers and listeners
Variable name protection (can wrap around a set of code, protecting whatever is inside from var names outside)

Normal functions are delcared as:
function area  (a, b) {};


access an object's properties using myObject['myKey'];

delete myObject.myProperty
new myObject(p1, p2, p3); //Can be used if you define your own constructor

myObject.myProperty = ''
myObject.myProperty = 'newValue';
myObject[myProperty] = 'newValue'

Gallery script to check if a user clicked on an image,
to display a larger version of the image

-Access page content
-Modify page content
-Rules for browser to follow
-React to events triggers by user/browsere



*/
