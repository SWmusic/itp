# I did a thing: Part 1

## What thing was it?

In processing, I made the elden ring.

## How did I do it?

Setting the size of the graph to 100 pixels wide and 100 pixels tall, I took the measurements I had of the ellipses on the graph paper I drew phase 1 on, and just translated the coordinates and sizes over to processing. I knew by starting with a perfect square might possibly help me with the tiling later, so I made sure to get it out of the way now. Then, by setting the ellipses to no fill (making them stroke/ border only) they overlapped creating the celtic ring pattern that is the elden ring. Nerdy, I know.

## What did I struggle with?

Well, at first not much. It was basic plotting and drawing out. Hell, I even got the diameters of the ellipses right by just counting it out on the graph paper. With all of that tooting of mine own horn, when it came time to run the code something really sad happened. Only three of the four circles showed up (presumably the first one had been covered by the other three), and even at that they were missing around a 3rd of their borders each.

## How did I solve this problem?

Well, at first I did some thunkin. Then I experimented with the no stroke and fill commands. Maybe by making the fill grey would make it overlap? Well, nostroke just deleted the lines and the borders, so I knew that wasn't it. And no matter what color or shade of grey I did they would not overlap. Taking away the fill command didn't do anything either (I later learned the reason why).

So, I knew I had to create an "empty shape". But how? I looked it up, "how to make overlapping shapes in processing". Nothing helpful. I asked reddit, they just told me to put it into chat gpt, but that was the easy way out so I didn't, and also because it's more satisfying to figure it out yourself than to have instant gratification.

After several days of just thinking about it and dealing with it in my head, I sat down this morning (Tuesday the 19th) and googled the same thing again. I saw a processing discussion forum about the same fundamental thing, but on a much more advanced scale as the person's project was really advanced, but wanted to figure out the overlapping shape problem. Someone's response was helpful to him, but not to me, until I saw the words "a more transparent color". Bells were ringing in my head, I knew I wasn't crazy, so where was this information?

It was on a page I had literally visited the first day of working on the project. I just had to scroll down LITERALLY 4 MORE INCHES AND I WOULD'VE SAW IT. It was on processing's page about color numerical values. I scrolled down maybe twice to see the noFill() command. Bingo. Phase 2? Complete.
