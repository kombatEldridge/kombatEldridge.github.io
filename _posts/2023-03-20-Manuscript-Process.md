I started writing a manuscript for publication on the Mulitlayer project on December 10th, 2022. I had gone home for Christmas, and I had some time before the festivities started. Here is a retroactive timeline of my progress. 

**TLDR: You can find the publication [here](https://www.mdpi.com/2079-4991/13/21/2893).**

## Step 0: Data Collection & Preparation
### Collection
Back in 2021, the Freed-Hardeman Computational Chemistry research group (in collab with Dr. Wang at the University of Memphis) started investigating layered nanoparticles. We were primarily interested in a Au core, a layer of SiO2, and another layer of Au. I was focused on completing my honors thesis on our previous work on heterodimers, so I wasn't terribly involved in the start of the project. 

The main sprint of the group included four students: Lauren Feilding, Christian Sachs, Katie Stickels, Paiton Williams. They focused on different core radii and a ratio between SiO2 and Au shell to make a total radius of 25nm. In hindsight, the investigation of two changing variables (SiO2 and Au shell) is a bit complicated, but we hoped to find an optimal ratio between Au core, SiO2, and Au shell for a fixed overall radius.

When I was able to join them on this project, I was told it would be best to focus on the individual effect of each component, so I ran four jobs on a changing SiO2 and four jobs on a changing Au shell. 

Graduation came and went, and I continued my research over the summer with Dr. Wang at the University of Memphis. Up until September, I had spent time working on a web-deployed analytical solution to the optical response of a multilayered NP using Mie Theory. I gained a lot of coding and web development skills through this, but at the end, we found a similar project by a Russian research group, so motivation for the work fizzled.

### Preparation
I had started classes for my certificate in data science at this point, and I was responsible for analysis of the entire group's data. The other members had graduated with me or had moved to another project. I decided to use by database systems skills I was learning to create a database of all the data we had collected. I have a [previous blog post](https://kombateldridge.github.io/2022/09/09/Au-SiO2-Au-Multilayer-Project-Update-1.html) on this database development.

I extensivly documented the process of entering data into the database so that the insertion of more data would be easy. Below is a graphic I devloped to describe the flow of the data.

![](/files/databaseOutline.png)

Once the python scripts were generalized for use on any job, the ability to run and insert new jobs into the database was easy. 

## Step 1: Literature Review
Considering the order of these events, I recommend doing a priliminary literature review before starting the project, but I was not part of that process, so I cannot comment on it here.

I used Google Scholar to find papers on Au@SiO2@Au NPs. Particularly, I was interesting in learning how the community presents its data. I had a lot of data, and I had the capability to present more than most papers because of the computational nature of the project. However, some datapoints are not useful to the community, so I compiled some notes from each paper on their findings and the presentation of their data. 

Later on in the writing process, I was encouraged by Dr. Wang to read into the experimental aspect of this NP system. I learned that our paper can be useful to the computational community, but its aim should be toward the experimentalist. At this point, I had learned that there is a pocket of chemists who are refering to these multilayered NPs as Nanomatryoshkas (NM) (as in the russian word for nesting doll). Updating my search terms in my literature review introduced me to more that double the amount of resources I had been looking at. If it had not been for this discovery, the paper would not have been as supported; note to self, make sure to always look into different names of your project incase it goes by another name.

## Step 2: Preliminary Data Analysis
Once I had an idea of how the community likes the data to be presented, I began pulling spectra from my database-connected Jupyter Notebook. I moved these to a powerpoint where I jotted notes of the trends I noticed in the spectra. It was a pretty big powerpoint, but it was important to start the project by looking at all the data we had collected. Without this, I would not have had a vision for the story this manuscript needed to tell.

I sent this ppt to my collegues and asked for their notes on the ideas I mentioned. After a couple back and forths, I had the confidence to start the manuscript.

## Step 3: Manuscript Drafting
From what I understand, it is typical to draft a paper while including collaboration in the writing process. However, since I had been the only one to seriously look into the paper, I planned on getting an entire working draft to my collegues first before having them write their own expertices in. 

Dr. Wang recommended I first look into the manuscript formatting for ACS Nano (high hoped for publication), so when I started drafting, I had an idea for the typical order I should write my sections in.

I had produced a short first draft and shared it with Dr. Wang. By the third working of the draft, I had learned about a mathematical theory to describe the optical response of a NM known as Plasmon Hybridization Theory. There were already papers out on this topic, but none of them explicitly provided the equations for description. Most every paper was done by one group lead by Dr. Prodan and Dr. Nordlander of Rice University in Texas. I spent days trying to derive the equations for my specific system, but my lacking physics background failed me and I had to move on.

There were moments during the drafting phase that I wanted to pass off the project to someone else. I had at times been so far separated from what the original paper was supposed to be about that I had to leave a vein of papers I had been following for weeks. 

Now, I have finished what I hope is the last draft, and I hope we will send it in for review. I know that the process of submission review takes a long time and this is likely not the last time I make a draft of the paper. However, now that the 6th draft is complete, I have optimism. Its in the hands of my collegues and I am able to focus on other tasks like web development and my blog.

## Step 4: Manuscript Submission
We submitted our manuscript on **April 7th, 2023** to the Journal of Physical Chemistry.

On **May 9th, 2023**, we recieved our notes back on the manuscript with a rejection of publication. Our notes were not as substantial as I would have thought, but we were recommended to submit to a journal with *less* of an emphasis on impact. The reviewers did not see a great impact to the scientific community in our paper.

After reworking the paper to emphasize the impact of our paper to the scientific body of knowledge, as well as addressing the issues the reviewers noted, we submitted our manuscript for its second round of review on **June 4th, 2023**. We had recently recieved a call for papers specific to nanoparticles from the Royal Society of Chemistry Nanoscale, so we submitted there.

The call for papers had a due date of July 31st, so it seems that our paper wasn't assigned a peer reviewer until the first of August. You are able to see the progress of the paper on their website:

* June 4th - submitted and given to an editor
* August 1st - assigned a peer reviewer (or multiple)
* August 19th - returned to the editor
* August 23rd - assigned another peer reviewer (or multiple)
* September 26th - paper rejected

Finally, after waiting the whole summer, we recieved some notes on the paper (which is good news dispite the rejection). We then made some edits, and submitted it to MDPI Nanomaterials. After a month of review and edits, we were **accepted**! You can find my paper here: [https://www.mdpi.com/2079-4991/13/21/2893](https://www.mdpi.com/2079-4991/13/21/2893)
