# gthumb-keywords
Use an AutoKey script with dmenu to fix gthumb's keyword (tags) system.

Gthumb seems to be the best image viewer on Linux for the following reasons:

Stable: Many other viewer I tried crashed often.

Fast: It may not be the fastest, but it's not slow either.

Animated Gifs and Movies: It's one of the few that supports animated gifs and movies.

Tags: If the file is .jpg, it will put your keyword tags into the file's metadata. (I'm not sure about movie formats.) Otherwise, such as for .gifs, it keeps the information in an xml file. 

Other image viewers capable of tagging often can only tag .jpgs or may not put it into the file's metadata.

For these reasons, I chose gthumb to tag my collection of images and movies, but Gthumb places the Tags window right over the image being tagged! My script automatically moves that window over, so you can look at the image (or movie) while selecting your tags.

Then, to tag things, you have to either use the mouse to select them from a list or type them by hand. There IS autocompletion, but you have to hit the down arrow to access it. Much better would be the Tab key, because then you wouldn't have to move your hand away from the home row. For tagging a lot of files one after the other, this kind of thing makes a difference!

However, there's an even better way: dmenu menus. Using dmenu, you can maintain categories of keywords, present them in any order, and the user can select keywords by typing characters from anywhere inside them. When there is no longer more than one match, that keyword is automatically selected.

This seems to be about the fastest way to enter keywords, as neither the mouse, nor moving from the home row is required. The script also automatically moves to the next image.

Also, this system helps you to not forget keywords by running through your categories one after the other. 

You could also put all the keywords into a single big category if you prefer and never deal with more than a single menu. I use a hybrid approach where I have menus go in order before reaching a menu with my most commonly used keywords. From this menu, however, all the remaining categories can be reached, each with its own menu.


