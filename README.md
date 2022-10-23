# Audur

## DevPost
https://devpost.com/software/audur

## nspiration
In creating the idea for Audur, we were heavily inspired by the popular image-sharing service called Imgur which allows users to share images without the need of creating an account or logging in beforehand. Although services like Google Drive and Soundcloud are popular means of sharing files, they come with the downside of having to login - thereby tying the files to the user, which can potentially leave the user’s information exposed. So, we wanted to create an alternative way to share audio files that is both quick and more secure.

## What it does
Users can upload their audio files on the website and give them a title and a description. The app is hosted on an EC2 instance on AWS, so the file is stored in the cloud and given a unique identifier. The user can then view the uploaded audio file along with a summary of the upload. A shareable tinyurl link is generated which can be used to share the audio file with others.

## How we built it
We first designed a basic prototype of the web app using Figma. Then, we charted out the implementable and feasible features. From here, we focused our energy on building the backend to enable users to upload audio files using form actions. This enabled us to ensure that we could generate a unique link for each upload. After verifying the functionality of the backend, we built the front-end and styled the pages.

## Challenges we ran into
We were initially going to use a Google Cloud instance to host the application. However, this proved to be troublesome, as the initial setup and the restrctions on the UI were difficult to mitigate. In addition, the rules for setting up firewalls were unclear, and did not provide us with many choices. We also considered using Firebase's storage to store the files and generate the URL, but then quickly realized that AWS best suited the application's needs. We were able to navigate through the console with ease and fearlessly experiment with powerful virtual machines due to the large budget ($400.00). Despite these challenges, we quickly learned when something was not feasible to implement and were able to mine efficient alternatives.

## Accomplishments that we're proud of
We're proud of how we built a fully working product from an idea that we instantaneously brainstormed, halfway through the event. We spent plenty of time coordinating, to make sure that everyone in the group had an equal share of work and that they were comfortable with carrying out assigned tasks. While this was the debut appearance for most of us at HackGT, we are extremely happy with the amount of learning and connections formed over 36 hours.

## What we learned
We learned how to deploy web applications on to AWS and Google Cloud. The team gained significant knowledge about networking and how ports were to be exposed while creating services for the public - in addition to uploading files on Python Flask. Lastly, we learned how to communicate effectively during stressful times.

## What's next for Audur
One of the main limitations of Audur that we've quickly noticed was that the frontend UI could be a bit more intuitive. Audur's design could make better use of responsive design, so that the app can be aesthetically appealing on screens of different devices. We would like to implement a feed section, where users can check the trending audio clips, and view similar content from our recommendations.
