<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 5/2/2023 7:07:32 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235575778-06c6c3c5-ce5a-44d0-993f-e8407098d835.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235575977-4ecf1231-93a5-40e8-b978-75550c722e4d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235576154-eae9f228-367d-498a-99a6-b31431d65984.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>passwords do not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235576830-ad95b4d2-bf97-4432-aecd-c579bbcada49.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful registration<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235577220-31dcd1a5-875d-4f53-afe2-a63456017cbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235577690-a1dab0c3-37ec-4e99-b998-006bd5127644.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235577957-d81c4cc9-80b2-4af4-a018-51e9a591042c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235578851-50b0e142-aa88-4a6f-bb97-6aa0528046b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1- both test1 and test2 were used.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>WTforms are utilized for obtaining user input via web forms, and validation occurs<br>upon form submission.<div>WTforms come with pre-built validators that display error messages to users<br>on the frontend, and additional validation is performed on the backend to verify<br>unique usernames and emails.&nbsp;</div><div>The database has restrictions in place on username and email<br>to prevent invalid data from being stored.&nbsp;</div><div>Passwords undergo validation and are encrypted using<br>bcrypt before being stored in the database, with the salt and hash stored<br>as well.</div><div>User information is stored in the database with constraints implemented to ensure<br>accuracy, and queries are executed using a database helper with responses sent to<br>the frontend.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235587993-cd817c97-5b85-4c7e-b7e1-536e85ff9607.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235588115-eafd742c-4eb6-44ae-9762-0ec905a0a6e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation based on non-existing user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235588327-ede4f8b8-2679-43bf-8d74-01c6a861b348.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>WTforms are utilized for obtaining user input via web forms, and validation occurs<br>upon form submission.<div>WTforms come with pre-built validators that display error messages to users<br>on the frontend, and additional validation is performed on the backend to verify<br>unique usernames and emails.&nbsp;</div><div>The database has restrictions in place on username and email<br>to prevent invalid data from being stored.&nbsp;</div><div>Passwords undergo validation and are encrypted using<br>bcrypt before being stored in the database, with the salt and hash stored<br>as well.</div><div>User information is stored in the database with constraints implemented to ensure<br>accuracy, and queries are executed using a database helper with responses sent to<br>the frontend.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235588496-7de193d5-203a-4193-aec4-3c48f65077d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logout successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235594565-7030b4d9-e7e2-4b44-801b-0a299e86db04.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Flask&#39;s built-in methods are used to maintain sessions. Flask uses flask_login to keep<br>the current session alive. Current_user stores information about the currently logged-in user. This<br>value is used in cross-page sessions to guarantee that the user remains logged<br>in across pages. We retrieve the current user_id and user_roles and keep them<br>consistent across pages.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235595030-cf05cbe1-a23b-4940-afc6-7ad5edd00115.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized user cannot access the Landing page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235595663-32e9513e-db6a-4f22-a05c-409f10c14fd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User without proper role cannot access role restricted features.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235605996-fb08a671-8c9e-4994-bb29-abecc5b8c82f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>roles table with admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235607922-a87176e6-2a58-4edf-bb71-ff4212d6b940.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user roles- Admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235608364-82d39714-d992-4988-9133-6fd03573386b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users in user table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For login-protected pages we use the inbuilt decorator called login_required. This checks if<br>a user is authenticated.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For role-protected pages, we retrieve the roles associated with the user&#39;s session and<br>compare them to the desired roles. To check this, we use flask&#39;s built-in<br>permission requirement decorator.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235638706-0d19bff2-ccee-43eb-818a-5f5a0f2decf0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Nav bar changed.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235638986-aee3c686-298a-4ceb-af0b-e713fc3781ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>changed table style to include borders.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235639150-a5c8560a-9482-4639-b98c-94ad83229213.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed form style<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>Changed the background color of navbar and form.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235595030-cf05cbe1-a23b-4940-afc6-7ad5edd00115.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235595663-32e9513e-db6a-4f22-a05c-409f10c14fd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>permission denied page.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235640929-3e833fb5-44c3-4b96-9d43-949128780e01.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>&quot;Page not found&quot; - page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>we are overriding the default page for error status codes such as 401,<br>403 and 404 by adding respective templates for each.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235641678-043c8d93-d2c4-4d21-b0e8-3cfcacba6050.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User name and email are prefilled.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>When a call to the endpoint is made, the formdata is fetched at<br>the start. If the form values exist, they are retrieved and presented.</div><div>If no<br>values are available, empty values are presented.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235644305-d740436a-3117-4ae1-8cb0-1b00294e2add.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>profile Username validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235644621-bba2958f-905a-4fc2-9d46-2ab6f28e4f77.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>profile email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235644823-47fc72d3-185b-4ab6-9aa8-491bab065629.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235645311-940360c4-642f-45b5-9130-ffaa4307a950.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235645731-3864f1dd-1903-4dfc-a4d9-21255a57da07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email already in use message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235646351-a52af513-5ec4-46e0-a2fe-6059ac3ae043.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username already in use message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235646748-83e3348f-486d-469a-9f31-a663509cff8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin- user ID: 5, table before updating the profile.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235647261-fe639559-1dc6-4e2e-b9be-0bbd7eadf33d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New value for username, Profile updated.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/235647770-cb4d9e86-c8dc-4423-a020-c35509eeb97a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Table after updating profile. User ID : 5 is changed from admin to<br>commander.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/30">https://github.com/RisheekK/IS601-006/pull/30</a> </td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/32">https://github.com/RisheekK/IS601-006/pull/32</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>For email and username, update calls to the table are made with the<br>user_id as the key. The update query will fail if the username or<br>email already exists in the table due to table limitations.&nbsp;<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Had Trouble with changing styles in CSS.<div>faced difficulty in navigating different between different<br>templates to make changes.</div><div>learned how to change table styles-&nbsp;<a href="https://getbootstrap.com/docs/4.0/content/tables/">https://getbootstrap.com/docs/4.0/content/tables/</a></div><div>learned how to style forms<br>-&nbsp;<a href="https://blog.logrocket.com/how-to-style-forms-with-css-a-beginners-guide/">https://blog.logrocket.com/how-to-style-forms-with-css-a-beginners-guide/</a></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/login/">https://is601-rr284-project-prod.herokuapp.com/login/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone1-deliverable/grade/rr284" target="_blank">Grading</a></td></tr></table>