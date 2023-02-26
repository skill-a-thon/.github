# Team Innovators

This is a team of different companies coming together to build a solution.

## Required details

| Team Name | Team members | Challenge Number | Product version | Product document | Product demo | User guide | Source code | Developer guide |
|--|--|--|--|--|--|--|--|--|
| Innovator | Giriraj D (Affinidi), Prashant M (Dhiway), Vikas J (BetterPlace), Denzil Lewis (Hacker Earth), Neeraj Sharma (SunStone) | 3 | 0.0.1 | [Product document](#product-document) | Product demo | [User guide](#user-guide) | [Source code](#source-code) | [Developer guide](#developer-guide) |


Other than above, considering this was an effort which needed multiple companies, and teams engaged, we had to include many more members in it.

* Sankarshan (Dhiway)
* Chaitanya S (Affinidi)
* Hitesth S (Affindi)
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
 - Upon clicking the 'Submit' button, the list of VCs along with PDF would be submitted to the Job portal.

### User Guide


The project involves multiple pieces / projects working together.


1. Issuers
  Issuer tools are critical for users to collect the documents in Verifiable Credential format. Having more than 1 issuer in the mix would make the ecosystem truely interoperable.
  - VCs can be created from either of
     - Dhiway's #MARK Studio (SaaS product),
     - with Affinidi's Developer tool kits.
     - by deploying the CORD sdk with an application,

2. Wallet for storing the VC.
  This is used as a storage /repository for User's VCs. Each wallet can have different ways of interacting and collecting VCs in them from the Issuers. But they should be having an option to export the VC of each credential when asked.
  -> Affinidi wallet can store VC issued from either of Dhiway Studio or Affinidi Toolkits.
  -> Dhiway is building the initial wallet, and hence, for now assumed VC can be available from system when the Credential is created and issued in the system. (directly using an URI)

3. Digital Resume Tool

This tool is the output of the current hackathon, which would be the one which will interact with BAP/BPP (DSEP APIs), and upon agreeing to submit for job application, allow one to fetch specific type of VCs from wallet and fill into the Resume. Allow someone to add a VC just before submitting.

This tool would need integration with Verification tools to make sure the VCs fetched from wallet are valid, and the VCs to be submitted are all being verified as per VC standards.
  
### Developer guide

#### Build and run

1. Clone the digital-resume repo

git clone https://github.com/dhiway/digital-resume

2. npm install

3. npm run start


### Source code

* https://github.com/dhiway/digital-resume
* https://github.com/dhiway/cord.js (SDK for Issuance and Verification of VCs).


### Status & Roadmap

This is still very early version of the project, and we are just showcasing the possibility here. Soon, with more features would be added as we identify the while developing.

Status: Demo works with lot of 'place-holder' code, and focus on showcasing the VC usage in DSEP ecosystem. Not near completion as needs a proper login and backend code to manage per user data management.

#### TODO

* Login, and user specific resume builder
* More granular control on VC addition
* Integrate with BAP/ BPP.
* More UI changes to resume submission flow
