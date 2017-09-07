# project

This is custom project developed in Django with REST Apis. It has following URL's to work with

1. admin/ for Django Admin UI
2. question/get-answer/<question.column_title> to get the answer of the question, question id and user.
3. question/search/<search_term> it returns the list of questions with their corresponding ID and user's name matching the term specified in the URL. If it dose not find any matching questions it will return an empty list.
4. get-dashboard-data/ This url handles the polling request comes from the homepage of the project. It return six different counters of questions, answers, tenants and users and it also return 2 lists of today's top api consumer and overall top api consumers.
5. / it simply renders the dashboard html page.
