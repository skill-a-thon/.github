<!-- Output copied to clipboard! -->

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 12

Conversion time: 2.185 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Mon Feb 27 2023 02:37:02 GMT-0800 (PST)
* Source doc: Product Overview
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!


WARNING:
You have 5 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 12.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>
<a href="#gdcalert9">alert9</a>
<a href="#gdcalert10">alert10</a>
<a href="#gdcalert11">alert11</a>
<a href="#gdcalert12">alert12</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# Abstract of Project

The Project leverages mentoring platform, using the power of advanced AI technologies to provide a seamless and effective mentoring experience. With features like Chat GPT 3, Assembly AI, Discord integration, and DigiLocker, our platform offers a comprehensive set of tools to help mentors to achieve their goals.

Using Chat GPT 3, our platform allows mentors to easily create sessions and generate session details with the help of AI. 

GPT-3 APIs can generate the session description and title, which will be passed to the needed BAPS.

Assembly AI is then used to generate transcripts and GPT-3 to generate session summaries, providing a complete record of each session. The session summary, transcript, discord invite link, and the recorded video URL are passed to BAPs via status and on_status endpoints, these will be added to fulfilments as tags.

For completed sessions, we create a dedicated Discord channel that includes the transcript and summary of the session. This allows mentors and mentees to continue the conversation and discuss further, building on the insights and knowledge gained from the session.

In addition, our platform integrates with DigiLocker, a secure digital document storage platform, to enable verifiable credentials for mentors. We’ll be mocking the Digilocker ‘/oauth2/2/xml/eaadhaar‘ endpoint to the best of our knowledge. These verified credentials can be passed in the creds field of the agent. We are making the platform more trustworthy.

Overall, our platform is a comprehensive mentoring solution that combines the latest AI technologies with innovative features to create a seamless and effective mentoring experience. 


# Features 



1. Chat GPT 3 integration for user-friendly session creation
2. GPT-3 API for auto-generation of  session descriptions
3. Assembly AI for generating session transcripts
4. GPT-3 for generating session summaries using transcripts
5. Auto-created a dedicated Discord channel for completed sessions discussions
6. DigiLocker integration for verifiable credentials
7. Passing verified credentials in the creds field of the agent


# User Workflows



1. A mentor registers to the app.

     \


<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")


<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.jpg "image_tooltip")



    

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.jpg "image_tooltip")


2. A mentor logs in to the platform and Edits his profile. \
 \


<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.jpg "image_tooltip")


<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.jpg "image_tooltip")

3. A mentor creates a new mentoring session using Chat GPT 3 AI.

    The mentor inputs the session title, and start and end date, using these data GPT-3 generates a session description.


    

<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.jpg "image_tooltip")


<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.jpg "image_tooltip")


4. Once the Session is completed, Assembly AI generates a transcript of the session using the recorded session mp4 file, and GPT-3 generates a summary using the transcript.

    

<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image8.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image8.jpg "image_tooltip")


5. The session summary along with the discord invite link, transcript, and recording URL is passed on to the BAP in the status /on_status call. The data will be added in the fulfillments as tags
6. After the session is completed, a dedicated Discord channel is created, and the transcript and summary are posted.

    

<p id="gdcalert9" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image9.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert10">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image9.png "image_tooltip")


7. The mentor and mentee can continue the conversation and discuss further in the dedicated Discord channel, building on the insights and knowledge gained from the session.
8. The mentor can also receive verifiable credentials through DigiLocker integration, increasing their trustworthiness as a mentor. The verified credentials can be passed in the creds field of the agent, further increasing the mentor's credibility on the platform.



<p id="gdcalert10" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image10.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert11">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image10.jpg "image_tooltip")


<p id="gdcalert11" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image11.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert12">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image11.jpg "image_tooltip")



# Tech stack


    Mobile: Angular + Ionic


    Backend: Node + Express


    Databases: Mongo(Storage) 


    External: DigiLocker, Assembly AI, ChatGpt and Discord  


    Data Streaming: Kafka 


# Architecture



<p id="gdcalert12" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image12.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert13">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image12.jpg "image_tooltip")



# Open-source and Digital Public Goods leveraged/used



1. [Mentoring Elevate Platform ](https://github.com/ELEVATE-Project)
2. [BigBlueButton](https://biggerbluebutton.com/)

	
