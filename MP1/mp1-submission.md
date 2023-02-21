<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 2/20/2023 11:33:30 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220221745-233cb3f1-5b5e-4247-be07-b6e730934e4c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>used Try and Except to handle the format error of &#39;due&#39;. If the<br>format does not match then the Print statement in the except will run.<br>i have used for loop to check if a field is missing a<br>value and store in fields_not_available then if the fields_not_available is empty success message<br>is shown if its not &quot;not added&quot; message is shown along with the<br>missing fields<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220221611-3db3d693-8087-443b-9193-39ab2d908f8f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of successful ouput<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220222333-b92e0b25-e404-47cf-a3fc-44bc0f97749d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure Due date does not match<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220222484-97ba5c12-4406-43b5-b97d-5f44bf98e39f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure if name and description are not provided<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p>used Try and Except to handle the format error of &#39;due&#39;. If the<br>format does not match then the Print statement in the except will run.&nbsp;<div>i<br>have used for loop to check if a field is missing a value<br>and store in fields_not_available then if the fields_not_available is empty success message is<br>shown if its not &quot;not added&quot; message is shown along with the missing<br>fields.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220223546-313f1516-036d-48d5-8ffc-a930843de1a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated process_update function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>if else clause is used to determine if the index provided is within<br>bounds.</div><div>if the index is out of bounds an appropriate message is given.</div><div>when an<br>available index is given we proceed with the code where the current values<br>for&nbsp;</div><div>the fields are displayed next to the question</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220224832-8b01ec78-e9be-46b3-967a-51be39691805.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated update start function. <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220225761-43d23b9c-bbf2-488c-8fbe-772614b8c194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful update process<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220226234-5ff8a4a6-ce59-4117-bd63-ae72dc8e5ad6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failure due to same or null value.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220226509-c14f3fb1-48b1-410b-9914-64eb7483995a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>irrelevant date format for Due. rest of the fields were changed/ updated.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div>No bound check is required since its taken cared of in&nbsp;<span style="letter-spacing: 0.09996px;">process_update()<br>function.</span></div><div>storing the chosen task in 'task'.</div><div>&nbsp;if the given value is null or the<br>same as the existing value then the field is not updated.</div><div>once a field<br>is updated the field name is stored in 'fields_changed' list.</div><div>when 'fields_changed' is empty<br>which would imply that no changes were made therefore the task is updated.<br>else the the fields that were updated will be displayed.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220229440-27e9d957-0dcd-4784-b6d7-803a9d55b7b9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated mark_done() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220228790-b9e61a12-80aa-4a9c-9519-05e0e10964dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success output for mark done function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220229578-582f04b7-eb68-4ad4-9950-ac656a47ec2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failed output<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>index is first checked for out of bounds.</div><div>"done" field is checked if it<br>False. in this case the task is not done therefore the current time<br>is stored.</div><div>if it is not false then the value was changed therefore we<br>can assume that the task was already done.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220248419-a360a9ad-563d-4641-97a3-8cec8ec7be65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220230273-25a96d12-5125-4924-969d-4b961fb8ab11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220248263-57ac9b70-6229-4b6b-a23e-977a74574d2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Out of bounds messages.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220231135-17c04cea-de3c-466a-822b-57bade9e0432.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>examples<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220232242-a10761d4-552e-4d95-bb20-24d7918a8479.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete_task() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220232797-98d292d1-2e84-4e0d-abca-d82243580388.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success output. please check the highlighted part.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220233109-80a2a20d-8e59-41f0-8d8f-acf5dbef7c3b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>failed due to out of bounds:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div>Checking for out of bounds.&nbsp;</div><div>if index lies outside appropriate messages are displayed</div><div>when a<br>valid index is provided the task is deleted from the list and a<br>success message is displayed.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220234630-4a48e956-19b2-478f-b329-4c299e9f7762.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>completed get_incomplete_tasks() function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220235109-e0037ada-7f69-4e2b-9c7a-ad30bcca0e9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success output for incomplete task function.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220235554-9e1e64f3-4e26-467a-b04d-b949ceabef5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>no incomplete tasks remain.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>for loop is used to check value for Key "done".</div><div>if its false then<br>the task is not completed and the task is appended to the '_tasks'<br>list.</div><div>if the list is empty it implies that there are no tasks that<br>are incomplete.</div><div>if the list is not empty then the _tasks list is given<br>in the list_tasks function.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220237211-381c32cf-92ef-43a8-b3bf-c8266b48f865.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>completed get_overdue_tasks() function:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220238250-09516927-a4cf-4be3-aee0-0fabd4065e4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success of overdue function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220238604-9e40fca0-091b-4322-b8c7-a17a628aac2c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>No overdue task available.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>two variables now and x are used to obtain the current date and<br>time in the required format.</div><div>for loop is used to run through each task<br>in 'tasks' list.</div><div>conv is the due date and str_to_datetime(x) is the current day<br>and time.</div><div>these 2 can be compared since both are in datetime datatype.</div><div>if the<br>due is less than our current date and time then its appended in<br>the _tasks list.</div><div>if the list is not empty then the _tasks list is<br>given in the list_tasks funtion.</div><div>if it is empty it implies that not task<br>is overdue</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220242417-ea261d49-d47a-467c-93e8-81377cd589bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>completed get_time_remaining function.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220242579-ec67a4d0-08d2-4191-9a8c-45c3f8bbbce3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>clearer ss of the code block of get_time_remaining function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220245267-c8a182e7-22c9-4426-bbb4-2057d29033b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success - time left for task.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220245514-ca8d1f84-9be8-4755-8a26-a7fa16f4468e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Overdue - time elapsed after due.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div>first we check if the index is out of bounds and if so<br>approptiate messages are displayed.</div><div>in now the current time is stored</div><div>in 'time' the the<br>difference between due and the present us stored</div><div>timediff is the absolute value of<br>time since days and time can only be positive.</div><div>then we convert the time<br>difference to seconds and store it in timediffsecs</div><div><br></div><div>later we use divmod method to<br>figure out the seconds, minutes, hours and days.</div><div>It takes two numbers as arguments<br>and returns their quotient and remainder in a tuple.</div><div>in this code"mins, secs =<br>divmod(timediffsecs,60)" we save the quotient in mins and the remainder in secs.</div><div>we use<br>similar code to calculate days, hours and minutes.</div><div><br></div><div>when time.days() is greater than zero<br>it means the there still time left until due.</div><div>therefore the output is displayed<br>as time left.</div><div>when time.days() is less than 0 it means the time diff<br>is negative.</div><div>therefore the output is displayed as overdue.</div><div><br></div><div>source: https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-37.php</div><div>the above link has been<br>used as reference.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220246159-71e4fac0-d44b-4684-8183-82426a10124f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Terminal Screenshot.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/220246373-304a9570-e583-4ee9-892b-f8abd4e590d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Saved Json body.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>The project was really fun.<div>The main learning point for me was understanding how<br>datatypes work in general.</div><div>faced few difficulties with datetime datatype. had to convert every<br>instances of of Due to string to effectively process data without any errors.</div><div>learned<br>how functions work and understood the power of a global variable (tasks).&nbsp;<br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/4">https://github.com/RisheekK/IS601-006/pull/4</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-1-tracker-app/grade/rr284" target="_blank">Grading</a></td></tr></table>