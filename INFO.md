# About the project

Cygnus is an online platform for students and tutors to communicate.

## Ideas

- Account: Tutors and students need to create an account to post. Some information is only visible with an account.
- Posting: Users can Tutors can post about the courses they offer, and students can post about study sessions, or courses they need help with.
- Dashboard: When users log in, they are redirected to their dashboard, a page with information about:
    - Students looking for study partners.
    - Recommended tutors.
- Search bar: Users can search the website for specific subjects, posts, and tutors. They can also filter the information by 'subject', 'most recent', 'oldest'.
- Rating System: After each session the student can rate the performance of the tutor. The tutor can also rate the behavior of the student. The tutor generate a key that only users with student accounts can use to access the rating page.
- Deletion: Users can modify or delete their posts after being created.
- No payment is done through the platform.

## Database

##### Conceptual Design

User: UserId, Name, Email, Password, Gender, Biography (Optional), Phone (Optional), Location (Optional), School (Optional)
Tutor: CoursesTaken, Rating, Fare, Posts, Availability
Student: SubjectsWanted, Posts
Post: PostId, Title, Description, Subject, User, Date_Posted, Status (Completed/Pending)

##### Questions and Assumptions

Is it possible for an user be both tutor and student at the same time? No, in that case the tutor should create an student account.

There are only two genders: Male and Female

## Guidelines

1. Do not push to the *master* branch.

## Paths

1. Home
2. Login
3. Register
4. 404 - Not Found

## CRUD

```
C - /add/model
R - /model/<id>
U - /model/<id>/edit
D - /model/<id>/delete
```