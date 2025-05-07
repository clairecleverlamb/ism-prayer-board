ISM Prayer Board 
| 🌐 Deployed App | [Live App](https://ism-prayer-board-frontend.vercel.app/) |

The **ISM Prayer Board** is a web application built with Django and PostgreSQL that allows authenticated users to submit, view, and pray for one another's prayer requests. Users can manage their own requests and interact with a beautiful interface designed with Bootstrap. The app supports both grid and carousel views for browsing.

## Features

- Submit, edit, and delete prayer requests
- Pray for a request and increase its count
- Authentication with email-restricted sign-up (domain only)
- Toggle between grid view and carousel view for prayers
- Toast notifications for actions (e.g., success on submission)
- Clean, responsive UI with Bootstrap 5
- PostgreSQL database integration

##  App Screenshots
Landing
![landing page Screenshot](ism_prayer_board_django/prayers/static/assets/landingPage.png)
LogIn
![signIn page Screenshot](ism_prayer_board_django/prayers/static/assets/login.png)
SignUp
![signUp page Screenshot](ism_prayer_board_django/prayers/static/assets/signup.png)

##  Tech Stack

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5 + Font Awesome
- **Database**: PostgreSQL
- **Auth**: Django's built-in session-based authentication
- **Styling**: Custom CSS and Bootstrap theming

## Authentication
- Only emails with @acts2 domain are allowed to sign up.
- Superusers have admin access and can delete any prayer.
- Regular users can only edit/delete their own prayers.


## Further Improvment 
- Add email notifications for prayer updates
- Enable filtering/search by mentor or status
- Add pagination or infinite scroll

## Credits
- Bootstrap 5 for frontend styling
- Font Awesome for icons
- Acts2 Network for inspiration