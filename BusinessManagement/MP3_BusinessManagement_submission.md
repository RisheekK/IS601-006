<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 4/19/2023 6:53:28 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/232688084-854c7f5f-cf5d-4a1c-8108-4443b844ffa3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-ucid of the student - nav.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233000175-f7d5b72c-890a-49b2-adfc-5b937984c2a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1)URL heroku dev 2) &quot;Brought to you by..&quot; 3)  Relevant url_for references<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233001712-80b8000e-7ba4-48cb-ab52-c3448e552039.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233002553-ecf5f99a-bfc8-4379-9dd4-4a3a9094cedf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot of /import route (code) - (1)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233002892-998ec5e2-a2b5-4c35-b346-c0e7860f8a5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub-Task 1: Add screenshot of /import route (code) - (2), Todo&#39;s completed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233003587-dade7f1b-5a51-43aa-ad94-e42145f2613b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>imported successful- flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233004049-d6b3f93b-5ac2-4c75-987c-5e9eea18431b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when the file is not a .csv file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233004218-7460afcf-af6f-4cd6-8858-6f0f3a3d0f1a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when the form was submitted without a file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233022284-cef76077-c870-4a63-bdde-ac640b25f278.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some employee data was uploaded, UCID visible below<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233022054-914d52ff-4b16-4d77-8bc5-57b4ed63c0a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing some company data was uploaded, UCID visible below<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233016463-7381e3a9-0b92-4337-a875-d6b487d5ef0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add employee route. All todo&#39;s are completed. Please note that flash messages were<br>because validations are done in the html side using wtforms.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233007785-a3658d96-5275-415f-80e4-1bea80d6b1f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233007944-49442a6a-60ee-462e-b3bc-c9b56ecc9f30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233008358-a6de01b4-7cd8-464f-b65c-4c5180ee8291.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233008601-d891d8b4-bd1f-409e-b13e-845db58c9a2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233008936-2c99a1f3-1854-43b6-b005-9e27b583d87a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233015958-80a6db60-7f0d-4848-8bc0-acea04dd0a53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid employee data shown previously. Employee name = &#39;Eren Iyengar&#39;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233011479-e2b00b87-14bc-4e43-958e-a1961687628b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee /search Route. all Todos are addressed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233023261-d96e9892-ba13-4a5c-9212-ca5bb8fd260e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233023607-558e6326-d366-477e-bdc2-6f09c8295d03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233023957-38858f1b-3116-4c10-a1c7-c81ad7368ced.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233024384-8d4c6a42-775f-42ee-8ce1-3b4948c3339e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233024848-ce48864b-688a-4666-86bb-a684f09d86af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Asc filter on First name is applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233025191-b265d003-1007-4f17-a97b-5e3ce35a89a8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Dsc filter applied on Last Name.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233026739-b9a3a394-d272-4c1a-9a07-5fe811b7d7b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit employee route. All todo&#39;s are completed. Please note that flash messages were<br>because validations are done in the html side using wtforms.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233029045-c4f599dd-e5cf-4d95-b748-843cbcde9ff6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee details before the Edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233031132-79f9a745-6856-444a-a0fd-9610d6996080.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee details after the edit. Last Name was changed from Munis to Ackerman.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233030805-f5d5f2ba-3e86-4613-869f-2235fd729bf7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row before editing.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233031802-ec312b19-1213-4b4b-a9d2-ee1108f249d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row after the edit.  Last Name was changed from Munis to<br>Ackerman.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233032415-f7f79a97-f389-4089-af31-bc0f2f392b26.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add route of company. Please note that flash messages were because validations are<br>done in the html side using wtforms.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233034783-9ed5d65d-a6e3-40ec-b7f0-ee4c2000a0b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid Data Prior to submission. please note that wtform error is shown instead<br>of a flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233035023-f7a55812-4b16-44a2-b589-d6fd5556f496.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company success message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233037821-f229cb04-01c6-40c9-96b0-7bfc5777778a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name error message. please note that wtform error is shown instead of a<br>flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233038036-6807694a-c534-454b-9dd5-62ec825a03c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company address error message. please note that wtform error is shown instead of<br>a flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233038222-f56277e5-9967-4419-a639-f268bf579b12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company city error message. please note that wtform error is shown instead of<br>a flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233038596-0fce79db-2ba1-4be2-ba73-a6b566c2c9dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>State error message. please note that wtform error is shown instead of a<br>flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233038749-256176f4-d33d-4ea2-995a-3a64e5486478.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country error message. please note that wtform error is shown instead of a<br>flash message.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233039277-00175977-13af-4d62-860f-9c3f0fdacfcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Zip error message. please note that wtform error is shown instead of a<br>flash message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233040090-9111ed0b-4aed-4db1-b8ff-d7ec3c5676a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data just added.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233041636-d6af061a-ed03-4c42-8d1a-4e6063b95903.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search route of company. All Todos are completed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233042336-8d8d0831-cbb1-462d-8c06-8af617e26e9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search with name filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233042763-ca7e7b2b-3778-4d37-a339-faff3750f2b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search with country filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233043516-efbeffc5-044d-4877-abb7-bd58415e1883.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search with state filter applied.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233043902-5010da56-518e-43c6-838a-7c54c0abe608.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country Field is returned in Asc order.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233044129-b9f0d24f-6778-4f78-a80b-14e4a0875ef1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name field is returned in Dsc order.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233044479-0b636432-a085-481a-ba6b-06dfb7e638c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit route of company.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233045803-fcf5d0ec-41c8-4945-bad0-1a16dd66f92a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233046247-d92929fb-a434-40ea-b7ff-0b07a0d3c05f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data after edit. Note that the city, State and the zip code<br>have been changed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233045600-4ead40b6-1be3-43d4-9e06-6d7a79d33805.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row of company before edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233046708-a2e07fcb-c5f6-45df-ab6b-36a1500e82d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB row of the company after edit. Note that the city, State and<br>the zip code have been changed.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233047824-b660b48a-dad5-4d11-990b-9e880f55f023.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete route of employee. All Todos are completed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233048810-8381e553-d16e-4bd5-b795-60abf0b9d49d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting Employee.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233049023-5fdea932-5350-4a72-8871-0e337c94036f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Deleting employee.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233049384-e0616e75-3598-4300-a349-e39d96053c15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete route of company. All Todos are completed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233049842-05d6bcdf-fdc2-4882-a5e9-24996c9dc0e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting Company.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233050274-f6bb5f3f-e00a-49c1-a340-d1e00eda7633.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting company.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233050704-2e56503c-c010-409b-a4ff-8429f5fc650d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pytest in VScode.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/233051699-304737d7-10cc-4668-a020-bb762ce7f017.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pytest in Terminal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>Had difficulty with writing SQL queries, Passing args in select statement was<br>initially confusing.<div>- Learned a lot in Html and wtforms.</div><div>- Understood Flask and working<br>with endpoints even better.</div><div>- Gained practical understanding of HTML and bootstrap elements.</div><br></li><br></ul><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/rr284" target="_blank">Grading</a></td></tr></table>