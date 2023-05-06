<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 8:13:10 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236573916-97cb6c64-1031-45d0-b8a4-b744b34d703c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB table of orders<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236573916-97cb6c64-1031-45d0-b8a4-b744b34d703c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB table for ordered Items.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236575410-9f70fc9f-a5b0-469b-9d31-6341373d6b19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Purchase UI is shown as pending order. User need to fill their info<br>before proceeding to the payment portal. They can choose different payment options among<br>Debit card, Credit card and Paypal.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236576698-39dde4e0-56fc-4d31-a925-015085a8d6bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pending Purchase form with data filled. It has a link to go back<br>to cart and The items shown are non-editable.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236587257-7a70dfaa-e4d3-47ec-9b55-873190e6bc7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart with item that has stock as zero (Air Jordan 1 mid).<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236587400-bfbe20f1-14dc-4d36-9b39-b7c9a26b8584.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The item has been deleted from the user&#39;s cart and the reason is<br>shown in a flash message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236577022-d9885ee8-b283-4f0e-a631-3cd3236ed2c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation to see if the proper details are provided by the user.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236577628-73b311b0-5456-48d0-940d-bcb16d6fad0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>validation is done to verify if  1) paid amount matches the cart<br>amount 2) the stock and price of items are correct<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236578185-e126c41b-8db2-4c2b-b0fe-34a4208db347.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entering wrong payment amount to record error messages.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236578387-a4778239-ee32-42c3-b8d8-56d1ad98f01a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash messages popped to inform user that the entered amount is incorrect.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236578643-f94367ac-1e02-489d-828f-75f68b515173.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Trying to update an item quantity to 90.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236579045-5704ef13-66e1-4306-b280-18b52812984f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message popped when the updated quantity is greater than stock.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <div>1. When the user clicks the place order button on the cart page,<br>they are taken to the place order page.</div><div>2. The cart information are checked<br>on this page. first. If the details are correct and the items are<br>in stock, the user is directed to a page where they may enter<br>their shipping address and payment information.</div><div>3. Once completed, the user will be forwarded<br>to the payment page.</div><div>4. The order will be confirmed if the payment is<br>successful. The stock and price are checked again on the backend. If the<br>verification is successful, an entry is made in the orders table, and an<br>entry is made in the order items table for each item in the<br>order.</div><div><div>5. If no problems arise, the items are deleted from the cart table.<br>Furthermore, the stock of those specific products is updated.</div><div>6. The user is given<br>with a confirmation page that includes the order id.</div></div><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/36">https://github.com/RisheekK/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/confirm_order">https://is601-rr284-project-prod.herokuapp.com/confirm_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236580429-8ac4aad0-c951-4e04-9809-2eb8c0f671ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order confirmation with order details from the Order and OrderItems table, cost of<br>each line item and the total value, Payment method, shipping info and a<br>Thank you message.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p><font size="2">Information given in the order confirmation page is recorded in the orders<br>table&nbsp;and displayed here in appropriate fields.</font><div><font size="2">This only happens when the order is<br>placed successfully and the amount matches the total amount due.</font></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/36">https://github.com/RisheekK/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/place_order">https://is601-rr284-project-prod.herokuapp.com/place_order</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236582213-9705d0d9-1acd-4ce3-8a1e-3b44ef77439f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Orders page that lists all the previous orders made my the user. Note<br>that each order has a view button that shows the order details.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236582630-5250c1cd-21cf-4934-a46d-79ccf2454e14.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When View button on any order is clicked it brings the user to<br>the order details page. All the details of the order including the buyer<br>details, list ordered item of ordered items and total cost. Note: The total<br>cost is in white so it might not be as visible as other<br>colors. chose white because it felt most aesthetic, but its probably not.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>When the user clicks on view button all the items linked to the order id is retrieved from the order items table along with the information they've provided in the confirmation page from orders table.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/36">https://github.com/RisheekK/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/order?id=7">https://is601-rr284-project-prod.herokuapp.com/order?id=7</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236583701-177d74a3-1d6b-4060-8c3b-d1c746967c2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Orders made by all the users are visible with a view button for<br>each order. The Username of the buyer is also given in the table.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236584476-2dd5a10b-a53d-4925-b3f2-8d0fa41ab470.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Details of an order from an user that is not an admin.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>similar logic to the purchase history is used here. But, the important distinction is the query used/generated to retrieve the data.<div>we make a cross join with the user table and the order table to retrieve the name of the buyer.</div><div>likewise when view is clicked the item ID is referred to pull in the data from orders and order items table.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/36">https://github.com/RisheekK/IS601-006/pull/36</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/admin/order?id=7">https://is601-rr284-project-prod.herokuapp.com/admin/order?id=7</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236574970-fbe22518-5768-4fd9-b5b2-a0c4b190a378.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart page with place order button.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Faced difficulties writing SQL in code to join different tables.<div>Used forms to carry data whenever redirect is used since data is not lost when done so.</div><div>Played around with styling different elements of the page which helped to get more familiar with CSS.</div><div>Navigating between different pages were tricky as few of them worked on Get and the others on both.</div><div>The quantity element when adding to cart<br>was defaulting to one when I realized it was being redirected to a<br>anther endpoint.</div><div>MultiDict import helped a lot to handle data from table rows.<br></div><div>Learned to work around with git to revert back to different commits as code changed were causing bugs and crashes.</div><div><br></div><div><br><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-3-shop-project/grade/rr284" target="_blank">Grading</a></td></tr></table>