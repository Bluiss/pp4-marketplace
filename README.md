# Project Title

### Brief Description

Brief description of the project.

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
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
  - [Python Testing](#python-testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Media](#media)
  - [Acknowledgments and Thanks](#acknowledgments-and-thanks)

___

## Site Objectives

Design and create a basic eccomerce store to demonstrate understanding of the libraries and frameworks available to developers.

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

Pallete

## Typography

The main font used isPlayfair Display, with Roboto filling in the rest of the site


## Wireframes

[Wireframe Figma Dock](https://www.figma.com/file/akNyT5Zxpro1TWotHL5VQq/finn's?type=design&node-id=0%3A1&mode=design&t=EjU8UEV3J0ANaX3T-1)

## Flow Diagram

Brief description of the flow diagram.

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


### Shopping Cart Model 

| Attribute | Type                 | Description                                    |
|-----------|----------------------|------------------------------------------------|
| user      | ForeignKey (User)    | References the user who owns the cart.         |
| product   | ForeignKey (Product) | References the product added to the cart.      |
| quantity  | IntegerField         | Represents the quantity of the product in cart.|


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

Brief description of the registration feature.

## Future Features

- Feature 1
- Feature 2
- Feature 3

## Features Not Included

- Feature 1
- Feature 2
- Feature 3

___

# Technologies Used

Brief description of the technologies used.

___

# Programming Languages, Frameworks and Libraries Used

- Language/Framework/Library 1
- Language/Framework/Library 2
- Language/Framework/Library 3

# Agile

Brief description of Agile methodology.

# Testing

Brief description of testing procedures.

## Manual Testing

Brief description of manual testing.

## Bugs

Brief description of encountered bugs and resolutions.

## Lighthouse

Brief description of Lighthouse performance scores.

## Validation Testing

Brief description of validation testing.

## Python Testing

Brief description of Python testing.

## Deployment

Brief description of deployment process.

## Credits

Brief description of credits.

## Media

Brief description of media sources.

## Acknowledgments and Thanks

Brief acknowledgment of individuals who provided assistance.
