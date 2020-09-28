# Denis Lymer Milestone Project 3 - CRUD app - 'Beer Tracker'
For my Milestone 3 project I decided to create an app I would find useful myself.
I enjoy craft beer and thought a clean, streamlined app that allowed a user to record and edit relevant details 
about the beers they have tried would be useful. Obviously such apps already exist, I have tried some of them,
but I always found them too over-complicated, especially if you've sampled a few beers in one sitting...
so I settled on developing a very user-friendly app that was easy to use and navigate. 
I was impressed by the Materialize framework used in the Code Institute tutorials from this module,
particularly the responsiveness, so I decided to use it in my own project to gain experience using it.

## Link to the website

https://beer-tracker-ci-ms3.herokuapp.com/

## Link to the github repository

https://github.com/menacethedenis/CI_Milestone_3_Denis_Lymer

# UX

Ease of use was the main goal of this project. I wanted to keep the CRUD functionality within as few clicks
as possible. I also decided to keep the layout to 3 seperate pages - Home/main, Add and Edit,
and make navigation between them as simple and obvious as possible.

### **User Stories**

I wrote the following user stories to keep in mind during development:
* As a user I want to be able to easily record details about beers I am drinking or have drank previously.
* As a user I want a streamlined app experience with no features more than one click away.
* As a user I want to be able to edit or delete previous entries.
* As a user I want to be able to record an entry with the minimal amount of info if I am in a rush.

### **Wire frames**

I again used the Balsamiq desktop app to create my wireframes to use as reference points for the app.
I focused on mobile first design, then tablet and finally desktop layout.

<details>
<summary>Mobile - Main Page</summary>
<br>

![Mobile - Beer Tracker - Home page](https://user-images.githubusercontent.com/48594804/94488878-5a564180-01db-11eb-94fd-9d5b5e4a7aa4.png)

</details>
<details>
<summary>Mobile - Add Page</summary>
<br>

![Mobile - Beer Tracker - Add page](https://user-images.githubusercontent.com/48594804/94488874-59bdab00-01db-11eb-8bd0-642a90172eb9.png)

</details>
<details>
<summary>Mobile - Edit Page</summary>
<br>

![Mobile - Beer Tracker - Edit page](https://user-images.githubusercontent.com/48594804/94488877-59bdab00-01db-11eb-83d9-68ee1af1a8d8.png)

</details>

<br>

<details>
<summary>Tablet - Main Page</summary>
<br>

![Tablet - Beer Tracker - Home page](https://user-images.githubusercontent.com/48594804/94488884-5aeed800-01db-11eb-9702-32348686edab.png)

</details>
<details>
<summary>Tablet - Add Page</summary>
<br>

![Tablet - Beer Tracker - Add page](https://user-images.githubusercontent.com/48594804/94488881-5a564180-01db-11eb-9e30-c33564557671.png)

</details>
<details>
<summary>Tablet - Edit Page</summary>
<br>

![Tablet - Beer Tracker - Edit page](https://user-images.githubusercontent.com/48594804/94488882-5aeed800-01db-11eb-9d0b-4404d43f793e.png)

</details>

<br>

<details>
<summary>Desktop - Main Page</summary>
<br>

![Desktop - Beer Tracker - Home page](https://user-images.githubusercontent.com/48594804/94488873-59251480-01db-11eb-9d46-b1b30212b809.png)

</details>
<details>
<summary>Desktop - Add Page</summary>
<br>

![Desktop - Beer Tracker - Add page](https://user-images.githubusercontent.com/48594804/94488870-588c7e00-01db-11eb-89a4-f27da0d0c7c4.png)

</details>
<details>
<summary>Desktop - Edit Page</summary>
<br>

![Desktop - Beer Tracker - Edit page](https://user-images.githubusercontent.com/48594804/94488871-59251480-01db-11eb-8a8d-3ea517a4ab15.png)

</details>

# Features

## Existing Features

### **General**

* Feature 1: Navbar: In keeping with my 'one-click away' philosophy for this site, I decided to leave the Navbar links open and visible across all screen sizes.
* Feature 2: Footer: The footer has working links to social media sites on the right and to the About page on the left. The icons are from Font-Awesome.
* Feature 3: Theme: I used a bootstrap template from bootswatch.com to kickstart my css and layouts.

### **Home page**

* Feature 4: Search bar - The home page prominently displays a brief message detailing the site's purpose and a large search bar with a search prompt. This should instantly let the user know what the site is for.
* Feature 5: Results - Using Javascript the search function connnects to the TMDB API and pulls back results to the browser window. The user can see the movie or tv show's poster, name and a button underneath labelled 'Details'.
* Feature 6: Lower page Image - The frustrated/scared woman repeating image only appears on large screens. CSS media queries were used to remove it on tablet and mobile screen sizes.

### **Details page**

* Feature 7: Detailed results - When a user clicks the 'Details' button under the search results the site navigates to a new page. Here a user can view details about the movie such as title and poster image. Rating, Tagline, Genre, Release Date and Runtime.
* Feature 8: Plot - The movie plot is displayed beneath the detailed results.
* Feature 9: View ImDB button - This button links to the ImDB page for the selected movie. This function is included in lieu of having to pay for API access.
* Feature 10: Go back - The user can return to the search/main page here if they are not happy with the result or want to check for something else.
* Feature 11: Disqus app - At the bottom of the page a fully functional Disqus app is embedded. This allows users to login and caht to other users about the particular movie.

### **About page**

* Feature 12: About section - This contains a brief mission statement. There is a link to the Forum page in the text. There is also a copyright-free placeholder image in lieu of a proper website logo. This only appears on large screens. It does not display on tablet or mobile sizes, the mission statment is centred instead.
* Feature 13: Footer - The link to About that appears on other pages footers is changed to allow the user to navigate back to the search/home page instead.

### **Forum page**

* Feature 14: Disqus app - This page is dedicated to the Disqus app so users can chat to each other outside of search results. There is a brief disclaimer displayed at the top of the page.


## Features Left to Implement

* I would have loved to spend more time on this project. I will definitely be returning to it once I have completed the course as I believe it has strong potential to be a going concern. Unfortunately I am up against the clock now in terms of my finish date so need to move on.
The CSS in general could be slicker. I will look into overhauling that.
* I would like to recode the javascript to connect to more APIs from established sites. That will require monetary investment but is something I would like to do once I am employed again.


# Technologies Used

## HTML5 - https://www.w3.org/TR/html52/
HTML5 was used for the general structuring and positioning on the website.

## CSS3 - https://www.w3.org/Style/CSS/Overview.en.html
CSS3 was used to style the website.

## JQuery - https://jquery.com/
JQuery was used to deploy javascript functionality with bootstrap/bootswatch.

## Javascript - https://www.javascript.com/
Javascript was used to access the API and manipulate the results, based on search info inputted by the user.

## Font Awesome - https://www.bootstrapcdn.com/fontawesome/
Font Awesome V4.7.0 icons were used for the Social Media links in the footer.

## Git, Gitpod & Github - https://github.com/
Gitpod was used as the development environment. Git was used to push my work from my local repository to my Github repository. Github hosts the project repository for others to see and the final deployed version of the website.

# Testing

## Manual Testing
Based on feedback from My Milestone one project, this time around I documented my testing in a word document. This is available to view in the assets folder of this project or can be downloaded directly at: https://c28e0d1a-181e-43e6-a8c0-f2acb6318d5f.ws-us02.gitpod.io/files/download/?id=84ab1048-22ab-45a8-91e9-ca88f2e8cd78 

You will see a long gap in testing dates between July and September, this is due to my emigrating from Ireland which interrupted development on the project. In addition to the word doc, similar to my milestone one project, as I was building this project I was ensuring to test the functionality of pagelinks, external links, navigation, features and elements as I was proceeding. At the end of every session I not only checked any new features I had added, but also all my existing features to ensure any changes I had made had not adversely affected other existing features.

All code was checked with the following validator: https://validator.w3.org/

## Responsiveness Testing with Chrome DevTools
All website pages have been extensively tested for mobile-first responsiveness using Chrome DevTools. I personally checked responsiveness on the following devices:
* Android 10 phone
* Android 10 tablet 
* Windows 10 laptop
* Windows 10 desktop

Some colleagues were asked to check responsiveness on:
* iPad - iPadOS 13.5
* iPhone - iOS 13.5
* iMac - MacOS 10.15

# Deployment
 I started this project by using the Code Institute template available on Github at: https://github.com/Code-Institute-Org/gitpod-full-template. As I was building the project I was regularly saving my work using the Git Add functionality and tracking my changes with descriptive messages using the Git Commit functionality. I used Git Push to send to the remote repository. I was able to pick up exactly where I left off by clicking on the Gitpod button to access my workspace on the remote repository. When the project was finished I accessed the settings menu and activated GitHub Pages.
 
 Other users can clone the project by entering the following command in their terminal: Git Clone https://github.com/menacethedenis/CI-milestone-two.git
 
 The finished website is deployed and can be viewed via Github pages:
 https://menacethedenis.github.io/CI-milestone-two/

# Credits
## Content

As the API functionality I wanted to use in this project was not covered in the Code Institute tutorials, I had to do a great deal of external research and learning over the course of this project. Some of the sites I found very helpful in general were:
https://rapidapi.com/blog/how-to-use-an-api-with-javascript/
https://www.youtube.com/watch?v=YsPqjYGauns
https://www.youtube.com/user/TechGuyWeb
https://www.youtube.com/user/shiffman
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Introduction

For the Javascipt functionality I relied heavily on Github and Stack Overflow threads for more detailed understanding. I repurposed or reused some code snippets from some of the following:

https://stackoverflow.com/questions/957537/how-can-i-display-a-javascript-object/4293047#4293047
https://stackoverflow.com/questions/1625208/print-content-of-javascript-object?noredirect=1&lq=1
https://stackoverflow.com/questions/1966503/does-imdb-provide-an-api
https://github.com/algolia/algoliasearch-client-javascript
https://github.com/EmmaSemutenga/movieInfo/blob/master/js/main.js
https://github.com/bvaughn/js-worker-search
https://github.com/FriesFlorian/viralvideos
https://github.com/anshulrgoyal/imdb-scrapper

The free API database I used was The Movie Database (TMDB):

https://developers.themoviedb.org/3/movies/get-movie-credits

I also linked search results to the more established and well-known review site ImDB:

https://www.imdb.com/

## Acknowledgements
I would like to thank the tutors at the Code Institute and my mentor Spencer Barriball for their outstanding support, advice and encouragement. Neil Kavanagh who graded my Milestone One project also gave me some excellent and useful feedback.

Thanks also to the Code Institute student care team for keeping me on track, checking in and always being so understanding, empathetic and helpful.