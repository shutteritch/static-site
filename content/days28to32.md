Title: 100DaysOfCode Days 29-32: Static Websites
Date: 2020-05-02 10:15
Category: Code
Tags: Markdown, HTML, CSS, 100DaysOfWeb, 100DaysOfCode, Python, Pelican, GitHub
Slug: static-website-with-pelican
Authors: Iain
Summary: A summary of the work I've done on this site as part of the 100 Days of Web in Python course.
Draft: True

For days 29-32 of the [\#100DaysOfWeb course](https://training.talkpython.fm/courses/explore_100days_web/100-days-of-web-in-python) I learned how to create a static website using Pelican. **This website in fact!**

Pelican automatically generates HTML pages from the more readable Markdown content that I create on my computer. I then push this to the connected repository on Github where Netlify detects new content and automatically adds it to the live site. It sounds a little bit disjointed but once it's setup it makes it really easy to update the site from a text editor and command line.

Once the site was up and running after days 1 and 2 it was just left to me to have a play on days 3 and 4 and what you see now it the result.

A summary of what I've done is as follows:

- Created a couple of new blog posts, using markdown to incorporate sections of code and hyperlinks.
- Created a page listing Python books that I've found useful, this page includes:
    - Images that hyperlink to the relevant amazon pages, written in markdown.
    - Buttons that link to amazon, which I tried to write in markdown but couldnt find a way, until I learned that you could simply write HTML - [I wrote a post about this](https://distracted-snyder-1a6b70.netlify.app/create_button_in_markdown.html#create_button_in_markdown).
- Installed a new theme to the site.
- Fixed a bug in the theme whereby the two parralel lines in the menu bar were displaying incorrectly between 'Home' and the rest.
- Changed the layout of a blog post to show the date at the top, above the title instead of below. This involved editing the HTML as well as the CSS to improve the spacing afterwards.
- Changed the order of the links in the sidebar by flipping the order of the for loops. It now goes Links then Pages rather than Pages then Links.
- Added some social accounts.
- Changed the photo.

I'm not sure that I'll be keeping this site active, it's a very simple and effective way to keep a text based blog, but looking forward in the plan for the rest of the 100 Days of Web course there are lots of other interesting frameworks in the pipeline!

Bye for now!