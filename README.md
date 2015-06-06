# ofe
So I was looking on Craigslist one night at job postings. And I saw this one, where these people had encoded their email address by:
* gzipping the address
* base64 encoding the gzip data
* reversing the base64 string

The idea being that you needed to be smart enough to run simple commands to get the email address back out.

It was late at night, and I was bored, and so I had the idea that it would be kinda fun to write up a script to reverse the process, rather than just do it quick by hand.

But.. I had, that week, also had the experience of writing my first python module... and so I also had the idea that it would be kinda fun to put everything into a module that would be easy to call.

Then I had the idea that it would also be fun to have the module do the work in both directions - decode and encode.

And so, here that is.
