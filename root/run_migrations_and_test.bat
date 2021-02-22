@echo off
rem run_migrations.bat
rem 
rem creates migrations to update data models, then applies them
rem (--no-input suppresses prompts asking for confirmation that you changed the given model)
rem
rem NEED TO RUN AFTER ANY MODEL CHANGE AFFECTING STRUCTURE OF DATA

rem Migrate
call run_migrations.bat

rem Test
call run_tests.bat