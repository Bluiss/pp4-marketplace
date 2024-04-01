# PP4 - Marketplace Testing

### Contents
* [Automated Testing](#automated-testing)
  * [W3C Validator](#w3c-validator)
  * [CSS Validation](#css-validation)
  * [Lighthouse](#lighthouse)
  *


* [MANUAL TESTING](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
  * [Full Testing](#full-testing)

* [BUGS](#bugs)
  * [Known Bugs](#known-bugs)
  * [Solved Bugs](#solved-bugs)

## AUTOMATED TESTING

###  W3C Validator

#### 
All HTML pages were tested through the W3C validator, all passed except one. 

When researching, there is an issue with the allauth framework code that throws an W3 error on signup.html. Other students have submitted the issue in the open source repo.



#### CSS Validation

![CSS Validation](/static/images/readme_images/testing/css%20validator.png)

### Lighthouse

All tests were completed with google lighthouse, when conducting tests there were consistent low performance scores. When researching on slack, other students had the same issue due to the bootstrap CDN and cloudinary images being too large. This would be part of a future update to incorporate a maximum size formatter built into the model. 

#### Index 
![index](/static/images/readme_images/testing/lighthouse/index.png)

#### About Us
![about](/static/images/readme_images/testing/lighthouse/about.png)

#### Product Page
![product](/static/images/readme_images/testing/lighthouse/product.png)

#### Product Detail
![product detail](/static/images/readme_images/testing/lighthouse/product-detail.png)

#### Contact Us
![Contact](/static/images/readme_images/testing/lighthouse/contact-us.png)

#### Profile
![profile](/static/images/readme_images/testing/lighthouse/profile.png)


### Python 
All python was validated with the CI Python Linter & the pycodestyle tool to ensure pep8 validation. 

![python validation](/static/images/readme_images/testing/pep8-validation.png)

### unittest

Product forms were tested both manually and through unittesting

## MANUAL TESTING

### Testing User Stories

#### Homepage
|Index.html| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Home Link|Redirect to Home|Pass|
|Shop Link|Redirect to Shop|Pass|
|About Us Link|Redirect to About Us|Pass|
|Contact Us Link|Redirect to Contact Us|Pass|
|Profile Icon Link|Redirect to Profile Page, if logged in/ Redirect to Login page is user signed out|Pass|
|Logout Link|Log User Out|Pass|
|Shop Link Footer|Redirect to Shop|Pass|
|About Us Link Footer|Redirect to Footer|Pass|
|Contact Us Link Footer|Redirect to Contact Us|Pass|
|Featured Products|Display 3 Products|Pass|
|Dynamic Welcome Title|Display Username|Pass|
|Burger Menu|Display on mobile devices|Pass|
|Burger Links|Direct to appropriate links|Pass|

#### product.html
|Product.html| | |
|:----|:----|:----|
| | | |
|Feature|Expected Outcome|Result|
|Product Title|Display Product Title|Pass|
|Product Price|Display Product Price|Pass|
|Product Category|Display Product Category|Pass|
|Product Image|Display Product Image|Pass|
|Next Button|Take user to next page|Pass|
|Total Products|Show 6 products per page|Pass|

#### product_detail.html
|Product_detail.html| | |
|:----|:----|:----|
| | | |
|Feature|Expected Outcome|Result|
|Product Title|Display Product Title|Pass|
|Product Price|Display Product Price|Pass|
|Product Category|Display Product Category|Pass|
|Product Image|Display Product Image|Pass|
|Product Stock|Display quantity if adim|Pass|
|Edit Button|Redirect to edit form|Pass|
|Delete Button|Redirect to delete form|Pass|

#### about_us.html
|about_us.html| | |
|:----|:----|:----|
| | | |
|Feature|Expected Outcome|Result|
|3 feature cards|Display 3 feature cards|Pass|

### contact_us.html
|contact_us.html| | |
|:----|:----|:----|
| | | |
|Feature|Expected Outcome|Result|
|Name Field|Accept name input|Pass|
|Email Field|Accept email input|Pass|
|Message Field|Accept message input|Pass|
|Submit Button|Post form to database & admin panel|Pass|

#### register.html if user logged out
|Register.html if user logged out| | |
|:----|:----|:----|
| | | |
|Feature|Expected Outcome|Result|
|Username Field|Accept Username|Pass|
|Password Field|Accept Password|Pass|
|Forgotten Password Link|Redirect to forgotten password|Pass|
|Register Link|Redirect to sign up page|Pass|
|Remember Me Checkbox|Check|Pass|
|Log user in |Redirect user to profile|Pass|

#### register.html is user logged in
|Register.html if user logged in| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Name|Display Name|Pass|
|User Name|Display User Name|Pass|
|D.O.B|Display dob|Pass|
|Country|Display country|Pass|
|Phone Number|Display phone number|Pass|
|Address|Display address|Pass|
|Admin Panel|Display admin panel, if user is staff|Pass|
|Logout Message|Disply message to notify user has logged out|Pass|
|Login Message|Disply message to notify user has logged in|Pass|
|Edit Button|Redirect user to edit profile form|Pass|
|New product link|Redirect to add product form if user staff|Pass|

#### Add product form
|Add product form| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Seller|Display Seller|Pass|
|Title|Accept Title input|Pass|
|Price|Accept Price input|Pass|
|Quantity|Accept quantity input|Pass|
|Category|Accept category input|Pass|
|Description|Accept description input|Pass|
|Submit form|Post form to database|Pass|

#### Edit product form
|Edit product form| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Seller|Display Seller|Pass|
|Title|Accept Title input|Pass|
|Price|Accept Price input|Pass|
|Quantity|Accept quantity input|Pass|
|Category|Accept category input|Pass|
|Description|Accept description input|Pass|
|Update form|Update product in database|Pass|

#### Delete product form
|Edit product form| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Delete product|Delete Prodcut|Pass|
|Edit product|Redirect to edit form|Pass|

#### Edit user profile
|Edit profile form| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Name|Edit name|Pass|
|DOB|Edit DOB|Pass|
|Country|Edit Country|Pass|
|Phone Number|Edit Phone Number|Pass|
|Address|Edit Address|Pass|
|Edit Message|Display message when user profile is edited|Pass|


#### Account Registration
|Account registration| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|

|Username|Accept Username|Pass|
|Email|Accept email|Pass|
|Password|Accept password twice|Pass|
|Sign up|Create account|Pass|

#### Forgotten password 

#### Logout page
|Account registration| | |
|:----|:----|:----|
|Feature|Expected Outcome|Result|
|Logout user|Logout|Pass|






### Full Testing

Full testing was performed on the following devices:

* Desktop:
  * 24 Inch Monitor
  * 27 Inch Monitor
* Laptop:
  * Macbook Pro 2021 13 inch screen
* Mobile Devices:
  * iPhone 14 pro.
  * iPhone 12 pro.

Each device tested the site using the following browsers:

* Google Chrome
* Safari
* Microsoft Edge



## BUGS

