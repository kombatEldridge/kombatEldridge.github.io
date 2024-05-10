# Updates to ywangcomp.org

When I joined the group, Dr. Wang gave me the task of updating the group's webpage for some small detail (I can't remember at this point). 

She bought her domain and a Linux box from GoDaddy that she is able to host the website from. To manage the content of the website, GoDaddy uses cPanel and an online terminal, but it also allows users to `ssh` into the box if they care to edit the code directly.

### Cosmetics 
My dad was a web developer for a long time before his current job, so growing up I had heard terms like *html* and *web app* but never worked on it (he helped me learn Java though!). After enough Google searches, I think a hobbyist can learn just about any computer language, so that's what I did. 

I made sure the group member's page was up-to-date, and I added some fancy *css* to the cards to make them pop (http://ywangcomp.org/people.html). I made the side navbar appear using *js* instead of having the *html* print it individually (which would've caused an issue when I added a new page).

### Python Applications

#### Mie Multilater
Dr. Wang had a previous student (Dr. Elise Chaffin) translate algorithms from an old 2003 paper on Mie Theory into Mathematica, and my first project with the group was to translate this again but into python.

Once I had done this, she wanted me to make it publicly available on our website. However, I learned quickly that you can't just run python in html. Luckily, the cPanel admin page does have a python app manager that you can use to call a python script from the website. After debugging several of my attempts to get this to work, the app now runs on the website (http://ywangcomp.org/multilayerInstructions.html). 

#### Protein Binding
Several months later, another one of Dr. Wang's projects finished, and she wanted it on the website too. This time, all I had to do was familiarize myself with my first app, and now its running (http://ywangcomp.org/proteinBindingInstructions.html)!

### LCCC Database
The newest adventure in my web dev journey: Angular. Dr. Wang studied polymer chemistry before my time and wanted a webpage where researchers could upload data about polymer experiments, so she contacted the computer science department for some seniors to work on the project. Three accepted, and they built us a website with user authentication, a data upload page, and a data search page -- all on Angular.

Graduation approached, and they still hadn't integrated the Angular app into our Linux box, so I let them know I would do it. Fast-forward to when I actually had time to try, and I find out that our Linux box was way too old to support a newer Angular app (for those curious, the app uses Firebase and many new features of Firebase are broken on Node v15, the newest version I could install on the old Linux box).

My friend Jack helped me put the Angular app on Azure's Static Web App hosting services. I figured out how to point the website to a subdomain of ours, and now its running publicly (https://lccc.ywangcomp.org)!

Sadly, the project wasn't as complete as what I thought. It was ugly, some buttons weren't responsive, some functionalities were missing. For the last couple of weeks I have learned more Angular than I thought I ever would. (And to think, two years ago, I thought I was gonna throw away my computer and go to med school!) I've had help from Jack and a new friend I made at a work event.

Currently, the website is running. It might still be ugly, but I'm working on that (give me a break, css is confusing.) Go check it out!