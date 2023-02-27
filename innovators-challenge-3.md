# Team Innovators

This is a team of different companies coming together to build a solution.

## Required details

| Team Name | Team members | Challenge Number | Product version | Product document | Product demo | User guide | Source code | Developer guide |
|--|--|--|--|--|--|--|--|--|
| Innovator | Giriraj Daga (Affinidi), Prashant M (Dhiway), Vikas J (BetterPlace), Denzil Lewis (Hacker Earth), Neeraj Sharma (SunStone) | 3 | 0.0.1 | [Product document](#product-document) | [Product demo](https://drive.google.com/file/d/1AM4nn7hBxRq-B9_B7QoWYirDS2g6zZb3/view?usp=sharing) | [User guide](#user-guide) | [Source code](#source-code) | [Developer guide](#developer-guide) |


Other than above, considering this was an effort which needed multiple companies, and teams engaged, we had to include many more members in it.

* Sankarshan (Dhiway)
* Chaitanya S (Affinidi)
* Hitesth Songra (Affindi)
* Ujjwal S (Dhiway)
* Sujith B (Dhiway)
* Amar T (Dhiway)

### Product Document

We picked Challenge 3, to build a 'digital resume' with Verifiable Credentials as a focus. In this flow expected behavior is something like below:

 - User will 'search' for a Job through DSEP (/search).
 - User will be shown the listing of the Jobs as per the search criteria
 - Upon clicking on the relavant job option to 'Apply' for, user will be taken to the page with details of his credentials.
 - A Digital resume would be shown to user before applying for the job, where user can see his credentials listed with categories of 'Proof of Work', 'Proof of Skill' and 'Proof of Education'.
 - He can add a VC JSON to this resume by clicking on 'Edit' in particular skill section
 - Upon clicking the 'Submit' button, the list of VCs along with PDF would be submitted to the Job portal. (/on_submit)

NOTE: for quick sampling of adding a Skill, check the output https://api.demo.dhiway.com/m/46826ff9-cb02-46b0-bc01-e1ee2d71dcf2.vc and paste it in the popup text box which appears, and 'Add'. This will come up in the resume now.

To check if the VC is valid, you can paste the same VC in https://verify-demo.dhiway.com and see that its all valid.


### User Guide

The project involves multiple pieces / projects working together.


1. Issuers
  Issuer tools are critical for users to collect the documents in Verifiable Credential format. Having more than 1 issuer in the mix would make the ecosystem truely interoperable.
  - VCs can be created from either of
     - Dhiway's #MARK Studio (SaaS product),
     - with Affinidi's Developer tool kits.
     - by deploying the CORD sdk with an application,

2. Credentials Wallet for storing the VC.
  This is used as a storage /repository for User's VCs. Each wallet can have different ways of interacting and collecting VCs in them from the Issuers. But they should be having an option to export the VC of each credential when asked.
  -> Affinidi wallet can store VC issued from either of Dhiway Studio or Affinidi Toolkits.
  -> Dhiway is building the initial wallet, and hence, for now assumed VC can be available from system when the Credential is created and issued in the system. (directly using an URI)
  -> User can view or share the stored VC as a qr code or URL from the wallet to use across systems 

3. Digital Resume Tool

This tool is the output of the current hackathon, which would be the one which will interact with BAP/BPP (DSEP APIs), and upon agreeing to submit for job application, allow one to fetch specific type of VCs from wallet and fill into the Resume. Allow someone to add a VC just before submitting.

This tool would need integration with Verification tools to make sure the VCs fetched from wallet are valid, and the VCs to be submitted are all being verified as per VC standards.


#### Internals of Wallet and Digital Resume tool

We are integrating with 'Affinidi Wallet' login (check the API's [Postman collection](https://www.postman.com/affinididevelopers/workspace/affinidi-developers/overview)). Hence, a user's details in resume would be populated fromt the wallet, and the particular Digital resume in question would be dynamically built based on the contents of the wallet.


### Developer guide

#### Build and run

1a. Clone the digital-resume repo

git clone https://github.com/dhiway/digital-resume

1b. Create an API Key using https://apikey.affinidi.com/ and update the environment variable 

2. npm install

3. npm run start

4. Open one of the browser tabs and type http://localhost:3000

5. The home page has 'Search' option to get Job listing (will be integrated with DSEP/BAP/BPP)

6. By Clicking on the listing, we would reach the resume, which can be submitted as is, or can be added with a Skill.

7. By clicking 'Edit', one can add a signed VC there (check signed VC from [here](https://api.demo.dhiway.com/m/46826ff9-cb02-46b0-bc01-e1ee2d71dcf2.vc)), and then we can see that particular skill mentioned in the VC is shown there.

8. Now, 'submit' should send the request to DSEP/BAP/BPP based on the context from the job listing.



----

The Same VC which would get added in the digital resume can be verified by copy-pasting (or drag-dropping in Verification Tool - https://verify-demo.dhiway.com)


### Source code

* https://github.com/dhiway/digital-resume
* https://github.com/dhiway/cord.js (SDK for Issuance and Verification of VCs).
* https://github.com/affinidi/affinidi-core-sdk 

Note: for higher productivity, leveraged the hosted version of Affinidi Open source SDK
https://build.affinidi.com/docs/api
Created API Key using https://apikey.affinidi.com/

### Status & Roadmap

This is still very early version of the project, and we are just showcasing the possibility here. Soon, with more features would be added as we identify the while developing.

Status: Demo works with lot of 'place-holder' code, and focus on showcasing the VC usage in DSEP ecosystem. Not near completion as needs a proper login and backend code to manage per user data management.

#### TODO

* Login, and user specific resume builder
  - Plan here is to integrate with the 'wallet', so the user's data from wallet can be used to build the resume.
* More granular control on VC addition
  - Currently only proof of skills can be added, extend it to proof of work and proof of education.
* Integrate with BAP/ BPP.
  - Must have.
* More UI changes to resume submission flow
  - Can have more changes in UI based on feedback.


