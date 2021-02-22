@echo off
rem run_migrations.bat
rem 
rem creates migrations to update data models, then applies them
rem (--no-input suppresses prompts asking for confirmation that you changed the given model)
rem
rem NEED TO RUN AFTER ANY MODEL CHANGE AFFECTING STRUCTURE OF DATA

rem TODO: loop through app tests in case more apps are added in the future
python C:\CCS\root\django_projects\ccs_test\manage.py test config_compare.tests