# Project Title

### Brief Description

![Site Header](/static/images/readme_images/site-header.png)

[FIINS Marketplace](https://django-marketplace-258f3b6d9a56.herokuapp.com/)

FINNS started off as a basic ecommerce store thats turned into a storefront for various skincare brands, Users are able to browse products, create an account and understand which products are being spoken about on the site. 

___

## Contents

- [Project Title](#project-title)
    - [Brief Description](#brief-description)
  - [Contents](#contents)
  - [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Logo and Favicon](#logo-and-favicon)
  - [Wireframes](#wireframes)
  - [Flow Diagram](#flow-diagram)
  - [Database Plan](#database-plan)
- [Features](#features)
  - [Registration](#registration)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing & Deployment](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___

## Site Objectives

Design and create a basic skincare storefront to demonstrate an understanding of the Django & Bootstrap Frameworks.

#### My three main objectives were:

- Create a readable, clean and responsive front end I wanted to make the site easily accessible and intuitively navigated for the users. Django and Bootstrap were used to create and style the front end.

- Make use of available backend functionality The use of the backend framework allows users to create a profile, comment on any of the blog posts on the site, as well as deleting their own comments should they wish to.

- Store data on an external cloud database I used ElephantSQL to store the PostgreSQL database for this project.


___

# User Experience/UX

## Target Audience

Users that are interested in skincare products 


## User Stories

### Registered User

As a Registered User, I can update my profile information.

Acceptance Criteria:

- I can access a profile management interface.
- I can update my profile information

### Site Administrator

As a Site Administrator, I want to manage product listings, including adding, editing, and deleting products so that I can maintain an up-to-date and organized product inventory.

Acceptance Criteria
- I can access an admin interface for managing products.
- I can add new products with relevant details.
- I can edit existing product information.
- I can delete outdated or irrelevant products.

### Site Vistor Story

As a Visitor, I can browse skincare products so that I can explore available skincare options without the need to log in.

Acceptance Criteria:

- I can access and browse skincare products without logging in.
- The skincare products are categorized into relevant sections (e.g., cleansers, moisturizers).
- I can click on a product to view detailed information.

### Shopper Story

As a Shopper, I can add and manage products in my shopping cart so that I can easily select and review my chosen items before proceeding to checkout.

Acceptance Criteria:
- I can add products to my shopping cart.
- I can view, modify, and remove items from my shopping cart.
- The shopping cart is seamlessly integrated into the overall shopping experience.

___

# Design Choices

## Colour Scheme

![Color Pallet](/static/images/readme_images/pp4-colors%20.png)

## Typography

The main font used is Playfair Display, with Roboto filling in the rest of the site


## Wireframes

[Wireframe Figma Dock](https://www.figma.com/file/akNyT5Zxpro1TWotHL5VQq/finn's?type=design&node-id=0%3A1&mode=design&t=EjU8UEV3J0ANaX3T-1)

## Flow Diagram

- Here you can see a basic flow diagram on how a site user and site admin would use the website
[Flow Chart](/static/images/readme_images/Flow%20.png)

## Database Plan

### Product Model

| Entity: Product |                  | Entity: User |                           |
|-----------------|------------------|---------------|---------------------------|
| **Attribute**   | **Type**         | **Attribute** | **Type**                  |
|-----------------|------------------|---------------|---------------------------|
| id              | PK               | id            | PK                        |
| seller_id       | FK               | username      | CharField                 |
| title           | CharField        | email         | EmailField                |
| description     | TextField        |               |                           |
| price           | DecimalField     |               |                           |
| quantity        | PositiveIntegerField |            |                           |
| category        | CharField        |               |                           |
| created_at      | DateTimeField    |               |                           |
| updated_at      | DateTimeField    |               |                           |
| product_image   | CloudinaryField  |               |                           |


### Account Model

| Attribute       | Type               | Description                               |
|-----------------|--------------------|-------------------------------------------|
| user            | OneToOneField(User)| References the associated user.           |
| name            | CharField          | The name of the user.                     |
| date_of_birth   | DateField          | The date of birth of the user.            |
| country         | CharField          | The country of the user.                  |
| phone_number    | CharField          | The phone number of the user.             |
| profile_picture | CloudinaryField    | Stores the profile picture of the user.   |
| address         | TextField          | The address of the user.                  |



# Features

## Registration

Users are able to, create and edit their profile information

#### Create Account
![Create Account](/static/images/readme_images/create_account.png)
#### Edit Account
![Edit Account](/static/images/readme_images/edit_profile.png)
## Product Features

#### Edit Product
![Edit Product](/static/images/readme_images/edit_product.png)
#### New Product
![New Product](/static/images/readme_images/new_product.png)
#### View All Product
![View All Products](/static/images/readme_images/product_page.png)
#### Delete Product
![Delete Product](/static/images/readme_images/delete_feature.png)
## Future Features

#### Cart Function
I had created a cart function that would allow users to add various products to a cart, the feature was able to add but ran into a issue and was advised from student services to descope this aspect of the project. 

##### Reviews

I would like to add a review system so users can rate all of the different products.
##### Filter
I would like to add a feature that allows users to filter through all of the different products using their categories


___

# Technologies Used

Here are the technologies used to build this project:

- [VS Code](https://code.visualstudio.com/) Was used as my main IDE
- [Github](https://github.com) To host and store the data for the site.
- [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
- [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database.
- [Cloudinary](https://cloudinary.com/) Used as cloud storage for images uploaded as part of the blog posts
- [Heroku](https://id.heroku.com/) Used to deploy the project

# Programming Languages, Frameworks and Libraries Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)


# Agile

This project was designed using Agile methodology, utilising the Project Board and Issues sections in GitHub

- [Project Board](https://github.com/users/Bluiss/projects/2)


___


# Testing & Deployment

[Testing Doc](/TESTING.MD)


## Deployment

### Github Deployment

The website was stored using GitHub for storage of data and version control. To do this I did the following;

After each addition, change or removal of code, in the terminal within your IDE (I used codeanywhere for this project) type:

- git add .
- git commit -m "meaningful commit message"
- git push

The files are now available to view within your github repository.

### Creating a Fork or Copying

To clone/fork/copy the repository you click on the fork tab which is situated next to unwatch tab in the top right corner of the page

### Clone

To create a clone you do the following;

1. Click on the code tab, left of the Gitpod tab
2. To the right of the repository name, click the clipboard icon
3. In the IED open GitBash
4. Change the working directory to the location you prefer
5. Add Git Clone with the copy of the repository name
6. Clone has been created

### Repository deployment via Heroku

- On the [Heroku Dashboard](https://dashboard.heroku.com) page, click New and then select Create New App from the drop-down menu.
- When the next page loads insert the App name and Choose a region. Then click 'Create app'
- In the settings tab click on Reveal Config Vars and add the key Port and the value 8000. The credentials for this app were:

1. Cloudinary URL
2. Postgres Database URL
3. Port (8000)

- Below this click Add buildpack and choose python and nodejs in that order.

### Deployment of the app

- Click on the Deploy tab and select Github-Connect to Github.
- Enter the repository name and click Search.
- Choose the repository that holds the correct files and click Connect.
- A choice is offered between manual or automatic deployment whereby the app is updated when changes are pushed to GitHub.
- Once the deployment method has been chosen the app will be built and can be launched by clicking the Open app button which should appear below the build information window, alternatively, there is another button located in the top right of the page.


## Credits

https://mdbootstrap.com/docs/standard/extended/profiles/
https://mdbootstrap.com/docs/standard/components/cards/

https://reintech.io/blog/building-a-shopping-cart-in-django (used in dormant shopping cart function)


