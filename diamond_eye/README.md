# Diamond Eye

Image storing system. Cheap and simple. 

## Why

Initial goal was to gather all images related to the Blade Runner theme 
(book, movie, anime, etc.). Actual media is stored in different repository 
called Nicord's catalogue (name is inspired by Sidney's Animal & Fowl Catalogue).

## How

Bunch of files on your hard drive. Updates once a month. 
JSON all the way. No database. No server.

## Algorithm

Image comparison algorithm is based on paper by H. Chi Wong, 
Marshall Bern and David Goldberg, published in Xerox Palo Alto Research Center.

You can read the paper here: http://www.cs.cmu.edu/~hcwong/Pdfs/icip02.ps

It has a reference implementation: https://www.pureftpd.org/project/libpuzzle

Currently I'm using slightly modified version of 
[Image Match](https://github.com/EdjoLabs/image-match).

Unfortunately I was unable to launch original code from their repository due 
to problems with building all of those outdated data science libraries. So I 
had to cut the most important parts of the original code and rearrange it 
slightly. Base idea of the Image Match was really suited for my needs, 
but I wanted to avoid the need of full scale server any way possible.

## How to use

At first you need to run web server on localhost. This will allow you to 
browse images, read and edit their tags. And also upload new images! Anything 
you've done will be saved in folder "staging". If you will archive this folder 
and send it to me, I could merge your changes into the main repository, and 
publish it into the next month release.

## Isn't this a bit too simple?

Well, I'm worrying only few people will be interested. So this is just a way 
to avoid renting full size server.

## Web interface

### User identification

On start of the server system will ask your name and will generate personal key 
for you. This is used only for statistic counting, no security measures are used 
on this. Please keep your **key.json** file, there's no way you could restore it. 
All statistic is stored in plain text, I hope that nobody will be really 
interested in cheating here.

### What can you do using web interface

- Browse random existing images.
- Browse some specific image, read and edit it's tags.
- Upload any amount of new images. System will automatically check them for being duplicated.

All actions are going through journal. Main idea behind this is the ability 
to revert changes or shift to some specific moment in past.
