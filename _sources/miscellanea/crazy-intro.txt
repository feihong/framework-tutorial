Secrets of the Framework Creators
=================================

Presenters
----------

*Feihong Hsu* lives in the wild and woolly exurbs of northwest Chicagoland. Although primarily a Python programmer, he has another, darker persona that dabbles in C#. Currently, he is between jobs and enjoying some time off. His previous job was at Morningstar Inc, where his responsibilities were to cajole, conflate, and massage vast quantities of financial data. He is the author of wxPita (a wrapper library for wxPython), and he blogs at http://feihonghsu.blogspot.com.

*Kumar McMillan* lives in sunny Chicago, IL and works as a Senior Software Engineer at Leapfrog Online, LLC. He uses Python to manage Leapfrog's ETL pipeline (Extracting, Transforming, and Loading data) as well as build web applications / services and automated testing strategies. He is an active member of the open source community, maintaining several packages like fixture, wsgi_intercept, wikir, and helping out on nose, blogmaker and several others. He writes about software from time to time on his blog, http://farmdev.com/.

A Long-Winded Introduction That Might Uplift Your Soul But Most Likely Will Bore You to Tears
---------------------------------------------------------------------------------------------
One day, I woke up in my bed and said to myself, "Hey, I should download a bunch of popular Python frameworks, take a look under the hood to see what makes them so awesome, and then give a tutorial at PyCon about my findings!"

Ha, as if.

The real story is much more convoluted. The truth is, it all started with me setting out on a doomed quest to create the Ultimate Python GUI Toolkit. Whenever you set out to create an "ultimate" anything, you tend to set yourself up for failure. And failed I did. Spectacularly. Minus the spectacular part, since almost no one even knew what I had attempted to do.

My Ultimate Python GUI Toolkit had turned into an Ultimate Piece of Crap. It was an unholy mess. My university teachers would probably lynch me if they saw that code. But I did produce a lot of code, all in a futile attempt to mimic the APIs of the latest Turbo-Django-Storm hotness.

I was pretty bummed about my failure, since I had been planning on showing off my results in time for PyCon 2008. But it slowly dawned on me that I had done one thing right: I had used my usual lazy-ass approach to programming. Instead of coming up with my own ideas, I stole a lot of good ideas from a number of well-known Python frameworks. So that meant that I knew how they worked! Actually, that only meant that I fooled myself into thinking I knew how they worked.

False confidence can lead to tragic consequences. Like if you spend your childhood playing Street Fighter, and from only that decide that you're tough enough to survive a real street fight. But false confidence is also the impetus we need to challenge fate, to throw caution to the wind and attempt something beyond our ken.

You can probably see where this is all headed. I submitted a tutorial proposal to the PyCon selection committee. To my surprise, they accepted it. I don't think it's because they weren't paying attention. I think it's probably because I'm as good at fooling other people as I am at fooling myself.

So I start seriously writing the tutorial in January. I'm actually proud of myself for starting so early, a whole two months before the actual conference. The God of Procrastination was throwing all these distractions my way (for example, a new Terminator TV show!), and I was swatting them all away as if I were Martina Navritilova.

But very early in the process, I find that I'm having some difficulty. Actually, I'm having a *really* hard time. It's so much work! There are so many decisions to make! I haven't taught computer stuff in ages! What if I pull a Britney Spears when I'm on stage?!? Metaphorically speaking, I had stepped right into a pit of fugly monsters. This was bad. Could I just quit?

But by this time I could see the registration numbers ramping up for the tutorial. Holy crap, Batman, people actually think that I can teach them something! My flagging confidence had been boosted by the (misplaced?) faith of others. Okay, so quitting is *not* an option now. I'd just have to keep plugging at it until I *Got It Done*. Metaphorically speaking, I'd have to keep killing fugly monsters with a teaspoon until I could pile their stinking corpses high enough to climb out of this goddamn pit.

I hope the irony of this situation is not lost on you. I failed to make an awesome framework, so I end up teaching others about how to make awesome frameworks. Wait, that's not ironic at all. That's just the embodiment of that old adage: "Those who can't do, teach".

The Briefer and Less Insane Intro
---------------------------------
In this tutorial, we are going to show you how to take your Python programming to a higher level. We are not going to do this by throwing Scary Computer Science Stuff at you. There is no discussion of algorithms, runtime complexity, or data structures. We are simply going to make you aware of some advanced features of the Python programming language.

The features we will be covering are: frame hacks, magic methods, decorators, and metaclasses. We say that these features are "advanced" because they are used by only 10% of Python programmers (our unscientific estimate). That means that most of the code you see in the wild will not be using them. However, they show up a lot in popular Python frameworks, which implies that they are inordinately useful for creating abstractions. In other words, these features help you write more code upfront so that you can write less code overall. If you're just a user of a framework, you get the benefit of writing less code without having to write a large amount of code at the beginning.

This tutorial is not a comprehensive study of advanced Python techniques, and will not necessarily help you become an expert Pythonista. In fact, the presenters of this tutorial are not experts (note the lack of the words "expert", "guru", or "master" in our bios). However, even non-experts can make effective use of these features. The extra syntax you need to know is minimal, and should not give you any trouble if you have been using Python for a moderate amount of time. To ensure that you grasp the underlying concepts, we have a short, interactive tutorial corresponding to each feature.

The main difficulty, as we see it, is figuring out *when* to use these advanced features. To that end, we have included a number of use cases and recipes. The use cases include both case studies and somewhat-contrived examples that show you real-world scenarios under which a particular feature is used. The recipes help you gain programming experience on a particular feature. Only through repeated exposure to a feature will you truly "get it", but hopefully the recipes will set you on the right course.

There are eight recipes in all, two recipes for each feature. Because we have a limited amount of time, and because we do not know the average skill level of the participants, we do not know if we have a realistic shot at presenting all eight recipes. However, each recipe is designed to be relatively self-contained and includes all the information you need to complete it on your own. For example, each recipe includes several sequential "steps" that progressively build up to a complete program. Each recipe step includes hints and full solutions, in case you get stuck at any point. There is also the `Google Group`_ that the presenters have created. There you can post questions, ask for hints, and otherwise interact with the presenters as well as your fellow participants.

.. _Google Group: http://groups.google.com/group/secrets-of-the-framework-creators/

Sections
--------

.. toctree::
   :maxdepth: 1

   ../framehack/index
   ../decorator/index
   ../metaclass/index
   ../magicmethod/index

Useless Epilogue
----------------

I sought the Holy Grail of GUI Toolkits, but tasted bitter defeat. If I were Indiana Jones, then I didn't save the girl and I didn't melt those Nazis' faces off; instead I ate the poisoned date and got flattened by the giant boulder. However, my efforts were rewarded by sweet, succulent knowledge, and as we all know, "Knowing Is Half the Battle(TM)". In other words, I will be a lady-killing, Nazi-liquefying, lion-whipping badass in the next sequel. (For the record, I don't know what I'm talking about anymore.)

Making this tutorial has taught me a lot of things. That's the funny thing about teaching -- if you're seriously engaged in the teaching process, then you're learning as much as you're teaching. I think it's helped me clarify my thoughts on what makes a useful framework. So, maybe someday, you'll finally see an "Ultimate Python GUI Toolkit" in the Cheeseshop. Except replace "Ultimate" with "Slightly Useful". And then replace "Slightly Useful" with "Not Completely Useless". Then watch me create another PyCon tutorial out of the ashes of my defeat...
