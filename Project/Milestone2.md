<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Risheek S Kumar Risheek S Kumar (rr284)</td></tr>
<tr><td> <em>Generated: </em> 5/5/2023 8:26:36 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/rr284" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236400009-e4850b7b-986f-4075-b2cc-449e6cd910dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add page with data filled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236400270-f9babe4e-6c08-4345-8fd5-cb200db65d07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Items table with all the items added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>The input is received in the form of form data. The data is<br>validated in the backend before being inserted into the database using a simple<br>insert statement.<div>If the stock is greater than zero, visibility is set to true<br>or 1 (in DB).</div><div><strike><br></strike></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/shop">https://is601-rr284-project-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236410405-c90ba898-3c02-4c38-89ad-b3e0dfcace0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop with all the items listed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236410852-5b157ce6-1870-49a2-be9c-fbad17a2c740.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filter using keyword &#39;Poster&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236411011-a3c96749-bfcb-44dd-b19e-602387b1ee61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236403634-721f5d14-c74b-4576-894b-eb15032cb588.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for listing products along with filters.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <div>to filter Name and description like filter is used.</div><div>To sort, the order by<br>command is used. we can specify asc or dsc order.</div>All products with visibility<br>True is fetched.<div><div><br></div></div><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/shop">https://is601-rr284-project-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236405302-4b84b080-ff19-4b25-b489-2b5c8b708ee8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Product listing page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>All the item are retrieved despite the visibility value.<div>A select command is used<br>with a limit value of 25.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/admin/items">https://is601-rr284-project-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236411438-c6aa0f7d-5262-40d0-b5a8-82d0f9164d4b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit option is visible only when the user is an admin.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236412000-06e76772-65f7-4167-85af-bf0bf0550c69.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button visible to the Admin on the Product Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236412214-34fa6f15-8c5c-415e-999d-0dff4ed227bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button visible to the Admin on the Admin Product List Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236412509-cf1bb8fb-76eb-4908-bc6d-111e4d0b6654.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item before an edit.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236433072-7bec1981-375e-40e6-9938-304526d7a1d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item info updated successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236433681-769a1f0e-25b6-4c51-b208-03de860cddf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item after successful edit.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>when edit button is clicked its taken to the view page where the<br>data is prefilled from querying the db.<div>If any value is changed it is<br>referred to the original query and an update query is made with data<br>that currently exists in the form.</div><div>If&nbsp; the updated quantity is zero the visibility<br>of the item is changed to false.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/admin/item">https://is601-rr284-project-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236440637-116382fb-5797-44e2-b4c6-0fb44f16daed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with view button on every product.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236440886-c78e8bda-e7ec-437e-9b16-64ae3b0901a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>product details page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>View button is clicked which directs us to the product details page.<div>it redirects<br>us to /shop/item page where the details of the item are pulled from<br>the db using the ID of the item.<br><div><br></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/shop/item">https://is601-rr284-project-prod.herokuapp.com/shop/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236448027-e1766b60-e82b-4719-afc6-83db85fac02f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successfully added to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236442618-dc357553-290a-4a65-9ef0-ae91c38f355d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized message when no user is logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236443354-311c4bb8-6c5d-4d33-8118-5a0ca94dbc11.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart table with items added to cart.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>every user has one cart where when a product is added the user<br>is taken to the /cart page where the chosen item is displayed.<div>The user<br>can also increase the quantity of the items they&#39;ve ordered in the cart<br>page.</div><div>when the user adds an item that they&#39;ve already chose the quantity of<br>the item in the cart is automatically increased.</div><div>once the order is placed the<br>cart is cleared.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>when an user clicks on cart button in the nav bar all the<br>items present in the cart table is retrieved from the db.<div>every time an<br>user adds a new item it gets populated in the cart table.</div><div>If an<br>user adds an item that&#39;s already in their cart the quantity attribute in<br>the row is increased for the item.<br><div><br></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236448027-e1766b60-e82b-4719-afc6-83db85fac02f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>items added to cart with the subtotal added.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>After items get added to cart the item values are retrieved from the<br>db.<div>the subtotal is calculated in the front end by by multiplying the quantity<br>and the price of the item.</div><div>later all subtotal values are added to give<br>us the total. Namespaces are used to ensure that all the subtotal are<br>calculated.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/cart">https://is601-rr284-project-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236449233-d04dd232-fdf7-4241-93a3-c6b6bb9e3b5d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before adding quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236449470-1939aaa8-5a35-466c-bd12-ecdb91746388.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after changing quantity<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236450317-5b5a7155-12a3-48e3-bf88-339438744c55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before changing quantity of PS5 joystick to zero<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236450712-f15a4243-094b-420d-a7fd-fd55ce06af23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after changing quantity of PS5 joystick to zero. item gets deleted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236450987-61ca7a82-0294-426e-a8a0-4a931015780f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before item quantity is changed to a negative value.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236451206-84ec33ca-e90c-4a6b-ae6d-7519d2c3cf0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before item quantity is changed to a negative value. Item gets deleted.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>If the quantity of an item is changed a value that&#39;s less that<br>zero it is considered as a deletion call.<div>The particular item is deleted from<br>the cart table and a flash message is given to the user saying<br>&quot;Deleted item from cart&quot;.<br><div><br></div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236452714-8995f443-7c69-4ec8-a845-3b26c8395a19.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting &quot;LORD OF WAR poster&quot;.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236453212-b1e39814-175c-4e54-96c8-d29604b9f139.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting &quot;LORD OF WAR poster&quot;.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236453549-c6ec92d7-6fae-4157-8f54-989487a9fff2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing cart.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/86208506/236453676-96f26c98-9008-42fd-841e-29d0eabf1420.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clearing cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>When a delete button is clicked, the particular item ID and the current<br>user ID is used to delete the item from the cart table.<div>when a<br>the cart is cleared no data is retrieved hence the zero is zero.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/RisheekK/IS601-006/pull/34">https://github.com/RisheekK/IS601-006/pull/34</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Had difficulty with Editing a particular item. This was later resolved by adding<br>&quot;if form.validate_on_submit():&quot; and checking the value of the id retrieved upon submission.<div><br></div><div>Adding custom<br>styles for every page was tedious. the issue was resolved when I added<br>style classes to the layout.html.</div><div><br></div><div>Learned a lot from adding CSS templates to address<br>aligning texts and images.</div><div><br></div><div>NOTE: a lot of screenshots were taken from the an<br>admin user but the features available work the same for all user roles.</div><div><br></div><div><br></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-rr284-project-prod.herokuapp.com/login">https://is601-rr284-project-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-milestone-2-shop-project/grade/rr284" target="_blank">Grading</a></td></tr></table>