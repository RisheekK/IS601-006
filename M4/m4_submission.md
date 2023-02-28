<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 2/28/2023 1:24:25 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sum-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221745019-0e96eec7-d969-4337-8867-c8cf51649a6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221745988-91501b86-09a1-47be-b517-ad642e1ca048.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add function Output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221755329-45bea902-bd72-42d6-8c04-6b87d62401e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221755598-59766695-c9ec-4c37-b572-8bdda56c8915.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sub function output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221756114-a929f8f1-6113-43b0-bd6a-8d91ad106f84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221756355-f5657155-28bc-4aa7-a73d-fa23fc9e4014.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiplication function output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221756625-c3b0443f-d651-47bb-bfc4-7da33a1b9be0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221757029-12b4fdb7-f48b-4257-84f4-c0de94e65311.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division function Output<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221759994-7c30e066-8dcc-4d41-8c88-7a63c3df5267.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> number-add-number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221760275-b7f69cff-3bdb-4276-9103-804c6e197d03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> number-add-number test case passes in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221760490-e4031e13-89fe-4f19-8f93-18ce436907ac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-add-number code snippet<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221760633-6bb5c82a-d8c0-48da-a4d1-1544bf156ffc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-add-number Test Case passed in Pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221761753-b5ed80d3-a3a8-42ca-8bf5-3c74440e7001.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number sub number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221762024-8737dfac-8d43-465b-b619-8e8d62727951.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number sub number test case passed in pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221762877-23f8cd9b-9c3c-4433-8778-61a3e1c61afb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-sub-number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221762964-4e9f6d04-ea47-4b29-9397-4c7ab1d4c87a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-sub-number passes pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221763535-e5d7a0cd-96e5-4409-a34b-4d90f87d1195.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221763727-1ba44b9b-9578-4b89-95a5-e6d364421e9f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-mult-number passes pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221764241-9652ae19-e463-41fa-9869-49ddef4a812d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-multi-number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221764514-833f1aec-18f7-405a-a40d-7d4ba742802f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-multi-number pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221767277-fef53305-647b-4134-8247-e26aea56d38d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221765871-87f54d4c-258e-4118-ace3-ee5e7ef78c9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>number-div-number pytest<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221767409-4e78772d-80c7-4eee-8e19-bb4891b78567.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/221767762-73e00786-ed6e-44cd-9c1e-a424042072e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ans-div-number Pytest<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>learnt how pytest works.<div>- further understood how data types work and their<br>importance.</div><div>- improved string handling.</div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>we used pytest to write functional test cases for our code.<div>it helped to<br>test multiple test case all at once saving considerable time.</div><div>learnt how to script<br>test cases for different functions.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/10">https://github.com/RisheekK/IS601-006/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/m4-simple-calc/grade/rr284" target="_blank">Grading</a></td></tr></table>