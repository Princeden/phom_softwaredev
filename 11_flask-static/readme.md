## K11: Some Things Never Change
### Due: 2024-09-26r before class

Predictions 
- Return the foo page w/ a random
-i don't think accessing the html through the url and not flask is possible and I will get an error bc it isn't loaded explicitly onto the server
- accessing it straight through foo would just load the html page
Results
-the link does work and you get the html page, that is how you access static pages. 
-if you run flask and route it to static/foo the return overrides whatever what on the html and all you get is the random float
-you can not return none for flask, it will give you an error
- going to foo downloads the file because we're not requesting thehtml file which our browser loads instead just a plain text file named foo which the browser downloads automatically
-the browser doesn't know what to do so it chooses to download it
Your Trio Mission:
1. In a new directory in your workshop, save a copy of the demo for using flask to serve static files.
1. As a team...
  - Familiarize yourself with the app directory structure and the files' content.
  - Note anything notable.
  - Predict expected behaviors.
  - Spin up your website on localhost and reconcile behavior with prediction.
  - Record your notes in `readme` in app's root directory.


1. Once your team has done this, compose and store another html file named `fixie.html` (containing some html to render your team name and roster) so that flask can serve it staticly.

<br>

DELIVERABLES:
* Save to workshop as indicated.
* Each teammate should submit matching sourcecode.

```
path/to/myworkshop$ tree 11_flask-static
.
├── app.py
├── readme
└── static
    ├── foo
    ├── foo.html
    └── fixie.html
```

<br>

[related](https://ukulelemagazine.com/lessons/uke-lesson-3-chords-and-the-truth-country-songwriting-legend-harlan-howard)  
[related](https://en.wikipedia.org/wiki/Plain_text)  

