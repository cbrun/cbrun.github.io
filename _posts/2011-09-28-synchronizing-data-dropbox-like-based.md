---
layout: post
title: "Synchronizing data : Dropbox-like based on open-source stack"
date: '2011-09-28T03:36:00.000-07:00'
categories: [eclipse]
tags:
  - eclipse
modified_time: '2011-09-28T03:36:00.168-07:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-5785203010688962162
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/09/synchronizing-data-dropbox-like-based.html
draft: true
---

I had to find a solution for my **backup/cloud drive** needs lately. [Dropbox](https://www.dropbox.com/pricing) works just fine, but the pricing is going high too fast as you want more space.

A 1To / 100Mbs dedicated server is [not that expensive](https://www.kimsufi.com/) and provides the nice perspective of more server/web-oriented hacks later on.

After trying a few open source projects in this regard ([Syncany](https://www.syncany.org/), [Csync](https://www.csync.org/) or [SparkleShare](https://sparkleshare.org/)) and keeping away from the desire of building my own, here is my short list:

- Sparkleshare is very nice for things which I want to keep versions of. I really like the fact that it's keeping everything in a git repository; any file manager providing git integration will then allow me to dig through the history of files. As I'm not interested in the fact that it works on multiple platforms (linux, mac and soon windows) I still have to check if a script launching automatic `git add . && git commit && git push` is not going to be as reliable as SparkleShare while being lighter.
- For non versioned directories, [inotifywait](https://linux.die.net/man/1/inotifywait) + csync are just fine. (incron, a cron-like tool but using filesystem events as an input did work but is not supporting recursive watching)

I also considered Syncany but did not like the fact that server side chunks of data are used which have no standard way of being accessed beside Syncany. I quickly had the feeling that git would do just fine in this regard, especially with a few `git gc --aggressive` from time to time.

I'm pretty sure using the new [Java 7 filesystem notifications](https://thecodersbreakfast.net/index.php?post/2011/05/18/Filesystem-notifications-with-Java-7) + [jgit](https://eclipse.org/jgit/) one could very quickly build an highly efficient and multi-platform solution. I managed to refrain myself trying it, but if you do or know someone who did, please let me know ;) edit: [Mikael](https://github.com/mbarbero) did start such a thing on [github](https://github.com/mbarbero/backgitup).

If you are an OpenSuse user here is the [magic repository](https://download.opensuse.org/repositories/network:/synchronization:/files/openSUSE_11.4/).

We'll see in a few months if I'm still happy with these solutions. Feel free to add a comment if you have other options!

