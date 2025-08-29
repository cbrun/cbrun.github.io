---
layout: post
title: "Do you want to discard this editor's changes ?"
date: '2011-12-16T09:55:00.000-08:00'
categories: [modeling]
tags:
  - emf compare
  - eclipse
  - ecore
modified_time: '2011-12-16T09:55:56.778-08:00'
blogger_id: tag:blogger.com,1999:blog-5749374620125186414.post-4696937203004590569
blogger_orig_url: https://model-driven-blogging.blogspot.com/2011/12/do-you-want-to-discard-this-editors.html
---

If you've used EMF editors you probably already have seen this kind of dialog:

![Discard changes]({{ site.url }}/images/blog/2011/discard-changes.png)

This happens when you changed your model and some external changes (aka somebody else changed your file) happened before you pressed "save". This is not only an EMF problem — any editor has this kind of problem. Either way the end user has a very hard time understanding why he has to pick one or the other version as most of the time these changes are not conflicting!

Is that the best we can do? Another option is to compare both versions, detect conflicts, and if there are no conflicts, just merge the changes.

![Unsync]({{ site.url }}/images/blog/2011/step2-unsync.png)

Here I changed the number of pages in the EMF Book from the model, and changed the title through the textual editor. When going back on my editor, the comparison, conflict detection and then merge process happens and I get this:

![Merged]({{ site.url }}/images/blog/2011/step3-merged.png)

And when I have conflicts? Then the editor can't do much — at least it can help you and show you the conflict:

![Conflict resolution]({{ site.url }}/images/blog/2011/step6-conflict-resolution.png)

How is it implemented? That's fairly easy using EMF and its [diff/merge support](https://www.eclipse.dev/emf/compare/):

<script src="https://gist.github.com/cbrun/1487029.js"></script>

The general process is: the editor tells the WorkspaceSync class when it got saved (or freshly loaded). This WorkspaceSync keeps a copy of the state of the editor as "ancestor". When an event comes from the workspace, the editor version and the workspace versions are compared using the original copy as a common ancestor to detect conflicts. If there is no conflict, it merges; if there is at least one conflict it asks the user.

The drawback is clear with this implementation: you're keeping around — in memory — a copy of your model to be able to detect conflicts later on. As such that solution is not for every case.

Other options are possible and might be great ways to exercise your EMF skills; if you try something, tell me!
