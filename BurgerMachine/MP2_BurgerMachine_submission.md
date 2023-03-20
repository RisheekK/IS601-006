<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 3/20/2023 11:33:52 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226145259-ed4559db-a4ee-436b-8a53-091aecd690ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>calculate_cost function:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226191499-69adf5d8-7953-4f82-b230-e1ddc7b26a14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing expected value in currency format.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226191357-844b9cc0-1521-4db7-a93f-904dcde741f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>formatting string in handle_pay method<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226191540-0a1dc318-f254-453a-9f50-2d68a1607b88.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output in terminal<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p><b>Calculating cost:</b><div>Items in list&nbsp;self.inprogress_burger are iterated over and their cost value is added<br>to the &quot;total&quot; and returned in the method.</div><div><br></div><div><b>Currency formatting:&nbsp;</b></div><div>We achieve this by using<br>the %f formatter in our string. In our case we use %.2f to<br>extend/limit the decimal places to Two.</div><div>example: formatting string - f&quot;{expected:.2f}&quot; to compare with<br>the total which is obtained as the input form the user.</div><div><br></div><div><br></div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226312147-4ec87eac-e443-4606-8a95-9e6ba78a51a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated OutOfStockException. we are converting the current stage value to a string and<br>replacing STAGE. with a blank to get the current stage name.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226319188-caabfbcf-de5a-4f79-b233-0ff598ab6a10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated NeedsCleaningException. A prompt is thrown asking permission from the user to clean<br>the machine. when &quot;clean&quot; is obtained as input self.clean_machine() is triggered.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226313876-c55f4e94-de4b-4e49-b681-8d24d87b45df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated InvalidChoiceExceptions. we are converting the current stage value to a string and<br>replacing STAGE. with a blank to get the current stage name and printing<br>it out in a statement.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226314445-30ad6245-9efa-432e-b41a-48ad1cd2ffbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated ExceededRemainingChoicesExceptions. we are converting the current stage value to a string and<br>replacing STAGE. with a blank to get the current stage name. if current<br>stage equals patty then an appropriate message is thrown and self.currently_selecting is set<br>to STAGE.Toppings. if the current stage is toppings the same happens as before<br>except the current stage is set to STAGE.pay.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226317615-a6a0faa6-556a-4d07-b13c-eba14f6bc83d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated InvalidPaymentException. A message is given to the user stating the entered value<br>is incorrect and asks the user to try again.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p><font size="2"><b style="">OutOfStockException:</b>&nbsp;we are converting the current stage value to a string and<br>replacing STAGE. with a blank to get the current stage name.</font><div><font size="2"><b>NeedsCleaningException:&nbsp;</b>A prompt<br>is thrown asking permission from the user to clean the machine. when &quot;clean&quot;<br>is obtained as input self.clean_machine() is triggered.<b><br></b></font></div><div><font size="2"><b>InvalidChoiceExceptions:&nbsp;</b>we are converting the current stage<br>value to a string and replacing STAGE. with a blank to get the<br>current stage name and printing it out in a statement.<b><br></b></font></div><div><font size="2"><b>ExceededRemainingChoicesException:&nbsp;</b>&nbsp;we are converting<br>the current stage value to a string and replacing STAGE. with a blank<br>to get the current stage name. if current stage equals patty then an<br>appropriate message is thrown and self.currently_selecting is set to STAGE.Toppings. if the current<br>stage is toppings the same happens as before except the current stage is<br>set to STAGE.pay.<b><br></b></font></div><div><font size="2"><b>InvalidPaymentException:&nbsp;</b>A message is given to the user stating the entered<br>value is incorrect and asks the user to try again.</font><span style="font-size: 13px;"><br></span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226359232-c9e5ba6b-de3f-4da4-8154-003fd50491bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test - 1:  First selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226377888-fa724d42-081e-411e-8659-0c509c1727c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 2 - can only add patties if they&#39;re in stock.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226378200-f02e99b6-ecf2-4319-bd3d-d300924eb55d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 3 - can only add toppings if they&#39;re in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226378363-49f35ec8-1a5c-4e34-a629-23cd2c0d288a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4 - Can add up to 3 patties of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226378753-528805d6-d5d8-4dda-8ce8-9f5d6618c52f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 5 - Can add up to 3 toppings of any combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226379374-e57e4aca-acdb-48f5-992b-f4f2b452092c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6 - cost must be calculated properly based on the choices<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226380308-01828b25-3eca-4905-a62e-a0e205d5e8ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 7 - Total Sales<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226380601-1c257b98-184b-4a5f-8db6-4f6c42e7a6c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8 - Total burgers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226381140-3d7d9bf6-ca90-47d1-ae0b-0f0fa13c3e95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passed Test cases.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226381873-35277d31-8a2a-417c-a198-0c648d634ebb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Testing section in VScode.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div><b>Test 1 - </b><i style="">First selection. </i>We directly start with the Patty stage<br>to see if&nbsp;&nbsp;InvalidStageException is triggered.</div><b>Test 2</b> - <i>can only add patties if they're<br>in stock</i>. We initialize the quantity of a patty we want to test<br>with to zero and try running the test with the same patty as<br>input. we use a temporary variable to store the original quantity of the<br>patty.<div><b>Test 3</b> - <i>can only add toppings if they're in stock. W</i>e do<br>the same thing we did for patty.</div><div><b>Test 4</b> - <i>Can add up to<br>3 patties of any combination. W</i>e input one bun and four patties to<br>check if it triggers exceededRemainingChoicesException.<br></div><div><b>Test 5</b> - <i>Can add up to 3 toppings<br>of any combination.</i>&nbsp;We input one bun and four toppings to check if it<br>triggers exceededRemainingChoicesException.<br></div><div><b>Test 6 </b>- <i>cost must be calculated properly based on the choices</i>.<br>We use for loop that run the code thrice (to have 3 valid<br>burgers), random function to randomize the choices and then calculate the cost of<br>all the items which are stored in their respective variables. we check if<br>the calculated cost does not equal to the expected cost if true we<br>assert the test to be false, else we proceed to payment stage and<br>process the amount. Each loop creates a unique combination and even if one<br>of these loops fail our test fails too.<br></div><div><b>Test 7</b> - <i>Total Sales</i>. We<br>use pytest fixtures to generate 3 different order with different combinations. In our<br>test_total function we create variables to hold the exact cost of each of<br>our fixture generated burger. we sum it up and compare it to the<br>total sales of the machine from our third fixture, this is possible since<br>we don't reset the machine after every order. if the sum and total<br>sales matches then its asserted as True.<br></div><div><b>Test 8</b> -&nbsp;<i>Total burgers</i>. We compare the<br>total_burgers from third order to three, this is possible since the machine is<br>not reset at the end.&nbsp;</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/18">https://github.com/RisheekK/IS601-006/pull/18</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Learned how to write test cases and understood pytest better.<div>changed few values in<br>code like quantity etc to manually test the code which caused a major<br>havock in the testing phase.</div><div>Understood exception handling in detail.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226385462-c7477d0f-c76a-452d-b6f2-9f1423a5204a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful ouput.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226386435-ab165689-14a0-4349-8a9b-241ffc9c3679.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output with caption showing the order of inputs: lettuce wrap -&gt; veggie -&gt;<br>next -&gt; mayo -&gt; cheese -&gt; pickles -&gt; done -&gt; 3.25<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/226387510-51ac526f-44bb-4939-84c1-02132271457c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output with caption showing the order of inputs: white burger bun -&gt; beef<br>-&gt; next -&gt; cheese -&gt; lettuce -&gt; done -&gt; 2.50 -&gt; quit<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/rr284" target="_blank">Grading</a></td></tr></table>