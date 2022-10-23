https://devpost.com/software/audur

# Inspiration
In creating the idea for Audur, we were heavily inspired by the popular image sharing service called Imgur which allows users to share images without the need of creating an account or logging in beforehand. Although services like Google Drive and Soundcloud are popular means of sharing files, they come with the downside of having to login and the files being tied to that user which can potentially leave the user’s information exposed. So we wanted to create an alternative way to share audio files that is both quick and more secure.

# What it does
Users can upload their audio files on the website and give it a title and a description. The song is hosted on an EC2 instance on AWS so the file is stored in the cloud and given a unique identifier. The user can then view the song they uploaded and a summary of the upload. A shareable tinyurl link is generated which can be used to share the audio file with others.

# How we built it
We first designed a basic prototype of the the web app using Figma. We then created a plan of which features would be feasible or not to implement. From this step, we prioritized on building the backend first to figure out how to upload the song from a form action and making sure that we can generate a unique link for each upload. We then proceeded to build the frontend and styling on top of this design once we verified the backend works.

# Challenges we ran into
We were initially going to use a Google Cloud instance to store the audio files. However, this proved to be troublesome since no one on our team had much experience with Google Cloud. We also considered using Firebase's storage to store the files and generate the URL but then quickly realized that AWS suites the app's needs better since we can directly deploy the app on the EC2 instance. Despite these challenges, we quickly learned when something was not feasible to implement and moved on.

# Accomplishments that we're proud of
We're proud of how we were able to build a fully working product from an idea that we just happened to brainstorm right on the spot. We spent a lot of time coordinating to make sure that everyone in the group had equal share of work and that they were comfortable with what they were developing. Also for many of us, this was our first hackathon at HackGT and so we're proud to see how much we've grown and the new connections we've formed over the course of 36 hours.

# What we learned
We learned a lot about deployment on cloud technologies like AWS and Google Cloud. Also, we learned how to communicate effectively with one another whenever we were running into pitfalls.

What's next for Audur
One of the main limitations of Audur that we've quickly noticed was that the frontend UI can be a bit more intuitive. Audur's design could make better use of responsivie design so that the app looks good on difference screen sizes and on mobile devices. It would also be nice it there was a feed section similar to what imgur has so that users can browse and find trending songs.
