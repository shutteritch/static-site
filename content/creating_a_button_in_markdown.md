Title: Creating a button in Markdown
Date: 2020-05-01 14:42
Category: Code
Tags: Markdown, HTML
Slug: create_button_in_markdown
Authors: Iain
Summary: I wanted to create a button for this site but am new to Markdown. Here's how I managed it.
Draft: True

The bad news is that google let me down in as much as I couldn't find a way to create a button in Markdown - however, what I did learn was extremely useful...

###You can simply add HTML to your Markdown code!!! 🤯

So, I added a button using HTML.

But then... I found an even better way. Instead of creating a button I simply created a link and added a class.

~~~
<a class="link-button" href="http://iainweir.info">My Site</a>
~~~

And then simply added some button styling to the CSS file for the site (I cut and paste this from the styling already used on the site for buttons elsewhere - thank you developer tools!!)

~~~
.link-button {
    background-color: #d9411e;
    padding: .2em .6em;
    font-size: .74em;
    line-height: 1;
    color: #fff;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: .25em;
}
~~~

You can see the button in action if you visit the [Python Books](https://distracted-snyder-1a6b70.netlify.app/pages/python-books.html#python-books) section of this website.